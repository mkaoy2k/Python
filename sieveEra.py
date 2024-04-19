import time
import math
import numpy as np
from primeLib import is_prime

# List implementation using Python list object


def primes_list(num):
    """Generate a list of primes, less than an integer num,
    using Sieve of Eratosthenes algorithm and
    returning a Python list object.
    >>> primes_list(30) returns:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    # checking the input must be a positive integer > 2
    if type(num) != int:
        raise TypeError("The input must be an integer\n")

    if num < 3:
        raise ValueError("The input must be an integer greater than 2\n")

    # Sieving algorithm begins
    L = [2]
    if num == 3:
        return L

    for n in range(3, num + 1, 2):
        if is_prime(n):
            L.append(n)  # add new prime into the list

    return L

# Set implementation: using Python set object


def primes_set(num):
    """Generate a list of primes, less than an integer num,
    using Sieve of Eratosthenes algorithm and
    returning a Python set object.
    >>> primes_list(30) returns:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    # checking the input must be a positive integer > 2
    if type(num) != int:
        raise TypeError("The input must be an integer\n")

    if num < 3:
        raise ValueError("The input must be an integer greater than 2\n")

    # Sieving algorithm begins
    S = {2}
    if num == 3:
        return S

    for n in range(3, num + 1, 2):
        if is_prime(n):
            S.add(n)

    return S

# Generator implementation: using Python Generator Function


def primes_gen(num):
    """Generate primes up to a given integer, num.
    using Sieve of Eratosthenes algorithm in Python Generator function and
    returning Python set object.
    >>>print(*gen_primes(30)) returns:
    2 3 5 7 11 13 17 19 23 29
    """

    if type(num) != int:
        raise TypeError("The input must be an integer\n")

    if num < 3:
        raise ValueError("The input must be an integer greater than 2\n")

    yield 2

    for n in range(3, num + 1, 2):
        if is_prime(n):
            yield n

# Numpy implementation using Numpy array


def eratosthenes(n):

        # initialize an integer map [0,num) in ndarray
    isPrime = np.ones(n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i ** 2, n + 1, i):
                isPrime[j] = 0
    # return the indeces of ndarray, indicating primes
    return {x for x in range(2, n + 1) if isPrime[x]}


if __name__ == '__main__':

    # Functional test
    num_max = 100
    print(f'\nCalling primes_list({num_max})')
    print(f'Primes < {num_max}: {primes_list(num_max)}')

    print(f'\nCalling primes_set({num_max})...')
    print(f'Primes < {num_max}: {primes_set(num_max)}')

    print(f'\nCalling primes_gen({num_max})...')
    print(f'Primes < {num_max}: {set(primes_gen(num_max))}')

    print(f'\nCalling eratosthenes({num_max})...')
    print(f'Primes < {num_max}: {eratosthenes(num_max)}')

    # Performance Test
    loop = 5_000

    # Time primes_list()
    t1 = time.time()
    print(f'\nTiming primes_list()...running {loop} times')
    for i in range(3, loop):
        primes_list(i)
    t2 = time.time()
    print(f'===>Time for primes_list(): {t2-t1}')

    # Time primes_set()
    t1 = time.time()
    print(f'\nTiming primes_set()...running {loop} times')
    for i in range(3, loop):
        primes_set(i)
    t2 = time.time()
    print(f'===>Time for primes_set(): {t2-t1}')

    # Time primes_gen()
    t1 = time.time()
    print(f'\nTiming primes_gen()...running {loop} times')
    for i in range(3, loop):
        set(primes_gen(i))
    t2 = time.time()
    print(f'===>Time for primes_gen(): {t2-t1}')

    # Time primes_np()
    t1 = time.time()
    print(f'\nTiming eratosthenes()...running {loop} times')
    for i in range(3, loop):
        eratosthenes(i)
    t2 = time.time()
    print(f'===>Time for eratosthenes(): {t2-t1}')
