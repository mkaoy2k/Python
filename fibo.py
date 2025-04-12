"""
斐波那契數列計算範例

本程式展示了兩種不同的斐波那契數列計算方法：
1. 純遞迴實現 (fibo 函數)
2. 使用 LRU 快取的遞迴實現 (fibonacci 函數)

主要功能特點：
- 支援正整數輸入檢查
- 提供效能比較
- 顯示不同資料結構的結果（列表和元組）
- 包含異常處理機制

使用方法：
直接運行此程式即可看到斐波那契數列的計算結果和效能比較

注意事項：
- 輸入必須為正整數
- 程式會自動處理非數字輸入
"""

import time
import logging
from pathlib import Path
from functools import lru_cache

# 設置日誌
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 確保 logger 目錄存在
log_dir = Path(__file__).parent / 'logger'
log_dir.mkdir(exist_ok=True)

# 建立日誌檔案處理器
log_file = log_dir / 'fibo.log'
file_handler = logging.FileHandler(log_file, encoding='utf-8')
file_handler.setLevel(logging.INFO)

# 設置日誌格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加處理器到日誌器
logger.addHandler(file_handler)


def fibo(n):
    """回傳斐波那契數列的第 n 個元素
    
    斐波那契數列是一個無限的正整數序列，
    從前兩個 1 開始，每個後續數字等於前兩個數字的和。
    """

    # 檢查輸入是否為正整數
    if type(n) != int:
        raise TypeError("輸入必須為整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    # 計算第 n 個項
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
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
def fibonacci(n):
    """回傳斐波那契數列的第 n 個元素
    
    斐波那契數列是一個無限的正整數序列，
    從前兩個 1 開始，每個後續數字等於前兩個數字的和。
    
    此函數使用 LRU 快取來優化效能
    """

    # 檢查輸入是否為正整數
    if type(n) != int:
        raise TypeError("輸入必須為正整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    # 計算第 n 個項
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Main
if __name__ == '__main__':

    max_loop = 30

    # Time both functions
    t1 = time.time()
    for n in range(1, max_loop):
        logger.info(f'{n}:{fibo(n)}')
    t2 = time.time()
    cacheless = t2 - t1
    print(f'不使用快取的斐波那契函數花費了 {cacheless} 秒\n')

    t3 = time.time()
    for n in range(1, max_loop):
        logger.info(f'{n}:{fibonacci(n)}')
    t4 = time.time()
    cached = t4 - t3
    print(f'使用 LRU 快取的斐波那契函數花費了 {cached} 秒\n')

    # Comparison
    print(
        f'比較：不使用快取的斐波那契函數花費了 {cacheless/cached:,.1f} 倍的時間。\n')

    # Fibonacci seq in a list
    L = [fibonacci(n) for n in range(1, 11)]
    print(f'斐波那契數列在列表中：\n===>{L}\n')

    # Fibonacci seq in a tuple
    T = (fibonacci(n) for n in range(1, 11))
    print(f'斐波那契數列在元組中：\n===>{tuple(T)}\n')

    # abnormal case
    message = f'fibonacci("hello world")'
    try:
        print(message)
        print(fibonacci("hello world"))
    except:
        print('===>發生異常')
