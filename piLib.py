"""
π值估算函式庫

本程式庫提供多種方法來估算圓周率π的值，並比較其精確度和效能：
1. 蒙地卡羅模擬法
2. Leibniz 級數法
3. math.pi 常數
4. numpy.pi 常數
5. Chudnovsky 算法
6. Bailey–Borwein–Plouffe (BBP) BBP 公式

每個方法都具有不同的計算效率和精確度，使用者可以根據需求選擇合適的方法。
"""

import random as rd
import math
import numpy as np
import decimal as dec
from functools import lru_cache
import time

def matchDigit(pi):
    """
    比較估算的π值與實際π值的精確度

    Args:
        pi (decimal.Decimal): 估算的π值（必須具有小於或等於 1001 位小數精確度）

    Returns:
        int: 與實際π值相符的位數

    Raises:
        ValueError: 如果輸入的π值不是 decimal.Decimal 或精確度超過
    """
    # 檢查輸入類型
    if not isinstance(pi, dec.Decimal):
        raise ValueError("輸入的π值必須是 decimal.Decimal 類型")
    
    # 檢查精確度
    pi_str = str(pi)
    if len(pi_str) > 1003:  # 整數部分 + 小數點 + 1001 位小數
        raise ValueError(f"輸入的π值最多只能有 1001 位小數精確度，當前有 {len(pi_str)-2} 位")
    
    # 小數點後1000位正確的π值參考
    exact_pi_1000 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
    exact_pi_1000_len = len(exact_pi_1000)
    # 設置 decimal 的精確度
    
    # 比較小數點前後的數字
    decimal_digits = 0  # 小數部分匹配的位數
    pi_str = str(pi)
    pi_str_len = len(pi_str)
    # 比較整數部分
    if pi_str[0] != exact_pi_1000[0]:
        print(f'\tπ字串 = {exact_pi_1000[:1]}')
        print(f'\tπ值 ~= {pi_str[:1]}')
        print(f"\t精確到小數點後 {decimal_digits} 位\n")
        return decimal_digits
    
    max_len = min(pi_str_len, exact_pi_1000_len)
    # 比較小數部分
    for i in range(2, max_len):
        if pi_str[i] != exact_pi_1000[i]:
            break
        decimal_digits += 1
    exact_pi_stop = min(decimal_digits + 3, exact_pi_1000_len)
    pi_stop = min(decimal_digits + 3, pi_str_len)
    print(f'\tπ字串 = {exact_pi_1000[:exact_pi_stop]}')
    print(f'\tπ估值 = {pi_str[:pi_stop]}')
    print(f"\t精確到小數點後 {decimal_digits} 位\n")
    return decimal_digits


def pi_MonteCarlo(n):
    """
    使用蒙地卡羅模擬法估算π值

    Args:
        n (int): 模擬次數

    Returns:
        decimal.Decimal: 估算的π值（小數點後1000位）

    說明:
        使用隨機點在單位正方形內的分布來估算π值
        公式: π ≈ 4 * (落在單位圓內的點數 / 總點數)
    """
    dec.getcontext().prec = 1001
    inside = 0
    for _ in range(n):
        x, y = rd.random(), rd.random()
        if x*x + y*y <= 1:
            inside += 1
    pi = dec.Decimal(4) * dec.Decimal(inside) / dec.Decimal(n)
    return pi


def pi_Leibniz(n):
    """
    使用 Leibniz 級數法估算π值

    Args:
        n (int): 迭代次數

    Returns:
        decimal.Decimal: 估算的π值（小數點後1000位）

    說明:
        使用 Leibniz 級數:
        π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
    """
    dec.getcontext().prec = 1001
    pi = dec.Decimal(0)
    for i in range(n):
        term = dec.Decimal(-1)**i / dec.Decimal(2*i + 1)
        pi += term
    return pi * dec.Decimal(4)


