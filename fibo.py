"""
斐波那契數列計算與效能分析

本程式實現了斐波那契數列的兩種計算方法，並提供效能比較和多種展示方式：

1. 基本實現:
   - 純遞迴實現 (fibo 函數)
   - 包含輸入參數驗證
   - 支援正整數輸入

2. 高效能實現:
   - 使用 LRU 快取的遞迴實現 (fibonacci 函數)
   - 最大快取容量為 1000
   - 显著提升重複計算的效能

3. 功能特點:
   - 效能比較工具 (compare_performance)
   - 多種資料結構展示 (display_results)
   - 異常處理機制 (test_abnormal_case)
   - 完整的日誌系統
   - 環境變數配置支援

4. 日誌系統:
   - 支援 DEBUG 和 INFO 兩種日誌等級
   - 同時輸出到控制台和日誌檔案
   - 日誌檔案每次運行時重新創建
   - 記錄詳細的執行流程和效能數據

使用方法:
1. 設置日誌等級:
   在 .env 檔案中設置 LOGGING 環境變數為 "DEBUG" 或 "INFO"

2. 運行程式:
   python fibo.py

3. 查看結果:
   - 控制台輸出
   - logger/fibo.log 檔案

注意事項:
- 程式會自動創建 logger 目錄和 fibo.log 檔案
- 日誌檔案每次運行時都會重新創建
- 可以通過修改 max_loop 參數調整效能測試範圍
"""

import time
import logging
from pathlib import Path
from functools import lru_cache
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
log_dir = Path(__file__).parent / 'logger'
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'fibo.log'
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

# set console handler level to INFO always    
console_handler.setLevel(logging.INFO)

# 添加處理器到日誌器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def fibo(n: int) -> int:
    """
    純遞迴實現的斐波那契數列計算
    
    Args:
        n (int): 要計算的斐波那契數列位置
        
    Returns:
        int: 斐波那契數列的第 n 個元素
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入不是正整數
    """
    if type(n) != int:
        raise TypeError("輸入必須為整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


"""
利用 'functools' 模組的快取策略

LRU 快取是一種快取策略，當快取滿了時，
會移除最久未使用的項目，然後添加新的項目。

有兩種情況：

1. 頁面命中：如果所需的頁面在主記憶體中，
    就是頁面命中。
2. 頁面錯誤：如果所需的頁面不在主記憶體中，
    就是頁面錯誤。

當頁面被引用時，所需的頁面可能在主記憶體中。

1. 如果在主記憶體中，需要將頁面從列表中分離，
    並將其移到隊列的前面。
2. 如果所需的頁面不在主記憶體中，
    就需要將其添加到主記憶體中。

簡而言之，

1. 將新頁面添加到隊列的前面
2. 更新對應的頁面地址在哈希表中

如果隊列滿了，需要移除隊列尾部的頁面。
當插入到隊列中時，需要將新頁面添加到隊列的前面。
"""


@lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    """
    使用 LRU 快取的斐波那契數列計算
    
    Args:
        n (int): 要計算的斐波那契數列位置
        
    Returns:
        int: 斐波那契數列的第 n 個元素
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入不是正整數
    """
    if type(n) != int:
        raise TypeError("輸入必須為正整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def compare_performance(max_loop: int = 30) -> None:
    """
    比較兩種斐波那契數列實現的效能
    
    Args:
        max_loop (int): 測試的最大範圍
    """
    # 測量不使用快取的版本
    logger.debug(f'{get_function_name()}:測量不使用快取的版本')
    t1 = time.time()
    for n in range(1, max_loop):
        logger.debug(f'{get_function_name()}:{n}:{fibo(n)}')
    t2 = time.time()
    cacheless_time = t2 - t1
    print(f'不使用快取的斐波那契函數花費了 {cacheless_time:.6f} 秒\n')

    # 測量使用快取的版本
    logger.debug(f'{get_function_name()}:測量使用快取的版本')
    t3 = time.time()
    for n in range(1, max_loop):
        logger.debug(f'{get_function_name()}:{n}:{fibonacci(n)}')
    t4 = time.time()
    cached_time = t4 - t3
    print(f'使用 LRU 快取的斐波那契函數花費了 {cached_time:.6f} 秒\n')

    # 比較結果
    logger.debug(f'{get_function_name()}:比較結果')
    print(f'比較：不使用快取的版本花費了 {cacheless_time/cached_time:.1f} 倍的時間。\n')

def display_results() -> None:
    """
    顯示斐波那契數列在不同資料結構中的表示
    """
    logger.debug(f'{get_function_name()}:顯示斐波那契數列在不同資料結構中的表示')
    # 斐波那契數列在列表中
    fib_list = [fibonacci(n) for n in range(1, 11)]
    logger.debug(f'{get_function_name()}:斐波那契數列在列表中：\n===>{fib_list}\n')
    print(f'斐波那契數列在列表中：\n===>{fib_list}\n')

    # 斐波那契數列在元組中
    fib_tuple = tuple(fibonacci(n) for n in range(1, 11))
    logger.debug(f'{get_function_name()}:斐波那契數列在元組中：\n===>{fib_tuple}\n')
    print(f'斐波那契數列在元組中：\n===>{fib_tuple}\n')

def test_abnormal_case() -> None:
    """
    測試異常情況
    """
    logger.debug(f'{get_function_name()}:測試異常情況')
    message = f'fibonacci("hello world")'
    try:
        print(message)
        print(fibonacci("hello world"))
    except Exception as e:
        logger.error(f'{get_function_name()}:發生異常：{str(e)}')
        print(f'===>發生異常：{str(e)}')

def main():
    """
    主函數，執行所有測試
    """
    logger.debug(f'{get_function_name()}:主函數，執行所有測試')
    # 清除快取
    fibonacci.cache_clear()
    
    # 執行效能比較
    compare_performance()
    
    # 顯示結果
    display_results()
    
    # 測試異常情況
    test_abnormal_case()

if __name__ == "__main__":
    main()
