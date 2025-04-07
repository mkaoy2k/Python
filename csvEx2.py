"""
Python CSV 檔案處理範例
本程式示範如何使用 csv 模組中的 reader 和 writer 方法
來讀取和寫入 CSV 檔案
"""

import csv
from datetime import datetime
from typing import List
import logging
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

# 設定日誌
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('csv_processor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 設定資料夾路徑
DATA_PATH = 'sample'  # 相對於當前目錄的資料夾位置

# 確保資料夾存在
Path(DATA_PATH).mkdir(parents=True, exist_ok=True)

# 定義要讀取和寫入的檔案路徑
def get_file_paths() -> tuple:
    """
    取得檔案路徑
    
    Returns:
        tuple: 包含讀取和寫入檔案路徑的元組，依序為原始檔案、每日回報率檔案和圖表檔案
    """
    return (
        f'{DATA_PATH}/csv_stocks.csv',    # 要讀取的原始檔案
        f'{DATA_PATH}/csv_stocks_daily_return.csv',  # 要寫入的新檔案
        f'{DATA_PATH}/csv_return.png'  # 圖表檔案
    )

def read_csv(file_path: str) -> List[List]:
    """
    使用 reader() 讀取 CSV 檔案
    
    Args:
        file_path: CSV 檔案路徑
        
    Returns:
        List[List]: 包含所有資料的二維列表
    """
    logger.info(f"開始讀取檔案: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            logger.debug("使用 csv.reader 讀取檔案")
            csv_reader = csv.reader(csv_file)
            
            data = []
            
            headers = next(csv_reader)
            logger.debug(f"欄位名稱: {headers}")
            
            for row in csv_reader:
                data.append(row)
            
            logger.debug(f"讀取到 {len(data)} 筆資料")
            return data
            
    except Exception as e:
        logger.error(f"讀取檔案時發生錯誤: {str(e)}")
        return []

def write_csv(file_path: str, data: List[List], headers: List[str]) -> bool:
    """
    使用 writer() 寫入 CSV 檔案
    
    Args:
        file_path: CSV 檔案路徑
        data: 要寫入的資料列表
        headers: 欄位名稱列表
        
    Returns:
        bool: 寫入是否成功
    """
    logger.info(f"開始寫入檔案: {file_path}")
    
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as csv_file:
            logger.debug("使用 csv.writer 寫入檔案")
            csv_writer = csv.writer(csv_file)
            
            logger.debug(f"寫入欄位名稱: {headers}")
            csv_writer.writerow(headers)
            
            logger.debug(f"寫入 {len(data)} 筆資料")
            csv_writer.writerows(data)
            
            logger.info(f"成功寫入檔案: {file_path}")
            return True
            
    except Exception as e:
        logger.error(f"寫入檔案時發生錯誤: {str(e)}")
        return False

def process_csv(input_file: str, output_file: str, plot_file: str) -> bool:
    """
    處理 CSV 檔案
    
    Args:
        input_file: 輸入的 CSV 檔案路徑
        output_file: 輸出的 CSV 檔案路徑
        plot_file: 圖表檔案路徑
        
    Returns:
        bool: 處理是否成功
    """
    logger.info("=== 開始 CSV 檔案處理 ===")
    
    try:
        # 讀取原始檔案
        logger.info(f"讀取檔案: {input_file}")
        data = read_csv(input_file)
        if not data:
            logger.error("讀取檔案失敗")
            return False
            
        # 處理資料
        processed_data = []
        for row in data:
            try:
                # 處理日期字串和轉換收盤價為浮點數
                date_str = row[0]
                close_price = float(row[4])
                
                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                
                if len(processed_data) > 0:
                    yesterday_close_price = float(processed_data[-1][1])
                    
                    # 檢查昨日收盤價是否為零
                    if yesterday_close_price == 0:
                        logger.warning(f"跳過計算：昨日收盤價為零，無法計算報酬率。日期: {date_str}")
                        processed_data.append([date_obj.strftime('%m/%d/%Y'), close_price, 0.0])
                    else:
                        daily_return = (close_price - yesterday_close_price) / yesterday_close_price
                        processed_data.append([date_obj.strftime('%m/%d/%Y'), close_price, daily_return])
                else:
                    # 處理第一筆資料，因為沒有前一日的收盤價，所以設定報酬率為0.0
                    processed_data.append([date_obj.strftime('%m/%d/%Y'), close_price, 0.0])
                    
            except (IndexError, ValueError) as e:
                logger.warning(f"跳過無效的資料: {row} - 錯誤: {str(e)}")
                continue
            
        # 寫入新檔案
        if processed_data:
            headers = ['Date', 'Close Price', 'return']
            logger.info(f"寫入檔案: {output_file}")
            
            success = write_csv(output_file, processed_data, headers)
            if success:
                logger.info(f"成功處理檔案: {input_file} -> {output_file}")
                
                # 繪製報酬率長條圖
                df = pd.read_csv(output_file)
                
                plt.figure(figsize=(15, 8))  # 調整圖表大小
                plt.bar(df['Date'], df['return'], color='blue')
                plt.title('Daily Return Rate')
                plt.xlabel('Date')
                plt.ylabel('Return Rate')
                plt.xticks(rotation=45, ha='right', fontsize=8)  # 調整 x 軸標籤的對齊方式和字體大小
                plt.tight_layout()
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.savefig(plot_file)
                plt.close()
                logger.info(f"已生成報酬率長條圖: {plot_file}")
            return success
            
        logger.warning("沒有有效的資料可以處理")
        return False
        
    except Exception as e:
        logger.error(f"處理檔案時發生錯誤: {str(e)}")
        return False

# 主程式
if __name__ == '__main__':
    # 取得檔案路徑
    input_file, output_file, plot_file = get_file_paths()
    
    logger.info("=== 開始主程式 ===")
    
    # 測試處理 CSV 檔案
    success = process_csv(input_file, output_file, plot_file)
    
    # 顯示結果
    if success:
        logger.info("=== 處理完成 ===")
        logger.info("CSV 檔案處理成功")
    else:
        logger.error("=== 處理失敗 ===")
        logger.error("請檢查錯誤訊息並重新嘗試")
