"""
Python 可迭代物件範例

本程式展示 Python 中各種內建的可迭代物件，並說明其特性
"""
import itertools
from typing import Iterable

def check_iterable(obj: object) -> bool:
    """
    檢查物件是否為可迭代物件

    Args:
        obj: 要檢查的物件

    Returns:
        bool: 如果物件可迭代則返回 True，否則返回 False
    """
    try:
        iter(obj)
        print(f'===> {type(obj)} 是可迭代物件')
        return True
    except TypeError:
        print(f'===> {type(obj)} 不是可迭代物件')
        return False

def show_iterable_examples():
    """展示各種可迭代物件的範例"""
    print("\n=== 序列類型 ===")
    check_iterable([1, 2, 3])      # list
    check_iterable((1, 2, 3))      # tuple
    check_iterable("hello")        # str
    check_iterable(b"hello")       # bytes
    check_iterable(range(3))       # range

    print("\n=== 集合類型 ===")
    check_iterable({1, 2, 3})      # set
    check_iterable(frozenset({1, 2, 3}))  # frozenset
    check_iterable({"a": 1, "b": 2})  # dict

    print("\n=== 生成器 ===")
    check_iterable((x for x in range(3)))  # 生成器表達式
    check_iterable(itertools.count())      # 無限生成器

    print("\n=== 其他 ===")
    check_iterable({1, 2, 3})      # set
    check_iterable(frozenset({1, 2, 3}))  # frozenset
    check_iterable({"a": 1, "b": 2})  # dict
    check_iterable(set())           # 空 set
    check_iterable(frozenset())     # 空 frozenset
    check_iterable(dict())          # 空 dict

def show_non_iterable_examples():
    """展示不可迭代物件的範例"""
    print("\n=== 不可迭代物件 ===")
    check_iterable(123)             # int
    check_iterable(3.14)            # float
    check_iterable(True)            # bool
    check_iterable(None)            # None
    check_iterable(object())        # 基本物件

def main():
    """主程式函數，展示可迭代物件的範例"""
    print("=== Python 可迭代物件範例 ===")
    show_iterable_examples()
    show_non_iterable_examples()

if __name__ == '__main__':
    main()
