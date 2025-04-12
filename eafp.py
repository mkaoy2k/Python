# 這個文件展示了 Python 中的兩種重要編程模式：
# 1. 鴨子類型（Duck Typing）
# 2. EAFP（Easier to Ask for Forgiveness than Permission）
# 
# 這些模式體現了 Python 的核心哲學，並展示了如何編寫更 Pythonic 的代碼。

class Duck:
    """
    鴨子類，實現了 quack 和 fly 方法
    """
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:
    """
    人物類，也實現了 quack 和 fly 方法，但行為不同
    """
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly_np(thing):
    """
    非 Pythonic 方式的實現：
    1. 使用 isinstance 檢查類型
    2. 使用 hasattr 和 callable 檢查屬性
    
    Args:
        thing: 任何具有 quack 和 fly 方法的對象
    """
    # Not Duck-Typed (Non-Pythonic)
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')

    # LBYL (Look before you leap, Non-Pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()


def quack_and_fly(thing):
    """
    Pythonic 方式的實現：
    使用 try-except 結構，遵循 EAFP 原則
    
    Args:
        thing: 任何具有 quack 和 fly 方法的對象
    """
    try:
        thing.quack()
        thing.fly()
        thing.bark()  # 這個方法不存在，會觸發 AttributeError
    except AttributeError as e:
        print(f"發生錯誤：{e}")

    print()


def main():
    """
    主函數，展示不同的編程模式示例
    """
    # 鴨子類型示例
    d = Duck()
    print('-'*20)
    print('Duck typed Non-Pythonic example:')
    quack_and_fly_np(d)

    print('-'*20)
    print('\nDuck typed Pythonic example:')
    quack_and_fly(d)

    p = Person()
    print('-'*20)
    print('\nPerson Non-Pythonic example:')
    quack_and_fly_np(p)

    print('-'*20)
    print('\nPerson Pythonic example:')
    quack_and_fly(p)

    print('-'*20)
    # EAFP 模式示例
    print('\nEAFP 模式優點：')
    print('1. 提高代碼可讀性')
    print('2. 減少對象的多次訪問')
    print('3. 避免競態條件')

    print('-'*20)
    # 減少對象訪問次數的示例
    my_list = [1, 2, 3, 4, 5]

    # 非 Pythonic 方式：多次訪問列表
    print('\n非 Pythonic 列表示例:')
    if len(my_list) >= 6:
        print(my_list[5])
    else:
        print('該索引不存在')

    print('-'*20)
    # Pythonic 方式：使用 try-except
    print('\nPythonic 列表示例:')
    try:
        print(my_list[5])
    except IndexError:
        print('該索引不存在')

    print('-'*20)
    # 競態條件示例
    import os
    from pathlib import Path

    current_dir = Path(__file__).parent
    my_file = current_dir / "sample/test.txt"

    # 非 Pythonic 方式：存在競態條件
    print('\n非 Pythonic 競態條件示例:')
    if os.access(str(my_file), os.R_OK):
        with open(my_file) as f:
            print(f.read())
    else:
        print('無法訪問文件')

    print('-'*20)
    # Pythonic 方式：避免競態條件
    print('\nPythonic 競態條件示例:')
    try:
        f = open(my_file)
    except IOError as e:
        print(f'發生錯誤：{e}')
    else:
        with f:
            print(f.read())


if __name__ == '__main__':
    main()
