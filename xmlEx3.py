"""
XML 文件處理範例
這個程式會讀取 XML 文件，刪除指定節點的屬性，然後寫入新的 XML 文件。
功能包括：
1. 讀取原始 XML 文件
2. 刪除指定節點的屬性
3. 將修改後的 XML 寫入新文件
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def process_xml(file_read: Path, file_write: Path) -> None:
    """
    處理 XML 文件的主函數
    
    Args:
        file_read: 輸入 XML 文件路徑
        file_write: 輸出 XML 文件路徑
    """
    # 讀取 XML 文件
    tree = ET.parse(file_read)
    print(f'讀取 XML 檔案 {file_read} ...')

    root = tree.getroot()

    # 刪除每一個 'investor' 節點的 'id' 屬性
    print(f'\t刪除每一個 \'investor\' 節點的 \'id\' 屬性...')
    for investor in root.findall('investor'):
        del(investor.attrib['id'])

    print(f'\t虛擬貨幣樹從根節點轉成字串:\n\t{ET.tostring(root)}')

    # 將修改後的 XML 寫入新文件
    tree.write(file_write)
    print(f'\n請打開 {file_write} 檢視 XML 格式的檔案...')

def main():
    """
    程式入口點
    設定檔案路徑並調用處理函數
    """
    # 獲取當前腳本所在目錄
    current_dir = Path(__file__).parent
    
    # 定義資料夾路徑（相對於當前腳本目錄）
    data_path = current_dir / 'sample'
    
    # 確保資料夾存在
    data_path.mkdir(exist_ok=True)
    
    # 定義檔案路徑
    file_read = data_path / 'xml_coins_id.xml'
    file_write = data_path / 'xml_coins_noid.xml'

    # 處理 XML 文件
    process_xml(file_read, file_write)

if __name__ == '__main__':
    main()
