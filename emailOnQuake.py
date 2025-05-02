"""
地震簡訊通知系統

這個程式會定期檢查地震資料，當發生符合條件的地震時，會自動發送電子郵件通知。
主要功能：
1. 取得地震資料
2. 檢查地震規模是否達到設定門檻
3. 發送電子郵件通知
"""

from quake import get_earthquake_data
from datetime import date, timedelta
import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from emailPublisher import EmailPublisher

def get_earthquake_info(event):
    """
    取得地震事件的詳細資訊
    
    Args:
        event (dict): 地震事件資料
    
    Returns:
        tuple: (地點, 規模, 深度, 發生時間)
    """
    try:
        loc = event['EarthquakeInfo']['Epicenter']['Location']
        val = float(event['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'])
        dep = event['EarthquakeInfo']['FocalDepth']
        eq_time = event['EarthquakeInfo']['OriginTime']
        return loc, val, dep, eq_time
    except (KeyError, ValueError) as e:
        logger.error(f"處理地震資料時發生錯誤：{str(e)}")
        return None, None, None, None

def should_notify(val, eq_time, min_magnitude):
    """
    判斷是否需要發送通知
    
    Args:
        val (float): 地震規模
        eq_time (str): 發生時間
        min_magnitude (float): 最小通知規模
    
    Returns:
        bool: 是否需要通知
    """
    try:
        date_occured = date.fromisoformat(eq_time.split(' ')[0])
        return (val >= min_magnitude and 
                date_occured in [date.today(), date.today() - timedelta(days=1)])
    except ValueError as e:
        logger.error(f"處理時間格式時發生錯誤：{str(e)}")
        return False


if __name__ == "__main__":
    """
    主程式入口點
    """
    # 設置日誌
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    # 載入環境變數
    load_dotenv()

    # 設定設定檔目錄位置
    current_dir = Path(__file__).parent
    config_dir = current_dir / 'sample'
    
    # 初始化 EmailPublisher 類別，讀取發件人和密碼
    email_sender = os.getenv('EMAIL_SENDER')
    if not email_sender:
        raise ValueError("環境變數 EMAIL_SENDER 未設定")
    email_password = os.getenv('EMAIL_PASSWORD')
    if not email_password:
        raise ValueError("環境變數 EMAIL_PASSWORD 未設定")

    try:
        # 初始化 EmailPublisher
        publisher = EmailPublisher(email_sender, email_password)
    
        # 取得地震資料
        earthquake_data = get_earthquake_data()
        min_magnitude = float(os.getenv('QUAKE_MAGNITUDE', 4.0))
    
        # 處理每個地震事件
        for event in earthquake_data.get('records', {}).get('Earthquake', []):
            loc, val, dep, eq_time = get_earthquake_info(event)
            
            if loc and val:
                message = f'Location: {loc}, Magnitude: {val}, Depth: {dep} km, Time: {eq_time}'
                logger.info(message)
                
                if should_notify(val, eq_time, min_magnitude):
                    logger.warning(f"{val} 級地震，簡訊通知地震位置圖...")
                    subject = f'地震警報'
                    recipients_file = config_dir / 'email_list.txt'
                    
                    # 發送 TXT 郵件
                    publisher.send_email(subject, message, "", recipients_file)    
    except Exception as e:
        logger.error(f"主程式執行時發生錯誤：{str(e)}")