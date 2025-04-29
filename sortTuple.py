"""
元組排序範例
這個程式示範如何使用 sorted() 函式對元組進行排序
由於元組是不可變的，因此不能直接使用 sort() 方法
"""

def main():
    """
    主程式函式
    1. 建立一個未排序的元組
    2. 使用 sorted() 函式將元組轉換為排序後的列表
    3. 將排序後的列表轉換回元組
    """
    # 建立一個未排序的元組
    tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
    print(f'原始元組位置在：{id(tup)}')
    print(f'原始元組內容：{tup}')
    print(f'\t類型: {type(tup)}\n')

    # 使用 sorted() 函式將元組轉換為排序後的列表
    print(f'使用 sorted() 函式後的結果：')
    slist = sorted(tup)
    print(f'排序後的列表位置在：{id(slist)}')
    print(f'排序後的列表內容：{slist}')
    print(f'\t類型: {type(slist)}\n')

    # 將排序後的列表轉換回元組
    s_tup = tuple(slist)
    print(f'最終排序後的元組位置在：{id(s_tup)}')
    print(f'最終排序後的元組內容：{s_tup}')
    print(f'\t類型: {type(s_tup)}')

if __name__ == '__main__':
    main()
