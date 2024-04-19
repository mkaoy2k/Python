"""Generator Function Example
產生器函式: 求數列中每一元素的立方"""

from sys import getsizeof

def gen_func(nums):
    # 定義產生器函式
    for n in nums:
        yield n * n * n


my_gen = gen_func([1, 2, 3])
size = getsizeof(my_gen)

print(f'產生器函式的物件類别是：{type(my_gen)}')
print(f'產生器函式的物件大小是：{size}\n')


# 廻路呼叫產生器函式
print(f'廻路呼叫產生器函式...')
counter = 0
for num in my_gen:
    counter += 1
    print(f'===> 呼叫 {counter} 次，返回資料：{num}')
