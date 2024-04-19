"""元組可以使用索引來訪問元組中的元素，注意索引都要用方括號，如下實例："""

tuple1 = (1, 2, 3, 4, 5, 4)
tuple2 = (1, 2, 5)

print(f'tuple1 物件類型: {type(tuple1)}\n')
print(f'tuple1 = {tuple1}\n')
print(f'tuple2 = {tuple2}\n')

print(f'tuple1 元組第一個元素 = {tuple1[0]}\n')
print(f'tuple1 元組最後一個元素 = {tuple1[-1]}\n')

"""截取元組例子"""

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 5, 7)

print(f'tuple1 元組奇數索引的元素 = {tuple1[1::2]}\n')
print(f'tuple2 元組第一個到第三個元素 = {tuple2[:3]}\n')

"""元組運算例子"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(f'元組1 = {tuple1}')
print(f'元組2 = {tuple2}')

# 組合多個元組物件成一個元組
tuple3 = tuple1 + tuple2
print(f'元組1 + 元組2 = {tuple3}\n')

# 重複元組中元素
# 注意: 元組中只包含一個元素時，需要在元素後面添加逗號
tuple_hello = ('哈囉',) * 4
print(f'元組 (\'哈囉\',) * 4 = {tuple_hello}\n')

"""元組物件的比較運例子"""

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print(f'元組1 = {tuple1}')
print(f'元組2 = {tuple2}\n')

print(f'3 in {tuple1}: {3 in tuple1}\n')
print(f'3 in {tuple2}: {3 in tuple2}\n')

if tuple1 == tuple2:
    print(f'{tuple1} 等於 {tuple2}')
elif tuple1 > tuple2:
    print(f'{tuple1} 大於 {tuple2}')
else:
    print(f'{tuple1} 小於 {tuple2}')
