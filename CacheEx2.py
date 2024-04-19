import time
from cacheLib import *


def fibo(n):
    """Return the n-th element of Fibonacci sequence without cache"""

    # checking the input must be a positive integer
    if type(n) != int:
        raise TypeError("The input must be a positive integer")
    elif n < 1:
        raise ValueError("The input must be a positive integer")

    # computing the n-th term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fiboCache(n):
    """Return the n-th element of Fibonacci sequence with cache"""
    # checking the input must be a positive integer
    if type(n) != int:
        raise TypeError("The input must be a positive integer")
    elif n < 1:
        raise ValueError("The input must be a positive integer")

    # computing the n-th term
    if n == 1:
        # Cache maintains a value object is a list with two elements:
        # 1. Fibonacci number, and
        # 2. Reference count (initialized as zero)
        my_cache.add(1, 1)
        return 1
    elif n == 2:
        my_cache.add(2, 1)
        return 1
    else:
        # Check the previous two fibo numbers
        a1 = n - 1
        a2 = n - 2
        if not my_cache.has(a1):
            # page fault
            my_cache.add(a1, fiboCache(a1))
        else:
            # increment reference count when page hit
            my_cache.inc(a1)

        if not my_cache.has(a2):
            # page fault
            my_cache.add(a2, fiboCache(a2))
        else:
            # increment reference count when page hit
            my_cache.inc(a2)

        # return the sum of a1 and a2
        return my_cache.get(a1) + my_cache.get(a2)


# Main
if __name__ == '__main__':

    max_loop = 31

    # Instantiate my cache
    my_cache = Cache()

    # Time both functions
    t1 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fibo(n)}')
    t2 = time.time()
    cacheless = t2 - t1
    print(f'cacheless Fibonancii function took {cacheless} seconds\n')

    t3 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fiboCache(n)}')
    t4 = time.time()
    cached = t4 - t3
    print(f'Cached Fibonancii function took {cached} seconds\n')

    # Comparison
    print(
        f'Comparison: Cacheless/Cached is {cacheless/cached:,.1f} times longer.\n')
