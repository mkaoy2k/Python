"""
Line Notify 訊息發送工具

這個工具可以透過 LINE Notify API 發送文字訊息和圖片到指定的 LINE 群組。
支援單純文字訊息、單純圖片，或同時發送文字和圖片。

使用方式：
    python lineSend.py -msg "你的訊息" -img "圖片路徑"

參數說明：
    -msg (選填): 要發送的文字訊息
        如果未指定，將從 LINE_FILE_MSG 指定的檔案讀取預設訊息
    -img (選填): 要發送的圖片檔案路徑
        如果未指定，則只發送文字訊息
"""

import requests
from dotenv import load_dotenv
import os
from absl import app
from absl import flags

# 讀取環境變數
load_dotenv()
LINE_GW_URL = os.getenv('LINE_GW_URL')
LINE_TOKEN = os.getenv('LINE_MY_TOKEN')
LINE_NAME = os.getenv('LINE_MY_NAME')
DEFAULT_MSG_FILE = os.getenv('LINE_FILE_MSG')

# 定義命令列參數
flags.DEFINE_string('msg', None, '要發送的文字訊息')
flags.DEFINE_string('img', None, '要發送的圖片檔案路徑')
FLAGS = flags.FLAGS

def send_line_notify(message: str, image_path: str = None) -> bool:
    """
    發送 LINE Notify 訊息

    Args:
        message (str): 要發送的文字訊息
        image_path (str, optional): 圖片檔案路徑。預設為 None

    Returns:
        bool: 發送是否成功
    """
    try:
        headers = {'Authorization': f'Bearer {LINE_TOKEN}'}
        data = {'message': message}

        if image_path:
            with open(image_path, 'rb') as image_file:
                files = {'imageFile': image_file}
                response = requests.post(LINE_GW_URL, headers=headers, data=data, files=files)
        else:
            response = requests.post(LINE_GW_URL, headers=headers, data=data)

        response.raise_for_status()
        return True

    except requests.exceptions.RequestException as e:
        print(f"發送訊息失敗: {str(e)}")
        return False

def get_message() -> str:
    """
    獲取要發送的訊息

    Returns:
        str: 訊息內容
    """
    if FLAGS.msg:
        return FLAGS.msg
    
    if not DEFAULT_MSG_FILE:
        raise ValueError("未指定預設訊息檔案路徑")
    
    try:
        with open(DEFAULT_MSG_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"找不到預設訊息檔案: {DEFAULT_MSG_FILE}")

def main(argv):
    """
    主程式
    """
    try:
        print(f"準備發送訊息到 {LINE_NAME}...")
        message = get_message()
        
        if send_line_notify(message, FLAGS.img):
            print("訊息發送成功！")
        else:
            print("訊息發送失敗！")
            
    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return 1

if __name__ == '__main__':
    app.run(main)
