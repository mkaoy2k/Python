"""
make your own iterator to simulate range() implementation
兩種方式可以自創迭代器：
1. 自創物件類別轉換成迭代器
    其的必要條件是實施以下兩種方法
    1. __iter__()
    2. __next__()
2. 用產生器函式
"""
class MyRange:
    """
    自定義的範圍迭代器類別，模擬內建的 range() 函數
    
    Attributes:
        start (int): 迭代的起始值
        end (int): 迭代的結束值
        value (int): 當前的迭代值
    """
    def __init__(self, start, end):
        """
        初始化 MyRange 類別
        
        Args:
            start (int): 迭代的起始值
            end (int): 迭代的結束值
        """
        self.value = start
        self.end = end

    def __iter__(self):
        """
        返回迭代器物件
        
        Returns:
            MyRange: 本物件實例
        """
        return self

    def __next__(self):
        """
        返回下一個值
        
        Returns:
            int: 當前的迭代值
            
        Raises:
            StopIteration: 如果已經到達結束值
        """
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end):
    """
    使用產生器函式實現的範圍迭代器
    
    Args:
        start (int): 迭代的起始值
        end (int): 迭代的結束值
        
    Yields:
        int: 當前的迭代值
    """
    current = start
    while current <= end:
        yield current
        current += 1


def main():
    """
    主程式入口，示範兩種範圍迭代器的使用方法
    """
    print(f'1. 自創的物件類別 "MyRange" 轉換成迭代器模擬 range() 函式...')
    i_nums = MyRange(1, 3)

    # 顯示第一個元素
    count = 1
    print(f'===> 第 {count} 元素: {next(i_nums)}')

    # 顯示剩餘元素
    while True:
        count += 1
        try:
            print(f'===> 第 {count} 元素: {next(i_nums)}')
        except StopIteration:
            print('===> 已經沒有更多元素了')
            break

    print(f'\n2. 用產生器函式模擬 range() 函式...')
    nums = my_range(1, 3)

    count = 0
    for num in nums:
        count += 1
        print(f'===> 第 {count} 元素: {num}')


if __name__ == '__main__':
    main()
