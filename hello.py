greeting = 'Hello'
name = 'Michael'
print(f'名字字串: {name}\n招呼字串: {greeting}\n')

print('使用 + 號串接名字字串…')
message = greeting + ', ' + name + '. Welcome!'
print('===>', message)

print('使用 str 類型的 format 方法…')
message2 = '{}, {}. Welcome!'.format(greeting, name)
print('===>', message2)

print('在 Python 3 使用 f-string 格式化（Python 2 不支援）…')
message3 = f'{greeting}, {name}. Welcome!'
print('===>', message3)

print('將名字字串轉換為大寫…')
message4 = f'{greeting}, {name.upper()}. Welcome!'
print('===>', message4)

# 查詢名字字串類型的類別方法及詳細說明
print(f'查詢名字字串類型變數 "name" 的所有類別方法：\n名字字串: {name}\n\t{dir(name)}\n')
print(f'查詢類別描述，"str.lower()":')
help(str.lower)