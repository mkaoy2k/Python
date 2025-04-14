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
import json
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

# 從環境變數讀取設定
line_gw_url = os.getenv('LINE_GW_URL')
line_pc_token = os.getenv('LINE_PC_TOKEN')
line_pc_name = os.getenv('LINE_PC_NAME')
quake_url = os.getenv('QUAKE_URL')
quake_magnitude = float(os.getenv('QUAKE_MAGNITUDE', 4.0))

def send_line(msg: str, img: str) -> None:
    """
    透過 LINE Notify 傳送地震通知

    Args:
        msg (str): 要發送的文字訊息
        img (str): 地震位置圖的 URL
    """
    headers = {
        'Authorization': 'Bearer ' + line_pc_token
    }
    data = {
        'message': msg,
        'imageThumbnail': img,
        'imageFullsize': img
    }
    
    try:
        response = requests.post(line_gw_url, headers=headers, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"發送 LINE 通知失敗：{str(e)}")

def get_earthquake_data() -> dict:
    """
    爬取中央氣象局地震資料

    Returns:
        dict: 包含地震資料的字典
    """
    try:
        response = requests.get(quake_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"爬取地震資料失敗：{str(e)}")
        return {}

def process_earthquake_events(data_json: dict) -> None:
    """
    處理地震事件，並發送通知

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
                    send_line(msg, img)
                    print(f'===> {val} 級地震，已發送 LINE 通知給 {line_pc_name}!')
        except (KeyError, ValueError) as e:
            print(f"處理地震事件時發生錯誤：{str(e)}")

def main():
    """
    主程式入口點
    """
    print("開始爬取地震資料...")
    data_json = get_earthquake_data()
    process_earthquake_events(data_json)
    print("完成資料處理")

if __name__ == "__main__":
    main()
