"""產生器表示式 (Generator Expression) 例子"""

from sys import getsizeof

my_genexp = (i for i in range(11) if i % 2 == 0)
size = getsizeof(my_genexp)

print(f'產生器表示式的物件類别是：{type(my_genexp)}')
print(f'產生器表示式的物件大小是：{size}\n')

print(f'0-10中偶數如下：')
for i in my_genexp:
    print(f'===> {i}')
