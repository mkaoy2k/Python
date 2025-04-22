"""
my_moduleEx - my_module 的使用範例程式

這個範例程式展示了如何使用 my_module 中的 find_index 函數來
在列表中查找特定元素的索引位置。程式使用了 try-except 結構來
處理可能發生的錯誤情況。

使用範例：
    >>> python my_moduleEx.py
    courses: ['History', 'Math', 'Physics', 'ComSci']
    1
"""

import my_module

def main():
    """
    主程式函數，展示 my_module 的使用方式
    """
    try:
        # 測試資料
        courses = ['History', 'Math', 'Physics', 'ComSci']
        print(f'courses: {courses}')
        
        # 查找 'Math' 的索引位置
        target = 'Math'
        index = my_module.find_index(courses, target)
        print(f"{target} 的索引位置是: {index}")
        
        # 測試找不到的元素
        try:
            my_module.find_index(courses, 'Art')
        except ValueError as e:
            print(f"錯誤：{str(e)}")
            
    except Exception as e:
        print(f"發生未知錯誤：{str(e)}")

if __name__ == "__main__":
    main()
