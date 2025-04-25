"""
比較四種不同的方法計算數列中每個元素的立方值

本程式展示四種不同的程式設計方法來計算數列中每個元素的立方值，
並比較它們的效能和記憶體使用情況。

方法包括：
1. 列表函數方法 (List function approach)
2. 產生器函數方法 (Generator function approach)
3. 列表生成式方法 (List comprehension approach)
4. 產生器表達式方法 (Generator expression approach)

使用 Python 標準 logging 模組進行日誌記錄，並使用自定義的裝飾器來測量執行時間。
"""

import logging
from glogTime import func_timer_decorator
from sys import getsizeof
import sys

from absl import app    # pip install absl-py
from absl import flags

def gen_list(nums):
    """
    使用傳統列表函數方法計算立方值
    
    Args:
        nums: 數字列表
    
    Returns:
        list: 包含每個元素立方值的列表
    """
    result = []
    for i in nums:
        result.append(i * i * i)
    return result


def gen_func(nums):
    """
    使用產生器函數方法計算立方值
    
    Args:
        nums: 數字列表
    
    Yields:
        int: 每個元素的立方值
    """
    for n in nums:
        yield n * n * n


def compr_list(nums):
    """
    使用列表生成式方法計算立方值
    
    Args:
        nums: 數字列表
    
    Returns:
        list: 包含每個元素立方值的列表
    """
    return [n * n * n for n in nums]


def gexpr(nums):
    """
    使用產生器表達式方法計算立方值
    
    Args:
        nums: 數字列表
    
    Returns:
        generator: 包含每個元素立方值的產生器
    """
    return (n * n * n for n in nums)


"""
複習一下：
以下利用裝飾器定義了一個函式包装 (Function Wrapper)，
叫 'func_timer_decorator' 套在一個受测函式 time_gen()，
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
    logging.info(f'{type(my_list)}')
    logging.info(f'size={size}')
    for num in my_list:
        logging.debug(num)


@func_timer_decorator
def time_gen(nums):
    # 執行產生器函式運算
    my_gen = gen_func(nums)
    size = getsizeof(my_gen)
    logging.info(f'{type(my_gen)}')
    logging.info(f'size={size}')
    for num in my_gen:
        logging.debug(num)


@func_timer_decorator
def time_compr(nums):
    # 執行列表生成式運算
    my_compr = compr_list(nums)
    size = getsizeof(my_compr)
    logging.info(f'{type(my_compr)}')
    logging.info(f'size={size}')
    for num in my_compr:
        logging.debug(num)


@func_timer_decorator
def time_gexpr(nums):
    # 執行產生器表達式運算
    my_gexpr = gexpr(nums)
    size = getsizeof(my_gexpr)
    logging.info(f'{type(my_gexpr)}')
    logging.info(f'size={size}')
    for num in my_gexpr:
        logging.debug(num)


FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

# Workaround for FATAL Flags parsing error:
flags.DEFINE_string('f', None, "Unknown command line flag 'f'")


def main(argv):
    """
    程式主入口點
    
    Args:
        argv: 命令列參數
    
    Returns:
        None
    """
    if FLAGS.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # 建立測試數列
    numbers = [i for i in range(100_000)]
    logging.debug(f'數列列表初始值：{numbers}\n')

    # 依序執行四種方法並記錄效能
    for method in ['列表函數', '產生器函數', '列表生成式', '產生器表達式']:
        logging.info(f'\n=== {method} 方法 ===')
        
        if method == '列表函數':
            time_list(numbers)
        elif method == '產生器函數':
            time_gen(numbers)
        elif method == '列表生成式':
            time_compr(numbers)
        else:
            time_gexpr(numbers)


if __name__ == '__main__':
    """
    程式入口點
    
    執行方式：
    python -m perfComprehensions --debug
    """
    try:
        app.run(main)
    except SystemExit:
        pass  # 正常結束
    except Exception as e:
        logging.error(f"程式執行時發生錯誤: {str(e)}")
        sys.exit(1)
