"""元組物件的相關方法例子"""

numbers = (1, 9, 8, 1, 2, 4, 7, 1)
print(f'數字列表: {numbers}\n')
item_new = 1

print(f'1. 列表中 1 出現次數: {numbers.count(item_new)}\n')

print(f'2. 列表中 1 第一次出現的索引: {numbers.index(item_new)}\n')

courses = ('歷史', '物理', '電腦', '物理')
print(f'課程元组: {courses}\n')

# 元组轉字串
course_str = ' - '.join(courses)
print(f'3. 元组轉字串: {course_str}\n')

# 字串轉列表，再轉元组
new_list = course_str.split(' - ')
new_tuple = tuple(new_list)
print(f'4. 元组轉元组: {new_tuple}\n')
