"""
範例：展示 Python 變數作用域（LEGB）和閉包概念

1. LEGB (Local, Enclosing, Global, Built-in) 查詢順序
2. 全域變數和局域變數的範圍
3. 閉包（Closure）的應用
"""


def test():
    """
    展示變數作用域的範例函式
    
    1. 使用 global 關鍵字宣告全域變數
    2. 展示局域變數和全域變數的範圍
    3. 檢查變數是否在當前作用域中存在
    """
    # 宣告全域變數 y
    print('\t宣告全域變數 y')
    global y

    # 指派局域變數 x
    x = 'test()指派的局域變數 x'
    print(f'\tx = "{x}"')

    y = 'test()指派的全域變數 y'
    print(f'\ty = "{y}"')

    # 檢查變數有效範圍
    print('\ttest()中的 x 是局域變數? ===>', 'x' in locals())
    print('\ttest()中的 y 是全域變數? ===>', 'y' in globals())


def count():
    """
    建立一個計算平均值的閉包函式
    
    Returns:
        function: 傳回內置的 avg 函式
    """
    print('閉包程式開始...')

    # 函式內的區域變數，用於存儲所有數值
    a = []

    def avg(val):
        """
        計算並返回平均值
        
        Args:
            val: 要加入的數值
            
        Returns:
            float: 目前所有數值的平均值
        """
        a.append(val)           # 將參數數值加入變數 a
        print(f'\t當前數值列表: {a}')  # 印出當前的數值列表
        return sum(a) / len(a)  # 回傳所有數值的平均
    
    return avg  # 回傳內置的 avg 函式


if __name__ == '__main__':
    """
    主程式入口點
    展示閉包和變數作用域的概念
    """
    
    # 建立閉包並測試
    push = count()
    print(f'第一次呼叫: {push(10)}')      # 將 10 存入 a
    print(f'第二次呼叫: {push(11)}')      # 將 11 存入 a
    print(f'第三次呼叫: {push(12)}\n')    

    print('主程式的全域變數...')
    # 指派全域變數 x
    x = '主程式指派的全域變數 x'
    print(f'x = "{x}"\n')

    print('呼叫 test()中...')
    test()

    print('返回主程式...')
    print(f'y = "{y}"')

    print(f'主程式中的 y 是全域變數? ===>{"y" in globals()}\n')