def pi_Chudnovsky(n):
    """
    使用 Chudnovsky 算法估算π值

    Args:
        n (int): 迭代次數

    Returns:
        decimal.Decimal: 估算的π值（小數點後1000位）

    說明:
        使用 Chudnovsky 算法，具有較高的收斂速度
    """
    dec.getcontext().prec = 1001
    sum = dec.Decimal(0)
    for k in range(n):
        numerator = dec.Decimal((-1)**k) * dec.Decimal(math.factorial(6*k)) * (dec.Decimal(13591409) + dec.Decimal(545140134)*k)
        denominator = dec.Decimal(math.factorial(3*k)) * (dec.Decimal(math.factorial(k))**3) * (dec.Decimal(640320)**(3*k))
        sum += numerator / denominator
    pi = dec.Decimal(426880) * dec.Decimal(10005).sqrt() / sum
    return pi


def pi_BBP(n):
    """
    使用 BBP 公式估算π值

    Args:
        n (int): 迭代次數

    Returns:
        decimal.Decimal: 估算的π值（小數點後n位）

    說明:
        Bailey-Borwein-Plouffe (BBP) 公式是一個用來計算π的數學公式，
        由David Bailey、Peter Borwein和 Simon Plouffe在1995年發現。
        這個公式有幾個重要的特點：

        公式形式：
        π = Σ (1/16^k) * (4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))
        其中Σ表示求和，k從0開始到無窮大。

        主要特點：
        - 無需計算前導位：這是BBP公式最特別的地方。它允許直接計算π的第n位十六進制數字，而不需要先計算前面的所有位數。這意味著我們可以跳過前面的數字，直接計算特定位置的數字。
        - 快速收斂：由於公式中的16^k項，它具有指數級的收斂速度，計算效率高。
        - 基於16進制：公式本身是基於16進制的，但可以通過簡單轉換得到10進制的結果。
        
        工作原理：
        - 对于每个k值，公式会计算出一个小的"项" (term)
        - 每个项都是一个分数，分母是8k+1、8k+4、8k+5和8k+6
        - 所有项加起来就得到π的值
        - 由於1/16^k的存在，後面的項會越來越小，因此只需要計算有限次就可以得到足夠精確的結果
    """
    
    dec.getcontext().prec = n+1
    pi = dec.Decimal(0)
    for k in range(n):
        term = dec.Decimal(1)/dec.Decimal(16)**k * (
            dec.Decimal(4)/(dec.Decimal(8)*k+dec.Decimal(1)) -
            dec.Decimal(2)/(dec.Decimal(8)*k+dec.Decimal(4)) -
            dec.Decimal(1)/(dec.Decimal(8)*k+dec.Decimal(5)) -
            dec.Decimal(1)/(dec.Decimal(8)*k+dec.Decimal(6))
        )
        pi += term
    return pi


def pi_GaussLegendre(n):
    """
    使用 Gauss-Legendre 迭代法估算π值

    Args:
        n (int): 迭代次數

    Returns:
        decimal.Decimal: 估算的π值（小數點後1000位）

    說明:
        使用 Gauss-Legendre 迭代法，具有指數收斂速度
    """
    dec.getcontext().prec = 1001
    a = dec.Decimal(1)
    b = dec.Decimal(1) / dec.Decimal(2).sqrt()
    t = dec.Decimal(1) / dec.Decimal(4)
    p = dec.Decimal(1)
    
    for _ in range(n):
        a_next = (a + b) / dec.Decimal(2)
        b_next = (a * b).sqrt()
        t_next = t - p * (a - a_next)**2
        p_next = dec.Decimal(2) * p
        
        a, b, t, p = a_next, b_next, t_next, p_next
    
    return (a + b)**2 / (dec.Decimal(4) * t)


@lru_cache(maxsize=None)
def pi_GaussLegendre_cache(n):
    return pi_GaussLegendre(n)


