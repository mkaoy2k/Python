"""
Python 生成式 (Comprehension) 範例
本程式示範各種生成式的使用方式，包括列表、集合、字典和產生器表達式
"""

# 1. 傳統程式寫法 vs 列表生成式
# 傳統寫法：使用 for 迴圈和 append()
list1 = []
for n in range(12):
    list1.append(n**2)  # 計算平方值
print(f'傳統程式寫法:')
print(f'===>{list1}\n')

# 使用列表生成式 (List Comprehension)
# 格式：[expression for item in iterable]
list2 = [n**2 for n in range(12)]
print(f'列表生成式:')
print(f'===>{list2}\n')

# 2. 多重迭代生成式
# 生成 2x3 的矩陣，每個元素為 (row, column) 元組
list3 = [(r, c) for r in range(2) for c in range(3)]
print(f'多重迭代列表生成式 (2x3 矩陣):')
print(f'===>{list3}\n')

# 3. 二維矩陣生成
# 生成 MxN 矩陣，元素從 1 開始遞增
M = 3  # 矩陣列數
N = 5  # 矩陣行數
matrix = [[c + N * r for c in range(1, N + 1)] for r in range(M)]
print(f'{M}x{N} 二維矩陣:')
print(f'===>{matrix}')

# 以格式化方式顯示矩陣
for r in range(M):
    for c in range(N):
        print(f'{matrix[r][c]:8d}', end=' ')  # 每個數字佔 8 個字元寬度
    print()
print()

# 4. 帶條件的生成式
# 生成 0-20 之間的偶數列表
list4 = [x for x in range(20) if x % 2 == 0]
print(f'帶條件的列表生成式 (偶數):')
print(f'===>{list4}\n')

# 5. 集合生成式 (Set Comprehension)
# 生成 0-20 之間的偶數集合
# 集合會自動去除重複元素
set1 = {x for x in range(20) if x % 2 == 0}
print(f'集合生成式 (偶數):')
print(f'===>{set1}\n')

# 6. 字典生成式 (Dictionary Comprehension)
# 生成 0-20 之間的偶數字典，鍵為數字，值為其平方
# 格式：{key_expression: value_expression for item in iterable if condition}
dict1 = {x: x**2 for x in range(20) if x % 2 == 0}
print(f'字典生成式 (數字:平方):')
print(f'===>{dict1}\n')

# 7. 產生器表達式 (Generator Expression)
# 類似列表生成式，但使用圓括號 ()
# 產生器是惰性計算，只在需要時才生成值
gexpr = (x for x in range(20) if x % 2 == 0)
print(f'產生器表達式:')
print(f'===>{gexpr}')  # 顯示產生器物件

# 逐一取出產生器中的值
print('產生器中的值:')
for n in gexpr:
    print(n, end=" ")
print()
