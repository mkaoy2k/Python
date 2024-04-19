"""元組物件的相關函式例子"""

numbers = (9, 8, 1, 2, 4, 7)
print(f'數字元组: {numbers}\n')

print(f'1. 元组長度: {len(numbers)}\n')

print(f'2. 元组中最大元素: {max(numbers)}\n')

print(f'3. 元组中最小元素: {min(numbers)}\n')

print(f'4. 元组總計: {sum(numbers)}\n')


courses_list = ['歷史', '物理', '電腦', '物理']
courses_tuple = tuple(courses_list)
print(f'課程列表: {courses_list}\n')


print(f'5. 列表轉元组: {courses_tuple}\n')
print(f'   元组轉列表: {list(courses_tuple)}\n')
