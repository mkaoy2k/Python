'''Python Messenger 容器類別

利用 'email', 'ssl' 及 'smtplib' 模組來生成並傳送電子郵件，
並透過 SMTP/SMS 門戶服務器發送簡訊。

主要功能:
    - 開啟和關閉 SMTP 連接
    - 發送純文字郵件
    - 發送 HTML 格式郵件
    - 發送簡訊 (透過 SMTP 門戶服務器)

使用範例:
    # 單次發送 (較簡潔)
    my_messenger = Messenger(電子郵件帳號, 密碼)
    msg = SMS(手機號碼, 門戶服務器, 主旨, 內文)
    my_messenger.send_sms(msg, one_time=True)
    msg = Email(收件人, 主旨, 內文)
    my_messenger.send_email(msg, one_time=True)

    # 多次發送 (較快速)
    my_messenger = Messenger(電子郵件帳號, 密碼)
    my_messenger.open_conn()
    # 在此發送多封郵件
    msg = SMS(手機號碼, 門戶服務器, 主旨, 內文)
    my_messenger.send_sms(msg)
    msg = Email(收件人, 主旨, 內文)
    my_messenger.send_email(msg)
    my_messenger.close_conn()

簡訊門戶服務器:
    AT&T: [號碼]@txt.att.net
    Sprint: [號碼]@messaging.sprintpcs.com 或 [號碼]@pm.sprint.com
    T-Mobile: [號碼]@tmomail.net
    Verizon: [號碼]@vtext.com
    Boost Mobile: [號碼]@myboostmobile.com
    Cricket: [號碼]@sms.mycricket.com
    Metro PCS: [號碼]@mymetropcs.com
    Tracfone: [號碼]@mmst5.tracfone.com
    U.S. Cellular: [號碼]@email.uscc.net
    Virgin Mobile: [號碼]@vmobl.com

SMTP 伺服器:
    Gmail: smtp.gmail.com (port 465)
    Outlook.com/Hotmail.com: smtp-mail.outlook.com
    Yahoo Mail: smtp.mail.yahoo.com
    AT&T: smpt.mail.att.net (port 465)
    Comcast: smtp.comcast.net
    Verizon: smtp.verizon.net (port 465)

注意事項:
1. 使用 Gmail 發送郵件時，必須:
    - 啟用兩步驟驗證
    - 建立應用程式密碼
2. 建議使用 .env 檔案來管理敏感資訊 (帳號、密碼等)
'''

# Using 'smtplib' module to create an SMTP client session object that
# sends an email to any SMTP server
import smtplib

import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass

from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

@dataclass
class Email:
    '''電子郵件訊息類別
    
    Attributes:
        to (str): 收件人電子郵件地址
        subject (str): 郵件主旨
        body (str): 郵件內容
        is_HTML (bool, optional): 是否為 HTML 格式郵件。預設為 False
    '''
    to: str
    subject: str
    body: str
    is_HTML: bool = False


@dataclass
class SMS:
    '''簡訊訊息類別
    
    Attributes:
        number (str): 手機號碼
        gateway (str): SMTP 門戶服務器地址
        subject (str): 簡訊主旨
        body (str): 簡訊內容
    '''
    number: str
    gateway: str
    subject: str
    body: str

    @property
    def recipient(self) -> str:
        '''組合完整的簡訊收件人地址
        
        Returns:
            str: 完整的收件人地址 (手機號碼 + 門戶服務器)
        '''
        return self.number + self.gateway


