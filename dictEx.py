"""
字典操作示例
本程式展示了字典的基本操作，包括：
1. 建立和訪問字典
2. 更新和修改字典
3. 刪除字典元素
4. 字典遍歷
"""

def create_and_access_dict() -> dict:
    """建立和訪問字典"""
    student = {
        'name': 'John',
        'age': 25,
        'courses': ['Math', 'ComSci']
    }
    
    print("\n=== 字典建立和訪問 ===")
    print(f"字典內容: {student}")
    print(f"訪問名字: {student['name']}")
    print(f"所有鍵: {list(student.keys())}")
    print(f"所有值: {list(student.values())}")
    print(f"所有鍵值對: {list(student.items())}")
    print(f"字典大小: {len(student)}")
    
    return student

def update_dict(student: dict) -> dict:
    """更新字典"""
    print("\n=== 字典更新 ===")
    
    # 更新單個值
    student['name'] = 'Jane'
    print(f"更新名字後: {student}")
    
    # 更新多個值
    student.update({
        'name': 'Jim',
        'age': 23,
        'phone': '888-8888'
    })
    print(f"批量更新後: {student}")
    
    return student

def delete_from_dict(student: dict) -> None:
    """從字典中刪除元素"""
    print("\n=== 字典刪除 ===")
    
    # 刪除指定鍵
    if 'phone' in student:
        del student['phone']
        print(f"刪除電話後: {student}")
    
    # 彈出並獲取值
    age = student.pop('age', None)
    print(f"彈出年齡後: {student}")
    print(f"彈出的年齡值: {age}")

def loop_through_dict(student: dict) -> None:
    """字典遍歷"""
    print("\n=== 字典遍歷 ===")
    
    # 使用 items() 方法遍歷
    print("使用 items() 方法遍歷:")
    for key, value in student.items():
        print(f"{key}: {value}")
    
    # 使用 keys() 方法遍歷
    print("\n使用 keys() 方法遍歷:")
    for key in student.keys():
        print(key)
    
    # 使用 values() 方法遍歷
    print("\n使用 values() 方法遍歷:")
    for value in student.values():
        print(value)

def main() -> None:
    """主函數"""
    # 建立和訪問字典
    student = create_and_access_dict()
    
    # 更新字典
    student = update_dict(student)
    
    # 從字典中刪除元素
    delete_from_dict(student)
    
    # 字典遍歷
    loop_through_dict(student)

if __name__ == "__main__":
    main()
