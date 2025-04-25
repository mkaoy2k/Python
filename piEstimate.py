"""
piEstimate.py - 使用BBP公式估算π的數字

這個程式使用BBP公式來估算π的數字，並估算特定位置的數字。
"""

from piLib import pi_BBP
import time
import decimal as dec

def estimate_pi_digit(ndigits: int) -> None:
    """
    估算π的小數位數並加總
    
    Args:
        ndigits (int): 要計算的小數位數
    """
    print(f'正在估算π的小數點後 {ndigits:,} 位數:')
    dec.getcontext().prec = ndigits+2
    start_time = time.time()
    pi = str(pi_BBP(ndigits))
    stop_time = time.time()
    time_taken = stop_time - start_time
    # 前100位數
    print(f'\tπ值小數點後80位數: {pi[:82]}')
    for n in range(10):
        print(f'\t小數點後第 {n+1:,} 位數的數字: {pi[n+2]}')
    print(f'\t第 {ndigits:,} 位數的數字: {pi[ndigits+1]}')
    print(f'\t耗時 {time_taken} 秒。')

    # 提取最後1000位數中每100位的數字
    print("\n分析最後笫9,000位數起每百位中的數字：")
    for n in range(ndigits-1000, ndigits+1, 100):
        print(f'\t第 {n:,} 位數的數字: {pi[n+1]}')

def main():
    """
    主程式入口點
    """
    ndigits = 10_000
    estimate_pi_digit(ndigits)

if __name__ == "__main__":
    main()
