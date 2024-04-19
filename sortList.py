""" Examples of sorting lists
列表排序例子
Two ways of sorting lists:
1. By sorted() function to create another sorted list (建立新的列表)
2. By sort() method to sort on the same list (原列表重新排序)
"""

#
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print(f'列表排序例子...')
print(f'===>原列表:\n{li}')
print(f'===>類型: {type(li)}\n')

# 1. sorted() 函式建立新的列表 (正向排序)
s_li = sorted(li)
print(
    f'===>1. 用 sorted() 函式建立新的列表(遞增排序):\n{s_li}\n===>Type: {type(s_li)}\n')

# 2. sort() 方法於原列表重新排序
li.sort()
print(f'===>2. 用 sort() 方法於原列表重新排序(遞增排序):\n{li}\n')

# Sort in a reverse order
s_li = sorted(li, reverse=True)
print(f'===>3. 用 sorted() 函式建立新的列表(遞減排序):\n{s_li}')

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

li.sort(reverse=True)
print(f'===>4. 用 sort() 方法於原列表重新排序(遞減排序):\n{li}\n')

# 絕對值排序
print(f'絕對值排序例子...')
li = [-6, -5, -4, 1, 2, 3]
print('Original List:\t', li)

s_li = sorted(li, key=abs)
print(f'===>5. 用 sorted() 函式建立新的列表(絕對值遞增排序):\n{s_li}')
