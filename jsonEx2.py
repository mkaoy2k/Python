'''JSON stands for JavaScript Object Notation.
This is an Example of writing a JSON-format string to a JSON file'''
import json
import os

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
# print(f'JSON 格式字串：\n===>{string_json}\n')

# Initialize the folder where data is located
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'sample')

# Specify data file name to write in this example
file_write = os.path.join(data_path, 'json_movies.json')

# read a string in JSON format into a Python dictionary
dict_movies = json.loads(string_json)
print(f'轉成字典 dict_movies 類型：{type(dict_movies)}:')
# print(f'===>{dict_movies}\n')

# print out the value with the key of 'movies'
print(f'電影清單:')
for movie in dict_movies['movies']:
  print(f'===>{movie}\n')

# converting a Python dictionary to a string in JSON format
# with indentatons and non-ascii for readability in print
# print(f'字典物件轉成JSON格式的字串 ...')
new_str_json = json.dumps(dict_movies, indent=2, ensure_ascii=False)
print(f'轉成JSON格式的字串 類型：{type(new_str_json)}')
# print(f'===>{new_str_json}\n')

# write to JSON file with utf-8 encoding
print(f'字典物件轉成JSON格式的字串並寫入檔案 ...')
with open(file_write, 'w', encoding="utf-8") as f:
  json.dump(dict_movies, f, indent=2, ensure_ascii=False)
print(
    f'===>請打開 {file_write} 檢視 JSON 格式的檔案...\n')
