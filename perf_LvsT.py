"""
比較 Python 中 list 和 tuple 的性能測試
本程式測試 list 和 tuple 在內存使用和執行效率上的差異
"""

import timeit

def measure_memory_usage():
    """
    測量 list 和 tuple 的內存使用量
    """
    L = list(range(1000))
    T = tuple(range(1000))
    list_mem = L.__sizeof__()
    tuple_mem = T.__sizeof__()
    print('初始化時的內存使用量:')
    print(f'\t  List[0-999] = {list_mem:,} bytes')
    print(f'\t Tuple(0-999) = {tuple_mem:,} bytes')
    ratio_LvsT = list_mem / tuple_mem
    print(f'\t內存使用量: list 比 tuple 耗內存 {ratio_LvsT:5.3f} 倍\n')

def create_process_code():
    """
    創建用於測試的處理代碼
    """
    process_L = """
def lookupList():
    L = list(range(1000))
    i = random.randint(0, L[999])
    j = random.randint(0, L[999])
    _ = (L[i] - L[j]) ** 2
"""
    
    process_T = """
def lookupTuple():
    T = tuple(range(1000))
    i = random.randint(0, T[999])
    j = random.randint(0, T[999])
    _ = (T[i] - T[j]) ** 2
"""
    
    return process_L, process_T

def measure_performance(process_L, process_T, max_loop=20_000_000):
    """
    測量 list 和 tuple 的執行性能
    
    Args:
        process_L (str): list 的測試代碼
        process_T (str): tuple 的測試代碼
        max_loop (int): 測試次數
    """
    list_performance = timeit.timeit(stmt=process_L, number=max_loop)
    tuple_performance = timeit.timeit(stmt=process_T, number=max_loop)
    
    print(f'list 與 tuple 的性能量測:\n\t{max_loop:,} 次生成和隨機讀取 1000 個元素的列表和元組任二個元素差的平方')
    print(f'\t處理  Lists 共耗時 {list_performance:.6f} 秒')
    print(f'\t處理 Tuples 共耗時 {tuple_performance:.6f} 秒')
    
    ratio_LvsT = list_performance / tuple_performance
    print(f'\t性能量測: list 比 tuple 耗時 {ratio_LvsT:5.3f} 倍\n')

def main():
    """
    主函數，執行所有測試
    """
    # 測量內存使用量
    measure_memory_usage()
    
    # 創建測試代碼
    process_L, process_T = create_process_code()
    
    # 測量性能
    measure_performance(process_L, process_T)

if __name__ == "__main__":
    main()
