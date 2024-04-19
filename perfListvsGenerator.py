"""Performance comparison using 'glog' in this example:
1. List append function approach
2. Generator function approach
產生器函式與一般函式中生成列表比較程式"""

import glog as log
from glogTime import func_timer_decorator
from sys import getsizeof


def gen_list(nums):
    # 建立列表
    result = []
    for i in nums:
        result.append(i * i * i)
    return result


def gen_func(nums):
    # 定義產生器函式
    for n in nums:
        yield n * n * n


"""
定義了一個裝飾器函式 'func_timer_decorator' 和一個被裝飾的函式 time_gen()，
當 time_gen() 函式執行後，會看見 'func_timer_decorator' 執行後的結果，
套用在 time_gen() 函式上。
"""


@func_timer_decorator
def time_gen(nums):
    # 執行產生器函式運算
    my_gen = gen_func(nums)
    size = getsizeof(my_gen)
    log.info(f'{type(my_gen)}')
    log.info(f'size={size}')
    for num in my_gen:
        log.debug(num)


@func_timer_decorator
def time_list(nums):
    # 執行列表運算
    my_list = gen_list(nums)
    size = getsizeof(my_list)
    log.info(f'{type(my_list)}')
    log.info(f'size={size}')
    for num in my_list:
        log.debug(num)


# 印出資料多寡的模式有二：較多"DEBUG"和較少"INFO"
log.setLevel("DEBUG")
# log.setLevel("INFO")

# 假設一個數列列表，求每一元素的立方
numbers = [i for i in range(100_000)]
log.debug(f'數列列表初始值：{numbers}\n')

log.info('採行產生器函式實作:')
time_gen(numbers)

log.info('採行一般列表函式實作:')
time_list(numbers)
