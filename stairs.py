"""
樓梯問題解決方案
這個程式計算到達特定樓層的所有可能方式。
使用者可以一次跨1階、2階或3階樓梯。
"""

from functools import lru_cache


@lru_cache(maxsize=100)
def steps_to(stair):
    """
    計算到達指定樓層的所有可能方式

    Args:
        stair (int): 目標樓層號碼

    Returns:
        int: 到達該樓層的所有可能方式數量
    """
    if stair == 1:
        # 一階樓梯只有一種方式：從地面跨一階
        return 1
    elif stair == 2:
        # 二階樓梯有兩種方式：
        # 1. 從地面直接跨兩階
        # 2. 分兩次跨一階
        return 2
    elif stair == 3:
        # 三階樓梯有四種方式：
        # 1. 從地面直接跨三階
        # 2. 先跨兩階再跨一階
        # 3. 先跨一階再跨兩階
        # 4. 分三次跨一階
        return 4
    else:
        # 一般情況：當前樓層可以從三個位置跨到：
        # 1. 從三階樓下
        # 2. 從兩階樓下
        # 3. 從一階樓下
        # 將這三個位置的可能方式加總即為解
        return (
            steps_to(stair - 3)
            + steps_to(stair - 2)
            + steps_to(stair - 1)
        )


def main():
    """
    主程式函數
    計算並顯示從第4階到第99階的所有可能方式
    """
    for n in range(4, 100):
        print(f'到達第{n}階有 {steps_to(n)} 種方式')


if __name__ == '__main__':
    main()
