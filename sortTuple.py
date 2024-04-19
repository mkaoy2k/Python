"""Examples of Sorting Tuples by sorted() function
元組排序例子
Note: no sort method with Tuples, since tuples are immutable.
i.e. <tuple obj>.sort() resulted in an error
元組排序只能用 sorted() 函式間接排序
"""

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
print(f'元組位置在：{id(tup)}:')
print(f'{tup}')
print(f'===>類型: {type(tup)}\n')

# Sort a tuple
print(f'元組經 sorted() 函式後變成列表:')
slist = sorted(tup)
print(f'列表位置在：{id(slist)}:')
print(f'{slist}')
print(f'===>類型: {type(slist)}\n')

s_tup = tuple(slist)
print(f'新元組位置在：{id(s_tup)}:')
print(f'{s_tup}')
print(f'===>類型: {type(s_tup)}\n')
