"""
發送 HTML 電子郵件的範例
功能：
1. 通過 Google 帳號發送帶有純文本和 HTML 內容的電子郵件
2. 支持使用臨時郵箱作為接收方
注意事項：
1. 發件人 Google 帳號需要配置：
   - 開啟兩步驗證
   - 創建應用程式密碼
2. 所有敏感信息（密碼等）都存儲在配置文件中
"""

import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib
from pathlib import Path
from dotenv import load_dotenv
import os

def read_config(file_path: str) -> str:
    """
    讀取配置文件內容
    
    Args:
        file_path: 配置文件路徑
        
    Returns:
        文件內容
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            logging.debug(f"成功讀取配置文件: {file_path}")
            return content
    except Exception as e:
        logging.error(f"讀取配置文件失敗: {file_path}, 錯誤: {str(e)}")
        raise

def create_email_message(sender: str, receiver: str, subject: str, text: str, html: str) -> MIMEMultipart:
    """
    創建電子郵件訊息
    
    Args:
        sender: 發件人地址
        receiver: 收件人地址
        subject: 郵件主題
        text: 純文本內容
        html: HTML 內容
        
    Returns:
        構建好的郵件訊息對象
    """
    try:
        # 創建多部分郵件訊息
        message = MIMEMultipart("alternative")
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject
        
        # 添加純文本部分
        part1 = MIMEText(text, "plain")
        # 添加 HTML 部分
        part2 = MIMEText(html, "html")
        
        # 附加到郵件訊息
        message.attach(part1)
        message.attach(part2)
        
        logging.info("成功創建郵件訊息")
        return message
    except Exception as e:
        logging.error(f"創建郵件訊息失敗: {str(e)}")
        raise

def send_email(message: MIMEMultipart, sender: str, password: str, receiver: str) -> None:
    """
    發送電子郵件
    
    Args:
        message: 郵件訊息對象
        sender: 發件人地址
        password: 發件人密碼
        receiver: 收件人地址
    """
    try:
        # 創建 SSL 上下文
        context = ssl.create_default_context()
        
        # 連接到 Gmail SMTP 伺服器
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, message.as_string())
            
            logging.info(f"成功發送郵件：")
            logging.info(f"發件人: {sender}")
            logging.info(f"收件人: {receiver}")
            
            print(f"===\u003e 請檢查來自 {receiver} 的郵件")
            print(f"===\u003e 主題: {message['Subject']}\n")
            
    except Exception as e:
        logging.error(f"發送郵件失敗: {str(e)}")
        raise

def main():
    """
    主函數：執行郵件發送流程
    """
    try:
        # 設置日誌
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('email_log.log'),
                logging.StreamHandler()
            ]
        )

        # 初始化登入參數，從 'sample' 資料夾中的文件讀取
        path_dir = Path(__file__).parent / 'sample'
        file_sender = path_dir / 'email_sender.txt'
        file_receiver = path_dir / 'email_list.txt'
        file_text = path_dir / 'email.txt'
        file_html = path_dir / 'email.html'
        
        # 加載環境變數
        load_dotenv()
        email_password = os.getenv('PASSWORD')
        if not email_password:
            raise ValueError("環境變數 PASSWORD 未設定")
        
        # 讀取配置文件
        email_sender = read_config(file_sender)
        email_list = read_config(file_receiver)  # 修改變數名稱
        text = read_config(file_text)
        html = read_config(file_html)
        
        # 創建郵件主題
        subject = f'內容來自 {file_html}'
        
        # 創建並發送郵件
        message = create_email_message(email_sender, email_list, subject, text, html)
        # 讀取收件人列表
        with open(file_receiver, 'r') as f:
            recipients = [line.strip() for line in f if line.strip()]
        
        # 為每個收件人發送郵件
        for recipient in recipients:
            try:
                send_email(message, email_sender, email_password, recipient)
                logging.info(f"成功發送郵件至: {recipient}")
            except Exception as e:
                logging.error(f"發送郵件至 {recipient} 失敗: {str(e)}")
                print(f"錯誤: 無法發送郵件至 {recipient}\n")
    except Exception as e:
        logging.error(f"郵件發送流程失敗: {str(e)}")
        print(f"錯誤: 無法發送郵件\n")

if __name__ == "__main__":
    main()
