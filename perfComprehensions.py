"""求數列中每一元素的立方
Yhere are 4 approaches demonstrated in this example:
1. List function approach
2. Generator function approach
3. List comprehension approach
4. Generator expression approach
"""

import glog as log  # pip install glog
from glogTime import func_timer_decorator
from sys import getsizeof

from absl import app    # pip install absl-py
from absl import flags


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


def compr_list(nums):
    return [n * n * n for n in nums]


def gexpr(nums):
    return (n * n * n for n in nums)


"""複習一下：
以下利用裝飾器定義了一個函式包装 (Function Wrapper)，叫 'func_timer_decorator' 套在一個受测函式 time_gen()，
當 time_gen() 函式執行後，函式包装 'func_timer_decorator' 執行：
1. 記錄 time_gen() 函式進入時間
2. 呼叫 time_gen() 函式
3. 記錄 time_gen() 函式結束時間
"""


@func_timer_decorator
def time_list(nums):
    # 執行列表運算
    my_list = gen_list(nums)
    size = getsizeof(my_list)
    log.info(f'{type(my_list)}')
    log.info(f'size={size}')
    for num in my_list:
        log.debug(num)


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
def time_compr(nums):
    # 執行列表生成式運算
    my_compr = compr_list(nums)
    size = getsizeof(my_compr)
    log.info(f'{type(my_compr)}')
    log.info(f'size={size}')
    for num in my_compr:
        log.debug(num)


@func_timer_decorator
def time_gexpr(nums):
    # 執行產生器表達式運算
    my_gexpr = gexpr(nums)
    size = getsizeof(my_gexpr)
    log.info(f'{type(my_gexpr)}')
    log.info(f'size={size}')
    for num in my_gexpr:
        log.debug(num)


FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

# Workaround for FATAL Flags parsing error:
flags.DEFINE_string('f', None, "Unknown command line flag 'f'")


def main(argv):
    if FLAGS.debug:
        log.setLevel("DEBUG")
    else:
        log.setLevel("INFO")

    # 假設一個數列列表，求每一元素的立方
    numbers = [i for i in range(100_000)]
    log.debug(f'數列列表初始值：{numbers}\n')

    log.info('1. 採行一般列表函式實作:')
    time_list(numbers)

    log.info('2. 採行產生器函式實作:')
    time_gen(numbers)

    log.info('3. 採行列表生成式實作:')
    time_compr(numbers)

    log.info('4. 採行產生器表達式實作:')
    time_gexpr(numbers)


if __name__ == '__main__':
    """
    To run this example (say in perComprehensions.py)
    with debug flag in the command line as follows:
    python -m perfComprehensions --debug 2> 'sample/perfComprehensions.log'
    """
    try:
        # workaround for a warning: exception SystemExit
        app.run(main)
    except:
        pass
