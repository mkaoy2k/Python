"""
示範如何從 JSON-API 伺服器獲取 JSON 格式的 bytes 物件資料

本程式示範如何：
1. 從遠端伺服器獲取 JSON 格式的資料
2. 將 bytes 物件轉換為 Python 的字典列表
3. 處理和顯示 JSON 資料

注意：本範例使用 Typicode 提供的測試伺服器
"""
import json
from urllib.request import urlopen


def main():
    """
    主程式，示範如何處理 JSON API 資料
    """
    # 資料來源：Typicode 提供的測試伺服器
    url_path = "https://my-json-server.typicode.com/typicode/demo/posts?format=json"

    # 開啟 URL 並讀取響應資料
    print(f'訪問網址：{url_path} ...')
    with urlopen(url_path) as response:
        source = response.read()

    # 顯示原始資料的類型和內容
    print(f'讀入 source 類型： {type(source)}')
    print(f'===>{source}\n')

    # 將 bytes 物件轉換為 Python 的字典列表
    data = json.loads(source)
    print(f'轉成 data 類型：{type(data)}')
    print(f'===>{data}\n')

    # 將列表物件轉換為 JSON 格式的字串
    print(f'列表物件轉成JSON格式的字串 ...')
    print(f'===>{json.dumps(data, indent=2)}\n')

    """Typicode Example: returns a list"""

    # 將列表物件轉換為字典物件
    # 初始化一個字典，包含空列表
    posts_d = dict()
    posts_d['posts'] = []

    # 將列表中的每個元素（字典）逐一取出並添加到字典中
    print(f'列表逐一取出每一元素（字典） ...')
    for item in data:
        post = dict()
        post['id'] = item['id']
        title = item['title']
        post['title'] = title
        posts_d['posts'].append(post)

    # 顯示轉換後的字典物件
    print(f'列表物件轉成字典物件 ...')
    print(f'===>{posts_d}\n')

    # 將字典物件轉換為 JSON 格式的字串
    new_str_json = json.dumps(posts_d, indent=2)
    print(f'字典轉成字串 new_str_json 類型：{type(new_str_json)}')
    print(f'===>{new_str_json}\n')


if __name__ == '__main__':
    main()
