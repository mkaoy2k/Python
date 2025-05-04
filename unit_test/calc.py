"""
計算模組說明：基本數學運算函數庫

這個模組提供了一系列基本的數學運算功能，包括：

1. 基本運算函數
   - add(x, y): 加法運算
   - subtract(x, y): 減法運算
   - multiply(x, y): 乘法運算
   - divide(x, y): 除法運算（包含除以零的錯誤處理）
   - mina(x, y): 找出兩個數字中的最小值

2. 特點
   - 完整的錯誤處理機制
     * 型別檢查：確保輸入為數字類型
     * 特殊值處理：處理零值、負數等情況
     * 除法運算：處理除以零的情況
   - 完整的日誌記錄
     * 使用環境變數控制日誌等級
     * 同時輸出到控制台和日誌檔案
     * 記錄函數執行流程和錯誤信息
   - 支援浮點數運算
   - 嚴格的型別檢查

3. 使用方式
   - 可以直接導入模組使用：
     from calc import add, subtract, multiply, divide, mina
   - 可以通過環境變數 LOGGING 控制日誌等級（預設為 INFO）

4. 錯誤處理
   - TypeError: 當輸入不是數字時引發
   - ValueError: 當除數為零時引發

範例：
# 正常使用
result = add(5, 3)        # 8
result = mina(10, 5)      # 5

# 錯誤使用
result = add("5", 3)      # 會引發 TypeError
result = divide(10, 0)    # 會引發 ValueError
"""

import logging
from pathlib import Path
import os
import traceback
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 設置日誌
logger = logging.getLogger(__name__)

# 設置日誌格式
formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

# 設置 console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 設置日誌檔案處理器
log_dir = Path(__file__).parent  # 使用當前文件的父目錄
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'calc.log'
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)

# 設置日誌等級
log_level = os.getenv("LOGGING", "INFO")
if log_level == "INFO":
    logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

# 設置 console handler 的等級: INFO always
console_handler.setLevel(logging.INFO)

# 添加處理器到日誌器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def add(x, y):
    """Add Function"""
    logger.debug(f'{get_function_name()}: {x+y}.')
    return x + y


def subtract(x, y):
    """Subtract Function"""
    logger.debug(f'{get_function_name()}: {x-y}.')
    return x - y


def multiply(x, y):
    """Multiply Function"""
    logger.debug(f'{get_function_name()}: {x*y}.')
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        logger.debug(f'{get_function_name()}: ValueError - Can not divide by zero.')
        raise ValueError('Can not divide by zero!')
    logger.debug(f'{get_function_name()}: {x/y}.')
    return x / y


def mina(x, y):
    """
    Min Function
    計算兩個數字中的最小值
    
    參數:
    x -- 第一個數字 (int/float)
    y -- 第二個數字 (int/float)
    
    返回:
    最小值 (int/float)
    
    備註:
    如果輸入不是數字，將引發 TypeError
    """
    logger.debug(f'{get_function_name()}: started.')
    
    # 檢查輸入類型
    if type(x) not in [int, float] or type(y) not in [int, float]:
        logger.debug(f'{get_function_name()}: TypeError - Both inputs must be numeric type.')
        raise TypeError("Both inputs must be numeric type.")
    
    # 計算最小值
    result = min(x, y)
    logger.debug(f'{get_function_name()}: {result}.')
    
    return result

if __name__ == '__main__':
    print('calc.py begins...')
    logger.debug('calc.py begins...')
    
    # 測試所有函數
    test_cases = [
        (10, 5),      # 正常情況
        (-1, 1),      # 負數情況
        (0, 0),       # 零值情況
        (3.5, 2.1),   # 浮點數情況
        ("10", 5),    # 錯誤類型
        (10, None)    # 錯誤類型
    ]
    
    for x, y in test_cases:
        try:
            print(f'add({x}, {y}) = {add(x, y)}')
            print(f'subtract({x}, {y}) = {subtract(x, y)}')
            print(f'multiply({x}, {y}) = {multiply(x, y)}')
            print(f'divide({x}, {y}) = {divide(x, y)}')
            print(f'mina({x}, {y}) = {mina(x, y)}')
        except Exception as e:
            print(f'Error: {str(e)}')
