"""
This example demonstrate sending an html email via Google email account
to multiple recipients, contained in a text file, that has one email per line.
試著同時發送一份郵件給一群人。
"""

# Import email packages
import email
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
file_receiver = f'{path_dir}/email_list.txt'
file_text = f'{path_dir}/email.txt'
file_html = f'{path_dir}/email.html'

with open(file_pw, 'r') as f:
    email_password = f.read()
with open(file_sender, 'r') as f:
    email_sender = f.read()

with open(file_receiver, 'r') as f:
    # Read in as a tring, stripping off leading and trailing spaces and '\n'
    emails_str = f.read().strip()

    # Split into a list, with one email per element
    recipients = emails_str.split("\n")

with open(file_text, 'r') as f:
    text = f.read()
with open(file_html, 'r') as f:
    html = f.read()

subject = f'The Contents of {file_html}'

# Compose the email object combines these into a signle email message with
# two alternative rendering options.
em = MIMEMultipart("alternative")
em['From'] = email_sender
em['To'] = ", ".join(recipients)
em['Subject'] = subject

# Compose Text part
part1 = MIMEText(text, "plain")

# Compose HTML part
part2 = MIMEText(html, "html")

# Add plain and html parts to MIMEMultipart message
# The recipiant client will try to render the last part first
em.attach(part1)
em.attach(part2)

# Create SMTP connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    # 送出 HTML 郵件
    try:
        smtp.sendmail(email_sender, recipients, em.as_string())
        print(f'從郵件信箱 {email_sender} 已送出 HTML 郵件...')
        print(f'===> 請到所有的郵件信箱 {recipients} 檢視郵件')
        print(f'===> 郵件標題 : {subject}\n')
    except:
        print(f'send_email(): 無法送出郵件\n')
