"""
這個模組用於比較生成器和列表的效能差異
模組包含兩個主要函數：
1. people_list - 使用列表生成大量資料
2. people_generator - 使用生成器生成大量資料
"""

import meminfo
import random
import time

# 人名和專業列表
names = ['Michael', 'Kao', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    """
    使用列表生成指定數量的學生資料
    
    Args:
        num_people (int): 要生成的學生數量
        
    Returns:
        list: 包含學生資料的列表
    """
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    """
    使用生成器生成指定數量的學生資料
    
    Args:
        num_people (int): 要生成的學生數量
        
    Yields:
        dict: 包含單個學生資料的字典
    """
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


def main():
    """
    主函數，用於測試生成器和列表的效能差異
    """
    total = 1_000_000
    
    print('生成器效能測試:')
    print('===>測試前:')
    meminfo.mem_info()
    print()

    # 測試生成器效能
    g1 = time.process_time()
    people_generator(total)
    g2 = time.process_time()

    print('===>測試後:')
    meminfo.mem_info()
    print(f'耗時: {g2 - g1:.5f} 秒')
    print()

    print('列表效能測試:')
    print('===>測試前:')
    meminfo.mem_info()
    print()

    # 測試列表效能
    t1 = time.process_time()
    _ = people_list(total)
    t2 = time.process_time()

    print('===>測試後:')
    meminfo.mem_info()
    print(f'耗時: {t2 - t1:.5f} 秒')

if __name__ == '__main__':
    main()
