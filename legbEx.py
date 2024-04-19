# LEGB variable scope
#	Local
#	Enclosing
#	Global
#	Built-in

x = 'global x'


def test():
    global y
    x = 'local x'

    print('\n    In test(), local scope...')
    print('   ', x)

    y = 'global y'
    print('   ', y)

    # checking variabe scope using locals and globals
    print('    x is local?', 'x' in locals())
    print('    y is global?', 'y' in globals())


print('\nIn main(), global scope...')
print('   ', x)
test()

print('\nIn main(), global scope...')
print('    y is global?', 'y' in globals())
print('   ', y)


def outer():
    print('\n    In outer() scope...')
    x = 'outer x'
    y = 'outer y'

    print('   ', x)
    print('   ', y)

    def inner():
        print('\n       In inner() scope...')
        x = 'inner x'

        # declare enclosing variable y
        nonlocal y
        y = 'inner y'
        print('      ', x)
        print('      ', y)

    inner()
    print('\n    In outer() scope...')
    print('   ', x)
    print('   ', y)


outer()

# 內建變數範圍的例子
import builtins

print(f'\'builtins\' 模組中內建變數 (屬性和方法)如下:\n{dir(builtins)}\n')

list_1 = [5, 1, 4, -8, 9]

num_min = min(list_1)
print(f'例子1: min({list_1}) =\t {num_min}')
print(f'例子2: abs({num_min}) =\t {abs(num_min)}')
