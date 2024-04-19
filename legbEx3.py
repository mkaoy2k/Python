"""外圍變數範圍的例子"""


def outer():
    # 外層函式

    print('\t 在 outer() 外圍範圍...')
    x = '指派外圍變數 x'
    y = '指派外圍變數 y'

    print(f'\t x = \'{x}\'')
    print(f'\t y = \'{y}\'\n')

    # 內層函式
    def inner():
        print('\t\t 在 inner() 局域範圍...')

        x = 'inner() 指派局域變數 x'
        print(f'\t\t x = \'{x}\'')

        # 宣告外圍變數 y
        print('\t\t 宣告外圍變數 y')
        nonlocal y
        y = 'inner() 指派外圍變數 y'
        print(f'\t\t y = \'{y}\'\n')

    print('\t 呼叫 inner()...')
    inner()
    print('\t 返回 outer() 外圍範圍...')
    print(f'\t x = \'{x}\'')
    print(f'\t y = \'{y}\'')


# 主程式
print('在主程式模組範圍...')
outer()
