"""
my_module - 提供序列搜尋功能的模組

這個模組主要提供了一個find_index函數，用於在序列中查找特定值的索引位置。
模組使用logging模組進行調試訊息的記錄。

使用範例：
    >>> from my_module import find_index
    >>> numbers = [1, 2, 3, 4, 5]
    >>> find_index(numbers, 3)
    2
"""

# my module
#
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug('Imported my_module...')

def find_index(to_search, target):
    """
    在序列中查找目標值的索引
    
    Args:
        to_search: 要搜尋的序列
        target: 要查找的目標值
        
    Returns:
        目標值在序列中的索引位置
        
    Raises:
        ValueError: 如果在序列中找不到目標值
    """
    for i, value in enumerate(to_search):
        if value == target:
            return i
    raise ValueError(f'目標值 {target} 在序列中不存在')

def main():
    """
    主程式函數，展示模組的使用方式
    """
    try:
        # 測試範例
        numbers = [10, 20, 30, 40, 50]
        print(f'測試範例: {numbers}')
        target = 30
        result = find_index(numbers, target)
        print(f"目標值 {target} 的索引位置是: {result}")
    except ValueError as e:
        print(e)
    except Exception as e:
        logging.error(f"發生未知錯誤: {str(e)}")

if __name__ == "__main__":
    main()