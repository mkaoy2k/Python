"""This example demonstrate to ping a HTTP server to check if
it is still responding.
藉著訪問 HTTP 伺服器的網址測試其是否正常回應。
"""

import urllib.request as ur
import time


def ping(url):
    print("訪問開始...")

    try:
        response = ur.urlopen(url)
        if response.getcode() == 200:
            print(f'===>訪問結果: {url} 正常！\n')

    except:
        print(f'===>訪問結果: {url} 不正常！\n')


print("測試網址是否正常回應...")
input_url = input("請輸入網址: ")
if input_url == "":
    # default to my github site
    input_url = 'https://github.com/mkaoy2k/Kids-Lets-Play-Python'

print(f"網址是: {input_url}")

# 每隔10秒測試一次，共三次
print(f"每隔10秒測試一次，共三次...")
for i in range(1, 4):
    print(f"測試 {i}")
    ping(input_url)
    time.sleep(10)
