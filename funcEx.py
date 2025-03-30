"""函數範例

這個程式展示了 Python 中不同類型的函數使用方式，
包括位置參數、關鍵字參數、可變參數等。
"""

def greet(greeting: str, name: str = "You") -> str:
    """示範位置參數和預設值
    
    Args:
        greeting (str): 招呼語
        name (str, optional): 名字. 預設為 "You".
        
    Returns:
        str: 完整的招呼語
    """
    return f"{greeting}, {name}"

def student_info(*subjects: str, **student_details: str) -> None:
    """示範可變參數和關鍵字參數
    
    Args:
        *subjects: 變數個數的科目名稱
        **student_details: 學生的詳細資訊
    """
    print("\n學生資訊：")
    print("科目：", subjects)
    print("詳細資訊：", student_details)

def is_leap(year: int) -> bool:
    """判斷是否為閏年
    
    Args:
        year (int): 年份
    
    Returns:
        bool: 是否為閏年
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    """取得月份的天數
    
    Args:
        year (int): 年份
        month (int): 月份
    
    Returns:
        int: 月份的天數
    """
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

def main():
    """主程式"""
    # 測試位置參數和預設值
    print("\n測試位置參數和預設值：")
    print(greet("你好"))
    print(greet("你好", name="Michael"))
    
    # 測試可變參數和關鍵字參數
    print("\n測試可變參數和關鍵字參數：")
    student_info("數學", "美術", name="John", age="22")
    
    # 測試閏年和月份天數
    print("\n測試閏年和月份天數：")
    print('Year 2017 leap?', is_leap(2017))
    print('2017/2月 has:', days_in_month(2017, 2), 'days\n')

    print('Year 2000 leap?', is_leap(2000))
    print('2000/2月 has:', days_in_month(2000, 2), 'days\n')

    print('Year 2200 leap?', is_leap(2200))
    print('2200/2月 has:', days_in_month(2200, 2), 'days\n')

if __name__ == "__main__":
    main()
