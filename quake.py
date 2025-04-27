"""
地震資訊通知系統

本程式會定期爬取台灣中央氣象局的地震資料，並在發生指定規模以上的地震時，
透過 LINE Notify 發送通知給指定的使用者。

主要功能：
1. 爬取中央氣象局地震資料
2. 過濾指定規模以上的地震
3. 透過 LINE Notify 發送通知
4. 記錄地震發生時間、地點、規模等資訊

使用方法：
1. 確保已安裝必要套件：pip install requests python-dotenv
2. 設定 .env 檔案中的相關參數
3. 執行本程式
"""

import requests
from datetime import date, timedelta
from dotenv import load_dotenv
import os
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import webbrowser

# 載入環境變數
load_dotenv()

# 從環境變數讀取設定
quake_url = os.getenv('QUAKE_URL')
quake_magnitude = float(os.getenv('QUAKE_MAGNITUDE', 4.0))

def create_session():
    """
    建立具有重試機制的 requests 會話
    """
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=False,
        raise_on_status=False
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def get_earthquake_data() -> dict:
    """
    爬取中央氣象局地震資料

    Returns:
        dict: 包含地震資料的字典
    """
    try:
        session = create_session()
        response = session.get(quake_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"爬取地震資料失敗：{str(e)}")
        return {}

def process_earthquake_events(data_json: dict) -> None:
    """
    處理地震事件，並大於等於指定規模的地震顯示地震資訊

    Args:
        data_json (dict): 地震資料的 JSON 格式字典
    """
    if not data_json:
        return

    eq = data_json.get('records', {}).get('Earthquake', [])
    yesterday = date.today() - timedelta(days=1)

    for event in eq:
        try:
            loc = event['EarthquakeInfo']['Epicenter']['Location']
            val = float(event['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'])
            dep = event['EarthquakeInfo']['FocalDepth']
            eq_time = event['EarthquakeInfo']['OriginTime']
            img = event['ReportImageURI']

            msg = f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}'
            print(msg)

            if val >= quake_magnitude:
                date_occured = date.fromisoformat(eq_time.split(' ')[0])
                if date_occured in [yesterday, date.today()]:
                    print(f'===> {val} 級地震，Browser顯示地震位置圖...')
                    webbrowser.open(img)  # 顯示地震位置圖
        except (KeyError, ValueError) as e:
            print(f"處理地震資料時發生錯誤：{str(e)}")

if __name__ == "__main__":
    """
    主程式入口點
    """
    print("開始爬取地震資料...")
    data_json = get_earthquake_data()
    print("開始處理地震資料...")
    process_earthquake_events(data_json)
    print("完成資料處理")
