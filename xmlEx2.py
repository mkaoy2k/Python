"""處理 XML 檔案的範例程式
這個程式會讀取 XML 檔案，對每個投資者節點添加屬性和子節點，然後寫入新的 XML 檔案。
主要功能包括：
1. 讀取原始 XML 檔案
2. 為每個投資者節點添加唯一 ID
3. 為每個投資者節點添加購買數量
4. 寫入更新後的 XML 檔案
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def main():
    """主函數，處理 XML 檔案的讀取、處理和寫入
    
    Returns:
        None
    """
    # 使用 pathlib 獲取當前腳本所在目錄的絕對路徑
    current_dir = Path(__file__).parent
    
    # 定義資料夾路徑（相對於當前腳本目錄）
    data_path = current_dir / 'sample'
   
    # 確保資料夾存在
    data_path.mkdir(exist_ok=True) 
    
    # 定義檔案路徑
    file_read = data_path / 'xml_coins.xml'
    file_write = data_path / 'xml_coins_id.xml'
    
    # 讀取 XML 檔案
    tree = ET.parse(file_read)
    print(f'讀取 XML 檔案 {file_read} ...\n')
    
    root = tree.getroot()
    
    # 設定 launched 屬性
    start_date = '2022-01-07'
    root.set('launched', start_date)
    print(f'\t設定 "launched" 屬性值成 "{start_date}"')
    
    # 定義每個投資者的購買數量
    coins_purchased = (10, 20, 30, 40, 50, 60, 70, 80, 90)
    print(f'\t對每一個 "investor" 節點加入不同數量的數字貨幣：\n\t{coins_purchased}')
    
    # 處理每個投資者節點
    print(f'\t對每一個 "investor" 節點加入不同且唯一的 "id" 屬性值')
    
    id = 0
    for investor in root.iter('investor'):
        # 添加 purchased 子節點
        purchased = ET.fromstring(
            f"<purchased>{str(coins_purchased[id])}</purchased>")
        investor.append(purchased)
        
        # 設定 purchased 子節點的 date 屬性
        purchased.set('date', start_date)
        
        id += 1
        investor.set('id', str(id))
    
    # 顯示更新後的 XML 結構
    print(f'\t虛擬貨幣樹從根節點轉成字串:\n\t{ET.tostring(root)}\n')
    
    # 寫入更新後的 XML 檔案
    tree.write(file_write)
    print(
        f'請打開 {file_write} 檢視 XML 格式的檔案...\n')

if __name__ == '__main__':
    main()
