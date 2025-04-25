"""
列表與元組的效能比較程式

本程式用於比較 Python 中列表 (list) 和元組 (tuple) 的效能差異，主要測試項目包括：
1. 記憶體佔用空間
2. 隨機存取效能

使用方式：
1. 一般執行：python perfListvsTuple.py
2. 詳細除錯資訊：python perfListvsTuple.py --debug
"""

import logging
from glogTime import func_timer_decorator
from sys import getsizeof
import random
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_boolean('debug', False, '顯示除錯資訊')


def square(x):
    """
    計算平方值

    Args:
        x (int): 輸入數值

    Returns:
        int: 平方值
    """
    return x ** 2


@func_timer_decorator
def timeList(L):
    """
    測試列表的隨機存取效能

    Args:
        L (list): 測試用的列表
    """
    num = len(L)
    for x in L:
        i = random.randint(0, num - 1)
        j = random.randint(0, num - 1)
        _ = square(L[i] - L[j])
        logging.debug(f'x={x}, i={i}, j={j}')


@func_timer_decorator
def timeTuple(T):
    """
    測試元組的隨機存取效能

    Args:
        T (tuple): 測試用的元組
    """
    num = len(T)
    for x in T:
        i = random.randint(0, num - 1)
        j = random.randint(0, num - 1)
        _ = square(T[i] - T[j])
        logging.debug(f'x={x}, i={i}, j={j}')


def main(argv):
    """
    主程式函數

    1. 設置日誌配置
    2. 建立測試數據
    3. 比較記憶體佔用
    4. 測試隨機存取效能
    """
    # 設置 logging 配置
    if FLAGS.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # 建立測試數據
    maxNum = 250_000

    # 檢視佔用空間
    L = list(range(maxNum))
    T = tuple(range(maxNum))
    logging.info(f'\n佔用空間  list[0-{maxNum-1}] = {getsizeof(L):,} bytes')
    logging.info(f'\n佔用空間 tuple[0-{maxNum-1}] = {getsizeof(T):,} bytes\n')

    logging.info('開始效能比較測試:')

    # 測試時間
    logging.info(f'測試列表操作時間...')
    timeList(L)

    logging.info(f'測試元組操作時間...')
    timeTuple(T)


if __name__ == '__main__':
    """
    程式入口點

    執行程式並存檔日誌：
    1. 命令列執行：python perfListvsTuple.py --debug 2> logger/perfListvsTuple.log
    2. JupyterNotebook 執行：!python perfListvsTuple.py --debug 2> logger/perfListvsTuple.log
    """
    app.run(main)
