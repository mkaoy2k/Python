import time
from cacheLib import *


def fibo(n):
    """
    計算費波那契數列的第n個元素（不使用快取）
    
    參數:
    n (int): 要計算的費波那契數列位置
    
    回傳:
    int: 費波那契數列的第n個元素
    
    備註:
    這個實作使用遞迴方式計算，沒有使用快取機制
    """
    # 驗證輸入是否為正整數
    if type(n) != int:
        raise TypeError("輸入必須為正整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    # 基本情況：前兩個費波那契數都是1
    if n == 1 or n == 2:
        return 1
    else:
        # 遞迴計算第n個費波那契數
        return fibo(n - 1) + fibo(n - 2)


def fiboCache(n):
    """
    計算費波那契數列的第n個元素（使用快取）
    
    參數:
    n (int): 要計算的費波那契數列位置
    
    回傳:
    int: 費波那契數列的第n個元素
    
    備註:
    這個實作使用快取機制來優化性能
    """
    # 驗證輸入是否為正整數
    if type(n) != int:
        raise TypeError("輸入必須為正整數")
    elif n < 1:
        raise ValueError("輸入必須為正整數")

    # 處理基本情況
    if n == 1 or n == 2:
        # 將結果存入快取
        my_cache.add(n, 1)
        return 1
    else:
        # 計算前兩個費波那契數
        a1 = n - 1
        a2 = n - 2
        
        # 檢查快取中是否已有a1的值
        if not my_cache.has(a1):
            # 如果沒有，遞迴計算並存入快取
            my_cache.add(a1, fiboCache(a1))
        else:
            # 如果有，增加參考計數
            my_cache.inc(a1)

        # 檢查快取中是否已有a2的值
        if not my_cache.has(a2):
            my_cache.add(a2, fiboCache(a2))
        else:
            my_cache.inc(a2)

        # 回傳兩個數的和
        return my_cache.get(a1) + my_cache.get(a2)


if __name__ == '__main__':
    # 設定最大計算範圍
    max_loop = 31
    
    # 建立快取實例
    my_cache = Cache()
    
    # 測試不使用快取的版本
    print("=== 不使用快取的版本 ===")
    t1 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fibo(n)}')
    t2 = time.time()
    cacheless_time = t2 - t1
    print(f'不使用快取的版本花費時間: {cacheless_time:.6f} 秒\n')

    # 測試使用快取的版本
    print("=== 使用快取的版本 ===")
    t3 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fiboCache(n)}')
    t4 = time.time()
    cached_time = t4 - t3
    print(f'使用快取的版本花費時間: {cached_time:.6f} 秒\n')

    # 比較兩個版本的性能
    speedup = cacheless_time / cached_time
    print(f'性能比較: 不使用快取的版本比使用快取的版本慢 {speedup:.1f} 倍')
