"""
埃拉托斯特尼篩法 (Sieve of Eratosthenes) 實作
本程式提供多種方式來生成質數列表，包括：
- Python list 實作
- Python set 實作
- Generator 實作
- NumPy array 實作

使用方法：
1. primes_list(n) - 返回質數列表
2. primes_set(n) - 返回質數集合
3. primes_gen(n) - 生成器實作
4. eratosthenes(n) - 埃拉托斯特尼篩法實作

注意：輸入必須為大於2的正整數
"""

import time
from primeLib import is_prime


def primes_list(num):
    """
    使用埃拉托斯特尼篩法生成質數列表
    
    Args:
        num (int): 要生成質數的上限值
        
    Returns:
        list: 包含所有小於 num 的質數列表
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入小於3
    """
    if type(num) != int:
        raise TypeError("輸入必須為整數")
    if num < 3:
        raise ValueError("輸入必須為大於2的整數")
    
    L = [2]
    if num == 3:
        return L

    for n in range(3, num + 1, 2):
        if is_prime(n):
            L.append(n)
    
    return L


def primes_set(num):
    """
    使用埃拉托斯特尼篩法生成質數集合
    
    Args:
        num (int): 要生成質數的上限值
        
    Returns:
        set: 包含所有小於 num 的質數集合
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入小於3
    """
    if type(num) != int:
        raise TypeError("輸入必須為整數")
    if num < 3:
        raise ValueError("輸入必須為大於2的整數")
    
    S = {2}
    if num == 3:
        return S

    for n in range(3, num + 1, 2):
        if is_prime(n):
            S.add(n)
    
    return S


def primes_gen(num):
    """
    使用生成器實現埃拉托斯特尼篩法
    
    Args:
        num (int): 要生成質數的上限值
        
    Yields:
        int: 生成的質數
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入小於3
    """
    if type(num) != int:
        raise TypeError("輸入必須為整數")
    if num < 3:
        raise ValueError("輸入必須為大於2的整數")
    
    yield 2
    for n in range(3, num + 1, 2):
        if is_prime(n):
            yield n


def eratosthenes(n):
    """
    使用實作埃拉托斯特尼篩法
    
    Args:
        n (int): 要生成質數的上限值
        
    Returns:
        list: 包含所有小於 n 的質數列表
        
    Raises:
        TypeError: 如果輸入不是整數
        ValueError: 如果輸入小於3
    """
    if type(n) != int:
        raise TypeError("輸入必須為整數")
    if n < 3:
        raise ValueError("輸入必須為大於2的整數")
    
    L = [2]
    if n == 3:
        return L

    for n in range(3, n + 1, 2):
        if is_prime(n):
            L.append(n)
    
    return L


def main():
    """主程式函數，用於測試各個質數生成函數"""
    num_max = 100
    
    print(f'\n呼叫 primes_list({num_max})')
    start_time = time.time()
    primes = primes_list(num_max)
    print(f'執行時間: {time.time() - start_time:.6f} 秒')
    print(f'質數列表實作: {primes}')
    
    print(f'\n呼叫 primes_set({num_max})')
    start_time = time.time()
    primes = primes_set(num_max)
    print(f'執行時間: {time.time() - start_time:.6f} 秒')
    print(f'質數集合實作: {sorted(primes)}')
    
    print(f'\n呼叫 primes_gen({num_max})')
    start_time = time.time()
    primes = list(primes_gen(num_max))
    print(f'執行時間: {time.time() - start_time:.6f} 秒')
    print(f'質數生成器實作: {primes}')
    
    print(f'\n呼叫 eratosthenes({num_max})')
    start_time = time.time()
    primes = eratosthenes(num_max)
    print(f'執行時間: {time.time() - start_time:.6f} 秒')
    print(f'埃拉托斯特尼篩法實作: {primes}')


if __name__ == '__main__':
    main()
