"""
這個範例程式展示了 Python 的日誌記錄功能，包括：

1. 日誌配置：
   - 設置日誌等級為 DEBUG
   - 使用格式化的日誌輸出
   - 同時記錄到檔案和控制台
   - 使用相對路徑創建日誌目錄

2. 日誌處理器：
   - FileHandler: 將 ERROR 級別以上的日誌記錄到檔案
   - StreamHandler: 將所有日誌輸出到控制台

3. 基本運算函數：
   - 加法、減法、乘法和除法運算
   - 包含異常處理機制

這個範例程式適合用於學習 Python 的日誌記錄系統和基本的錯誤處理。
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

# 使用 pathlib 創建相對路徑的 logger 目錄
log_dir = Path(__file__).parent / 'logger'
log_dir.mkdir(exist_ok=True)

log_file = log_dir / 'loggingEx.log'
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(x, y):
    """加法函數"""
    logger.info(f'計算 {x} + {y}')
    return x + y

def subtract(x, y):
    """減法函數"""
    logger.info(f'計算 {x} - {y}')
    return x - y

def multiply(x, y):
    """乘法函數"""
    logger.info(f'計算 {x} * {y}')
    return x * y

def divide(x, y):
    """除法函數"""
    try:
        logger.info(f'計算 {x} / {y}')
        result = x / y
        return result
    except ZeroDivisionError:
        logger.error('除數不能為零')
        raise

def main():
    """
    主函數，示範日誌記錄和運算函數的使用
    """
    # 測試運算函數
    logger.info('開始運算測試')
    
    # 測試加法
    result = add(10, 5)
    logger.info(f'加法結果: {result}')
    
    # 測試減法
    result = subtract(10, 5)
    logger.info(f'減法結果: {result}')
    
    # 測試乘法
    result = multiply(10, 5)
    logger.info(f'乘法結果: {result}')
    
    # 測試除法（正常情況）
    result = divide(10, 5)
    logger.info(f'除法結果: {result}')
    
    # 測試除法（除以零的情況）
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        logger.error('發生除以零的錯誤')

if __name__ == '__main__':
    main()
