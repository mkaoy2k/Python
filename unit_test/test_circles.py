"""
測試模組說明：圓形面積計算模組的單元測試

這個測試模組用於驗證 circles.py 中圓形面積計算功能的正確性，
主要包含以下測試案例：

1. 正常情況測試（test_area）
   - 測試半徑為正數時的面積計算
   - 測試半徑為 0 時的面積計算
   - 測試浮點數半徑的面積計算

2. 值錯誤測試（test_values）
   - 測試負數半徑時是否正確引發 ValueError

3. 類型錯誤測試（test_types）
   - 測試複數數字是否正確引發 TypeError
   - 測試布林值是否正確引發 TypeError
   - 測試字串是否正確引發 TypeError

特點：
- 使用 unittest 框架進行單元測試
- 測試結果會同時輸出到控制台
"""

import unittest
from math import pi

# Unit Test Cases
from circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test area calculation when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Test value errors of radius
        with self.assertRaises(ValueError):
            circle_area(-2)

    def test_types(self):
        # Test type errors of radius
        with self.assertRaises(TypeError):
            circle_area(3 + 5j)
        with self.assertRaises(TypeError):
            circle_area(True)
        with self.assertRaises(TypeError):
            circle_area("string")


if __name__ == '__main__':
    print(f'Unit Testing circles.py begins...')
    unittest.main()
