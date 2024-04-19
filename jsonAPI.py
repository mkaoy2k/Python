import json
from urllib.request import urlopen
"""Demonstrate to get a JSON 'bytes' obj data from a JSON-API server"""

# # source1 : From Yahoo site, which no longer exists asof 2022-7-18
# url_path = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"

# source 2: From a fake server, hosted at Typicode site
url_path = "https://my-json-server.typicode.com/typicode/demo/posts?format=json"

# Open URL via urlopen()
print(f'訪問網址：{url_path} ...')
with urlopen(url_path) as response:
    source = response.read()

print(f'讀入 source 類型： {type(source)}')
print(f'===>{source}\n')

# convert 'bytes' obj into a list of dictionary objects
data = json.loads(source)
print(f'轉成 data 類型：{type(data)}')
print(f'===>{data}\n')

# print the list obj in an indented string format
print(f'列表物件轉成JSON格式的字串 ...')
print(f'===>{json.dumps(data, indent=2)}\n')

"""Typicode Example: returns a list"""

# wrap the list into a dictionary

# initialize a dictionary with the key of 'posts' containing empty list
posts_d = dict()
posts_d['posts'] = []

# iterate the list to append one post at a time, which is also a dictionary
print(f'列表逐一取出每一元素（字典） ...')
for item in data:
    post = dict()
    id = item['id']
    title = item['title']
    post['id'] = id
    post['title'] = title
    posts_d['posts'].append(post)

print(f'列表物件轉成字典物件 ...')
print(f'===>{posts_d}\n')

# Convert a Python dictionary to a string in JSON format
# with indentatons for readability in print
new_str_json = json.dumps(posts_d, indent=2)
print(f'字典轉成字串 new_str_json 類型：{type(new_str_json)}')
print(f'===>{new_str_json}\n')
