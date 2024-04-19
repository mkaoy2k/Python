import xml.etree.ElementTree as ET
"""This is an example of reading an XML file, deleting an attribute
of a given nodes and writing to a new XML file.
讀入 xml 檔案
删除每一個 'investor' 節點的 'id' 屬性
寫出 xml 檔案
"""

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/xml_coins_id.xml'
file_write = f'{data_path}/xml_coins_noid.xml'

tree = ET.parse(file_read)
print(f'讀取 XML 檔案 {file_read} ...\n')

root = tree.getroot()

# 删除每一個 'investor' 節點的 'id' 屬性
print(f"===>删除每一個 'investor' 節點的 'id' 屬性...")
for investor in root.findall('investor'):
    del(investor.attrib['id'])

print(f'虚擬貨幣樹從根節點轉成字串:\n===>{ET.tostring(root)}\n')

# Save the updated tree to a new XML file
tree.write(file_write)
print(
    f'===>請打開 {file_write} 檢視 XML 格式的檔案...\n')
