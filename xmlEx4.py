import xml.etree.ElementTree as ET
"""This is an example of reading an XML file, adding nodes on the fly
and then writing to a new XML file.
讀入 xml 檔案
1. 用 fromstring() 加入 'investor' 節點
2. 實例化 (Instantiate) 'investor' 節點物件後，加入 xml 樹物件
寫出 xml 檔案"""

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/xml_coins_id.xml'
file_write = f'{data_path}/xml_coins_new.xml'

tree = ET.parse(file_read)
print(f'讀取 XML 檔案 {file_read} ...\n')

root = tree.getroot()

# 2 ways to Add 'investor' nodes on the fly.

# 1. 用 fromstring() 加入 'investor' 節點
print(f"1. 用 fromstring() 加入 'investor' 節點...")
investor1 = ET.fromstring("<investor>Henry Kao</investor>")
root.append(investor1)

# Add a record of coins purchased
purchased = ET.fromstring("<purchased>1428.57</purchased>")
investor1.append(purchased)
purchased.set('date', '2021-02-19')

# Add a record of coins sold
sold = ET.fromstring("<sold>28.57</sold>")
investor1.append(sold)
sold.set('date', '2022-03-15')

# 2. 實例化 (Instantiate) 'investor' 節點物件後，加入 xml 樹物件
print(f"2. 實例化 (Instantiate) 'investor' 節點物件後，加入 xml 樹物件...")
investor2 = ET.Element("investor")
investor2.text = "Christine Kao"
root.append(investor2)

# Add a record of coins purchased
purchased = ET.Element("purchased")
purchased.text = '1000'
purchased.set('date', '2021-03-31')
investor2.append(purchased)

# Add a record of coins sold
sold = ET.Element("sold")
sold.text = '500'
sold.set('date', '2022-04-30')
investor2.append(sold)

print(f'虚擬貨幣樹從根節點轉成字串:\n===>{ET.tostring(root)}\n')

# Save the updated tree to a new XML file
tree.write(file_write)
print(
    f'===>請打開 {file_write} 檢視 XML 格式的檔案...\n')
