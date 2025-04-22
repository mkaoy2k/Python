"""
使用窮舉法破解數位密碼鎖

此程式示範如何使用窮舉法（暴力破解）來嘗試破解一個數位密碼鎖。
"""

import itertools
import logging

# 設定 logging 格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def crackLock(pass_code):
    """
    使用窮舉法嘗試破解密碼鎖
    
    Args:
        pass_code (tuple): 目標密碼
        
    Returns:
        bool: 是否成功破解密碼
    """
    # n位數密碼鎖
    n_digit = len(pass_code)
    
    # 生成0-9的數字序列
    numbers = tuple(range(10))
    logging.info(f'{numbers}\n===>{type(numbers)}')

    # 生成所有可能的數字組合
    combos = (
        combo for combo in itertools.product(numbers, repeat=n_digit)
    )

    logging.info(f'生成所有可能的數字組合 {type(combos)}\n')
    logging.info(f'===> {n_digit}位數密碼鎖的密碼可看成{n_digit}個元素的元組物件')
    logging.info(f'===> 每一個元素值介於[0-9]的數字')
    max_combo = len(numbers) ** n_digit
    logging.info(f'===> 理論上用窮舉法最多試： {max_combo:,} 組合，即可破解！\n')

    # 開始嘗試所有可能的組合
    logging.info(f'開始嘗試所有可能的組合...')

    counter = 1
    for combo in combos:
        if combo == pass_code:
            logging.info(f'試第 {counter:,} 次組合是： {combo}')
            return True
        logging.debug(f'===>{combo}')
        counter += 1
    return False


def main():
    """
    主函數，負責處理使用者輸入並執行密碼破解
    """
    passcode_str = input('輸入你的數位密碼，數字之間空白隔開: ')
    if passcode_str == "":
        # 預設密碼
        passcode = (1, 3, 4, 2)
    else:
        passcode_list = [int(x) for x in passcode_str.split(' ')]
        passcode = tuple(passcode_list)

    if crackLock(passcode):
        logging.info(f'成功破解密碼\n===>{passcode} 破解.')
    else:
        logging.info('未能破解密碼')


if __name__ == '__main__':
    main()
