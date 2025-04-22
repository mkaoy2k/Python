'''
JSON (JavaScript Object Notation) 是一種輕量級的資料交換格式。
本範例示範如何將 JSON 格式的字串寫入 JSON 檔案。

程式功能說明：
1. JSON 字串處理：
   - 包含電影資料的 JSON 格式字串
   - 資料結構包含：
     * 電影標題
     * 發行年份
     * 是否精彩
     * 是否獲得奧斯卡獎
     * 演員陣容
     * 預算（null 值）

2. 資料寫入：
   - 將 JSON 格式的字串轉換為 Python 字典
   - 將字典資料寫入 JSON 檔案
   - 使用縮排格式化輸出，提高可讀性

使用方法：
1. 確保有足夠的寫入權限
2. 執行程式後，會在當前目錄生成 JSON 檔案

注意事項：
- JSON 格式字串中使用了 true/false 表示布林值
- 使用 null 表示空值
- 列表中的元素可以是多種資料類型
'''
import json
from pathlib import Path

def main():
    # 使用 pathlib 初始化當前目錄和資料夾路徑
    current_dir = Path(__file__).parent
    data_path = current_dir / 'sample'

    # JSON 格式的字串，包含電影資料
    string_json = '''
{
  "movies": [
    {
      "title": "Gattaca",
      "release_year": 1997,
      "is_awesome": true,
      "won_oscar": false,
      "actors": ["Ethan Hawke", "Uma Thurman",
      "Jude Law", "Alan Arkin", "Lauren Dean"],
      "budget": null,
      "credits": {"director": "Andrew Nicol",
      "writer": "Andrew Nicol",
      "composer": "Michael Nyman",
      "cinematographer": "S\u0142awomir Idziak"}
    },
    {
    "title": "Minority Report",
    "director": "Steven Spielberg",
    "composer": "Jogn Williams",
    "actors": ["Tom Cruise", "Colin Farrell",
    "Samantha Morton", "Max von Sydow"],
    "is_awesome": true,
    "budget": 102000000,
    "cinematographer": "Janusz Kami\u0144ski"
    },
    {
      "title": "太陽旗",
      "director": "魏德聖",
      "composer": "何國傑",
      "actors": [
        "林慶台",
        "遊大慶",
        "馬志翔",
        "安藤政信",
        "木村祐一",
        "徐若瑄",
        "溫嵐",
        "羅美玲",
        "田中千繪"
      ],
      "is_awesome": true,
      "budget": null,
      "cinematographer": "秦鼎昌"
    },
    {
      "title": "彩虹旗",
      "director": "魏德聖",
      "composer": "何國傑",
      "actors": [
        "林慶台",
        "遊大慶",
        "馬志翔",
        "安藤政信",
        "木村祐一",
        "徐若瑄",
        "溫嵐",
        "羅美玲",
        "田中千繪"
      ],
      "is_awesome": true,
      "budget": null,
      "cinematographer": "秦鼎昌"
    }
  ]
}
'''

    # 將 JSON 格式字串轉換為 Python 字典
    dict_movies = json.loads(string_json)
    print(f'轉換後的字典類型：{type(dict_movies)}')
    print(f'字典內容：\n===>{dict_movies}\n')

    # 指定輸出檔案路徑
    output_file = data_path / 'movies.json'

    # 將字典寫入 JSON 檔案
    print(f'正在寫入檔案 {output_file} ...')
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(dict_movies, f, indent=2, ensure_ascii=False)
    print(f'===>請打開 {output_file} 檢視 JSON 格式的檔案...\n')

if __name__ == '__main__':
    main()
