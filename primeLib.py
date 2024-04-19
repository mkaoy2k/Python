import math

def generate_primes(n):
    sieve = [True] * (n * 10)  # Create a boolean array, prime is True
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers

    for current_prime in range(2, int(n ** 0.5) + 1):
        if sieve[current_prime]:
            # Mark as composite all the multiples of the current prime
            for multiple in range(current_prime ** 2, n * 10, current_prime):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes[:n]


def is_prime_v1(n):
    """
    Return 'True' if 'n' is a prime number. 
    'False', otherwise.
    """
    if n == 1:
        return False  # 1 is not a prime

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_prime_v2(n):
    """
    Return 'True' if 'n' is a prime number. 
    'False', otherwise.
    """
    if n == 1:
        return False  # 1 is not a prime

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


def is_prime(n):
    """
    Return 'True' if 'n' is a prime number. 
    'False', otherwise.
    """
    if n == 1:
        return False  # 1 is not a prime

    # If it's even and not 2, then not a prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


if __name__ == '__main__':

    import time

    # Functional Test
    print(generate_primes(10000))

    num_max = 31
    print(f'\nCalling is_prime_v1({num_max})...')
    S = set()
    for n in range(1, num_max):
        if is_prime_v1(n):
            S.add(n)
    print(S)

    print(f'\nCalling is_prime_v2({num_max})...')
    S = set()
    for n in range(1, num_max):
        if is_prime_v2(n):
            S.add(n)
    print(S)

    print(f'\nCalling is_prime({num_max})...')
    S = set()
    for n in range(1, num_max):
        if is_prime(n):
            S.add(n)
    print(S)

    # Performance Testing
    loop = 30_000

    # Time function is_prime_v1()
    t1 = time.time()
    print(f'\nTiming is_prime_v1()...running {loop} times')
    S = set()
    for n in range(1, loop):
        if is_prime_v1(n):
            S.add(n)
    t2 = time.time()
    print(f'===>Time for is_prime_v1(): {t2-t1}')

    # Time function is_prime_v2()
    t1 = time.time()
    print(f'\nTiming is_prime_v2()...running {loop} times')
    S = set()
    for n in range(1, loop):
        if is_prime_v2(n):
            S.add(n)
    t2 = time.time()
    print(f'===>Time for is_prime_v2(): {t2-t1}')

    # Time function is_prime()
    t1 = time.time()
    print(f'\nTiming is_prime()...running {loop} times')
    S = set()
    for n in range(1, loop):
        if is_prime(n):
            S.add(n)
    t2 = time.time()
    print(f'===>Time for is_prime(): {t2-t1}')
