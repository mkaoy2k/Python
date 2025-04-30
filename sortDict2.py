"""
展示如何使用 sortedcollections 模組進行字典排序

功能:
    1. 依鍵值排序字典
    2. 依數值排序字典（假設數值可進行字母數字排序）
"""

from sortedcollections import OrderedDict
from inspect import getmembers, isfunction, ismethod, isclass

def display_package_info(package):
    """
    顯示 package 包裝中的函數、方法和類別
    
    這個函數會列印出 package 模組中所有公開的函數、方法和類別，並顯示其文檔說明
    """
    # 取得所有公開的函數
    print(f"\n顯示 '{package}' 包裝中的函數:")
    functions = [(name, func) for (name, func) in getmembers(package, isfunction) if not name.startswith("_")]
    for name, func in functions:
        print(f"\n函數: {name}")
        print(f"文檔說明: {func.__doc__.strip() if func.__doc__ else '沒有文檔說明'}")

    # 取得所有公開的方法
    print(f"\n顯示 '{package}' 包裝中的方法:")
    methods = [(name, method) for (name, method) in getmembers(package, ismethod) if not name.startswith("_")]
    for name, method in methods:
        print(f"\n方法: {name}")
        print(f"文檔說明: {method.__doc__.strip() if method.__doc__ else '沒有文檔說明'}")

    # 取得所有公開的類別
    print(f"\n顯示 '{package}' 包裝中的類別:")
    classes = [(name, cls) for (name, cls) in getmembers(package, isclass) if not name.startswith("_")]
    for name, cls in classes:
        print(f"\n類別: {name}")
        print(f"文檔說明: {cls.__doc__.strip() if cls.__doc__ else '沒有文檔說明'}")



def sort_dict_by_key(d):
    """
    依鍵值排序字典
    
    Args:
        d (dict): 要排序的字典
    
    Returns:
        dict: 排序後的新字典
    """
    od = OrderedDict(sorted(d.items()))
    print(f'OrderDict() 返回的類型是:\n\t{type(od)}')
    print(f'OrderedDict 物件值是:\n\t{od}')
    
    # 建立新的字典
    d_sorted = {}
    od["one"] = 'aaa'
    od.update(two='bbb')
    
    for key, val in od.items():
        d_sorted[key] = val
        print(f'\t{key}:{val}')
    
    return d_sorted

def sort_dict_by_value(d):
    """
    依數值排序字典
    
    Args:
        d (dict): 要排序的字典
    
    Returns:
        dict: 排序後的新字典
    """
    od = OrderedDict(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))
    print(f'OrderDict() 返回的類型是:\n\t{type(od)}')
    print(f'OrderedDict 物件值是:\n\t{od}')
    
    # 建立新的字典
    d_sorted = {}
    for key, val in od.items():
        d_sorted[key] = val
        print(f'\t{key}:{val}')
    
    return d_sorted

def main():
    """
    主程式函數，展示字典排序功能
    """
    # 顯示包裝資訊
    display_package_info(OrderedDict)
    
    # 原始字典
    d = {"one": 1, "two": 2, "three": 3}
    print(f'\n原始字典 d 是:\n\t{d}')
    
    # 依鍵值排序
    print('\n依鍵值排序:')
    d_key_sorted = sort_dict_by_key(d)
    print(f'依鍵值排序後的新字典是:\n\t{d_key_sorted}')
    
    # 依數值排序
    print('\n依數值排序:')
    d_val_sorted = sort_dict_by_value(d)
    print(f'依數值排序後的新字典是:\n\t{d_val_sorted}')

if __name__ == "__main__":
    main()
