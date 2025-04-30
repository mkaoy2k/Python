"""
XML 文件處理示例
這個程式示範如何讀取 XML 文件，動態添加節點，並寫入新的 XML 文件。
主要功能包括：
1. 讀取現有的 XML 文件
2. 使用兩種方式添加投資者節點
3. 添加購買和售出記錄
4. 寫入更新後的 XML 文件
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def setup_paths() -> tuple[Path, Path]:
    """
    設置並創建必要的目錄和文件路徑
    
    Returns:
        tuple[Path, Path]: (輸入文件路徑, 輸出文件路徑)
    """
    # 獲取當前腳本所在目錄
    script_dir = Path(__file__).parent
    
    # 定義 sample 目錄
    sample_dir = script_dir / 'sample'
    
    # 如果 sample 目錄不存在，則創建它
    sample_dir.mkdir(exist_ok=True)
    
    # 定義輸入和輸出文件路徑
    file_read = sample_dir / 'xml_coins_id.xml'
    file_write = sample_dir / 'xml_coins_new.xml'
    
    return file_read, file_write

def process_xml(file_read: Path, file_write: Path) -> None:
    """
    處理 XML 文件的主要函數
    
    Args:
        file_read (Path): 輸入 XML 文件路徑
        file_write (Path): 輸出 XML 文件路徑
    """
    try:
        # 確保輸入文件存在
        if not file_read.exists():
            print(f"錯誤：輸入文件 {file_read} 不存在")
            return

        # 讀取 XML 文件
        tree = ET.parse(str(file_read))
        print(f'讀取 XML 檔案 {file_read} ...')
        
        # 獲取根節點
        root = tree.getroot()
        
        # 方法 1: 使用 fromstring() 添加投資者節點
        print("\n1. 使用 fromstring() 添加投資者節點...")
        investor1 = ET.fromstring("<investor>Henry Kao</investor>")
        root.append(investor1)
        
        # 添加購買記錄
        purchased = ET.fromstring("<purchased>1428.57</purchased>")
        investor1.append(purchased)
        purchased.set('date', '2021-02-19')
        
        # 添加售出記錄
        sold = ET.fromstring("<sold>28.57</sold>")
        investor1.append(sold)
        sold.set('date', '2022-03-15')
        
        # 方法 2: 使用 Element 類別添加投資者節點
        print("\n2. 使用 Element 類別添加投資者節點...")
        investor2 = ET.Element("investor")
        investor2.text = "Christine Kao"
        root.append(investor2)
        
        # 添加購買記錄
        purchased = ET.Element("purchased")
        purchased.text = '1000'
        purchased.set('date', '2021-03-31')
        investor2.append(purchased)
        
        # 添加售出記錄
        sold = ET.Element("sold")
        sold.text = '500'
        sold.set('date', '2022-04-30')
        investor2.append(sold)
        
        # 顯示 XML 樹的內容
        print(f'\n虛擬貨幣樹從根節點轉成字串:\n\t{ET.tostring(root, encoding="unicode")}')
        
        # 確保輸出目錄存在
        file_write.parent.mkdir(parents=True, exist_ok=True)
        
        # 寫入更新後的 XML 文件
        tree.write(str(file_write))
        print(f'\n請打開 {file_write} 檢視 XML 格式的檔案...')
        
    except Exception as e:
        print(f"處理 XML 時發生錯誤: {str(e)}")

def main():
    """
    程式入口點
    設置數據路徑並調用處理函數
    """
    # 設置文件路徑
    file_read, file_write = setup_paths()
    
    # 處理 XML 文件
    process_xml(file_read, file_write)

if __name__ == "__main__":
    main()
