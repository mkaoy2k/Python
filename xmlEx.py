"""
XML 文件讀取和節點遍歷示例
這個範例展示了如何讀取 XML 文件並遍歷整個樹結構。
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def load_xml_data(file_path):
    """
    讀取 XML 文件並解析
    
    Args:
        file_path (str): XML 文件的路徑
    
    Returns:
        ElementTree: 解析後的 XML 树
    """
    try:
        tree = ET.parse(file_path)
        print(f'讀取 XML 檔案 {file_path} ...\n')
        return tree
    except ET.ParseError as e:
        print(f'解析 XML 時發生錯誤: {e}')
        return None

def print_root_info(root):
    """
    印出 XML 根節點的資訊
    
    Args:
        root (Element): XML 的根節點
    """
    print(f'虛擬貨幣樹從根節點轉成字串:\n\t{ET.tostring(root)}\n')
    
    # 檢視節點屬性: 'coin'
    coin = root.get('coin')
    print(f'虛擬貨幣 名稱 = {coin}')

def traverse_investors(root):
    """
    遍歷所有投資者節點並印出其內容
    
    Args:
        root (Element): XML 的根節點
    """
    print(f'1. 用 findall() 遍歷並印出節點資料值...')
    for investor in root.findall('investor'):
        print(f'\tinvestor: {investor.text}')
    print()

    print(f'2. 用 iter() 遍歷並印出節點資料值...')
    for investor in root.iter('investor'):
        print(f'\tinvestor: {investor.text}')
    print()

def main():
    """
    主程式入口
    負責初始化資料路徑並執行 XML 文件讀取和處理
    """
    # 初始化資料夾路徑
    # 使用 pathlib 確保相對路徑正確
    current_dir = Path(__file__).parent
    data_path = current_dir / 'sample'
    file_path = data_path / 'xml_coins.xml'

    # 確保資料夾存在
    data_path.mkdir(exist_ok=True)

    # 讀取和解析 XML
    tree = load_xml_data(str(file_path))
    if tree:
        root = tree.getroot()
        print_root_info(root)
        traverse_investors(root)

if __name__ == '__main__':
    main()
