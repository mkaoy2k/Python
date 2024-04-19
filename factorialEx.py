from functools import lru_cache

"""
Recursive Example: To calculate factorial of a non-negative integer.
遞廻函式例子: 求非負整數的乘冪
"""


@lru_cache(maxsize=10_000)
def factorial(num):
    """ This is a recursive function to calculate the factorial of a non-negative integer
    遞廻函式: 求某一正整數的乘冪
    """

    # checking the input must be a positive integer
    if type(num) != int:
        raise ValueError("The input must be a non-negative integer")
    elif num < 0:
        raise ValueError("The input must be a non-negative integer")

    # computing the n-th term
    if num == 1 or num == 0:
        return 1
    return (num * factorial(num - 1))


# Example factorial
if __name__ == '__main__':

    import time
    import math
    
    t1 = time.time()
    for n in range(0, 100):
        print(f'{n}! = {factorial(n)}')
    t2 = time.time()
    print(f'===>Time for factorial(): {t2-t1}')

    
    t1 = time.time()
    for n in range(0, 100):
        print(f'{n}! = {math.factorial(n)}')
    t2 = time.time()
    print(f'===>Time for math.factorial(): {t2-t1}')

    num = 'string'
    print(f'{num}! = {factorial(num)}\n')
