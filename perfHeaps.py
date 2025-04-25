"""
比較 Fibonacci heap 與 Python 內建 heapq 的性能

這個程式會:
1. 初始化兩個堆結構：Fibonacci heap 和 heapq
2. 向每個堆中插入隨機數字
3. 測量並比較從堆中提取最小值的運行時間
"""

from heapq import *
from fibheap import Fheap, Node
from random import randint
import time

def initialize_heaps(size=1000):
    """
    初始化兩個堆結構並填充數據
    
    Args:
        size: 要插入的元素數量。預設為 1000
        
    Returns:
        tuple: 包含兩個堆的元組
            - 第一個元素：Fibonacci heap 實例
            - 第二個元素：包含整數的 heapq 列表
    """
    # 初始化堆結構
    fib_heap = Fheap()
    python_heap = []
    
    # 生成並插入隨機數據
    for _ in range(size):
        random_num = randint(1, 1000)
        fib_heap.insert(Node(random_num))  # 使用 Node 對象
        heappush(python_heap, random_num)
    
    return fib_heap, python_heap

def measure_performance(fib_heap, python_heap):
    """
    測量兩個堆的性能並打印結果
    
    Args:
        fib_heap: Fibonacci heap 實例
        python_heap: heapq 實例
    """
    # 測量 Fibonacci heap 的運行時間
    start_time = time.time()
    while fib_heap.num_nodes > 0:  # 使用 num_nodes 來檢查堆是否為空
        fib_heap.extract_min()
    fib_time = time.time() - start_time
    
    # 測量 heapq 的運行時間
    start_time = time.time()
    while python_heap:
        heappop(python_heap)
    heap_time = time.time() - start_time
    
    # 打印結果
    print(f"===>{fib_time:15.10f} 秒 - Fibonacci heap 運行時間")
    print(f"===>{heap_time:15.10f} 秒 - heapq 運行時間")

def main():
    """
    主函數，執行性能測試
    """
    # 初始化堆
    fib_heap, python_heap = initialize_heaps()
    
    # 測量性能
    measure_performance(fib_heap, python_heap)

if __name__ == "__main__":
    main()
