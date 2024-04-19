import xml.etree.ElementTree as ET
"""This is an example of reading an XML file and traverse
the whole tree.
流覽 (traverse) 印出節點資料值"""

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/xml_coins.xml'


tree = ET.parse(file_read)
print(f'讀取 XML 檔案 {file_read} ...\n')

root = tree.getroot()
print(f'虚擬貨幣樹從根節點轉成字串:\n===>{ET.tostring(root)}\n')

# 檢視節點屬性: 'coin'
coin = root.get('coin')
print(f'虚擬貨幣 名稱 = {coin}')

# 2 ways of looping all the investor nodes of xml tree

# First with findall()
print(f'1. 用 findall() 流覽 (traverse) 印出節點資料值...')
for investor in root.findall('investor'):
    print(f'===>investor: {investor.text}')
print()

# Alternatively, using iterable works too
print(f'2. 用 iter() 流覽 (traverse) 印出節點資料值to traverse the xml tree...')
for investor in root.iter('investor'):
    print(f'===>investor: {investor.text}')
print()
