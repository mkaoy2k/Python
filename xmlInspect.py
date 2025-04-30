"""
這個程式用於檢視 Python XML 模組的內部結構
使用 inspect 模組來顯示 XML 模組中的類別和函數資訊
"""

import xml.etree.ElementTree as ET
from inspect import getmembers, isfunction, isclass, ismethod

def display_package_info(package):
    """
    顯示指定包裝中的所有公開函數、方法和類別

    Args:
        package: 要檢視的 Python 包裝

    Returns:
        None

    這個函數會:
    1. 列出所有公開的函數及其文檔說明
    2. 列出所有公開的方法及其文檔說明
    3. 列出所有公開的類別及其文檔說明
    """
    # 顯示函數
    print(f"\n顯示 '{package.__name__}' 包裝中的函數:")
    functions = [(name, func) for (name, func) in getmembers(package, isfunction) if not name.startswith("_")]
    for name, func in functions:
        print(f"\n函數: {name}")
        print(f"文檔說明: {func.__doc__.strip() if func.__doc__ else '沒有文檔說明'}")

    # 顯示方法
    print(f"\n顯示 '{package.__name__}' 包裝中的方法:")
    methods = [(name, method) for (name, method) in getmembers(package, ismethod) if not name.startswith("_")]
    for name, method in methods:
        print(f"\n方法: {name}")
        print(f"文檔說明: {method.__doc__.strip() if method.__doc__ else '沒有文檔說明'}")

    # 顯示類別
    print(f"\n顯示 '{package.__name__}' 包裝中的類別:")
    classes = [(name, cls) for (name, cls) in getmembers(package, isclass) if not name.startswith("_")]
    for name, cls in classes:
        print(f"\n類別: {name}")
        print(f"文檔說明: {cls.__doc__.strip() if cls.__doc__ else '沒有文檔說明'}")

def main():
    """
    程式主函數

    這個函數會:
    1. 初始化 XML 模組
    2. 顯示 XML 模組的相關資訊
    """
    # 初始化 XML 模組
    print("\n=== XML 模組檢視工具 ===")
    print("顯示 ElementTree 模組的相關資訊:")
    display_package_info(ET) 

if __name__ == "__main__":
    main()
