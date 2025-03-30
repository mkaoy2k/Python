"""最大公約數計算器

這個程式使用遞迴函數來計算兩個整數的最大公約數（GCD）。
使用歐幾里得算法（Euclidean algorithm）來實現計算。
"""

def validate_input(num, name):
    """驗證輸入是否為非負整數
    
    Args:
        num (int): 要驗證的數字
        name (str): 數字的名稱，用於錯誤訊息
        
    Raises:
        ValueError: 如果輸入不是非負整數
    """
    if not isinstance(num, int):
        raise ValueError(f"{name} 必須是整數")
    if num < 0:
        raise ValueError(f"{name} 必須是非負整數")

def gcd(a, b):
    """計算兩個整數的最大公約數
    
    使用歐幾里得算法（Euclidean algorithm）來計算最大公約數。
    
    Args:
        a (int): 第一個整數
        b (int): 第二個整數
        
    Returns:
        int: 兩個整數的最大公約數
    """
    # 驗證輸入
    validate_input(a, "第一個數字")
    validate_input(b, "第二個數字")
    
    # 基本情況：如果 b 為 0，則 a 就是最大公約數
    if b == 0:
        return a
    
    # 遞迴情況：計算 b 和 a % b 的最大公約數
    return gcd(b, a % b)

def main():
    """主程式"""
    print("最大公約數計算器")
    print("-" * 30)
    
    try:
        # 獲取使用者輸入
        num1 = int(input("請輸入第一個整數: "))
        num2 = int(input("請輸入第二個整數: "))
        
        # 計算最大公約數
        result = gcd(num1, num2)
        
        # 顯示結果
        print(f"\n{num1} 和 {num2} 的最大公約數是: {result}")
        
    except ValueError as e:
        print(f"錯誤: {str(e)}")
    except Exception as e:
        print(f"發生未知錯誤: {str(e)}")

if __name__ == "__main__":
    main()
