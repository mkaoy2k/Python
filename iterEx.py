"""檢視一下 Python 内建的可迭代物件
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


# All objects, shown below, are iterables
# List
X = ['c123', 142_857, '尤勇', '夏琪']
for element in X:
    print(element, end=" ")
check_iterable(X)

# Tuple
X = ('c123', 142_857, '尤勇', '夏琪')
for element in X:
    print(element, end=" ")
check_iterable(X)

# Set
X = {'c123', 142_857, '尤勇', '夏琪'}
for element in X:
    print(element, end=" ")
check_iterable(X)

# Dictionary
X = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci']}

# Looping thru Dictionary
for key, value in X.items():
    print(f'{key}:{value}')
check_iterable(X)

# String
X = 'Michael Kao'
for letter in X:
    print(letter, end="")
check_iterable(X)

# Bytes String
X = b'Binary'
for byte in X:
    print(byte, end=" ")
check_iterable(X)

# However, an integer type is not iterable, as follows
# Integer
X = 142_857
print(X, end=" ")
check_iterable(X)
