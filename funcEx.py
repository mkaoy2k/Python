"""
函數範例

這個程式展示了 Python 中不同類型的函數使用方式，
包括位置參數、關鍵字參數、可變參數等。
"""

from typing import Optional

class GreetingManager:
    """
    管理問候語的類別
    
    提供問候語的相關功能，包括基本問候和自定義問候。
    """
    
    @staticmethod
    def greet(greeting: str, name: str = "You") -> str:
        """
        產生問候語
        
        Args:
            greeting (str): 招呼語
            name (str, optional): 名字. 預設為 "You".
            
        Returns:
            str: 完整的招呼語
        """
        return f"{greeting}, {name}"

class StudentManager:
    """
    學生資訊管理類別
    
    提供學生資訊的相關功能，包括記錄科目和學生詳細資訊。
    """
    
    @staticmethod
    def student_info(*subjects: str, **student_details: str) -> None:
        """
        記錄學生資訊
        
        Args:
            *subjects: 變數個數的科目名稱
            **student_details: 學生的詳細資訊
        """
        print("\n學生資訊：")
        print("科目：", subjects)
        print("詳細資訊：", student_details)

class DateManager:
    """
    日期管理類別
    
    提供日期相關的功能，包括閏年判斷和月份天數計算。
    """
    
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    @staticmethod
    def is_leap(year: int) -> bool:
        """
        判斷是否為閏年
        
        Args:
            year (int): 年份
            
        Returns:
            bool: 是否為閏年
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(year: int, month: int) -> Optional[int]:
        """
        取得月份的天數
        
        Args:
            year (int): 年份
            month (int): 月份
            
        Returns:
            Optional[int]: 月份的天數，無效月份時返回 None
        """
        if not 1 <= month <= 12:
            print(f"錯誤：無效的月份 {month}")
            return None
            
        if month == 2 and DateManager.is_leap(year):
            return 29

        return DateManager.MONTH_DAYS[month]

def main():
    """
    主程式
    
    測試各個功能模組的功能。
    """
    # 測試問候語功能
    print("\n測試問候語功能：")
    print(GreetingManager.greet("你好"))
    print(GreetingManager.greet("你好", name="Michael"))
    
    # 測試學生資訊功能
    print("\n測試學生資訊功能：")
    StudentManager.student_info("數學", "美術", name="John", age="22")
    
    # 測試日期功能
    print("\n測試日期功能：")
    print('2017年是否為閏年？', DateManager.is_leap(2017))
    print('2017年2月有', DateManager.days_in_month(2017, 2), '天\n')

    print('2000年是否為閏年？', DateManager.is_leap(2000))
    print('2000年2月有', DateManager.days_in_month(2000, 2), '天\n')

    from datetime import datetime
    current_year = datetime.now().year
    print(f'{current_year}年是否為閏年？', DateManager.is_leap(current_year))
    print(f'{current_year}年2月有', DateManager.days_in_month(current_year, 2), '天\n')

if __name__ == "__main__":
    main()
