import xml.etree.ElementTree as ET
"""This is an example of reading an XML file, adding attributes to
given nodes and then writing to a new XML file.
讀入 xml 檔案
對每一個 "investor" 節點加入不同數量的數字貨幣
對每一個 "investor" 節點加入不同且唯一的 "id" 屬性值
寫出 xml 檔案"""

# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_read = f'{data_path}/xml_coins.xml'
file_write = f'{data_path}/xml_coins_id.xml'

tree = ET.parse(file_read)
print(f'讀取 XML 檔案 {file_read} ...\n')

root = tree.getroot()

# Set 'launched' 屬性
start_date = '2022-01-07'
root.set('launched', start_date)
print(f'===>設定 "launched" 屬性值成 "{start_date}"')

# 每一個 "investor" 首輪有不同數量的數字貨幣，如下
coins_purchased = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(f'===>對每一個 "investor" 節點加入不同數量的數字貨幣：\n{coins_purchased}')

# 對每一個 "investor" 節點加入不同且唯一的 "id" 屬性值
print(f'===>對每一個 "investor" 節點加入不同且唯一的 "id" 屬性值')

id = 0
for investor in root.iter('investor'):

    # 對每一個 "investor" 節點加入 "purchased" 子節點
    purchased = ET.fromstring(
        f"<purchased>{str(coins_purchased[id])}</purchased>")
    investor.append(purchased)

    # "purchased" 子節點加入 "date" 屬性值
    purchased.set('date', start_date)

    id += 1
    investor.set('id', str(id))

print(f'虚擬貨幣樹從根節點轉成字串:\n===>{ET.tostring(root)}\n')

# Save the updated tree to a new XML file
tree.write(file_write)
print(
    f'===>請打開 {file_write} 檢視 XML 格式的檔案...\n')
