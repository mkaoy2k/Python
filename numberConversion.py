"""Python 浮點數取整的方法，有四種方式：
1. 向下取整:直接用内建的 int() 函数
2. 四捨五入到最接近的偶整數: 用 round() 函数
3. 向上取整: 需要用到 math 模組中的 ceil() 方法
4. 需要分別獲取整數部分和小數部分: 用 math 模組中的 modf() 方法
"""
import math  # import 指令是载入 'math' 工具模組（第6章詳述）

# 1. 向下取整:直接用内建的 int() 函数即可
print(f'1. 向下取整:直接用内建的 int() 函数...')
float_1 = 3.75
int_1 = int(float_1)
print(f'{float_1} ===> {int_1}')
print(f'{float_1} 類型是 {type(float_1)}')
print(f'{int_1} 類型是 {type(int_1)}\n')
# 3

# 2. 四捨五入到最接近的偶整數: 用 round() 函数
# 注意：round(數字, 目標位數) 函数返回最接近的目標數。
# 若有两個目標數，會選擇為偶或較近偶整數的目標數。
print(f'2. 四捨五入到最接近的數: 用 round() 函数...')
float_1 = 3.2
int_1 = round(float_1)
print(f'{float_1} ===> {int_1}')
print(f'{float_1} 類型是 {type(float_1)}')
print(f'{int_1} 類型是 {type(int_1)}\n')
# 3
print(f'round(5.5) ===> {round(5.5)}\n')
# 5

float_1 = 3.85
float_2 = round(float_1, 1)
print(f'round(3.85) ===> {float_2} 較接近偶整數4')
# 3.9 較接近偶整數4
print(f'{float_1} 類型是 {type(float_1)}')
print(f'{float_2} 類型是 {type(float_2)}\n')

# 3. 向上取整: 需要用到 math 模組中的 ceil() 方法
print(f'3. 向上取整: 需要用到 math 模組中的 ceil() 方法...')
float_1 = 3.85
int_1 = math.ceil(float_1)
print(f'math.ceil(3.85) ===> {int_1}')
# 4
print(f'{float_1} 類型是 {type(float_1)}')
print(f'{int_1} 類型是 {type(int_1)}\n')

print(f'math.ceil(3.14) ===> {math.ceil(3.14)}\n')
# 4
print(f'math.ceil(5.85) ===> {math.ceil(5.85)}\n')
# 6

# 4. 需要分別獲取整數部分和小數部分: 用 math 模組中的 modf() 方法
# 該方法返回一個包含小數部分和整數部分的元組>>> import math
print(f'4. 需要分別獲取整數部分和小數部分:...')
float_1 = 3.14
print(f'math.modf(3.14) ===> {math.modf(3.14)}')
#(0.14, 3.0)
print(f'math.modf(3.14) 類型是 {type(math.modf(float_1))}\n')

print(math.modf(3.85))
#(0.85, 3.0)
