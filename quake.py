import requests
from bs4 import BeautifulSoup   #pip install bs4
import webbrowser

def get_earthquake_info():
    # 發送 GET 請求至中央氣象局的地震資訊網頁
    url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/data/'
    response = requests.get(url)
    
    # 解析 HTML 內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到地震資訊的標籤
    earthquake_tag = soup.find('div', class_='earthquakeInfoHtml')

    # 提取地震資訊
    earthquake_info = earthquake_tag.text.strip()
    
    # 打印地震資訊
    print(earthquake_info)
    
    # 提取地震位置圖的連結
    map_link = earthquake_tag.find('a')['href']
    
    # 在瀏覽器中打開地震位置圖
    webbrowser.open(map_link)

if __name__ == '__main__':
    get_earthquake_info()
