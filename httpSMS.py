"""使用 textbelt HTTP 服務器發送簡訊

這個模組使用 textbelt HTTP 服務器來發送簡訊到手機。
簡訊內容會從指定的檔案讀取，並限制在 80 個字元以內（textbelt 的限制）。
"""

from dotenv import load_dotenv
import os
import requests
from pathlib import Path

# 載入環境變數
load_dotenv()


def send_text(msg: str) -> dict:
    """
    使用 textbelt HTTP 服務器發送簡訊

    Args:
        msg (str): 要發送的簡訊內容

    Returns:
        dict: textbelt API 的回應
    """
    resp = requests.post('https://textbelt.com/text', {
        'phone': os.getenv('SMS_MOBILE_NUMBER'),
        'message': msg,
        'key': 'textbelt'
    })
    return resp.json()


def get_message_from_file(file_path: Path) -> str:
    """
    從檔案讀取簡訊內容

    Args:
        file_path (Path): 包含簡訊內容的檔案路徑

    Returns:
        str: 簡訊內容（限制在 80 個字元以內）
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    return content[:80]  # textbelt 限制簡訊長度為 80 個字元


def main():
    """
    主程式
    """
    try:
        # 定義資料夾路徑
        sample_dir = Path(__file__).parent / 'sample'
        file_path = sample_dir / 'test.txt'

        # 確認手機號碼設定
        mobile_number = os.getenv('SMS_MOBILE_NUMBER')
        if not mobile_number:
            raise ValueError("未設定手機號碼")

        # 讀取並發送簡訊
        message = get_message_from_file(file_path)
        print(f"準備發送簡訊到 {mobile_number}...")
        response = send_text(message)
        print("發送結果:", response)

    except Exception as e:
        print(f"發生錯誤: {str(e)}")


if __name__ == '__main__':
    main()
