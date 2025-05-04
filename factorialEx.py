"""
這個程式是一個階乘計算的示範，主要特點包括：

1. 功能說明:
   - 實現階乘計算功能
   - 支援非負整數輸入
   - 使用遞迴方式實現

2. 技術特點:
   - 使用 @lru_cache 裝飾器進行快取優化
     - 最大快取大小設為 10,000
     - 可以大幅提高重複計算的效能
   - 包含輸入參數驗證
     - 檢查輸入是否為整數
     - 檢查輸入是否為非負數
   - 使用 logging 模組進行日誌記錄

3. 使用場景:
   - 適用於需要頻繁計算階乘的場景
   - 特別適合重複計算相同數字的階乘
   - 適用於數學運算和組合數學問題

注意事項:
1. 階乘運算會隨著數字增大而迅速增長
2. 雖然使用了快取，但過大的數字仍可能導致記憶體問題
3. 輸入必須為非負整數，否則會引發 ValueError
"""

from functools import lru_cache
import math
import time
import logging
import sys
from pathlib import Path
import os
import traceback
from dotenv import load_dotenv

# 設置整數轉換為字串的限制
sys.set_int_max_str_digits(1000000)  # 設置為 1000000 位數

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
log_dir = Path(__file__).parent / 'logger'
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'factorialEx.log'
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

@lru_cache(maxsize=10_000)
def factorial(num):
    """這是個遞迴函式，用於計算非負整數的階乘
    遞迴函式: 求某一正整數的乘冪
    """
    logger.debug(f'呼叫 {get_function_name()}')
    # 檢查輸入必須是正整數
    if type(num) != int:
        logger.error(f"{get_function_name()}: 輸入必須為整數")
        raise ValueError("輸入必須為整數")
    elif num < 0:
        logger.error(f"{get_function_name()}: 輸入必須為非負整數")
        raise ValueError("輸入必須為非負整數")
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    try:
        print("Case 1. 測試自定義的階乘函式:")
        t1 = time.time()
        for n in range(0, 1_000):
            logger.debug(f'{get_function_name()}: {n}! = {factorial(n)}')
        t2 = time.time()
        case1 = t2 -t1
        print(f'\t自定義階乘函式耗時: {case1} 秒\n')

        print("Case 2. 測試 math 模組的階乘函式:")
        t1 = time.time()
        for n in range(0, 1_000):
            logger.debug(f'{get_function_name()}: {n}! = {math.factorial(n)}')
        t2 = time.time()
        case2 = t2 -t1
        fold = case1 / case2
        print(f'\tmath.factorial() 耗時: {case2} 秒\n')
        print(f'自定義階乘函式耗時/math.factorial() 耗時:  {fold:.2f} 倍\n')
        
        print("Case 3. 測試異常情況:")
        num = '字串'
        print(f'測試輸入: {num}')
        print(f'{num}! = {factorial(num)}\n')
    except ValueError as e:
        print(f"發生錯誤: {e}")
    except Exception as e:
        print(f"發生未知錯誤: {e}")
    finally:
        print("程式結束")
