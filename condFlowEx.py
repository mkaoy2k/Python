# Comparisons:
#
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=

language = 'Java'

if language == 'Python':
	print('Language is Python\n')
elif language == 'Java':
	print('Language is Java\n')
elif language == 'JavaScript':
	print('Language is JavaScript\n')
else:
	print('No match\n')

# Conditional expression 
# and
# or
# not

user = 'Admin'
logged_in = True

if not logged_in:
	print('Please log in\n') 
else:
	print('Welcome\n')

if user == 'Admin' and logged_in:
	print('Admin Page\n')
else:
	print('Bad Creds\n')

"""
Python 物件身份 (Object Identity) 範例
本程式示範 Python 中物件的身份和相等性的差異
"""

# 建立三個列表物件
a = [1, 2, 3]  # 第一個列表
b = a          # b 指向 a 的同一個記憶體位置
c = [1, 2, 3]  # 建立一個新的列表，內容與 a 相同

# 顯示每個物件的記憶體地址 (id)
print(f'a 的記憶體地址: {id(a)}')
print(f'b 的記憶體地址: {id(b)}')
print(f'c 的記憶體地址: {id(c)}\n')

# 檢查物件內容是否相等
# 使用 == 運算符比較物件內容
print(f'a 和 c 的內容是否相等? {a == c}')

# 檢查物件身份是否相同
# 使用 is 運算符檢查物件是否指向同一個記憶體位置
print(f'a 和 c 是否指向同一個物件? {a is c}')
print(f'a 和 b 是否指向同一個物件? {a is b}')

# 說明：
# 1. a == c 為 True，因為它們的內容相同
# 2. a is c 為 False，因為它們是不同的物件，只是內容相同
# 3. a is b 為 True，因為 b 是 a 的引用，指向同一個記憶體位置

# 進一步示範：修改 a 的內容會影響 b，但不會影響 c
print('\n進一步示範:')
a.append(4)  # 在 a 中新增一個元素
print(f'修改 a 後:')
print(f'a: {a}')  # [1, 2, 3, 4]
print(f'b: {b}')  # [1, 2, 3, 4]，因為 b 和 a 是同一個物件
print(f'c: {c}')  # [1, 2, 3]，因為 c 是獨立的物件

"""
Python 布林值評估 (Boolean Evaluation) 範例
本程式示範 Python 中各種值在布林上下文中的評估結果
"""

# 建立測試條件列表
# 包含各種類型的值，用於測試布林評估
conditions = [
    False,    # 布林值 False
    None,     # None 物件
    0,        # 整數 0
    10,       # 非零整數
    '',       # 空字串
    'Test',   # 非空字串
    (),       # 空元組
    [],       # 空列表
    {},       # 空字典
]

print("\n=== 布林值評估示範 ===")
print("測試不同值在布林上下文中的評估結果：\n")

# 逐一測試每個條件值
for cond in conditions:
    # 使用 if-else 進行布林評估
    if cond:
        # 如果條件為 True
        print(f'"{cond}" 在布林上下文中評估為 True')
    else:
        # 如果條件為 False
        print(f'"{cond}" 在布林上下文中評估為 False')

# 詳細說明 Python 中的假值 (False Values)
print("\n=== Python 中的假值 (False Values) ===")
print("在 Python 中，以下值在布林上下文中會被評估為 False：")
print("1. False - 布林值 False")
print("2. None - None 物件")
print("3. 數值 0 - 包括整數 0 和浮點數 0.0")
print("4. 空序列 - 包括空字串 ('')、空元組 (())、空列表 ([])")
print("5. 空映射 - 包括空字典 ({})、空集合 (set())")

# 實際應用示範
print("\n=== 實際應用示範 ===")
def check_value(value):
    """
    檢查值是否為真值
    
    Args:
        value: 要檢查的值
        
    Returns:
        布林值，True 表示值為真值，False 表示值為假值
    """
    return bool(value)

# 測試不同類型的值
print("\n測試不同類型的值：")
test_values = [0, 1, '', 'Hello', [], [1, 2], {}, {'key': 'value'}]
for value in test_values:
    result = check_value(value)
    print(f'值: ...{value}... (類型: {type(value).__name__}) -> 布林評估結果: {result}\n')
