"""
使用快取來優化 HTTP 請求的範例
這個範例展示了如何使用快取來避免重複的 HTTP 請求，
從而提高應用程式的性能。
"""

import requests
import random
from cacheLib import Cache


def get_url(url):
    """
    獲取指定 URL 的內容，優先從快取中取得
    
    參數:
    url (str): 要訪問的 URL
    
    回傳:
    str: URL 的內容
    
    備註:
    這個函數會先檢查快取中是否有該 URL 的內容，
    如果有則直接從快取獲取，否則會發送 HTTP 請求並存入快取
    """
    print("===>正在獲取 URL...")

    # 檢查快取中是否已有該 URL 的內容
    if my_cache.has(url):
        print(f"===>快取命中: {url}")
        # 增加該 URL 的存取次數
        my_cache.inc(url)
        # 從快取獲取內容
        val_obj = my_cache.get(url)
    else:
        print(f"===>快取未命中: {url}")
        # 發送 HTTP 請求並處理可能的錯誤
        try:
            response = requests.get(url, timeout=2.50)
            if response.status_code == requests.codes.ok:
                # 將內容存入快取
                my_cache.add(url, response.text)
                # 從快取獲取內容
                val_obj = my_cache.get(url)
            else:
                print(f"===>錯誤: HTTP 狀態碼 {response.status_code}")
                val_obj = None
        except requests.exceptions.RequestException as e:
            print(f"===>錯誤: 無法連接到伺服器 - {str(e)}")
            val_obj = None

    return val_obj


def get_url_from_server(url):
    """
    從 HTTP 伺服器獲取指定 URL 的內容
    
    參數:
    url (str): 要訪問的 URL
    
    回傳:
    str: URL 的內容，如果請求失敗則返回 None
    """
    print("===>從伺服器獲取 URL...")
    try:
        response = requests.get(url, timeout=2.50)
        if response.status_code == requests.codes.ok:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"===>錯誤: 無法連接到伺服器 - {str(e)}")
    return None


# 主程式
if __name__ == '__main__':
    # 建立快取實例
    my_cache = Cache()

    # 測試 URL 列表
    urls = (
        "https://invalid_url",
        "https://invalid_url2",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/toolbox.py",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/greetings.py",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/README.md",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/f845d66ac49fb2e17296da9078abdc3ace7a1632/1.0%20%E5%B0%8F%E6%9C%8B%E5%8F%8B%E7%8E%A9%E5%A4%A7%E8%9F%92%E8%9B%97%20-%20100%20pages.pdf",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/1.0%20小朋友玩大蟒蛇.ipynb",
        "https://github.com/mkaoy2k/Kids-Lets-Play-Python/blob/main/2.0%20小朋友玩大蟒蛇.ipynb"
    )

    # 設定最大讀取次數
    max_read = 100
    
    # 隨機選擇 URL 進行測試
    for count in range(max_read):
        url = random.choice(urls)
        print(f'{count}: Get {url}')
        val_str = str(get_url(url))
        print(f'===>URL: ...{val_str[5:50]}...\n')

    # 測試快取管理功能
    print(f'測試快取管理功能...')
    print(f'{my_cache}\n')

    # 保留一半大小的快取，保留使用頻率最高的項目
    print(f'保留一半大小的快取，保留使用頻率最高的項目，不重置參考計數')
    my_cache.shrink(percent=50)
    print(f'{my_cache}\n')

    # 保留使用頻率最高的 3 個項目，並重置參考計數
    nbr = 3
    print(f'保留並重置使用頻率最高的 {nbr} 個項目')
    my_cache.purge(size=nbr)
    print(f'{my_cache}\n')
