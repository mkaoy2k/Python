"""
這個模組展示了 Python 中不同的浮點數取整方法。
主要包含四種取整方式：
1. 向下取整 (使用 int())
2. 四捨五入到最接近的偶整數 (使用 round())
3. 向上取整 (使用 math.ceil())
4. 分別獲取整數和小數部分 (使用 math.modf())

使用方法：
    python numberConversion.py

"""
import math

def demonstrate_floor_conversion():
    """示範向下取整的使用方法"""
    print("1. 向下取整: 直接用內建的 int() 函數...")
    float_1 = 3.75
    int_1 = int(float_1)
    print(f"{float_1} ===> {int_1}")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{int_1} 類型是 {type(int_1)}\n")

def demonstrate_rounding():
    """示範四捨五入到最接近的偶整數的使用方法"""
    print("2. 四捨五入到最接近的數: 用 round() 函數...")
    float_1 = 3.2
    int_1 = round(float_1)
    print(f"{float_1} ===> {int_1}")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{int_1} 類型是 {type(int_1)}\n")
    
    print(f"round(5.5) ===> {round(5.5)}\n")
    
    float_1 = 3.85
    float_2 = round(float_1, 1)
    print(f"round(3.85) ===> {float_2} 較接近偶整數4")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{float_2} 類型是 {type(float_2)}\n")

def demonstrate_ceil():
    """示範向上取整的使用方法"""
    print("3. 向上取整: 需要用到 math 模組中的 ceil() 方法...")
    float_1 = 3.85
    int_1 = math.ceil(float_1)
    print(f"math.ceil(3.85) ===> {int_1}")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{int_1} 類型是 {type(int_1)}\n")
    
    print(f"math.ceil(3.14) ===> {math.ceil(3.14)}\n")
    print(f"math.ceil(5.85) ===> {math.ceil(5.85)}\n")

def demonstrate_modf():
    """示範分離整數和小數部分的使用方法"""
    print("4. 需要分別獲取整數部分和小數部分...")
    float_1 = 3.14
    print(f"math.modf(3.14) ===> {math.modf(3.14)}")
    # 取整數部分
    int_1 = int(math.modf(float_1)[1])
    print(f"\t整數部分: {int_1}")
    dec_1 = math.modf(float_1)[0]
    print(f"\t小數部分: {dec_1}")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{int_1} 類型是 {type(int_1)}")
    print(f"\t{dec_1} 類型是 {type(dec_1)}\n")
    
    float_1 = 3.85
    print(f"math.modf(3.85) ===> {math.modf(3.85)}")
    # 取整數部分
    int_1 = int(math.modf(float_1)[1])
    print(f"\t整數部分: {int_1}")
    dec_1 = math.modf(float_1)[0]
    print(f"\t小數部分: {dec_1}")
    print(f"\t{float_1} 類型是 {type(float_1)}")
    print(f"\t{int_1} 類型是 {type(int_1)}")
    print(f"\t{dec_1} 類型是 {type(dec_1)}\n")

def main():
    """主函數，用於執行所有示範"""
    demonstrate_floor_conversion()
    demonstrate_rounding()
    demonstrate_ceil()
    demonstrate_modf()

if __name__ == "__main__":
    main()
