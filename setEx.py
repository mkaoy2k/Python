"""
集合運算範例
展示 Python 集合的基本操作，包括交集、差集和聯集運算
"""

def main():
    """
    主函數：展示集合運算的範例
    """
    # 建立電腦科學課程集合（自動移除重複元素）
    cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'}
    print('\n電腦科學課程集合（無重複）:', cs_courses, '\n')

    # 建立藝術課程集合
    art_courses = {'History', 'Math', 'Art', 'Design'}

    # 顯示集合交集
    print('\n集合交集（同時存在於兩集合中的元素）:')
    print(cs_courses.intersection(art_courses))

    # 顯示集合差集
    print('\n集合差集（只存在於第一個集合中的元素）:')
    print(cs_courses.difference(art_courses))

    # 顯示集合聯集
    print('\n集合聯集（兩個集合的所有元素）:')
    print(cs_courses.union(art_courses))

    # 空集合的正確建立方式
    print('\n\n空集合的建立方式：')
    print('錯誤方式：{} 會建立空字典')
    print('正確方式：set()')

if __name__ == '__main__':
    main()