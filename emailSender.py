"""
使用 Gmail 帳號發送純文字電子郵件的範例
功能說明：
1. 從檔案讀取收件人清單（每行一個電子郵件地址）
2. 從檔案讀取電子郵件內容
3. 使用 SSL 加密連接發送電子郵件

使用前提：
1. 發件人的 Gmail 帳號需要：
    a) 啟用兩步驗證
    b) 創建應用程式密碼
2. 可以使用 temp-mail.org 生成的臨時電子郵件作為收件人
"""

# 引入必要的套件
from email.message import EmailMessage
import ssl
import smtplib
from pathlib import Path
import logging
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 設置日誌記錄系統
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # 設置日誌等級為 INFO

# 定義日誌格式
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# 獲取當前 Python 檔案的目錄
base_dir = Path(__file__).parent
log_dir = base_dir / 'logger'  # 日誌檔案存放目錄

# 如果日誌目錄不存在，則創建它
os.makedirs(log_dir, exist_ok=True)

# 指定日誌檔案路徑
log_file = os.path.join(log_dir, 'email.log')
file_handler = logging.FileHandler(log_file, mode='w')  # 使用 'w' 模式覆寫日誌檔案
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# 檔案路徑設定
class Config:
    """程式設定類別，用於存放所有檔案路徑"""
    BASE_DIR = Path(__file__).parent / 'sample'  # 相對於當前目錄的路徑
    
    # 各種檔案的路徑
    EMAIL_PASSWORD_FILE = BASE_DIR / 'email_password.txt'
    SENDER_EMAIL_FILE = BASE_DIR / 'email_sender.txt'
    RECEIVER_LIST_FILE = BASE_DIR / 'email_list.txt'
    EMAIL_CONTENT_FILE = BASE_DIR / 'email.txt'


def read_file_content(file_path):
    """讀取檔案內容的輔助函數
    
    Args:
        file_path (str): 要讀取的檔案路徑
        
    Returns:
        str: 檔案內容
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        # 讀取所有行，去除空白行和空白字符
        lines = [line.strip() for line in file if line.strip()]
        # 如果有多行，用換行符連接
        return '\n'.join(lines) if lines else ''

def get_recipients_list(file_path):
    """從檔案讀取收件人清單
    
    Args:
        file_path (str): 收件人清單檔案路徑
        
    Returns:
        list: 收件人電子郵件地址清單
    """
    content = read_file_content(file_path)
    return [email.strip() for email in content.split('\n') if email.strip()]

def create_email_message(sender, recipients, subject, body):
    """構建電子郵件訊息
    
    Args:
        sender (str): 發件人電子郵件地址
        recipients (list): 收件人電子郵件地址清單
        subject (str): 電子郵件主旨
        body (str): 電子郵件內容
        
    Returns:
        EmailMessage: 構建好的電子郵件訊息物件
    """
    message = EmailMessage()
    message['From'] = sender
    message['To'] = ", ".join(recipients)
    message['Subject'] = subject
    message.set_content(body, subtype='plain', charset='utf-8')
    return message

def send_email(sender, password, recipients, message):
    """發送電子郵件"""
    try:
        logging.info(f"開始連接 SMTP 伺服器...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            logging.info(f"正在登入發件人信箱...")
            # 使用 base64 編碼處理密碼
            import base64
            encoded_password = base64.b64encode(password.encode('ascii', errors='ignore')).decode('ascii')
            smtp.login(sender, encoded_password)
            
            logging.info(f"開始發送郵件至 {len(recipients)} 個收件人...")
            for recipient in recipients:
                try:
                    # 確保訊息內容使用 UTF-8 編碼
                    if isinstance(message, str):
                        message = message.encode('utf-8')
                    smtp.send_message(message)
                    logging.info(f"成功發送郵件至: {recipient}")
                except Exception as e:
                    logging.error(f"發送郵件至 {recipient} 失敗: {str(e)}")
                    raise
            
            logging.info("所有郵件發送完成")
            
    except Exception as e:
        logging.error(f"發送郵件失敗: {str(e)}")
        raise

def main():
    """主函數，負責協調整個發送流程"""
    try:
        logging.info("開始郵件發送流程")
        
        # 讀取所有必要的資訊
        logging.info("讀取配置文件...")
        email_password = read_file_content(Config.EMAIL_PASSWORD_FILE)
        email_sender = read_file_content(Config.SENDER_EMAIL_FILE)
        recipients = get_recipients_list(Config.RECEIVER_LIST_FILE)
        email_body = read_file_content(Config.EMAIL_CONTENT_FILE)
        
        # 建立電子郵件主旨
        subject = f'檔案內容：{Config.EMAIL_CONTENT_FILE}'
        logging.info(f"郵件主旨設定為：{subject}")
        
        # 建立並發送電子郵件
        logging.info("正在建立電子郵件...")
        email_message = create_email_message(
            email_sender,
            recipients,
            subject,
            email_body
        )
        
        logging.info("開始發送電子郵件...")
        send_email(email_sender, email_password, recipients, email_message)
        logging.info("郵件發送完成")
        
    except Exception as e:
        logging.error(f"郵件發送流程失敗: {str(e)}")
        print(f'錯誤：無法發送電子郵件\n')
        raise
if __name__ == '__main__':
    main()
