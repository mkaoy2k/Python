"""
Python 生成式 (Comprehension) 進階範例
本程式示範列表生成式的各種應用，包括基本用法、條件篩選、多重迭代等
"""

# 建立數字列表
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'原始數字列表: {nums}\n')

# 1. 基本列表生成式
# 使用傳統 for 迴圈建立列表
my_list = []
for n in nums:
    my_list.append(n)  # 將每個數字加入列表
print(f'使用 for 迴圈建立列表:')
print(f'===>{my_list}\n')

# 使用列表生成式建立列表
# 格式：[expression for item in iterable]
my_list2 = [n for n in nums]
print(f'使用列表生成式建立列表:')
print(f'===>{my_list2}\n')

# 2. 計算平方值
# 使用傳統 for 迴圈計算平方值
my_list = []
for n in nums:
    my_list.append(n * n)  # 計算平方值
print(f'使用 for 迴圈計算平方值:')
print(f'===>{my_list}\n')

# 使用列表生成式計算平方值
my_list2 = [n * n for n in nums]
print(f'使用列表生成式計算平方值:')
print(f'===>{my_list2}\n')

# 3. 帶條件篩選的列表生成式
# 篩選出偶數
my_list = []
for n in nums:
    if n % 2 == 0:  # 篩選條件：偶數
        my_list.append(n)
print(f'使用 for 迴圈篩選偶數:')
print(f'===>{my_list}\n')

# 使用列表生成式篩選偶數
# 格式：[expression for item in iterable if condition]
my_list2 = [n for n in nums if n % 2 == 0]
print(f'使用列表生成式篩選偶數:')
print(f'===>{my_list2}\n')

# 4. 多重迭代的列表生成式
# 生成所有可能的配對
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))  # 生成字母和數字的配對
print(f'使用多重 for 迴圈生成配對:')
print(f'===>{my_list}\n')

# 使用列表生成式生成配對
# 格式：[expression for item1 in iterable1 for item2 in iterable2]
my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(f'使用列表生成式生成配對:')
print(f'===>{my_list2}\n')

# 5. 帶條件篩選的多重迭代
# 生成所有可能的配對，但排除特定條件
my_list = []
for letter in 'abcd':
    for num in range(4):
        if num != 2:  # 篩選條件：排除數字 2
            my_list.append((letter, num))
print(f'使用多重 for 迴圈生成配對 (排除數字 2):')
print(f'===>{my_list}\n')

# 使用列表生成式生成配對 (排除數字 2)
my_list2 = [(letter, num) for letter in 'abcd' for num in range(4) if num != 2]
print(f'使用列表生成式生成配對 (排除數字 2):')
print(f'===>{my_list2}\n')

# 6. 字典生成式
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_dict = {name: hero for name, hero in zip(names, heros)}
print(f'使用字典生成式建立字典:')
print(f'===>{my_dict}\n')

# 7. 集合生成式
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {n * n for n in nums}
print(f'使用集合生成式建立集合:')
print(f'===>{my_set}\n')

# 8. 生成器表達式
my_gen = (n * n for n in nums)
print(f'使用生成器表達式建立生成器:')
print(f'===>{tuple(my_gen)}\n')
