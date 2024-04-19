from heapq import *
from fibHeap import *
from random import randint
import time

# Initialize both heaps with some data
f = FibonacciHeap()
h = []
n = 1000
for i in range(0, n):
    r = randint(1, 1000)
    f.insert(r)
    heappush(h, r)

# Extract the min from both heaps and print the running time:

# Measure fib heap running time
start_time = time.time()
while f.total_nodes > 0:
    m = f.extract_min()
print(f"===>{(time.time() - start_time):15.10f} seconds run time for fib heap\n")

# Measure heapq running time
start_time = time.time()
while h:
    m = heappop(h)

print(f"===>{(time.time() - start_time):15.10f} seconds run time for heapq\n")
