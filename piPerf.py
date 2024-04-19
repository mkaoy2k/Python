import time
from piLib import *
import decimal as dec

"""Measure various Pi estimate functions.
Five methods to estimate π

    1. Using Monte Carlo simulation
    2. Using Leivniz Series
    3. Using math.pi constant
    4. Using numpy.pi constant
    5. Using Chudnovsky Algorithm

效能測試: 五種估算π值方法"""

# Main: Measure Pi functions
if __name__ == '__main__':

    # Set the number of simulation and terms
    num_max = 10_000_000

    # Decimal precision
    digits = 50

    print(f"1. Using Monte Carlo simulation {num_max:,} times:")
    t1 = time.time()
    pi = pi_monte_carlo(num_max, digits)
    t2 = time.time()
    print(f"===>Time took {(t2-t1):.2f} seconds\n")

    print(f"2. Using Leibniz Series {num_max:,} sumations:")
    t1 = time.time()
    pi = pi_leibniz(num_max, digits)
    t2 = time.time()
    print(f"===>Time took {(t2-t1):.2f} seconds\n")

    digits = 50
    dec.getcontext().prec = digits
    print(f"3. Using 'math' Module:")
    t1 = time.time()
    pi = pi_math_constant(digits)
    t2 = time.time()
    print(f"===>Time took {(t2-t1):.10f} seconds\n")

    print(f"4. Using 'numpy' Module:")
    t1 = time.time()
    pi = pi_numpy_constant(digits)
    t2 = time.time()
    print(f"===>Time took {(t2-t1):.10f} seconds\n")

    # The Chudnovsky Algorithm runs up to 1001 sumations of 𝜋-formula
    print(f"5. Using Chudnovsky Algorithm 1001 sumations:")
    digits = 1005
    t1 = time.time()
    for n in range(1, 1001):
        pi = pi_chudnovsky(n, digits)
    t2 = time.time()

    # Time pi_chudnovsky()
    print(f"===>Time took {(t2-t1):.2f} seconds\n")
