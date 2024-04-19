"""This example demonstrate sending an email via Google email account
with attached file.
用 'email', 'ssl' 及 'smtplib' 這些模組發送可附帶檔案的郵件。
"""

# Import email packages
# import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import ssl

# Using 'smtplib' module to create an SMTP client session object that
# sends an email to any SMTP server
import smtplib

# 設定資料夾位置及檔案名稱
path_dir = 'sample'  # relative to the current dir
file_pw = f'{path_dir}/email_password.txt'
file_sender = f'{path_dir}/email_sender.txt'
file_receiver = f'{path_dir}/email_receiver.txt'
file_text = f'{path_dir}/email.txt'
file_html = f'{path_dir}/email.html'
file_attached = f'{path_dir}/Olisan.JPG'

with open(file_pw, 'r') as f:
    email_password = f.read()
with open(file_sender, 'r') as f:
    email_sender = f.read()
with open(file_receiver, 'r') as f:
    email_receiver = f.read()
with open(file_text, 'r') as f:
    text = f.read()
with open(file_html, 'r') as f:
    html = f.read()

subject = f'The Contents of {file_html} with attachment'

# Compose the email object combines these into a signle email message with
# two alternative rendering options.
em = MIMEMultipart("alternative")
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

# Compose Text part
part1 = MIMEText(text, "plain")

# Compose HTML part
part2 = MIMEText(html, "html")

# Add plain and html parts to MIMEMultipart message
# The recipiant client will try to render the last part first
em.attach(part1)
em.attach(part2)

# Add attachment
with open(file_attached, "rb") as attachment:
    part3 = MIMEBase("application", "octet-stream")
    part3.set_payload(attachment.read())

# encode the above part
encoders.encode_base64(part3)

# Add specific content header to the attachment
part3.add_header("Content-Disposition", "attachment", filename=file_attached)
em.attach(part3)

# Create SMTP connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    # 送出 HTML 郵件
    try:
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f'從郵件信箱 {email_sender} 已送出 HTML 郵件...')
        print(f'===> 請到郵件信箱 {email_receiver} 檢視郵件')
        print(f'===> 郵件標題 : {subject}\n')
    except Exception as err:
        print(f"Caught '{err}'. class is {type(err)}")
        print(f'send_email(): 無法送出郵件\n')
