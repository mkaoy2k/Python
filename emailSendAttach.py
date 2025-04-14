"""使用 'email', 'ssl' 及 'smtplib' 模組發送可附帶檔案的郵件
本程式示範如何透過 Google 電子郵件帳號發送帶有附件的郵件
"""

import os
from pathlib import Path
import logging
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
from dataclasses import dataclass
from dotenv import load_dotenv

# 設置日誌系統
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class EmailConfig:
    """郵件配置類別
    用於存放所有郵件相關的配置信息
    """
    sender: str  # 發件人電子郵件地址
    receiver: str  # 收件人電子郵件地址
    password: str  # 發件人電子郵件密碼
    subject: str  # 郵件主題
    text_content: str  # 文字內容
    html_content: str  # HTML 內容
    attachment_path: str  # 附件檔案路徑
    
    @classmethod
    def from_files(cls, config_dir: str = 'sample') -> 'EmailConfig':
        """從配置檔案讀取郵件設定
        
        Args:
            config_dir (str): 配置檔案所在目錄
            
        Returns:
            EmailConfig: 包含所有配置信息的物件
        """
        current_dir = Path(__file__).parent
        config_dir = current_dir / config_dir
        load_dotenv()
        password = os.getenv('PASSWORD')
        if not password:
            raise ValueError("環境變數 PASSWORD 未設定")
        
        return cls(
            sender=config_dir.joinpath('email_sender.txt').read_text().strip(),
            receiver=config_dir.joinpath('email_receiver.txt').read_text().strip(),
            password=password,
            subject=f'The Contents of email.html with attachment',
            text_content=config_dir.joinpath('email.txt').read_text(),
            html_content=config_dir.joinpath('email.html').read_text(),
            attachment_path=str(config_dir.joinpath('Olisan.JPG'))
        )

class EmailSender:
    """郵件發送類別
    負責建立和發送郵件
    """
    
    def __init__(self, config: EmailConfig):
        """初始化郵件發送器
        
        Args:
            config (EmailConfig): 包含郵件配置的物件
        """
        self.config = config
        self.smtp_server = 'smtp.gmail.com'  # Gmail SMTP 伺服器
        self.smtp_port = 465  # SSL 連接埠號
        
    def create_email_message(self) -> MIMEMultipart:
        """建立郵件訊息
        
        Returns:
            MIMEMultipart: 包含所有郵件內容的物件
        """
        msg = MIMEMultipart("alternative")
        msg['From'] = self.config.sender
        msg['To'] = self.config.receiver
        msg['Subject'] = self.config.subject
        
        # 添加文字內容
        text_part = MIMEText(self.config.text_content, "plain")
        msg.attach(text_part)
        
        # 添加 HTML 內容
        html_part = MIMEText(self.config.html_content, "html")
        msg.attach(html_part)
        
        # 添加附件
        try:
            with open(self.config.attachment_path, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(self.config.attachment_path)}"
                )
                msg.attach(part)
        except FileNotFoundError:
            logger.warning(f"附件檔案 {self.config.attachment_path} 不存在")
            
        return msg
        
    def send_email(self) -> bool:
        """發送郵件
        
        Returns:
            bool: 發送是否成功
        """
        try:
            msg = self.create_email_message()
            
            with smtplib.SMTP_SSL(
                self.smtp_server, 
                self.smtp_port, 
                context=ssl.create_default_context()
            ) as server:
                server.login(self.config.sender, self.config.password)
                server.sendmail(
                    self.config.sender,
                    self.config.receiver,
                    msg.as_string()
                )
                
            logger.info(f"已成功發送郵件到 {self.config.receiver}")
            logger.info(f"郵件標題: {self.config.subject}")
            return True
            
        except Exception as e:
            logger.error(f"發送郵件時發生錯誤: {str(e)}")
            return False

def main():
    """主程式函數
    負責初始化配置並發送郵件
    """
    try:
        # 從配置檔案讀取郵件設定
        config = EmailConfig.from_files()
        
        # 創建並發送郵件
        email_sender = EmailSender(config)
        if email_sender.send_email():
            print("\n郵件發送成功！")
        else:
            print("\n郵件發送失敗！")
            
    except Exception as e:
        logger.error(f"程式執行時發生錯誤: {str(e)}")
        raise

if __name__ == "__main__":
    main()
