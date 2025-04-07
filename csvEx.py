"""
Python CSV 檔案處理範例
本程式示範如何使用 csv 模組進行 CSV 檔案的讀取和寫入操作
"""

import csv
from typing import List, Dict
import re

# 設定資料夾路徑
DATA_PATH = 'sample'  # 相對於當前目錄的資料夾位置

# 定義要讀取和寫入的檔案路徑
def get_file_paths() -> tuple:
    """
    取得檔案路徑
    
    Returns:
        tuple: 包含讀取和寫入檔案路徑的元組
    """
    return (
        f'{DATA_PATH}/csv_data.csv',    # 要讀取的原始檔案
        f'{DATA_PATH}/csv_data_new.csv'  # 要寫入的新檔案
    )

def read_csv(file_path: str) -> List[Dict]:
    """
    讀取 CSV 檔案
    
    Args:
        file_path: CSV 檔案路徑
        
    Returns:
        List[Dict]: 包含所有資料的列表，每個元素都是字典
    """
    print(f"\n讀取檔案: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            # 使用 DictReader 讀取 CSV 檔案
            # DictReader 會將每一列轉換為字典，其中鍵為第一列的欄位名稱
            reader = csv.DictReader(csv_file)
            
            # 印出欄位名稱
            print("\n欄位名稱:")
            print(reader.fieldnames)
            
            # 讀取所有資料
            data = list(reader)
            
            # 印出資料內容
            print("\n資料內容:")
            for row in data:
                print(row)
                
            return data
            
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {str(e)}")
        return []

def write_csv(file_path: str, data: List[Dict], fieldnames: List[str]) -> bool:
    """
    寫入 CSV 檔案
    
    Args:
        file_path: CSV 檔案路徑
        data: 要寫入的資料列表
        fieldnames: 欄位名稱列表
        
    Returns:
        bool: 寫入是否成功
    """
    print(f"\n寫入檔案: {file_path}")
    
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as csv_file:
            # 使用 DictWriter 寫入 CSV 檔案
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # 寫入欄位名稱
            writer.writeheader()
            
            # 寫入資料
            writer.writerows(data)
            
            print(f"成功寫入檔案: {file_path}")
            return True
            
    except Exception as e:
        print(f"寫入檔案時發生錯誤: {str(e)}")
        return False

# 電子郵件格式驗證函數
def is_valid_email(email: str) -> bool:
    """
    驗證電子郵件地址格式是否正確
    
    Args:
        email: 要驗證的電子郵件地址
        
    Returns:
        bool: 電子郵件格式是否正確
    """
    # 電子郵件格式正則表達式
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

def process_csv(input_file: str, output_file: str) -> bool:
    """
    處理 CSV 檔案
    
    Args:
        input_file: 輸入的 CSV 檔案路徑
        output_file: 輸出的 CSV 檔案路徑
        
    Returns:
        bool: 處理是否成功
    """
    print("\n=== CSV 檔案處理 ===")
    
    try:
        # 讀取原始檔案
        data = read_csv(input_file)
        if not data:
            print("讀取檔案失敗")
            return False
            
        # 處理資料
        processed_data = []
        for row in data:
            # 在這裡可以對資料進行處理
            # 範例：驗證電子郵件地址格式
            try:
                email = row['email']
                if not is_valid_email(email):
                    print(f"跳過無效的電子郵件地址: {row}")
                    continue
                
                # 將電子郵件地址轉換為小寫
                row['Email'] = email.lower()
                processed_data.append(row)
                
            except (KeyError, TypeError):
                print(f"跳過無效的資料: {row}")
                continue
            
        # 寫入新檔案
        if processed_data:
            success = write_csv(output_file, processed_data, data[0].keys())
            if success:
                print(f"成功處理檔案: {input_file} -> {output_file}")
            return success
            
        print("沒有有效的資料可以處理")
        return False
        
    except Exception as e:
        print(f"處理檔案時發生錯誤: {str(e)}")
        return False

# 主程式
if __name__ == '__main__':
    # 取得檔案路徑
    input_file, output_file = get_file_paths()
    
    # 測試處理 CSV 檔案
    success = process_csv(input_file, output_file)
    
    # 顯示結果
    if success:
        print("\n=== 處理完成 ===")
        print("CSV 檔案處理成功")
    else:
        print("\n=== 處理失敗 ===")
        print("請檢查錯誤訊息並重新嘗試")
