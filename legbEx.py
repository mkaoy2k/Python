"""
LEGB 變數範圍示範
這個程式展示了 Python 中的四種變數範圍：
1. Local (區域範圍)
2. Enclosing (封閉範圍)
3. Global (全域範圍)
4. Built-in (內建範圍)

內建範圍示範
展示內建範圍中的變數和函數
使用 builtins 模組來查看 Python 內建的變數和函數
"""

import builtins

# 全域變數範圍示範
x = 'global x'  # 定義一個全域變數 x

def test():
    """
    展示區域變數和全域變數的範圍
    這個函數會：
    1. 定義一個區域變數 x
    2. 使用 global 關鍵字創建一個全域變數 y
    3. 顯示變數的範圍
    """
    global y  # 使用 global 關鍵字宣告 y 為全域變數
    x = 'local x'  # 這個 x 是區域變數，與全域的 x 不同

    print('\n在 test() 中，區域範圍...')
    print(f'x="{x}"')  # 顯示區域變數 x

    y = 'global y'  # 創建全域變數 y
    print(f'y="{y}"')  # 顯示全域變數 y

    # 檢查變數範圍
    print('\tx 是區域變數？', 'x' in locals())
    print('\ty 是全域變數？', 'y' in globals())


def outer():
    """
    展示封閉範圍（Enclosing）的示範
    這個函數會：
    1. 定義區域變數 x 和 y
    2. 定義一個內函數 inner
    3. 顯示變數範圍的變化
    """
    print('\n在 outer() 中，區域範圍...')
    x = 'outer local x'  # outer 函數中的區域變數
    y = 'outer local y'  # outer 函數中的區域變數

    print(f'x="{x}"')
    print(f'y="{y}"')

    def inner():
        """
        內函數，展示封閉範圍的使用
        使用 nonlocal 關鍵字修改封閉範圍中的變數
        """
        print('\n在 inner() 中，區域範圍...')
        x = 'inner local x'  # inner 函數中的區域變數

        # 使用 nonlocal 關鍵字修改封閉範圍中的 y
        nonlocal y
        y = 'inner nonlocal y'
        
        print(f'x="{x}"')
        print(f'y="{y}"')

    inner()  # 呼叫 inner 函數
    print('\n在 outer() 中，區域範圍...')
    print(f'x="{x}"')
    print(f'y="{y}"')


def main():
    """
    主程式函數，展示 LEGB 變數範圍的示範
    """
    print('\n在主程式中，全域範圍...')
    print(f'x="{x}"')  # 顯示全域變數 x
    test()  # 呼叫 test 函數

    print('\n在主程式中，全域範圍...')
    print('\ty 是全域變數？', 'y' in globals())
    print(f'y="{y}"')  # 顯示全域變數 y

    outer()  # 呼叫 outer 函數

    # 內建範圍示範
    print(f'\n展示 "builtins" 模組中內建變數 (屬性和方法)如下:\n{dir(builtins)}\n')

    # 內建函數示範
    list_1 = [5, 1, 4, -8, 9]

    num_min = min(list_1)  # 使用內建的 min 函數
    print(f'例子1: min({list_1}) =\t{num_min}')
    print(f'例子2: abs({num_min}) =\t{abs(num_min)}')  # 使用內建的 abs 函數


if __name__ == '__main__':
    main()
