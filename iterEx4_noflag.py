"""Exhaustive guess approach to crack open a n-digit combo lock
駭客解鎖的例子"""

import itertools
import glog as log
from glogTime import func_timer_decorator

# log.setLevel("INFO")
log.setLevel("DEBUG")


@func_timer_decorator
def crackLock(pass_code):
    # n-digit lock
    n_digit = len(pass_code)
    numbers = tuple(range(10))
    log.info(f'{numbers}\n===>{type(numbers)}')

    # 模擬數字鎖:可迭代的產生器表達式
    combos = (
        combo for combo in itertools.product(numbers, repeat=n_digit))

    log.info(f'模擬數字鎖:可迭代的產生器表達式 {type(combos)}\n')
    log.info(f'===> {n_digit}位數字鎖的密碼可看成{n_digit}個元素的元組物件')
    log.info(f'===> 每一個元素值介於[0-9]的數字')
    max_combo = len(numbers) ** n_digit
    log.info(f'===> 理論上用窮盡法最多試： {max_combo:,} 組合，即可破解！\n')

    # 駭客用窮盡法，試試所有的可能組合
    log.info(f'駭客用窮盡法開始...')

    counter = 1
    for combo in combos:
        if combo == pass_code:
            log.info(f'試第 {counter:,} 次組合是： {combo}')
            return True
        log.debug(f'===>{combo}')
        counter += 1
    return False


if __name__ == '__main__':

    passcode_str = input('輸入你的數字密碼，數字之間空白隔開: ')
    if passcode_str == "":
        # default
        passcode = (1, 3, 4, 2)
    else:
        passcode_list = [int(x) for x in passcode_str.split(' ')]
        passcode = tuple(passcode_list)

    if crackLock(passcode):
        log.info(f'駭客用窮盡法結束\n===>{passcode} 破解.')
