"""
這個程式示範如何根據自定義物件的屬性進行排序
主要展示了三種排序方式：
1. 使用自定義函數作為 key
2. 使用 lambda 函數作為 key
3. 使用 attrgetter 函數作為 key
"""

from operator import attrgetter

class Employee:
    """
    員工類別，包含姓名、年齡和薪資屬性
    """
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        """
        定義物件的字串表示方式
        """
        return f'({self.name},{self.age},{self.salary})'

def sort_by_name(emp):
    """
    根據員工姓名進行排序的函數
    
    Args:
        emp (Employee): 員工物件
    
    Returns:
        str: 員工姓名
    """
    return emp.name

def sort_by_age(emp):
    """
    根據員工年齡進行排序的函數
    
    Args:
        emp (Employee): 員工物件
    
    Returns:
        int: 員工年齡
    """
    return emp.age

def sort_by_salary(emp):
    """
    根據員工薪資進行排序的函數
    
    Args:
        emp (Employee): 員工物件
    
    Returns:
        int: 員工薪資
    """
    return emp.salary

def main():
    """
    主程式函數，示範不同的排序方式
    """
    # 建立員工物件
    e1 = Employee('Carl Washington', 37, 70_000)
    e2 = Employee('Sarah Dumbo', 29, 80_000)
    e3 = Employee('Michael Kao', 43, 90_000)
    
    print("\n=== 員工排序示範 ===")
    
    # 原始員工列表
    emp_list = [e1, e2, e3]
    print("\n原始員工列表:")
    print(f'\t{emp_list}')
    
    # 1. 使用自定義函數排序
    print("\n=== 1. 使用自定義函數排序 ===")
    
    # 按姓名排序
    sorted_by_name = sorted(emp_list, key=sort_by_name)
    print("\n按姓名排序:")
    print(f'\t{sorted_by_name}')
    
    # 按年齡排序
    sorted_by_age = sorted(emp_list, key=sort_by_age)
    print("\n按年齡排序:")
    print(f'\t{sorted_by_age}')
    
    # 按薪資遞減排序
    sorted_by_salary = sorted(emp_list, key=sort_by_salary, reverse=True)
    print("\n按薪資遞減排序:")
    print(f'\t{sorted_by_salary}')
    
    # 2. 使用 lambda 函數排序
    print("\n=== 2. 使用 lambda 函數排序 ===")
    sorted_by_lambda = sorted(emp_list, key=lambda e: e.name, reverse=True)
    print("\n按姓名遞減排序:")
    print(f'\t{sorted_by_lambda}')
    
    # 3. 使用 attrgetter 函數排序
    print("\n=== 3. 使用 attrgetter 函數排序 ===")
    sorted_by_attrgetter = sorted(emp_list, key=attrgetter('salary'), reverse=True)
    print("\n按薪資遞減排序:")
    print(f'\t{sorted_by_attrgetter}')

if __name__ == "__main__":
    main()
