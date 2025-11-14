"""
伺服器連線測試工具

這個模組提供了一個簡單的介面來測試伺服器的連線狀態和回應時間。
可以從命令列參數指定要測試的伺服器網址。

範例:
    1. 使用命令列參數:
       python pingSvr.py --url http://example.com
       
       或直接提供網址:
       python pingSvr.py http://example.com

命令列參數:
    --url: 要測試的伺服器網址

依賴套件:
    - requests: 用於發送 HTTP 請求
    - absl: 用於命令列參數解析
"""

import requests, time
from absl import app, flags

FLAGS = flags.FLAGS
flags.DEFINE_string('url', None, 'Server URL')

def main(argv) -> None:
    """
    主函數，處理伺服器連線測試流程
    
    這個函數會：
    1. 解析命令列參數
    2. 發送 HTTP 請求到指定網址
    3. 計算並顯示回應時間
    
    參數:
        argv: 命令列參數列表 (由 absl 自動處理)
        
    異常:
        ValueError: 當未提供必要的網址參數時
        requests.exceptions.RequestException: 當請求失敗時
    """
    try:
        # 解析命令列參數
        FLAGS(argv)
        
        # 檢查必要參數
        if not FLAGS.url:
            if len(argv) > 1:
                url = argv[1]
            else:
                raise ValueError("請提供要測試的伺服器網址 (使用 --url 參數或直接提供網址)")
        else:
            url = FLAGS.url
        print(f"伺服器網址: {url}")
        start = time.perf_counter()
        response = requests.get(url, timeout=10)
        elapsed = time.perf_counter() - start
        print(f"狀態碼: {response.status_code}")
        print(f"回應時間: {elapsed:.3f} 秒")
    except requests.exceptions.RequestException as e:
        print(f"連線錯誤: {str(e)}")
        return 1
    except Exception as e:
        print(f"執行過程中發生錯誤: {str(e)}")
        return 1


if __name__ == '__main__':
    app.run(main)
