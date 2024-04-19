"""Measuring an elapsed time of function execution
by creating a timestamp object, inAndOutLog, using 'glog' module.
用法:

@func_timer_decorator
def xyz():
    ...

當 xyz() 函式執行後，會看見 'func_timer_decorator' 執行後的結果，
套用在 xyz() 函式上。
"""
import glog as log
import datetime
import random

class inAndOutLog():
    def __init__(self, funcName):
        self.funcName = funcName

    def __enter__(self):
        log.info(f'開始: {self.funcName}')
        self.init_time = datetime.datetime.now()
        return self

    def __exit__(self, type, value, tb):
        log.info(
            f'結束: {self.funcName} 共花 {datetime.datetime.now() - self.init_time} 秒.\n')


def func_timer_decorator(func):

    def func_wrapper(*args, **kwargs):
        with inAndOutLog(func.__name__):
            return func(*args, **kwargs)
    return func_wrapper

# Function testing
# Comparing read time between List and Tuple
# Alternatively, check with perf_LvsT.py
@func_timer_decorator
def lookupList(cnt):
    L = list(range(cnt))
    for _ in range(cnt):
        i = random.randint(0, L[cnt-1])
        j = random.randint(0, L[cnt-1])
        _ = abs( L[i] - L[j] )

@func_timer_decorator
def lookupTuple(cnt):
    T = tuple(range(cnt))
    for _ in range(cnt):
        i = random.randint(0, T[cnt-1])
        j = random.randint(0, T[cnt-1])
        _ = abs( T[i] - T[j] )

if __name__ == '__main__':

    # Number of times to read a List vs Tuple
    max_loop = 2_000_000

    print(f'{max_loop:,} times to initiate and read a List vs Tuple:')
    lookupList(max_loop)
    lookupTuple(max_loop)