"""This is an example of reading and writing EXCEL files.
讀寫 EXCEL 檔案的例子：今夕是何年？火星移民十年"""

# 載入 math 模塊
# 利用其中的函式 ceil() 把年齡換成大於或等於浮點數的最小整數
import math
import pandas as pd # pip install pandas
from pathlib import Path

question = """問：
    假設有一天，科技能讓你移民火星的時候，而你媽媽仍住在地球。
    離開地球這一天你 20 歲剛替媽媽辦了44歲生日趴。
    可是已知地球一年 365 天而火星一年 687 天。
    隨著時間過去，問題來了。
    在火星過了10年後的你，才能回地球看望你的母親。
    這時候回到地球家的你，阿母已經是多少歲了？
"""

print(f'{question}\n')

# Facts
days_perEarthYear = 365
days_perMarsYear = 687

# 移民火星時歲數
yourAge = 20
momAge = 44

# 移民火星住在火星年數
years_in_Mars = 10

# 移民火星時換成地球日
yourAge_inDays = yourAge * days_perEarthYear
momAge_inDays = momAge * days_perEarthYear

# 火星待了十年換成地球日
days_inMars = years_in_Mars * days_perMarsYear

# 回地球時歲數
yourAge_onReturn = math.ceil(
    (yourAge * days_perEarthYear +
     years_in_Mars * days_perMarsYear) / days_perEarthYear)

momAge_onReturn = math.ceil(
    (momAge * days_perEarthYear +
     years_in_Mars * days_perMarsYear) / days_perEarthYear)

# Populate the table 二維列表 (3x5)
mars_table = [

    # 第一列
    [
        '人物',
        '移民火星時歲數',
        '移民火星時換成地球日',
        '火星待了十年換成地球日',
        '回地球時歲數'
    ],

    # 第二列
    [
        '你',
        yourAge,
        yourAge_inDays,
        days_inMars,
        yourAge_onReturn
    ],

    # 第三列
    [
        '媽媽',
        momAge,
        momAge_inDays,
        days_inMars,
        momAge_onReturn
    ]
]

print(f"推論：你回到故鄉時...\n你一生已過了地球日總共...")
print(f"\t{yourAge} * {days_perEarthYear} + {years_in_Mars} * {days_perMarsYear}")
total = yourAge_inDays + days_inMars
print(f"\t= {yourAge_inDays} + {days_inMars}")
print(f"\t= {total}\n")

print(f"你的年紀...")
print(f"\t= {total} / 365")
print(f"\t= {yourAge_onReturn:.0f} 地球歲\n")


print(f"你媽媽一生已過了地球日總共...")
print(f"\t{momAge} * {days_perEarthYear} + {years_in_Mars} * {days_perMarsYear}")
total = momAge_inDays + days_inMars
print(f"\t= {momAge_inDays} + {days_inMars}")
print(f"\t= {total}\n")

print(f"你媽媽的年紀...")
print(f"\t= {total} / 365")
print(f"\t= {momAge_onReturn} 地球歲\n")

# 二維列表用兩個方括號訪問：[列][行]
# 注意索引從 0 開始

print(f'答案是：\n你回家時，你已經 {mars_table[1][4]} 地球歲了')
print(f'要幫阿母辦個慶祝 {mars_table[2][4]} 歲的生日趴\n')

# 把2维列表寫入一個 EXCEL 檔案

# Creating a 3x5 dataframe
# df = pd.DataFrame(mars_table, index=['第一列', '第二列', '第三列'], columns=[
#                   '第一行', '第二行', '第三行', '第四行', '第五行'])
df = pd.DataFrame(mars_table)

# Initialize the folder where data is located
current_dir = Path(__file__).parent
data_path = current_dir / 'sample'  # relative to the current dir

# Specify all data files in this example
file_write = data_path / 'mars.xlsx'
file_read = data_path / 'mars.xlsx'

df.to_excel(file_write)
print(
    f'===>請打開 {file_write} 檢視 EXCEL 格式的檔案...\n')

df2 = pd.read_excel(file_read)
print(f'從 {file_read} EXCEL 檔案讀入 ...')

print(f'===>資料框列出答案如下 ...\n{df2.iloc[[0,1,2],5]}\n')
