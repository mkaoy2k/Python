'''JSON stands for JavaScript Object Notation.
This is an Example of reading from JSON file into a dictionary obj
and writing a dictionary obj to JSON file'''
import json


# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# Specify data file names in this example
file_read = f'{data_path}/json_states.json'
file_write = f'{data_path}/json_states_new.json'

# read in a Json file into a Python dictionary obj
print(f'從 {file_read} JSON 檔案讀入 ...')
with open(file_read) as f:
  data = json.load(f)
print(f'轉成字典 data 類型：{type(data)}\n')
print(f'===>{data}\n')

# filter out area-code in the dictionary
print(f'字典中删除邮遞區號 ...')
for state in data['states']:
  del state['area_codes']

# write USA state name and its abbreviation to a file in Json format
print(f'字典物件轉成JSON格式的字串並寫入檔案 ...')
with open(file_write, 'w') as f:
  json.dump(data, f, indent=2)
print(
    f'===>請打開 {file_write} 檢視 JSON 格式的檔案...\n')

# Another example of reading/writing a string in JSON format

# A string in JSON format, containing a list of states, in which
# has a state name and associated abbreviation.
string_json = '''{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"
    },
    {
      "name": "Alaska",
      "abbreviation": "AK"
    }
  ]
}
'''

print(f'JSON 格式字串：\n===>{string_json}\n')

# read a JSON-format string into a Python dictionary
dict_pi = json.loads(string_json)
print(f'载入 JSON 字串轉成字典 dict_pi 類型：{type(dict_pi)}:')
print(f'===>{dict_pi}\n')

# Iterate the value of key='states', which is the list of dictionary objects
print(f'取出鍵="states"的值（列表）逐一印出每一元素 ...')
for state in dict_pi['states']:

  # print each element which is a dictionary
  print(f'===>{state}')
print()

# Converting a Python dictionary to a JSON-format string
# optionally, with indentatons for readability in print
new_str_json = json.dumps(dict_pi, indent=2)

print(f'字典轉成字串 new_str_json 類型：{type(new_str_json)}')
print(f'===>{new_str_json}\n')
