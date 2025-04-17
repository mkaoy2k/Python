"""
產生器表示式 (Generator Expression) 範例

本程式示範如何使用 Python 的產生器表示式 (Generator Expression)
來生成 0-10 之間的所有偶數，並展示其記憶體使用效率。

主要功能：
1. 建立產生器表示式來生成偶數
2. 計算並顯示產生器物件的大小
3. 逐一輸出產生器中的所有元素
"""

from sys import getsizeof

def create_even_generator():
    """
    建立一個產生器表示式來生成 0-10 之間的偶數

    Returns:
        generator: 包含 0-10 之間所有偶數的產生器
    """
    return (i for i in range(11) if i % 2 == 0)

def display_generator_info(gen):
    """
    顯示產生器的資訊，包括類別和大小

    Args:
        gen (generator): 要顯示資訊的產生器物件
    """
    size = getsizeof(gen)
    print(f'產生器表示式的物件類別是：{type(gen)}')
    print(f'產生器表示式的物件大小是：{size}\n')

def main():
    """
    主函數，執行所有主要的程式邏輯
    """
    # 建立產生器
    my_genexp = create_even_generator()
    
    # 顯示產生器資訊
    display_generator_info(my_genexp)
    
    # 顯示產生器中的所有元素
    print(f'0-10中偶數如下：')
    for i in my_genexp:
        print(f'\t{i}')

if __name__ == '__main__':
    main()
