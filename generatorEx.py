"""產生器函式範例

本程式示範如何使用 Python 的產生器函式來計算數列中每個元素的立方值。
使用產生器可以有效節省記憶體空間，特別適合處理大量數據。
"""

from sys import getsizeof

def gen_func(nums):
    """產生器函式：計算數列中每個元素的立方值

    Args:
        nums (list): 輸入的數字列表

    Yields:
        int: 每個數字的立方值
    """
    for n in nums:
        yield n * n * n

def main():
    """主程式函式
    
    1. 建立產生器物件
    2. 測量產生器物件的大小
    3. 透過廻路呼叫產生器並顯示結果
    """
    # 建立產生器物件
    my_gen = gen_func([1, 2, 3])
    size = getsizeof(my_gen)

    # 顯示產生器物件資訊
    print(f'產生器函式的物件類別是：{type(my_gen)}')
    print(f'產生器函式的物件大小是：{size}\n')

    # 廻路呼叫產生器函式
    print(f'廻路呼叫產生器函式...')
    counter = 0
    for num in my_gen:
        counter += 1
        print(f'\t呼叫 {counter} 次，返回資料：{num}')

if __name__ == '__main__':
    main()
