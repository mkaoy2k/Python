"""
黃金比例計算器

此程式提供兩種計算黃金比例(Phi, φ)的方法：

1. 斐波那契數列相除法
   - 使用斐波那契數列的相鄰兩項相除來逼近黃金比例
   - 隨著項數增加，估算值會越來越接近真實的黃金比例

2. 手算除法模擬法
   - 模擬手算除法的過程來計算黃金比例的小數位
   - 可以設定計算的小數位精確度

使用方法：
1. 建立 GoldenRatioCalculator 物件
2. 使用 fibonacci_ratio() 方法計算斐波那契數列相除法
3. 使用 manual_division() 方法計算手算除法模擬法

注意事項：
- 程式使用 decimal 模組來處理高精度計算
- 設定的小數位精確度會影響計算結果的準確度
- 輸入的參數必須為正整數

作者：
日期：
"""

from decimal import Decimal, getcontext

class GoldenRatioCalculator:
    """
    黃金比例計算器類別
    
    此類別提供兩種計算黃金比例的方法：
    1. 斐波那契數列相除法
    2. 手算除法模擬法
    
    Attributes:
        precision (int): 小數點後精確度
    """

    def __init__(self, precision: int = 101):
        """
        初始化黃金比例計算器
        
        Args:
            precision (int): 設定小數點後精確度，預設為101位
        """
        self.precision = precision
        getcontext().prec = precision

    def fibonacci_ratio(self, n: int, a: int = 1, b: int = 1) -> tuple:
        """
        使用斐波那契數列相除法計算黃金比例
        
        Args:
            n (int): 斐波那契數列的項數
            a (int): 初始值1，預設為1
            b (int): 初始值2，預設為1

        Returns:
            tuple: (前一項, 當前項)

        Raises:
            ValueError: 如果輸入不是正整數
        """
        if not all(isinstance(x, int) and x > 0 for x in [n, a, b]):
            raise ValueError("所有輸入必須為正整數")

        for _ in range(n):
            a, b = b, a + b
        return a, b

    def manual_division(self, fibo_max: int) -> str:
        """
        使用手算除法模擬法計算黃金比例
        
        Args:
            fibo_max (int): 使用的斐波那契數列最大項數

        Returns:
            str: 格式化的黃金比例結果
        """
        a, b = self.fibonacci_ratio(fibo_max)
        quotient = b // a
        remainder = b % a

        # 計算小數部分
        decimal_part = []
        for _ in range(self.precision):
            remainder *= 10
            digit = remainder // a
            remainder = remainder % a
            decimal_part.append(str(digit))

        # 格式化輸出
        result = f"{quotient}." + "".join(decimal_part)
        return result

def main():
    """
    主函數，示範黃金比例的計算方法
    """
    calculator = GoldenRatioCalculator()

    print("=== 黃金比例計算示範 ===")
    
    # 方法1: 斐波那契數列相除法
    print("\n1. 斐波那契數列相除法:")
    x0, x1 = calculator.fibonacci_ratio(240)
    print(f"===> 斐波那契數(240) 黃金比例估值 =")
    print(102 * "=")
    print(f"{x1/x0}")
    print(f"a={x0}\nb={x1}\n")

    # 方法2: 手算除法模擬法
    print("\n2. 手算除法模擬法:")
    result = calculator.manual_division(66)
    print(f"===> 黃金比例 (66項斐波那契數列) {calculator.precision}位小數 =")
    print(102 * "=")
    for i in range(0, calculator.precision, 10):
        print(result[i:i + 10])

if __name__ == "__main__":
    main()
