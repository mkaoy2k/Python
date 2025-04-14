"""
範例：展示 Python 的變數範圍（LEGB：Local, Enclosing, Global, Built-in）
這個範例展示了如何在嵌套函數中使用局部變數和非局部變數
"""

def outer():
    """
    外層函數，展示外圍變數範圍的使用
    """
    print('\t 在 outer() 外圍範圍...')
    x = '指派外圍變數 x'
    y = '指派外圍變數 y'

    print(f'\t x = "{x}"')
    print(f'\t y = "{y}"\n')

    def inner():
        """
        內層函數，展示如何使用局部變數和非局部變數
        """
        print('\t\t 在 inner() 局域範圍...')

        # 局部變數 x
        x = 'inner() 指派局域變數 x'
        print(f'\t\t x = "{x}"')

        # 使用 nonlocal 關鍵字宣告外圍變數 y
        print('\t\t 宣告外圍變數 y')
        nonlocal y
        y = 'inner() 指派外圍變數 y'
        print(f'\t\t y = "{y}"\n')

    print('\t 呼叫 inner()...')
    inner()
    print('\t 返回 outer() 外圍範圍...')
    print(f'\t x = "{x}"')
    print(f'\t y = "{y}"')

def main():
    """
    主函數，程式入口點
    """
    print('在主程式模組範圍...')
    print('呼叫 outer()...')
    outer()
    print('返回主程式模組範圍...')
    print('結束主程式模組範圍...')

if __name__ == "__main__":
    main()
