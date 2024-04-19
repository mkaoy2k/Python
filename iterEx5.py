"""make your own iterator to simulate range() implementation
兩種方式方法可以自創迭代器：
1. 自創物件類別轉換成迭代器
    其的必要條件是實施以下兩種方法
    1. __iter__()
    2. __next__()
2. 用產生器函式"""

import itertools


class MyRange:
    # 1. 自創的物件類別模擬 range() 函式
    def __init__(self, start, end):
        self.value = start
        self.end = end

    # 定義可迭代物件
    def __iter__(self):
        return self

    # 定義可依序讀取
    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


def my_range(start, end):
    # 2. 另外一種模擬 range() 函式，就是用產生器函式
    current = start
    while current <= end:
        yield current
        current += 1


print(f'1. 自創的物件類別 "MyRange" 轉換成迭代器模擬 range() 函式...')
i_nums = MyRange(1, 3)

count = 1
# print the 1st item
print(f'===> 第 {count} 元素: {next(i_nums)}')

# print the rest
while True:
    count += 1
    try:
        print(f'===> 第 {count} 元素: {next(i_nums)}')
    except StopIteration:
        print('===> StopIteration 廻圈到底.\n')
        break


print(f'2. 用產生器函式模擬 range() 函式...')

nums = my_range(1, 3)

count = 0
for num in nums:
    count += 1
    print(f'===> 第 {count} 元素: {num}')
