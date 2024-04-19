"""Lambda Function Example
匿名函式例子"""

from sys import getsizeof

# 例子1: 印出哈囉!


def hello(title):
    print(f'一般函式：{title}')


print(f'例子1: 印出哈囉...')
hello('哈囉!')

# 上面三行精簡成一行 Lambda 匿名函式
my_lambda = (lambda title: print(f'匿名函式：{title}\n'))
size = getsizeof(my_lambda)
my_lambda('哈囉!')

print(f'匿名函式的物件類别是：{type(my_lambda)}')
print(f'匿名函式的物件大小是：{size}\n')

# 例子2: 印出偶數
print(f'例子2: 印出偶數...')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'數字列表： {nums}')

print(f'列表中偶數如下：')
for even in filter(lambda n: n % 2 == 0, nums):
    print(f'===> {even}')
