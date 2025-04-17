"""火星移民年齡計算器
這個程式計算當你從火星返回地球時，你和你母親的年齡。
考慮到地球和火星的公轉週期不同，程式會計算出準確的年齡。

地球一年 = 365天
火星一年 = 687天
"""

import math
import pandas as pd
from pathlib import Path

def calculate_age(days: int, days_per_year: int = 365) -> int:
    """
    計算年齡
    
    Args:
        days: 總天數
        days_per_year: 一年的天數 (預設為地球的365天)
        
    Returns:
        計算出的年齡 (向上取整)
    """
    return math.ceil(days / days_per_year)

def create_age_table(your_age: int, mom_age: int, years_in_mars: int, days_per_earth_year: int, days_per_mars_year: int) -> list:
    """
    創建年齡計算表格
    
    Args:
        your_age: 移民火星時你的年齡
        mom_age: 移民火星時母親的年齡
        years_in_mars: 在火星居住的年數
        days_per_earth_year: 地球一年的天數
        days_per_mars_year: 火星一年的天數
        
    Returns:
        包含年齡計算結果的二維列表
    """
    # 計算地球日
    your_age_in_days = your_age * days_per_earth_year
    mom_age_in_days = mom_age * days_per_earth_year
    days_in_mars = years_in_mars * days_per_mars_year
    
    # 計算返回地球時的年齡
    your_age_on_return = calculate_age(your_age_in_days + days_in_mars)
    mom_age_on_return = calculate_age(mom_age_in_days + days_in_mars)
    
    # 創建表格
    table = [
        ['人物', '移民火星時歲數', '移民火星時換成地球日', '火星待了十年換成地球日', '回地球時歲數'],
        ['你', your_age, your_age_in_days, days_in_mars, your_age_on_return],
        ['媽媽', mom_age, mom_age_in_days, days_in_mars, mom_age_on_return]
    ]
    
    return table

def print_age_calculation(your_age: int, mom_age: int, years_in_mars: int, days_per_earth_year: int, days_per_mars_year: int) -> None:
    """
    顯示年齡計算過程
    
    Args:
        your_age: 移民火星時你的年齡
        mom_age: 移民火星時母親的年齡
        years_in_mars: 在火星居住的年數
        days_per_earth_year: 地球一年的天數
        days_per_mars_year: 火星一年的天數
    """
    your_age_in_days = your_age * days_per_earth_year
    mom_age_in_days = mom_age * days_per_earth_year
    days_in_mars = years_in_mars * days_per_mars_year
    
    print("推論：你回到故鄉時...")
    print(f"你一生已過了地球日總共...")
    print(f"\t{your_age} * {days_per_earth_year} + {years_in_mars} * {days_per_mars_year}")
    total = your_age_in_days + days_in_mars
    print(f"\t= {your_age_in_days} + {days_in_mars}")
    print(f"\t= {total}\n")
    
    print(f"你的年紀...")
    print(f"\t= {total} / 365")
    print(f"\t= {calculate_age(total)} 地球歲\n")
    
    print(f"你媽媽一生已過了地球日總共...")
    print(f"\t{mom_age} * {days_per_earth_year} + {years_in_mars} * {days_per_mars_year}")
    total = mom_age_in_days + days_in_mars
    print(f"\t= {mom_age_in_days} + {days_in_mars}")
    print(f"\t= {total}\n")
    
    print(f"你媽媽的年紀...")
    print(f"\t= {total} / 365")
    print(f"\t= {calculate_age(total)} 地球歲\n")

def write_to_excel(table: list) -> None:
    """
    將表格寫入 Excel 檔案
    
    Args:
        table: 包含年齡計算結果的二維列表
    """
    df = pd.DataFrame(table)
    current_dir = Path(__file__).parent
    data_path = current_dir / 'sample'
    file_write = data_path / 'mars.xlsx'
    df.to_excel(file_write)
    print(f'===>請打開 {file_write} 檢視 EXCEL 格式的檔案...\n')

def read_from_excel() -> None:
    """
    從 Excel 檔案讀取表格
    """
    current_dir = Path(__file__).parent
    data_path = current_dir / 'sample'
    file_read = data_path / 'mars.xlsx'
    df = pd.read_excel(file_read)
    print(f'從 {file_read} EXCEL 檔案讀入 ...\n')
    print(f'===>資料框列出答案如下 ...\n{df}\n')

def main():
    """
    主程式函數
    設置初始參數並執行年齡計算
    """
    # 問題敘述
    question = """問：
    假設有一天，科技能讓你移民火星的時候，而你媽媽仍住在地球。
    離開地球這一天你 20 歲剛替媽媽辦了44歲生日趴。
    可是已知地球一年 365 天而火星一年 687 天。
    隨著時間過去，問題來了。
    在火星過了10年後的你，才能回地球看望你的母親。
    這時候回到地球家的你，阿母已經是多少歲了？
"""
    
    print(f'{question}\n')
    
    # 設置初始參數
    your_age = 20
    mom_age = 44
    years_in_mars = 10
    
    # 設置公轉週期
    days_per_earth_year = 365  # 地球一年的天數
    days_per_mars_year = 687  # 火星一年的天數
    
    # 執行計算並顯示結果
    age_table = create_age_table(your_age, mom_age, years_in_mars, days_per_earth_year, days_per_mars_year)
    print_age_calculation(your_age, mom_age, years_in_mars, days_per_earth_year, days_per_mars_year)
    
    # 顯示表格
    print("年齡計算表格：")
    for row in age_table:
        print("\t".join(str(item) for item in row))
    
    # 寫入 Excel 檔案
    write_to_excel(age_table)
    
    # 讀取 Excel 檔案
    read_from_excel()

if __name__ == "__main__":
    main()
