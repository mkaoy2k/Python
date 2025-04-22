"""
這個程式示範如何將整數物件轉換為可迭代物件
並提供兩種轉換方法：字串轉換和列表轉換
"""

import itertools

def check_iterable(obj):
    """
    檢查物件是否為可迭代物件
    
    參數:
        obj: 要檢查的物件
    
    回傳:
        布林值: True 表示可迭代，False 表示不可迭代
    """
    try:
        iter(obj)
        print(f'===> {type(obj)} 是可迭代物件\n')
        return True
    except TypeError:
        print(f'===> {type(obj)} 不是可迭代物件\n')
        return False

def convert_integer_to_iterable(X):
    """
    示範兩種將整數轉換為可迭代物件的方法
    
    參數:
        X: 要轉換的整數
    """
    print(f'===>1. 把整數物件轉成字串')
    for digit in str(X):
        print(digit, end=" ")
    print()  # 換行
    check_iterable(str(X))

    print(f'===>2. 把整數物件轉成列表')
    digits = [int(d) for d in str(X)]
    for digit in digits:
        print(digit, end=" ")
    print()  # 換行
    check_iterable(digits)

def main():
    """
    主程式函數，負責程式的主要流程
    """
    X = 142_857
    print(X, end=" ")
    check_iterable(X)
    
    print(f'兩種方法把整數物件變成迭代器物件...')
    convert_integer_to_iterable(X)

if __name__ == "__main__":
    main()
