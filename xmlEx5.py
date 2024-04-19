import xml.etree.ElementTree as ET
"""This is an example of reading an XML file and finding
a particular node.
讀入 xml 檔案
找出 XML樹中的<investor>節點"""

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/xml_coins_id.xml'

tree = ET.parse(file_read)
print(f'讀取 XML 檔案 {file_read} ...\n')

root = tree.getroot()

# 例子：已知 investor id，找出 XML樹中的節點
str_id = '7'
investor = root.find(f".//investor[@id='{str_id}']")
print(f"已知 investor id='{str_id}'...")
print(f"===> 找出 XML樹中的<investor>節點 = '{investor.text}'\n")
