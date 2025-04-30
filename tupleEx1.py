"""
這個程式示範 Python 元組的基本操作，包括：
1. 元組索引訪問
2. 元組切片操作
3. 元組運算
4. 元組比較運算
"""

def show_tuple_indexing():
    """
    顯示元組索引訪問示例
    """
    tuple1 = (1, 2, 3, 4, 5, 4)
    tuple2 = (1, 2, 5)
    
    print(f'\ttuple1 物件類型: {type(tuple1)}')
    print(f'\ttuple1 = {tuple1}')
    print(f'\ttuple2 = {tuple2}')
    
    print(f'\ttuple1 元組第一個元素 = {tuple1[0]}')
    print(f'\ttuple1 元組最後一個元素 = {tuple1[-1]}')

def show_tuple_slicing():
    """
    顯示元組切片操作示例
    """
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (1, 2, 5, 7)
    
    print(f'\ttuple1 元組奇數索引的元素 = {tuple1[1::2]}')
    print(f'\ttuple2 元組第一個到第三個元素 = {tuple2[:3]}')

def show_tuple_operations():
    """
    顯示元組運算示例，包括元組相加和重複
    """
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    print(f'\t元組1 = {tuple1}')
    print(f'\t元組2 = {tuple2}')
    
    # 組合多個元組物件成一個元組
    tuple3 = tuple1 + tuple2
    print(f'\t元組1 + 元組2 = {tuple3}')
    
    # 重複元組中元素
    tuple_hello = ('哈囉',) * 4
    print(f'\t元組 (\'哈囉\',) * 4 = {tuple_hello}')

def show_tuple_comparison():
    """
    顯示元組比較運算示例
    """
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 4)
    
    print(f'\t元組1 = {tuple1}')
    print(f'\t元組2 = {tuple2}')
    
    print(f'\t3 in {tuple1}: {3 in tuple1}')
    print(f'\t3 in {tuple2}: {3 in tuple2}')

    if tuple1 == tuple2:
        print(f'\t{tuple1} 等於 {tuple2}')
    elif tuple1 > tuple2:
        print(f'\t{tuple1} 大於 {tuple2}')
    else:
        print(f'\t{tuple1} 小於 {tuple2}')

def main():
    """
    主函數，按順序執行所有元組操作示例
    """
    print("\n=== 元組索引訪問示例 ===")
    show_tuple_indexing()
    
    print("\n=== 元組切片操作示例 ===")
    show_tuple_slicing()
    
    print("\n=== 元組運算示例 ===")
    show_tuple_operations()
    
    print("\n=== 元組比較運算示例 ===")
    show_tuple_comparison()

if __name__ == "__main__":
    main()
