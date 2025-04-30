"""
這個程式示範如何讀取 XML 檔案並搜尋特定節點。
主要功能：
1. 讀取 XML 檔案
2. 使用 XPath 查找特定的 investor 節點
3. 顯示找到的節點內容
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def find_investor_by_id(xml_file, investor_id):
    """
    根據 investor id 查找 XML 檔案中的節點
    
    Args:
        xml_file (Path): XML 檔案的路徑
        investor_id (str): 要查找的 investor id
    
    Returns:
        str: 找到的 investor 節點的內容
    """
    tree = ET.parse(str(xml_file))
    root = tree.getroot()
    investor = root.find(f".//investor[@id='{investor_id}']")
    return investor.text if investor is not None else None

def main():
    """
    主程式函數，負責設定檔案路徑並執行查詢
    """
    # 取得當前程式碼所在的目錄
    current_dir = Path(__file__).parent
    
    # 設定資料夾路徑（相對於程式碼所在目錄）
    data_path = current_dir / 'sample'
    xml_file = data_path / 'xml_coins_id.xml'
    
    # 確保資料夾存在
    data_path.mkdir(exist_ok=True)
    
    # 輸出讀取資訊
    print(f'讀取 XML 檔案 {xml_file} ...\n')
    
    # 查詢特定 investor
    investor_id = '7'
    result = find_investor_by_id(xml_file, investor_id)
    
    # 顯示結果
    print(f"已知 investor id='{investor_id}'...")
    print(f"\t找出 XML樹中的<investor>節點 = '{result}'\n")

if __name__ == "__main__":
    main()
