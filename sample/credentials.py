"""----------------------------------------------------------------------------
The following parms are used by qrCode.py
"""
qr_url = 'https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/e966378bd5aab2e9f15c1bf194189d17a6f1da7c/2.1%20%E5%B0%8F%E6%9C%8B%E5%8F%8B%E7%8E%A9%E5%A4%A7%E8%9F%92%E8%9B%87%20Chapter1%20ebook.pdf'
qr_file = 'sample/QRCode.png'

"""
The following parms are used by lineSend.py and Python Club apps 
via LINE-Notify service
nWCFwof6qNiYJGd8rpcu9zqdgkms0Ilax3Tfqf7Hya6
    To: misosushi
NeqyZhxSEFlWWVh6Y2NZApFvCuWc3GG3J0zhQ93yewn
    To: 玉山國中1972級

CWB-C515B0FE-D9E4-472F-9DAE-BFCC71CD3467
    中央氣象局會員之授權碼
https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization=CWB-C515B0FE-D9E4-472F-9DAE-BFCC71CD3467&format=JSON

"""
line_gw_url = 'https://notify-api.line.me/api/notify'
line_my_token = 'nWCFwof6qNiYJGd8rpcu9zqdgkms0Ilax3Tfqf7Hya6'
line_my_name = 'misosushi'
line_fileMsg = 'sample/line_msg.txt'

# The follwoing parms used by Python-Bot app originally, but got some Jupyter notebook failed to read during import
# workaround: created the credentials in a separated file, called "line_credentials.py"
# line_chToken = 'ERE+6F/pg4t+H5BTPmncPDmvXM5AEouRY06mMYDez+VfRSXrbx+5RcSAg/bbqAjbnbD5DBlm2/k/aDkG9Tv16Qh1IsTXjUUBqRrni6DgTI2gp/7fKFGSWfXLecv34Fo2QVlRXItfuh9YDoYHik6GCAdB04t89/1O/w1cDnyilFU='
# line_chSecret = '0c68feab867f502cd30564af990d6c02'

"""----------------------------------------------------------------------------
The following parms are used by lineQuake.py

爬取台灣中央氣象局會地震資訊及位置圖
使用 Requests 函式庫的 get 的方法，抓取氣象觀測資料的 JSON 網址:
https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=rdec-key-123-45678-011121314

接著使用字典的取值方法，搭配 for-迴圈印出某一地震强度以上 (如4.0)
城市名稱、區域名稱和觀測點名稱。

"""
quake_url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=rdec-key-123-45678-011121314'
quake_magnitude = 4.0
line_pc_token = 'NeqyZhxSEFlWWVh6Y2NZApFvCuWc3GG3J0zhQ93yewn'
line_pc_name = '玉山國中1972級'

"""----------------------------------------------------------------------------
The following parms are used by both smtpMessenger.py and httpSMS.py
"""
mobile_number = "4088969982"
# Heather
# mobile_number = "4088384519"
# Jeff Liaw
# mobile_number = "4084726611"

mobile_number_cc = "14088969982"

"""SMS Gateways:
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
"""
SMSgateway = "@txt.att.net"
SMSmsg = "Pls visit https://github.com/mkaoy2k/Kids-Lets-Play-Python"

# end of file
