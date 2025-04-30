"""
這個程式展示了 Python sys 模組中的主要功能和結構
通過這個程式，我們可以了解 Python 的系統資訊和模組結構
"""

import inspect
import sys
from inspect import getmembers, isfunction, ismethod, isclass


def display_package_info(package):
    """
    顯示指定包裝中的函數、方法和類別資訊
    
    Args:
        package: 要顯示資訊的包裝
        
    這個函數會:
    1. 列印出所有公開的函數及其文檔說明
    2. 列印出所有公開的方法及其文檔說明
    3. 列印出所有公開的類別及其文檔說明
    """
    # 顯示函數資訊
    print(f"\n顯示 '{package.__name__}' 包裝中的函數:")
    functions = [(name, func) for (name, func) in getmembers(package, isfunction) if not name.startswith("_")]
    for name, func in functions:
        print(f"\n函數: {name}")
        print(f"文檔說明: {func.__doc__.strip() if func.__doc__ else '沒有文檔說明'}")

    # 顯示方法資訊
    print(f"\n顯示 '{package.__name__}' 包裝中的方法:")
    methods = [(name, method) for (name, method) in getmembers(package, ismethod) if not name.startswith("_")]
    for name, method in methods:
        print(f"\n方法: {name}")
        print(f"文檔說明: {method.__doc__.strip() if method.__doc__ else '沒有文檔說明'}")

    # 顯示類別資訊
    print(f"\n顯示 '{package.__name__}' 包裝中的類別:")
    classes = [(name, cls) for (name, cls) in getmembers(package, isclass) if not name.startswith("_")]
    for name, cls in classes:
        print(f"\n類別: {name}")
        print(f"文檔說明: {cls.__doc__.strip() if cls.__doc__ else '沒有文檔說明'}")

def display_sys_info():
    """
    顯示 Python 系統相關資訊
    
    這個函數會顯示:
    1. Python 的版本資訊
    2. Python 可執行檔案的路徑
    """
    print('Python 版本資訊:')
    print('sys.version:')
    print(sys.version)
    print('\nPython 可執行檔案路徑:')
    print('sys.executable:')
    print(sys.executable)

def main():
    """
    主函數，執行系統資訊的顯示
    
    這個函數會:
    1. 顯示 Python 系統資訊
    2. 顯示 inspect 模組的詳細資訊
    """
    print("開始顯示系統資訊...")
    display_sys_info()
    print("\n開始顯示 inspect 模組的詳細資訊...")
    display_package_info(inspect)
    print("\n資訊顯示完成！")

if __name__ == '__main__':
    main()
