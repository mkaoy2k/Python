import time
"""
Recursive Example: calculate Fibonacci sequence.
遞廻函式例子: 求斐波那契數列
"""


def fibo(n):
    """Return the n-th element of Fibonacci sequence.
    Fibonacci sequnce is an infinite list of positive numbers,
    begining with the first two ones, and any subsequent number that equals to
    the sum of the previous two numbers."""

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


from functools import lru_cache
"""
利用 'functools' 模組的快取策略

The LRU caching scheme in 'functools' Module is to remove
the least recently used frame when the cache is full,
and a new page is referenced which is not there in the cache.

There are generally two cases with LRU Cache,

1. Page hit: If the required page is found in the main memory,
    it is a page hit.
2. Page Fault: If the required page is not found in the main 
    memory, page fault occurs.

When a page is referenced, the required page may be in the memory.

1. If it is in the memory, we need to detach the node of 
    the list and bring it to the front of the queue.
2. If the required page is not in memory, 
    we bring that in memory.

In other words,

1. we add a new node to the front of the queue
2. update the corresponding node address in the hash.

If the queue is full, i.e. all the frames are full, 
we remove a node from the rear of the queue.
When insert into the queue, we add the new node to the front 
of the queue.
"""


@lru_cache(maxsize=1000)
def fibonacci(n):

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
        return fibonacci(n - 1) + fibonacci(n - 2)


# Main
if __name__ == '__main__':

    max_loop = 30

    # Time both functions
    t1 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fibo(n)}')
    t2 = time.time()
    cacheless = t2 - t1
    print(f'Cacheless Fibonancii function took {cacheless} seconds\n')

    t3 = time.time()
    for n in range(1, max_loop):
        print(f'{n}:{fibonacci(n)}')
    t4 = time.time()
    cached = t4 - t3
    print(f'Fibonancii function with lru-cache took {cached} seconds\n')

    # Comparison
    print(
        f'Comparison: Cacheless/Cached took {cacheless/cached:,.1f} times longer.\n')

    # Fibonacci seq in a list
    L = [fibonacci(n) for n in range(1, 11)]
    print(f'Fibonacci seq in a list:\n===>{L}\n')

    # Fibonacci seq in a tuple
    T = (fibonacci(n) for n in range(1, 11))
    print(f'Fibonacci seq in a tuple:\n===>{tuple(T)}\n')

    # abnormal case
    message = f'fibonacci("hello world")'
    try:
        print(message)
        print(fibonacci("hello world"))
    except:
        print(f'===>Something is not right')
