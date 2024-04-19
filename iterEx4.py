"""Exhaustive guess approach to crack open a n-digit combo lock
駭客解鎖的例子"""

import itertools
import glog as log
from glogTime import func_timer_decorator


@func_timer_decorator
def crackLock(pass_code):
    # n-digit lock
    n_digit = len(pass_code)
    numbers = tuple(range(10))
    log.debug(f'{numbers}\n===>{type(numbers)}')

    # 模擬數字鎖:可迭代的產生器表達式
    combos = (
        combo for combo in itertools.product(numbers, repeat=n_digit))
    log.debug(f'===>{combos}')
    print(f'模擬數字鎖:可迭代的產生器表達式 {type(combos)}\n')
    print(f'===> {n_digit}位數字鎖的密碼可看成{n_digit}個元素的元組物件')
    print(f'===> 每一個元素值介於[0-9]的數字')
    max_combo = len(numbers) ** n_digit
    print(f'===> 理論上用窮盡法最多試： {max_combo:,} 組合，即可破解！\n')

    # 駭客用窮盡法，試試所有的可能組合
    log.info(f'駭客用窮盡法開始...')

    counter = 1
    for combo in combos:
        if combo == pass_code:
            print(f'試第 {counter:,} 次組合是： {combo}')
            return True
        log.debug(f'試第 {counter:,} 次組合是： {combo}')
        counter += 1
    return False


from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_boolean('debug', False, 'Produces debugging output.')

# Workaround for FATAL Flags parsing error:
flags.DEFINE_string('f', None, "Unknown command line flag 'f'")


def main(argv):
    if FLAGS.debug:
        log.setLevel("DEBUG")
    else:
        log.setLevel("INFO")

    passcode_str = input('輸入你的數字密碼，數字之間空白隔開: ')
    if passcode_str == "":
        # default
        passcode = (1, 3, 4, 2)
    else:
        passcode_list = [int(x) for x in passcode_str.split(' ')]
        passcode = tuple(passcode_list)

    if crackLock(passcode):
        print(f'駭客用窮盡法結束\n===>{passcode} 破解.')


# Note: restart the kernel first if re-run is needed to avoid DuplicateFlagError
if __name__ == '__main__':
    """
    To run this example (say in iterEx4.py)
    with debug flag in the command line as follows:
    python -m iterEx4 --debug 2> 'sample/iterEx4.log'
    """
    try:
        # workaround for a warning: exception SystemExit
        app.run(main)
    except:
        pass
