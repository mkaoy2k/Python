"""
這個範例示範如何使用 Google 電子郵件帳戶
發送 HTML 格式的郵件給多個收件人，
收件人列表存放在文字檔案中，每行一個電子郵件地址。
"""

from typing import List
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
from pathlib import Path
import logging
from dotenv import load_dotenv
import os

# 設置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmailPublisher:
    def __init__(self, email_sender: str, email_password: str):
        self.email_sender = email_sender
        self.email_password = email_password
        
    def _read_file(self, filename: str) -> str:
        """從設定目錄讀取檔案內容"""
        if not filename.exists():
            raise FileNotFoundError(f"找不到檔案: {filename}")
        with open(filename, 'r') as f:
            return f.read().strip()

    def _get_recipients(self, recipients_file: str) -> List[str]:
        """讀取並解析收件人列表檔案"""
        if not recipients_file.exists():
            raise FileNotFoundError(f"找不到收件人列表的檔案: {recipients_file}")
        with open(recipients_file, 'r') as f:
            return [email.strip() for email in f.read().splitlines() if email.strip()]

    def _create_email(self, subject: str, text: str, html: str, recipients: List[str]) -> MIMEMultipart:
        """建立包含文字和 HTML 兩種格式的電子郵件訊息"""
        msg = MIMEMultipart("alternative")
        msg['From'] = self.email_sender
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        # 添加文字和 HTML 部分
        if text:
            msg.attach(MIMEText(text, "plain"))
        if html:
            msg.attach(MIMEText(html, "html"))
        
        return msg

    def send_email(self, subject: str, text: str, html: str, recipients_file: str):
        """發送電子郵件給多個收件人"""
        try:
            recipients = self._get_recipients(recipients_file)
            
            # 建立電子郵件訊息
            msg = self._create_email(subject, text, html, recipients)
            
            # 建立安全的 SSL 連線
            context = ssl.create_default_context()
            context.load_default_certs()
            context.minimum_version = ssl.TLSVersion.TLSv1_2
            
            # 發送電子郵件
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                try:
                    smtp.login(self.email_sender, self.email_password)
                    smtp.sendmail(self.email_sender, recipients, msg.as_string())
                    logger.info(f'從郵件信箱 {self.email_sender} 已發佈郵件...')
                    logger.info(f'===> 請到所有的郵件信箱 {recipients} 檢視郵件')
                    logger.info(f'===> 郵件標題 : {subject}\n')
                    return True
                except smtplib.SMTPAuthenticationError as e:
                    logger.error(f'send_email(): 登入失敗: {str(e)}')
                    logger.error("請確認：")
                    logger.error("1. 您的 Google 帳號是否已啟用 2 步驟驗證")
                    logger.error("2. 您是否已經生成並使用應用程式密碼")
                    logger.error("3. 您的 .env 檔案中是否包含正確的應用程式密碼")
                    return False
                except Exception as e:
                    logger.error(f'send_email(): 發送郵件時發生錯誤: {str(e)}')
                    return False
        except Exception as e:
            logger.error(f'send_email(): 發生一般錯誤: {str(e)}')
            return False

if __name__ == "__main__":
    """主程式函數"""
    
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
    with open(config_dir / 'email.txt', 'r') as f:
        text_content = f.read()
    with open(config_dir / 'email.html', 'r') as f:
        html_content = f.read()
    
    # 設定郵件主題和收件人檔案
    subject = f'大蟒蛇日誌'
    recipients_file = config_dir / 'email_list.txt'
    
    # 發送郵件
    publisher.send_email(subject, text_content, html_content, recipients_file)

    
