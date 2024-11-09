# 定義一個函數來檢查是否滿足條件
def find_abcd():
    for abcd in range(1000, 10000):  # 四位數範圍
        dcba = abcd * 4  # 計算乘以4的值
        if dcba < 10000:  # 確保dcba仍然是四位數
            # 將數字轉換為字符串並反轉
            if str(dcba) == str(abcd)[::-1]:
                return abcd  # 返回符合條件的數字

# 調用函數並打印結果
result = find_abcd()
if result:
    print(f"符合條件的四位數 ABCD 是: {result}")
else:
    print("沒有找到符合條件的四位數。")
