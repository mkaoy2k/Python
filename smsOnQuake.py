from smsViaSMTP import Messenger, SMS
from quake import get_earthquake_data
from datetime import date, timedelta
from dotenv import load_dotenv
import os

# 載入環境變數
load_dotenv()

def main():
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    my_messenger = Messenger(email_sender, email_password)
    sms_number = os.getenv('SMS_MOBILE_NUMBER')
    sms_gateway = os.getenv('SMS_GATEWAY')
    sms_subject = os.getenv('SMS_SUBJECT')
    
    earthquake_data = get_earthquake_data()
    quake_magnitude = float(os.getenv('QUAKE_MAGNITUDE', 4.0))
    eq = earthquake_data.get('records', {}).get('Earthquake', [])
    yesterday = date.today() - timedelta(days=1)

    for event in eq:
        try:
            loc = event['EarthquakeInfo']['Epicenter']['Location']
            val = float(event['EarthquakeInfo']['EarthquakeMagnitude']['MagnitudeValue'])
            dep = event['EarthquakeInfo']['FocalDepth']
            eq_time = event['EarthquakeInfo']['OriginTime']

            msg = f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}'
            print(msg)

            if val >= quake_magnitude:
                date_occured = date.fromisoformat(eq_time.split(' ')[0])
                if date_occured in [yesterday, date.today()]:
                    sms = SMS(sms_number, sms_gateway, sms_subject, msg)
                    print(f'===> {val} 級地震，簡訊通知地震位置圖...')
                    try:
                        my_messenger.send_sms(sms, one_time=True)
                        print(f'===> {val} 級地震，已簡訊通知地震位置圖！')
                    except Exception as e:
                        print(f"發送簡訊時發生錯誤：{str(e)}")
        except (KeyError, ValueError) as e:
            print(f"處理地震資料時發生錯誤：{str(e)}")
            
if __name__ == "__main__":
    main()