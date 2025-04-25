"""
生成器函式與列表函式效能比較程式

本程式用於比較以下兩種方式的效能：
1. 使用列表生成器函式
2. 使用一般列表函式

主要功能：
- 比較兩種方法的執行時間
- 記錄運算過程中的記憶體使用量
- 提供詳細的日誌記錄
"""

import logging
from sys import getsizeof
from glogTime import func_timer_decorator


def gen_list(nums):
    """
    使用列表方式計算數列的立方值

    Args:
        nums (list): 輸入的數列列表

    Returns:
        list: 包含每個元素立方值的列表
    """
    result = []
    for i in nums:
        result.append(i * i * i)
    return result


def gen_func(nums):
    """
    使用生成器函式計算數列的立方值

    Args:
        nums (list): 輸入的數列列表

    Yields:
        int: 每個元素的立方值
    """
    for n in nums:
        yield n * n * n


"""
定義了一個裝飾器函式 'func_timer_decorator' 和一個被裝飾的函式 time_gen()，
當 time_gen() 函式執行後，會看見 'func_timer_decorator' 執行後的結果，
套用在 time_gen() 函式上。
"""


@func_timer_decorator
def time_gen(nums):
    """
    測試生成器函式的效能

    Args:
        nums (list): 輸入的數列列表
    """
    # 執行生成器函式運算
    my_gen = gen_func(nums)
    size = getsizeof(my_gen)
    logging.info(f'生成器類型: {type(my_gen)}')
    logging.info(f'生成器大小: {size} bytes')
    for num in my_gen:
        logging.debug(f'生成器產生值: {num}')


@func_timer_decorator
def time_list(nums):
    """
    測試列表函式的效能

    Args:
        nums (list): 輸入的數列列表
    """
    # 執行列表運算
    my_list = gen_list(nums)
    size = getsizeof(my_list)
    logging.info(f'列表類型: {type(my_list)}')
    logging.info(f'列表大小: {size} bytes')
    for num in my_list:
        logging.debug(f'列表值: {num}')


def main():
    """
    主程式函數

    1. 設置日誌配置
    2. 建立測試數據
    3. 執行效能比較測試
    """
    # 設置 logging 配置
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # 建立測試數據
    numbers = [i for i in range(100_000)]
    logging.debug(f'測試數據大小: {len(numbers)}個元素')

    # 執行效能比較
    logging.info('開始效能比較測試:')
    logging.info('1. 使用生成器函式:')
    time_gen(numbers)
    
    logging.info('2. 使用列表函式:')
    time_list(numbers)


if __name__ == '__main__':
    main()
