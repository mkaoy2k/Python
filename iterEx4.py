"""
Exhaustive guess approach to crack open a n-digit combo lock
駭客解鎖的例子
"""

import itertools
import logging
from glogTime import func_timer_decorator
from absl import app
from absl import flags

# 設置 logging 格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

FLAGS = flags.FLAGS

# 定義 debug 參數旗標
flags.DEFINE_boolean('debug', False, '是否顯示 debug 訊息')

# 解決 flags 解析錯誤的 workaround
flags.DEFINE_string('f', None, "未知的命令列旗標 'f'")


@func_timer_decorator
def crackLock(pass_code):
    """
    使用窮盡法破解密碼鎖
    
    Args:
        pass_code (tuple): 正確的密碼組合
    
    Returns:
        bool: 是否成功破解密碼
    """
    # n-digit lock
    n_digit = len(pass_code)
    numbers = tuple(range(10))
    logger.debug(f'數字範圍: {numbers}\n===>{type(numbers)}')

    # 模擬數字鎖:可迭代的產生器表達式
    combos = (
        combo for combo in itertools.product(numbers, repeat=n_digit))
    logger.debug(f'===>{combos}')
    print(f'模擬數字鎖:可迭代的產生器表達式 {type(combos)}\n')
    print(f'===> {n_digit}位數字鎖的密碼可看成{n_digit}個元素的元組物件')
    print(f'===> 每一個元素值介於[0-9]的數字')
    max_combo = len(numbers) ** n_digit
    print(f'===> 理論上用窮盡法最多試： {max_combo:,} 組合，即可破解！\n')

    # 駭客用窮盡法，試試所有的可能組合
    logger.info('駭客用窮盡法開始...')

    counter = 1
    for combo in combos:
        if combo == pass_code:
            print(f'試第 {counter:,} 次組合是： {combo}')
            return True
        logger.debug(f'試第 {counter:,} 次組合是： {combo}')
        counter += 1
    return False


def main(argv):
    """
    主程式入口
    """
    # 設置 logging 等級
    if FLAGS.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # 讀取使用者輸入的密碼
    passcode_str = input('輸入你的數位密碼，數字之間空白隔開: ')
    if passcode_str == "":
        # 預設密碼
        passcode = (1, 3, 4, 2)
    else:
        passcode_list = [int(x) for x in passcode_str.split(' ')]
        passcode = tuple(passcode_list)

    # 嘗試破解密碼
    if crackLock(passcode):
        print(f'駭客用窮盡法結束\n===>{passcode} 破解.')


if __name__ == '__main__':
    """
    程式執行入口
    
    使用方法:
    1. 不帶參數運行: python iterEx4.py
    2. 帶 debug 參數運行: python iterEx4.py --debug
    """
    try:
        # workaround for a warning: exception SystemExit
        app.run(main)
    except:
        pass
