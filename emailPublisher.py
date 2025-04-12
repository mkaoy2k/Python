"""
這個範例示範如何使用 Google 電子郵件帳戶
發送 HTML 格式的郵件給多個收件人，收件人列表存放在文字檔案中，每行一個電子郵件地址。
試著同時發送一份郵件給一群人。
"""

from typing import List
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
from pathlib import Path
import logging

# 設置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EmailPublisher:
    def __init__(self, config_dir: str):
        """初始化 EmailPublisher 類別，讀取發件人和密碼"""
        current_dir = Path(__file__).parent
        self.config_dir = current_dir / config_dir
        self.email_sender = self._read_file('email_sender.txt')
        self.email_password = self._read_file('email_password.txt')
        
    def _read_file(self, filename: str) -> str:
        """從設定目錄讀取檔案內容"""
        file_path = self.config_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"找不到檔案: {file_path}")
        with open(file_path, 'r') as f:
            return f.read().strip()

    def _get_recipients(self, recipients_file: str) -> List[str]:
        """讀取並解析收件人列表檔案"""
        file_path = self.config_dir / recipients_file
        with open(file_path, 'r') as f:
            return [email.strip() for email in f.read().splitlines() if email.strip()]

    def _create_email(self, subject: str, text: str, html: str, recipients: List[str]) -> MIMEMultipart:
        """建立包含文字和 HTML 兩種格式的電子郵件訊息"""
        msg = MIMEMultipart("alternative")
        msg['From'] = self.email_sender
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        # 添加文字和 HTML 部分
        msg.attach(MIMEText(text, "plain"))
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
                    logger.error("3. 您的 email_password.txt 檔案中是否包含正確的應用程式密碼")
                    return False
                except Exception as e:
                    logger.error(f'send_email(): 發送郵件時發生錯誤: {str(e)}')
                    return False
        except Exception as e:
            logger.error(f'send_email(): 發生一般錯誤: {str(e)}')
            return False

def main():
    """主程式函數"""
    # 設定設定檔目錄位置
    current_dir = Path(__file__).parent
    config_dir = current_dir / 'sample'
    
    # 初始化 EmailPublisher
    publisher = EmailPublisher(config_dir)
    
    # 讀取郵件內容
    with open(config_dir / 'email.txt', 'r') as f:
        text_content = f.read()
    with open(config_dir / 'email.html', 'r') as f:
        html_content = f.read()
    
    # 設定郵件主題
    subject = f'小朋友玩大蟒蛇日誌'
    
    # 發送郵件
    publisher.send_email(subject, text_content, html_content, 'email_list.txt')

if __name__ == "__main__":
    main()
