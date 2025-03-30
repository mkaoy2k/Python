"""進階字串格式化示範

這個程式展示了 Python 中多種進階的字串格式化方法，
包括基本格式化、數字格式化、日期格式化等。
"""

# 進階字串格式化示範
#

person = {'name': 'Jenn', 'age': 23}
print('格式化字典:\t', person)

sentence = '我的名字是' + person['name'] + \
    '，我今年' + str(person['age']) + '歲。'
print('\t使用串接字串:\t', sentence)


sentence = '我的名字是{}，我今年{}歲。'.format(
    person['name'], person['age'])
print('\t使用 format 函數:\t', sentence)


sentence = '我的名字是{0}，我今年{1}歲。'.format(
    person['name'], person['age'])
print('\t使用位置參數:\t', sentence)


tag = 'h1'
text = '這是一個標題'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print('\t使用 HTML 標籤:\t', sentence)


sentence = '我的名字是{0}，我今年{1}歲。'.format(
    person['name'], person['age'])
print('\t訪問參數中的鍵:\t', sentence)


sentence = '我的名字是{0[name]}，我今年{1[age]}歲。'.format(
    person, person)
print('\t訪問格式化占位符中的鍵:\t', sentence)


sentence = '我的名字是{0[name]}，我今年{0[age]}歲。'.format(person)
print('\t傳遞單個參數字典:\t', sentence)


li = ['Jenn', 23]
print('格式化列表:\t', li)
sentence = '我的名字是{0[0]}，我今年{0[1]}歲。'.format(li)
print('\t訪問列表索引:\t', sentence)


累加器 = 0
for i in range(1, 11):
    累加器 += i

sentence = '累加器的值是 {}'.format(累加器)
print(sentence)


pi = 3.14159265
sentence = '圓周率等於:\t {}'.format(pi)
print(sentence)
print('格式化小數點後的數字:\t')

sentence = '\t圓周率保留三位小數:\t {:0.3f}'.format(pi)
print(sentence)


sentence = '1 MB 等於 {} 字節'.format(1000**2)
print(sentence)
print('格式化數字和小數點:\t')
sentence = '1 MB 等於 {:,.02f} 字節'.format(1000**2)
print('\t', sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')
print('格式化物件:\t', p1)

sentence = '我的名字是{0.name}，我今年{0.age}歲。'.format(p1)
print('\t訪問屬性:\t', sentence)


sentence = '我的名字是{name}，我今年{age}歲。'.format(
    name='Jenn', age='30')
print('\t替換參數:\t', sentence)


sentence = '我的名字是{name}，我今年{age}歲。'.format(**person)
print('\t最推薦的格式化方式:\t', sentence)


print('格式化填充數字:\t')
for i in range(1, 11):
    sentence = '\t補零到三位數:\t {:03}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = '圓周率等於:\t {}'.format(pi)
print(sentence)
print('格式化小數點後的數字:\t')

sentence = '\t圓周率保留三位小數:\t {:0.3f}'.format(pi)
print(sentence)


sentence = '1 MB 等於 {:,} bytes'.format(1000**2)
print(sentence)
print('格式化數字和小數點:\t')
sentence = '1 MB 等於 {:,.02f} bytes'.format(1000**2)
print('\t', sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print('格式化日期:\t')
print('\t', my_date)

# 9月24日，2016年
sentence = '{:%m月%d日，%Y年}'.format(my_date)
print('\t', sentence)

# 9月24日，2016年是星期六，是今年的第267天。

sentence = '{0:%m月%d日，%Y年}是{0:%A}，是今年的第{0:%j}天'.format(
    my_date)
print('\t', sentence)
