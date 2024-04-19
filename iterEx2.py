"""Python Integer object is not literable. In order to make an iteger iterable,
extra conversions are needed. There are 2 ways making integer iterable.
把整數物件變成迭代器物件
"""

import itertools


def check_iterable(obj):
    # The iter() built-in function checks whether the obj implements
    # __iter__() or not. And calls that to obtain an iterator.
    # Python raises TypeError if failed.
    try:
        iter(obj)
        print(f'===> {type(obj)} 是可迭代物件\n')
        return True
    except TypeError:
        print(f'===> {type(obj)} 不是可迭代物件\n')
        return False


X = 142_857
print(X, end=" ")
check_iterable(X)

# 两種方法把整數物件變成迭代器物件
print(f'两種方法把整數物件變成迭代器物件...')
# 1. convert to a string to make iteger iterable
print(f'===>1. 把整數物件轉成字串')
for digit in str(X):
    print(digit, end=" ")
check_iterable(str(X))

# 2. convert to a list to make  iteger iterable
digits = [int(d) for d in str(X)]
print(f'===>2. 把整數物件轉成列表')
for digit in digits:
    print(digit, end=" ")
check_iterable(digits)