@dataclass
class Messenger:
    '''郵件發送器類別
    
    Attributes:
        username (str): 發件人電子郵件地址
        password (str): 郵件伺服器登入密碼
        conn (smtplib.SMTP_SSL): SMTP 連接物件
    '''
    username: str
    password: str
    conn: smtplib.SMTP_SSL = None

    def open_conn(self):
        '''建立 SMTP 連接
        
        使用 SSL 加密連接到 Gmail SMTP 伺服器
        '''
        context = ssl.create_default_context()
        self.conn = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        self.conn.login(self.username, self.password)

    def close_conn(self):
        '''關閉 SMTP 連接
        '''
        if self.conn:
            self.conn.close()

    def send_sms(self, msg: SMS, one_time: bool = False):
        '''發送簡訊
        
        Args:
            msg (SMS): 簡訊訊息物件
            one_time (bool, optional): 是否為單次發送。預設為 False
        '''
        if one_time:
            self.open_conn()

        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.recipient
        message["Subject"] = msg.subject
        message.attach(MIMEText(msg.body, "plain"))
        
        self.conn.sendmail(self.username, msg.recipient, message.as_string())
        
        if one_time:
            self.close_conn()

    def send_email(self, msg: Email, one_time: bool = False):
        '''發送電子郵件
        
        Args:
            msg (Email): 郵件訊息物件
            one_time (bool, optional): 是否為單次發送。預設為 False
        '''
        if one_time:
            self.open_conn()

        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.to
        message["Subject"] = msg.subject
        
        if msg.is_HTML:
            message.attach(MIMEText(msg.body, "html"))
        else:
            message.attach(MIMEText(msg.body, "plain"))
        
        self.conn.sendmail(self.username, msg.to, message.as_string())
        
        if one_time:
            self.close_conn()


# Example
if __name__ == '__main__':

    # 設定資料夾位置及檔案名稱
    path_dir = 'sample'  # relative to the current dir
    file_sender = f'{path_dir}/email_sender.txt'
    file_receiver = f'{path_dir}/email_receiver.txt'
    file_text = f'{path_dir}/test.txt'
    file_html = f'{path_dir}/test.html'

    # 從環境變數讀取密碼
    email_password = os.getenv('PASSWORD')
    if not email_password:
        raise ValueError("環境變數 PASSWORD 未設定")

    with open(file_sender, 'r') as f:
        email_sender = f.read().strip()

    my_messenger = Messenger(email_sender, email_password)

    # 組合 TXT 郵件
    with open(file_receiver, 'r') as f:
        email_receiver = f.read().strip()
    with open(file_text, 'r') as f:
        body = f.read().strip()
    subject = f'The Contents of {file_text}'
    msg = Email(email_receiver, subject, body, is_HTML=False)

    # 送出 TXT 郵件
    try:
        my_messenger.send_email(msg, one_time=True)
        print(f'從郵件信箱 {email_sender} 已送出郵件...')
        print(f'===> 請到郵件信箱 {email_receiver} 檢視郵件')
        print(f'===> 郵件標題 : {subject}\n')
    except:
        print(f'send_email(): 無法送出郵件\n')

    # 組合 HTML 郵件
    with open(file_html, 'r') as f:
        html = f.read().strip()

    subject = f'The Contents of {file_html}'
    msg = Email(email_receiver, subject, html, is_HTML=True)

    # 送出 HTML 郵件
    try:
        my_messenger.send_email(msg, one_time=True)
        print(f'從郵件信箱 {email_sender} 已發佈郵件...')
        print(f'===> 請到郵件信箱 {email_receiver} 檢視郵件')
        print(f'===> 郵件標題 : {subject}\n')
    except:
        print(f'send_email(): 無法送出郵件\n')

    # 組合簡訊郵件
    mobile_number = os.getenv('SMS_MOBILE_NUMBER')
    SMSgateway = os.getenv('SMS_GATEWAY')
    SMSmsg = os.getenv('SMS_MESSAGE')
    subject = "test SMS from Michael Kao"
    body = SMSmsg

    msg = SMS(mobile_number, SMSgateway, subject, body)

    # 送出簡訊郵件
    try:
        my_messenger.send_sms(msg, one_time=True)
        print(f'從郵件信箱 {email_sender} 已送出簡訊郵件...')
        print(f'===> 經 {SMSgateway} smtp/sms 門戶服務器')
        print(f'請到手機上 {mobile_number} 檢視簡訊')
        print(f'===> 簡訊標題 : {subject}\n')
    except:
        print(f'send_sms(): 無法送出簡訊郵件\n')
