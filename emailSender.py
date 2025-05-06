"""
Gmail 電子郵件發送器

程式概述：
這是一個使用 Gmail SMTP 服務發送純文字電子郵件的 Python 程式，主要功能包括：

    1. 初始化日誌系統
    2. 載入環境變數
    3. 讀取配置檔案
    4. 初始化 EmailPublisher 實例
    5. 發送電子郵件
    
    執行流程：
    - 檢查環境變數設置
    - 讀取郵件內容
    - 設定郵件主題和收件人
    - 發送郵件
    
    可能的錯誤情況：
    - 環境變數未設定
    - 配置檔案不存在
    - SMTP 發送失敗
"""
import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from emailPublisher import EmailPublisher

if __name__ == "__main__":
    """
    主程式入口點
    """
    # 設置日誌
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s'
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

    # 初始化 EmailPublisher
    publisher = EmailPublisher(email_sender, email_password)
    
    # 讀取郵件內容
    with open(config_dir / 'emailAlert.txt', 'r') as f:
        text_content = f.read()
    
    # 設定郵件主題和收件人檔案
    subject = f'電子郵件警報'
    recipients_file = config_dir / 'email_list.txt'
    
    # 發送 TXT 郵件
    publisher.send_email(subject, text_content, "", recipients_file)