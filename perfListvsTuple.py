"""Performance Testing between List and Tuple
列表與元組的效能測試
"""

import random
import glog as log
from glogTime import func_timer_decorator
from sys import getsizeof


@func_timer_decorator
def timeList(L):
    # 列表運算
    num = len(L)
    for x in L:
        i = random.randint(0, num - 1)
        j = random.randint(0, num - 1)
        _ = abs(L[i] - L[j])
        log.debug(f'x={x}, i={i}, j={j}')


@func_timer_decorator
def timeTuple(T):
    # 元組運算
    num = len(T)
    for x in T:
        i = random.randint(0, num - 1)
        j = random.randint(0, num - 1)
        _ = abs(T[i] - T[j])
        log.debug(f'x={x}, i={i}, j={j}')


from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Produces debugging output.')


def main(argv):
    if FLAGS.debug:
        log.setLevel("DEBUG")
    else:
        log.setLevel("INFO")

    # Number of times to process Lists vs Tuples
    maxNum = 250_000

    # 檢視佔用空間
    L = list(range(maxNum))
    T = tuple(range(maxNum))
    log.info(f'佔用空間  list[0-{maxNum-1}] = {getsizeof(L):,} bytes')
    log.info(f'佔用空間 tuple[0-{maxNum-1}] = {getsizeof(T):,} bytes\n')

    # 測試時間
    log.info(f'測試列表操作時間...')
    timeList(L)

    log.info(f'測試元組操作時間...')
    timeTuple(T)


if __name__ == '__main__':
    """
    在 command 視窗下執行程式並存檔如下：
    python <此檔案名稱> --debug 2> sample/perfListvsTuple.log

    在 JupyterNotebook 視窗下執行程式並存檔如下：
    !python <此檔案名稱> --debug 2> sample/perfListvsTuple.log
    """
    app.run(main)
