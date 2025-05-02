"""
地震簡訊通知系統

這個程式會定期檢查地震資料，當發生符合條件的地震時，會自動發送簡訊通知。
主要功能：
1. 取得地震資料
2. 檢查地震規模是否達到設定門檻
3. 發送簡訊通知
"""

from smsViaSMTP import Messenger, SMS
from quake import get_earthquake_data
from datetime import date, timedelta
from dotenv import load_dotenv
import os
import logging

# 設定日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 載入環境變數
load_dotenv()

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

def send_notification(messenger, sms_info, message):
    """
    發送簡訊通知
    
    Args:
        messenger (Messenger): 簡訊發送器實例
        sms_info (dict): 簡訊設定資訊
        message (str): 要發送的訊息內容
    """
    try:
        sms = SMS(
            sms_info['number'],
            sms_info['gateway'],
            sms_info['subject'],
            message
        )
        messenger.send_sms(sms, one_time=True)
        logger.info(f"成功發送簡訊通知：{message}")
    except Exception as e:
        logger.error(f"發送簡訊時發生錯誤：{str(e)}")

def main():
    """
    主程式入口
    1. 初始化簡訊發送器
    2. 取得地震資料
    3. 檢查每個地震事件
    4. 發送通知（如果需要）
    """
    try:
        # 設置日誌
        logger.setLevel(logging.INFO)
        
        # 初始化簡訊發送器
        email_sender = os.getenv('EMAIL_SENDER')
        email_password = os.getenv('EMAIL_PASSWORD')
        my_messenger = Messenger(email_sender, email_password)
        
        # 簡訊設定
        sms_info = {
            'number': os.getenv('SMS_MOBILE_NUMBER'),
            'gateway': os.getenv('SMS_GATEWAY'),
            'subject': 'Taiwan Earthquake Alert'
        }
        
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
                    send_notification(my_messenger, sms_info, message)
    
    except Exception as e:
        logger.error(f"主程式執行時發生錯誤：{str(e)}")

if __name__ == "__main__":
    main()