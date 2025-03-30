"""尋找一個四位數，當乘以4時等於其反轉的數字。

這個程式解決一個數學謎題，需要找到一個四位數ABCD，使其滿足：
1. 當乘以4時，結果仍然是四位數
2. 結果是原始數字的反轉
"""


def is_reverse(num1, num2):
    """檢查num2是否為num1的反轉。
    
    Args:
        num1 (int): 第一個數字
        num2 (int): 要檢查是否為num1反轉的第二個數字
        
    Returns:
        bool: 如果num2是num1的反轉則返回True，否則返回False
    """
    return str(num2) == str(num1)[::-1]


def is_valid_result(result):
    """檢查數字乘以4後是否仍然是四位數。
    
    Args:
        result (int): 要檢查的數字
        
    Returns:
        bool: 如果結果是四位數則返回True，否則返回False
    """
    return 1000 <= result <= 9999


def find_abcd():
    """生成所有滿足謎題條件的四位數。
    
    Yields:
        int: 滿足條件的四位數
    """
    for num in range(1000, 10000):  # 四位數範圍，從小到大
        result = num * 4
        if is_valid_result(result) and is_reverse(num, result):
            yield num


def main():
    """主要函數，用於運行謎題求解器並顯示結果。"""
    print("\n正在解四位數謎題...")
    print("-" * 50)
    print("謎題條件：")
    print("1. 數字是一個四位數 (1000-9999)")
    print("2. 當乘以4時，結果仍然是四位數")
    print("3. 結果是原始數字的反轉")
    print("-" * 50)
    
    solutions = list(find_abcd())
    if solutions:
        print(f"\n找到 {len(solutions)} 個解答！")
        for solution in solutions:
            print(f"\n解答：{solution}")
            print(f"當乘以4時：{solution * 4}")
            print(f"這是：{solution} 的反轉")
    else:
        print("\n找不到滿足所有條件的解答。")


if __name__ == '__main__':
    main()
