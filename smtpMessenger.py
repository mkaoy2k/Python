'''Python Messenger container class

利用 'email', 'ssl' 及 'smtplib' 模組來生成並傳送電子郵件。
並透過 SMTP/SMS 門户服務器 (gateway) 發送簡訊。

### 傳送電子郵件前置作業:

1. 必備可傳送電子郵件帳號 (以下例子我們安装 Gmail 来展示) 。並且按照 Google 規定，郵件帳號必須配置如下：
    - 設定成 two-step confirmation
    - 建立一個 app password
2. 必備可接收電子郵件帳號 (以下例子我們用 Apple iCloud email 来展示) 。


Provided Functions: -> Example usage below
    - open_conn()
    - close_conn()
    - send_txt(msg, one_time=False)
    - send_email(msg, one_time=False)
            
EXAMPLES:
    ----------------------------------------------------------------------------
    Example usage (one_time): -> cleaner code if sending one message
        my_messenger = Messenger(<your gmail username>, <your gmail password>)
        msg = SMS(number, gateway, subject, body)
        my_messenger.send_sms(msg, one_time=True)
        msg = Email(to, subject, body)
        my_messenger.send_email(msg, one_time=True)

    Example usage (not one_time): -> faster for sending lots of messages
        my_messenger = Messenger(<your gmail username>, <your gmail password>)
        my_messenger.open_conn()
        # send as many messages as you want here
        msg = SMS(number, gateway, subject, body)
        my_messenger.send_sms(msg)
        msg = Email(to, subject, body)
        my_messenger.send_email(msg)
        my_messenger.close_conn()
        
SMS GATEWAYS
    ----------------------------------------------------------------------------
    AT&T: [number]@txt.att.net
    Sprint: [number]@messaging.sprintpcs.com or [number]@pm.sprint.com
    T-Mobile: [number]@tmomail.net
    Verizon: [number]@vtext.com
    Boost Mobile: [number]@myboostmobile.com
    Cricket: [number]@sms.mycricket.com
    Metro PCS: [number]@mymetropcs.com
    Tracfone: [number]@mmst5.tracfone.com
    U.S. Cellular: [number]@email.uscc.net
    Virgin Mobile: [number]@vmobl.com
    
SMTP server names
    ----------------------------------------------------------------------------
    Gmail                        smtp.gmail.com  (port 465)
    Outlook.com/Hotmail.com      smtp-mail.outlook.com
    Yahoo Mail                   smtp.mail.yahoo.com
    AT&T                         smpt.mail.att.net (port 465)
    Comcast                      smtp.comcast.net
    Verizon                      smtp.verizon.net (port 465)
'''

# Using 'smtplib' module to create an SMTP client session object that
# sends an email to any SMTP server
import smtplib

import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dataclasses import dataclass


@dataclass
class Email:
    to: str
    subject: str
    body: str
    is_HTML: bool = False


@dataclass
class SMS:
    number: str
    gateway: str
    subject: str
    body: str

    @property
    def recipient(self) -> str:
        return self.number + self.gateway


'''
    Messenger Class
'''


@dataclass
class Messenger:
    username: str  # ALSO THE FROM ADDRESS
    password: str
    conn: smtplib.SMTP_SSL = None

    def open_conn(self):
        # CREATE SSL CONNECTION TO SMTP SERVICE
        context = ssl.create_default_context()
        self.conn = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
        self.conn.login(self.username, self.password)

    def close_conn(self):
        # CLOSE CONNECTION TO SMTP SERVICE
        self.conn.close()

    def send_sms(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # 組合簡訊郵件訊息
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.recipient
        message["Subject"] = msg.subject
        message.attach(MIMEText(msg.body, "plain"))

        # 送出簡訊郵件訊息
        self.conn.sendmail(self.username, msg.recipient, message.as_string())

        if one_time:
            self.close_conn()

    def send_email(self, msg, one_time=False):
        if one_time:
            self.open_conn()

        # 組合郵件訊息
        message = MIMEMultipart("alternative")
        message["From"] = self.username
        message["To"] = msg.to
        message["Subject"] = msg.subject
        if msg.is_HTML:
            message.attach(MIMEText(msg.body, "html"))
        else:
            message.attach(MIMEText(msg.body, "plain"))

        # 送出郵件訊息
        self.conn.sendmail(self.username, msg.to, message.as_string())

        if one_time:
            self.close_conn()


# Example
if __name__ == '__main__':

    # 設定資料夾位置及檔案名稱
    path_dir = 'sample'  # relative to the current dir
    file_pw = f'{path_dir}/email_password.txt'
    file_sender = f'{path_dir}/email_sender.txt'
    file_receiver = f'{path_dir}/email_receiver.txt'
    file_text = f'{path_dir}/test.txt'
    file_html = f'{path_dir}/test.html'

    with open(file_pw, 'r') as f:
        email_password = f.read().strip()
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
        print(f'從郵件信箱 {email_sender} 已送出 HTML 郵件...')
        print(f'===> 請到郵件信箱 {email_receiver} 檢視郵件')
        print(f'===> 郵件標題 : {subject}\n')
    except:
        print(f'send_email(): 無法送出郵件\n')

    # 組合簡訊郵件
    from sample.credentials import mobile_number, SMSgateway, SMSmsg
    subject = "test SMS from Michael Kao"
    body = SMSmsg

    msg = SMS(mobile_number, SMSgateway, subject, body)

    # 送出簡訊郵件
    try:
        my_messenger.send_sms(msg, one_time=True)
        print(f'從郵件信箱 {email_sender} 已送出簡訊郵件...')
        print(f'===> 經 {SMSgateway} smtp/sms 門户服務器')
        print(f'請到手機上 {mobile_number} 檢視簡訊')
        print(f'===> 簡訊標題 : {subject}\n')
    except:
        print(f'send_sms(): 無法送出簡訊郵件\n')
