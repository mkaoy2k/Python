"""局域和全域變數範圍的例子"""


def test():

    # 宣告全域變數 y
    print('\t 宣告全域變數 y')
    global y

    # 指派局域變數 x
    x = 'test()指派的局域變數 x'
    print(f'\t x = \'{x}\'')

    y = 'test()指派的全域變數 y'
    print(f'\t y = \'{y}\'')

    # 檢查變數有效範圍
    if 'x' in locals():
        print('\t test()中的 x 是? ===>局域變數')

    if 'y' in globals():
        print('\t test()中的 y 是? ===>全域變數\n')


"""建立一個 avg 函式的閉包 (closure)，執行後雖然 test() 執行了三次，
但因為每次執行時保留下一個作用域 (scope) 的繫結關係，
所以會不斷將傳入的數值進行計算，最後就會得到 11 的結果。
"""


def count():                    # 建立一個 count 函式
    a = []                      # 函式內有區域變數 a 是串列

    def avg(val):               # 建立內置函式 avg ( 閉包 )
        a.append(val)           # 將參數數值加入變數 a
        print(a)                # 印出 a
        return sum(a) / len(a)  # 回傳 a 串列所有數值的平均
    return avg                  # 回傳 avg


if __name__ == '__main__':

    print('閉包程式開始...')
    push = count()
    print(f'{push(10)}')      # 將 10 存入 a
    print(f'{push(11)}')      # 將 11 存入 a
    print(f'{push(12)}\n')    # 印出 11

    print('主程式的全域變數...')
    # 指派全域變數 x
    x = '主程式指派的全域變數 x'
    print(f'x = \'{x}\'\n')

    print(f'呼叫 test()中...')
    test()

    print('返回主程式...')
    print(f'y = \'{y}\'')

    if 'y' in globals():
        print(f'主程式中的 y 是? ===>全域變數\n')
