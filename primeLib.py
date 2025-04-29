"""
primeLib.py - 質數相關函數庫

此模組提供多種質數相關的函數，包括質數生成和質數檢測功能。

主要功能：
1. generate_primes: 使用埃拉托斯特尼篩法生成前 n 個質數
2. is_prime_v1: 最簡單的 O(n) 質數檢測演算法
3. is_prime_v2: 使用平方根優化的 O(√n) 質數檢測
4. is_prime: 綜合多種優化策略的質數檢測（6k±1、奇數跳躍）
5. main: 示範與效能測試函數

使用方式：
- 直接執行模組：python primeLib.py
- 匯入特定函數：from primeLib import generate_primes, is_prime
"""

from typing import List
import math
import time

def generate_primes(n: int) -> List[int]:
    """
    生成前 n 個質數
    
    使用埃拉托斯特尼篩法 (Sieve of Eratosthenes) 生成質數列表
    
    Args:
        n (int): 需要生成的質數數量
    
    Returns:
        list: 包含前 n 個質數的列表
    """
    # 根據質數定理估算篩選範圍
    if n < 6:
        sieve_size = 15
    else:
        sieve_size = int(n * (math.log(n) + math.log(math.log(n)))) + 3
    sieve = [True] * sieve_size
    sieve[0:2] = [False, False]  # 0 和 1 不是質數

    limit = int(math.sqrt(sieve_size)) + 1
    for current_prime in range(2, limit):
        if sieve[current_prime]:
            # 將當前質數的所有倍數標記為合數
            for multiple in range(current_prime ** 2, sieve_size, current_prime):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes[:n]

def is_prime_v1(n: int) -> bool:
    """
    檢查數字是否為質數 (版本 1)
    
    使用最簡單的方法檢查質數，時間複雜度為 O(n)
    
    Args:
        n (int): 需要檢查的數字
    
    Returns:
        bool: 如果 n 是質數則返回 True，否則返回 False
    """
    if n == 1:
        return False  # 1 不是質數

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n: int) -> bool:
    """
    檢查數字是否為質數 (版本 2)
    
    使用平方根優化的方法檢查質數，時間複雜度為 O(√n)
    
    Args:
        n (int): 需要檢查的數字
    
    Returns:
        bool: 如果 n 是質數則返回 True，否則返回 False
    """
    if n == 1:
        return False  # 1 不是質數

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def is_prime(n: int) -> bool:
    """
    檢查數字是否為質數 (最優化版本)
    
    使用多種優化策略的質數檢查函數，包括：
    - 奇數優化
    - 6k±1 優化
    - 平方根優化
    
    Args:
        n (int): 需要檢查的數字
    
    Returns:
        bool: 如果 n 是質數則返回 True，否則返回 False
    """
    if n == 1:
        return False
    if n < 4:  # 2 和 3 是質數
        return True
    if n % 2 == 0 or n % 3 == 0:  # 排除偶數和 3 的倍數
        return False
    if n < 9:  # 4, 6, 8 已經排除，5 和 7 是質數
        return True
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(5, 1 + max_divisor, 6):  # 6k±1 優化
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True


    
if __name__ == '__main__':
    """
    主程式函數，用於測試各個質數生成函數
    """
    
    # 測試不同的質數檢查函數
    test_numbers = [1, 2, 3, 4, 5, 97, 100, 101]
    print("\n測試數字是否為質數:")
    for num in test_numbers:
        print(f"{num} 是質數嗎？(v1): {is_prime_v1(num)}")
        print(f"{num} 是質數嗎？(v2): {is_prime_v2(num)}")
        print(f"{num} 是質數嗎？(最優化): {is_prime(num)}")
    
    # 測試效能
    large_number = 1_000_000_007
    print(f"\n給定一個測試數字: {large_number:,}")
    print("效能測試開始...")
    for func in [is_prime_v1, is_prime_v2, is_prime]:
        start_time = time.time()
        result = func(large_number)
        end_time = time.time()
        print(f"{func.__name__}({large_number:,}): {result} ({end_time - start_time:.6f} 秒)")
 
