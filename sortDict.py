""" Examples of Sorting Dictionaries in two ways:
    字典排序例子
    1. Sorted by key (依鍵排序)
    2. Sorted by value (依值排序， 但前提值要有可排序性，即文字數字類型),
        assuming sortable alphanumeric attribute values
"""

# Original dictionary
di = {'name': 'Mike', 'job': 'programmer', 'age': '20', 'os': 'Mac'}
print(f'原字典:\n{di}')
print(f'===>類型: {type(di)}\n')

# 1. 依字典用 sorted() 函式建立新的字典(依鍵遞增排序)
s_li = sorted(di)
print(f'1. 依字典用 sorted() 函式建立新的列表(依鍵遞增排序)...')
print(f'===>其元素只含鍵，不含值:\n{s_li}')
print(f'===>類型: {type(s_li)}\n')

# 2. 依字典逐項用 sorted() 函式依鍵遞增排序 ()
s_li = sorted(di.items(), key=lambda kv: (kv[0], kv[1]))  # kv[0]是鍵、kv[1]是值
print(f'2. 依字典逐項用 sorted() 函式建立新的列表(依鍵遞增排序)...')
print(f'===>其元素是含鍵及值元组:\n{s_li}')
print(f'===>類型: {type(s_li)}\n')


# 3. 依字典逐項用 sorted() 函式依值遞增排序
s_li = sorted(di.items(), key=lambda kv: (kv[1], kv[0]))  # kv[0]是鍵、kv[1]是值
print(f'3. 依字典逐項用 sorted() 函式建立新的列表(依值遞增排序)...')
print(f'===>其元素是含鍵及值元组:\n{s_li}')
print(f'===>類型: {type(s_li)}\n')