def pi_math(n):
    """
    使用 math 模組的π常數

    Args:
        n (int): 迭代次數（無用，僅為了保持接口一致性）

    Returns:
        decimal.Decimal: π值（1000位小數精確度）
    """
    dec.getcontext().prec = 1001  # 設置精確度
    pi_value = dec.Decimal(math.pi)
    return pi_value.quantize(dec.Decimal('1.' + '0' * 1000))  # 限制到1000位小數


def pi_numpy(n):
    """
    使用 numpy 模組的π常數

    Args:
        n (int): 迭代次數（無用，僅為了保持接口一致性）

    Returns:
        decimal.Decimal: π值（1000位小數精確度）
    """
    dec.getcontext().prec = 1001  # 設置精確度
    pi_value = dec.Decimal(np.pi)
    return pi_value.quantize(dec.Decimal('1.' + '0' * 1000))  # 限制到1000位小數


def test_all_methods():
    """
    測試所有π值計算方法

    測試方法包括：
    1. 蒙地卡羅模擬 (100萬次)
    2. Leibniz 級數 (10萬次)
    3. math.pi 常數 (1次)
    4. numpy.pi 常數 (1次)
    5. Chudnovsky 算法 (100次)
    6. BBP 公式法 (1000次)
    7. Gauss-Legendre 迭代 (1000次)
    """
    methods = {
        "1. 蒙地卡羅模擬": (pi_MonteCarlo, 1_000_000),
        "2. Leibniz 級數": (pi_Leibniz, 100_000),
        "3. math.pi 常數": (pi_math, 1),
        "4. numpy.pi 常數": (pi_numpy, 1),
        "5. Chudnovsky 算法": (pi_Chudnovsky, 100),
        "6. BBP 公式": (pi_BBP, 1_000),
        "7. Gauss-Legendre 迭代": (pi_GaussLegendre, 1000)
    }
    for name, (method, iterations) in methods.items():
        print(f"\n{name}: {iterations:,} 次")
        start_time = time.time()
        pi = method(iterations)
        stop_time = time.time()
        time_taken = stop_time - start_time
        matched_digits = matchDigit(pi)
        print(f"\t精確到小數點後 {matched_digits} 位")
        print(f'\t執行時間: {time_taken:.6f} 秒')


def measure_all_methods():
    """
    測試所有π值計算方法

    測試方法包括：
    1. 蒙地卡羅模擬 (100萬次)
    2. Leibniz 級數 (10萬次)
    3. math.pi 常數 (1次)
    4. numpy.pi 常數 (1次)
    5. Chudnovsky 算法 (100次)
    6. BBP 公式法 (1000次)
    7. Gauss-Legendre 迭代 (1000次)
    """
    methods = {
        "1. 蒙地卡羅模擬": (pi_MonteCarlo, 1_000_000),
        "2. Leibniz 級數": (pi_Leibniz, 100_000),
        "3. math.pi 常數": (pi_math, 1),
        "4. numpy.pi 常數": (pi_numpy, 1),
        "5. Chudnovsky 算法": (pi_Chudnovsky, 100),
        "6. BBP 公式": (pi_BBP, 1_000),
        "7. Gauss-Legendre 迭代": (pi_GaussLegendre, 1000)
    }
    for name, (method, iterations) in methods.items():
        print(f"\n{name}: {iterations:,} 次")
        start_time = time.time()
        pi = method(iterations)
        stop_time = time.time()
        time_taken = stop_time - start_time
        matched_digits = matchDigit(pi)
        print(f"\t精確到小數點後 {matched_digits} 位")
        print(f'\t耗時: {time_taken:.6f} 秒')


def main():
    """
    主程式函數

    1. 測試所有π值計算方法
    2. 顯示每個方法的精確度和執行時間
    """
    print("=== π值計算方法比較 ===")
    print("開始性能測試各個方法...")
    measure_all_methods()
    print("性能測試完成！")


if __name__ == '__main__':
    """
    程式入口點

    執行主程式函數，進行π值計算方法的比較測試
    """
    main()