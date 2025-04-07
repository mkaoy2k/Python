"""
日期和時間操作的示例程式
"""
from datetime import datetime, date, time, timedelta
import pytz
"""
pytz: a powerful date/time and timezone library for Python
https://pypi.org/project/pytz/
"""

def create_date(year: int, month: int, day: int) -> date:
    """建立日期物件"""
    return date(year, month, day)

def create_time(hour: int, minute: int, second: int, microsecond: int) -> time:
    """建立時間物件"""
    return time(hour, minute, second, microsecond)

def get_current_datetime() -> datetime:
    """取得目前的日期時間"""
    return datetime.now()

def get_timezone_aware_datetime(tz: str = 'UTC') -> datetime:
    """取得時區感知的日期時間"""
    try:
        timezone = pytz.timezone(tz)
        return datetime.now(timezone)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"未知的時區: {tz}")

def format_datetime(dt: datetime, format_str: str = '%Y-%m-%d %H:%M:%S') -> str:
    """格式化日期時間為字串"""
    return dt.strftime(format_str)

def parse_datetime(dt_str: str, format_str: str = '%Y-%m-%d %H:%M:%S') -> datetime:
    """解析字串為日期時間"""
    try:
        return datetime.strptime(dt_str, format_str)
    except ValueError as e:
        raise ValueError(f"無法解析日期時間字串: {str(e)}")

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    """計算兩個日期時間之間的差異"""
    return end - start

def convert_timezone(dt: datetime, target_tz: str) -> datetime:
    """轉換日期時間的時區"""
    try:
        timezone = pytz.timezone(target_tz)
        return dt.astimezone(timezone)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"未知的目標時區: {target_tz}")

def display_date_info(d: date) -> None:
    """顯示日期資訊"""
    print(f"日期: {d}")
    print(f"年: {d.year}")
    print(f"月: {d.month}")
    print(f"日: {d.day}")

def display_time_info(t: time) -> None:
    """顯示時間資訊"""
    print(f"時間: {t}")
    print(f"小時: {t.hour}")
    print(f"分鐘: {t.minute}")
    print(f"秒: {t.second}")
    print(f"微秒: {t.microsecond}")
    print("-" * 10)

def display_datetime_info(dt: datetime) -> None:
    """顯示日期時間資訊"""
    print(f"日期時間: {dt}")
    print(f"年: {dt.year}")
    print(f"月: {dt.month}")
    print(f"日: {dt.day}")
    print(f"小時: {dt.hour}")
    print(f"分鐘: {dt.minute}")
    print(f"秒: {dt.second}")
    print(f"微秒: {dt.microsecond}")
    print("-" * 10)

def main():
    # 建立日期物件
    d = create_date(2001, 9, 11)
    display_date_info(d)
    
    # 建立時間物件
    t = create_time(9, 30, 45, 100000)
    display_time_info(t)
    
    # 當前日期時間
    now = get_current_datetime()
    display_datetime_info(now)
    
    # 時區感知日期時間
    try:
        utc_now = get_timezone_aware_datetime('UTC')
        display_datetime_info(utc_now)
        
        pacific_time = convert_timezone(utc_now, 'US/Pacific')
        display_datetime_info(pacific_time)
        
        eastern_time = convert_timezone(utc_now, 'US/Eastern')
        display_datetime_info(eastern_time)
    except ValueError as e:
        print(f"錯誤: {str(e)}")
    
    # 格式化日期時間
    formatted = format_datetime(now)
    print(f"格式化日期時間: {formatted}")
    
    # 解析日期時間
    try:
        parsed = parse_datetime(formatted)
        display_datetime_info(parsed)
    except ValueError as e:
        print(f"解析錯誤: {str(e)}")

if __name__ == "__main__":
    main()
