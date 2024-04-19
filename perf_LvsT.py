"""
Performance Testing between List and Tuple
Alternatively, check with glogTime.py
"""

import timeit
import random

# Measure space taken
L = list(range(1000))
T = tuple(range(1000))
print('Memory usage taken when initiated:')
print(f'===> List[0-999] = {L.__sizeof__():,} bytes')
print(f'===> Tuple[0-999] = {T.__sizeof__():,} bytes\n')

# Measure time taken with the same processing

# Create processing codes
process_L = """
def lookupList():
    L = list(range(1000))
    i = random.randint(0, L[999])
    j = random.randint(0, L[999])
    _ = abs( L[i] - L[j] )
"""

process_T = """
def lookupTuple():
    T = tuple(range(1000))
    i = random.randint(0, T[999])
    j = random.randint(0, T[999])
    _ = abs( T[i] - T[j] )
"""

# Number of times to instantiate and read List vs Tuple
max_loop = 20_000_000

list_performance = timeit.timeit(stmt=process_L, number=max_loop)
tuple_performance = timeit.timeit(stmt=process_T, number=max_loop)

print('To instantiate and read List vs Tuple:')
print(f'===> Lists  {max_loop:,} times = {list_performance} seconds')
print(f'===> Tuples {max_loop:,} times = {tuple_performance} seconds')

ratio_LvsT = list_performance / tuple_performance
print(
    f'===> Processing List over Tuple, took {ratio_LvsT:5.3f} times longer\n')
