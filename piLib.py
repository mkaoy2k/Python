"""Recursive Example: estimate Pi value.
Six methods to estimate π

    1. Using Monte Carlo simulation
    2. Using Leivniz Series
    3. Using math.pi constant
    4. Using numpy.pi constant
    5. Using Chudnovsky Algorithm
        leveraging recusive and LRU cache
    6. Using Bailey–Borwein–Plouffe (BBP) formula

遞廻函式例子: 估算無理數π值"""
import random as rd
import itertools
import math
import numpy as np
import decimal as dec
from functools import lru_cache

# The following string 'exact_pi_val' contains 1001 correct digit of 𝜋.
# So, The program will itself check if the calculated 𝜋 value
# is right or wrong up to 1000 digit.
exact_pi_1001 = str(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)


def matchDigit(pi):
    """Return the matched digits of 𝜋
    """
    for n in range(len(exact_pi_1001)):
        matched = (str(pi)[:n] == exact_pi_1001[:n])
        if matched is False:
            print(f'===>π值 = {exact_pi_1001[:n]}')
            print(f'===>π值~= {pi}')
            print(f"===>matched upto {n-2} after decimal point\n")
            return matched
    print(f'===>π值 = {exact_pi_1001}')
    print(f'===>π值~= {pi}')
    print(f"===>matched upto 1,000 after decimal point.")
    return matched


def pi_monte_carlo(num, digits):
    """Using Monte Carlo simulation
    Calculate the value of Pi using Monte Carlo Simulation
    where:
        num: number of samples
        digits: precision of dec.Decimal
    利用蒙地卡羅模擬方法估算圓周率"""

    circles = dec.Decimal(0)
    dec.getcontext().prec = digits + 1

    for n in range(num):
        a, b = rd.random(), rd.random()

        # 計算到圓心的距離
        if pow(a**2 + b**2, 0.5) < 1:
            circles += 1

    # 將四分之一的圓×4返回
    pi = 4 * circles / dec.Decimal(num)
    return (int(pi * 10**digits))


def pi_leibniz(num, digits):
    """Using Leivniz Series
    Estimate π value using Leibniz’s Series
    Where
        1. num: number of terms
        2. digits: precision of dec.Decimal
    The Leibniz formula is:

        Pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ....

    This series is never-ending, the more terms this series contains,
    the closer the value converges to the Pi value.
    """
    dec.getcontext().prec = digits + 1

    pi = dec.Decimal(4)
    minus = itertools.cycle((True, False))
    for denominator in range(3, num, 2):

        if next(minus):
            pi -= 4 / dec.Decimal(denominator)
        else:
            pi += 4 / dec.Decimal(denominator)
    return int(pi * 10**digits)


def pi_math_constant(digits):
    """Using math.pi constant
    Return pi attribute of 'math' Module with 'digits' precision
    """

    dec.getcontext().prec = digits + 1

    return int(dec.Decimal(math.pi) * 10**digits)


def pi_numpy_constant(digits):
    """Using numpy.pi constant
    Return pi attribute of 'numpy' Module with 'digits' precision
    """

    dec.getcontext().prec = digits + 1

    return int(dec.Decimal(np.pi) * 10**digits)


@lru_cache(maxsize=2000)
def pi_chudnov(n, digits):
    """Implement Chudnovsky inner series recursively
    Use LRU (Least Recently Used) cache strategey for performance
    """

    dec.getcontext().prec = digits + 1

    pi_chud = (((dec.Decimal(-1))**n) * (dec.Decimal(math.factorial(6 * n))) 
        * (13591409 + 545140134 * n)) / dec.Decimal(math.factorial(3 * n) 
        * ((math.factorial(n))**3) 
        * (640320**((3 * n) + (dec.Decimal(1.5)))))
    
    if n > 0:
        pi_chud = pi_chud + pi_chudnov(n - 1, digits)

    return pi_chud


def pi_chudnovsky(n, digits):
    """Using Chudnovsky Algorithm
    Estimate π value using Chudnovsky Algorithm,
    where: 'n' is the number of terms
    This algorithm is one of the fastest methods to
    estimate the value of 𝜋.
    Using this algorithm, 62.8 trillion digits of 𝜋 was calculated
    on 14th August, 2021.
    """

    dec.getcontext().prec = digits + 1

    pi_chud = pi_chudnov(n, digits)
    pi_chud = (dec.Decimal(pi_chud) * 12)
    pi_chud = (dec.Decimal(pi_chud**(-1)))

    return int(pi_chud * 10**n)


def pi_BBP(digits):
    """
    Computes the constant pi to a number of decimal digits,
    specified in the parameter, call 'digits',
    using the Bailey–Borwein–Plouffe (BBP)
    formula.
    """
    dec.getcontext().prec = digits + 1

    pi = dec.Decimal(0)
    k = dec.Decimal(0)
    precision = dec.Decimal(digits)

    while True:
        pi += (1 / pow(16, k)) * (
            (4 / (8 * k + 1)) - (2 / (8 * k + 4)) -
            (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
        k += 1
        if k >= precision:
            break
    return int(round(pi, digits) * 10**digits)


# to measure the elapsed time
import time

# Main: Estimate Pi value
def main():
    
    # Set the number of simulation and terms
    num_max = 10_000_000

    # dec.Decimal precision
    digits = 50

    print(f"1. Using Monte Carlo simulation {num_max:,} times:")
    start_time = time.time()
    pi = pi_monte_carlo(num_max, digits)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

    print(f"2. Using Leibniz Series {num_max:,} sumations:")
    start_time = time.time()
    pi = pi_leibniz(num_max, digits)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

    print(f"3. Using 'math' Module:")
    start_time = time.time()
    pi = pi_math_constant(digits)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

    print(f"4. Using 'numpy' Module:")
    start_time = time.time()
    pi = pi_numpy_constant(digits)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

    print(f"5. Using Chudnovsky Algorithm 1001 sumations:")
    start_time = time.time()
    for n in range(0, 1001):
        pi = pi_chudnovsky(n, 1005)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

    print(f"6. Using BBP Formula:")
    start_time = time.time()
    pi = pi_BBP(1000)
    stop_time = time.time()
    time_taken = stop_time - start_time
    matchDigit(pi)
    print(f'===>Took {time_taken} seconds.\n')

if __name__ == '__main__':
    main()