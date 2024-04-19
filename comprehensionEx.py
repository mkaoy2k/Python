"""List Comprehension examples"""

# 傳統程式寫法
list1 = []
for n in range(12):
  list1.append(n**2)
print(f'傳統程式...')
print(f'===>{list1}\n')

# 與上面等價的列表生成式如下
list2 = [n**2 for n in range(12)]
print(f'列表生成式...')
print(f'===>{list2}\n')

"""
多重迭代
一行列表生成式來定義 2x3 的矩陣
"""
list3 = [(r, c) for r in range(2) for c in range(3)]
print(f'多重迭代列表生成式 List of tuples initialization...')
print(f'===>{list3}\n')

# Example: M x N matrix  initialized with positive integers
# from left to right and then up down

M = 3
N = 5
matrix = [[c + N * r for c in range(1, N + 1)] for r in range(M)]
print(f'2-dim matrix initialization...\n===>{matrix}')
for r in range(0, M):
  for c in range(0, N):
    print(f'{matrix[r][c]:8d}', end=' ')
  print()
print()

"""
條件控制迭代
返回從0到小於20的偶數列表物件
"""
list4 = [x for x in range(20) if x % 2 == 0]
print(f'條件控制迭代列表生成式...')
print(f'===>{list4}\n')

"""
集合生成式 (Set Comprehension)
如下例返回從0到小於20的偶數集合物件
"""
set1 = {x for x in range(20) if x % 2 == 0}
print(f'集合生成式...')
print(f'===>{set1}\n')

"""
字典生成式 (Dictionary Comprehension)
如下例返回從0到小於20的偶數鍵字典物件，其值為鍵的平方
"""
dict1 = {x: x**2 for x in range(20) if x % 2 == 0}
print(f'字典生成式...')
print(f'===>{dict1}\n')

"""
元组生成式
即是上一章學過的產生器表達式 (Generator Expression)，然通常以產生器表達式稱之，
因為元组生成式回傳的是產生器物件，不是元組物件，如下例返回從0到小於20的偶數產生器物件：
"""
gexpr = (x for x in range(20) if x % 2 == 0)
print(f'元组生成式即是上一章學過的產生器表達式...')
print(f'===>{gexpr}')
for n in gexpr:
  print(n, end=" ")
print()
