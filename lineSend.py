"""
LINE Messaging API 訊息發送工具

這個工具可以透過 LINE Messaging API 發送文字訊息和圖片到指定的使用者。
支援單純文字訊息、單純圖片，或同時發送文字和圖片。

使用方式：
    python lineSend.py -msg "你的訊息" -img "圖片路徑"

參數說明：
    -msg (選填): 要發送的文字訊息
        如果未指定，將從 LINE_FILE_MSG 指定的檔案(預設為 sample/line_msg.txt)讀取預設訊息
    -img (選填): 要發送的圖片檔案路徑
        如果未指定，則只發送文字訊息
        
Todo: migrate Line Notify to Line Messaging API interface
"""

import requests
from dotenv import load_dotenv
from pathlib import Path
import os
from absl import app
from absl import flags
import json
import base64

# 讀取環境變數
load_dotenv()
LINE_GW_URL = os.getenv('LINE_GW_URL')
LINE_TOKEN = os.getenv('LINE_MY_TOKEN')
LINE_NAME = os.getenv('LINE_MY_NAME')
DEFAULT_MSG_FILE = os.getenv('LINE_FILE_MSG') 

# 初始化當前目錄和 sample 目錄路徑
current_dir = Path(__file__).parent
sample_dir = current_dir / 'sample'

# 確保 sample 目錄存在
sample_dir.mkdir(exist_ok=True)

# 使用 Path 物件來處理檔案路徑
DEFAULT_MSG_FILE = sample_dir / DEFAULT_MSG_FILE

# 定義命令列參數
flags.DEFINE_string('msg', None, '要發送的文字訊息')
flags.DEFINE_string('img', None, '要發送的圖片檔案路徑')
FLAGS = flags.FLAGS

def send_line_notify(message: str, image_path: str = None) -> bool:
    """
    透過 LINE Messaging API 發送通知

    Args:
        message (str): 要發送的文字訊息
        image_path (str, optional): 圖片檔案路徑。預設為 None

    Returns:
        bool: 發送是否成功
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {LINE_TOKEN}'
        }
        
        # 建立訊息物件
        message_obj = {
            'type': 'text',
            'text': message
        }

        # 如果有圖片，建立圖片訊息物件
        if image_path:
            image_path = Path(image_path)
            if not image_path.exists():
                print(f"錯誤：圖片檔案 {image_path} 不存在")
                return False

            # 讀取圖片並轉換為 base64
            try:
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()
                    # 轉換為 base64
                    image_base64 = base64.b64encode(image_data).decode('utf-8')
                
                message_obj = {
                    'type': 'image',
                    'originalContentUrl': f'data:image/jpeg;base64,{image_base64}',
                    'previewImageUrl': f'data:image/jpeg;base64,{image_base64}'
                }
            except Exception as e:
                print(f"讀取圖片檔案時發生錯誤: {str(e)}")
                return False

        # 建立請求資料
        data = {
            'to': LINE_NAME,
            'messages': [message_obj]
        }

        # 發送請求
        response = requests.post(LINE_GW_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        
        print(f"成功發送訊息到 {LINE_NAME}")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"發送訊息失敗: {e}")
        print(f"詳細錯誤: {response.text}")
        return False
    except Exception as e:
        print(f"發生未知錯誤: {str(e)}")
        return False

def get_message() -> str:
    """
    獲取要發送的訊息

    Returns:
        str: 訊息內容
    """
    if FLAGS.msg:
        return FLAGS.msg
    
    if not DEFAULT_MSG_FILE.exists():
        raise FileNotFoundError(f"找不到預設訊息檔案: {DEFAULT_MSG_FILE}")
    
    try:
        with open(DEFAULT_MSG_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"讀取預設訊息檔案時發生錯誤: {str(e)}")
        raise

def main(argv):
    """
    主程式入口點
    """
    if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')

    # 確保必要參數存在
    if not LINE_GW_URL or not LINE_TOKEN:
        print("錯誤：請在 .env 檔案中設定 LINE_GW_URL 和 LINE_TOKEN")
        return

    # 獲取要發送的訊息
    message = get_message()

    # 執行發送通知
    success = send_line_notify(message, FLAGS.img)
    if not success:
        print("訊息發送失敗！")

if __name__ == '__main__':
    app.run(main)
