"""
寫一個 Python 程式印出從今天開始300年前後的完全平方日及其完全平方數。
完全平方日的定義就是西元年月日 'yyyymmdd' 格式所代表的整數
剛好又是某個正整數的平方。
例如：日期「20241001」是 4499 的平方，就是一個「完全平方日」。
"""

import datetime

def is_perfect_square(n):
    """檢查數字 n 是否為完全平方數"""
    root = int(n**0.5)
    return root * root == n, root

def find_perfect_square_dates(start_date, years):
    """找到從 start_date 開始的 years 年內的完全平方日"""
    perfect_square_dates = []
    
    # 計算結束日期
    end_date = start_date.replace(year=start_date.year + years)
    
    # 遍歷每一天
    current_date = start_date
    while current_date < end_date:
        # 生成 yyyymmdd 格式的整數
        date_number = int(current_date.strftime('%Y%m%d'))
        
        # 檢查是否為完全平方日
        is_square, root = is_perfect_square(date_number)
        if is_square:
            perfect_square_dates.append((current_date.strftime('%Y-%m-%d'), 
                                         root, 
                                         date_number))
        
        # 移動到下一天
        current_date += datetime.timedelta(days=1)
    
    return perfect_square_dates

# 主程式
if __name__ == "__main__":
    today = datetime.date.today()
    years_to_check = 300
    current_date = today.replace(year=today.year - years_to_check)
    
    perfect_squares = find_perfect_square_dates(current_date, years_to_check)
    
    # 印出結果
    print("今天以前300年的完全平方日及其完全平方數：")
    for date_str, root, square in perfect_squares:
        print(f"日期: {date_str}, 完全平方根: {root}, 完全平方數: {square}")

    perfect_squares = find_perfect_square_dates(today, years_to_check)
    print("今天以後300年的完全平方日及其完全平方數：")
    for date_str, root, square in perfect_squares:
        print(f"日期: {date_str}, 完全平方根: {root}, 完全平方數: {square}")
