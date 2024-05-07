"""
爬取台灣中央氣象局會地震資訊及位置圖
使用 Requests 函式庫的 get 的方法，抓取氣象觀測資料的 JSON 網址
(https://opendata.cwb.gov.tw/devManual/insrtuction)。

接著使用字典的取值方法，搭配 for-迴圈印出某一地震强度以上 (如4.0)
城市名稱、區域名稱和觀測點名稱。
"""

import requests # pip install requests
from sample.credentials import line_gw_url, line_pc_token, line_pc_name, quake_url, quake_magnitude
from datetime import date, timedelta
import json

def send_line(msg, img):
    # 透過 LINE Notify 傳送信息 msg (必要) 和 圖片 img (非必要)

    # POST 使用的 header 加上 LINE Notify 權杖
    headers = {
        'Authorization': 'Bearer ' + line_pc_token
    }
    data = {
        'message': msg,            # 發送的訊息
        'imageThumbnail': img,     # 預覽圖網址
        'imageFullsize': img       # 完整圖片網址
    }

    # 發送 LINE NOtify
    data = requests.post(line_gw_url, headers=headers,
                         data=data)


data = requests.get(quake_url)  # 台灣中央氣象局網址
data_json = data.json()

## Dump the Json data into a file to examine
# file_write = f'Sample/earthquake.json'
# with open(file_write, 'w') as f:
#   json.dump(data_json, f, indent=2)
# print(
#     f'===>請打開 {file_write} 檢視 JSON 格式的檔案...\n')

eq = data_json['records']['Earthquake']    # 轉換成 json 格式

# 算出昨天日期
yesterday = date.today() - timedelta(days=1)

# Loop thru all events
for i in eq:
    loc = i['EarthquakeInfo']['Epicenter']['Location']
    val = i['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue']
    dep = i['EarthquakeInfo']['FocalDepth']
    eq_time = i['EarthquakeInfo']['OriginTime']
    img = i['ReportImageURI']
    msg = f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}'
    print(msg)

    # Get events that occured not less than quake_magnitude
    if val >= quake_magnitude:
        # 截取日期部份
        date_occured = date.fromisoformat(eq_time.split(' ')[0])

        # 只爬取今天和昨天的資料
        if date_occured == yesterday or date_occured == date.today():
            send_line(msg, img)
            print(f'===> {val} felt, a LINE message sent to {line_pc_name}!')
