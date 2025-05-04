"""
模組說明：圓形面積計算模組

這個模組提供了計算圓形面積的功能，並包含完整的錯誤處理和日誌記錄功能。
主要功能包括：
1. 計算圓形面積
2. 參數類型檢查
3. 負數半徑檢查
4. 完整的日誌記錄（同時輸出到控制台和檔案）
5. 環境變數配置支持

使用說明：
- 可以通過環境變數 LOGGING 控制日誌等級（預設為 INFO）
- 日誌檔案會自動生成在模組所在的目錄下
- 支援整數和浮點數作為半徑輸入

範例：
area = circle_area(5)  # 正確使用
area = circle_area(-3) # 會引發 ValueError
area = circle_area("5") # 會引發 TypeError
"""

from math import pi
import logging
from pathlib import Path
import os
import traceback
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 設置日誌
logger = logging.getLogger(__name__)

# 設置日誌格式
formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

# 設置 console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 設置日誌檔案處理器
log_dir = Path(__file__).parent  # 使用當前文件的父目錄
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'circles.log'
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)

# 設置日誌等級
log_level = os.getenv("LOGGING", "INFO")
if log_level == "INFO":
    logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

# 設置 console handler 的等級: INFO always
console_handler.setLevel(logging.INFO)

# 添加處理器到日誌器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

# calculate circle area function
def circle_area(r):
    if type(r) not in [int, float]:
        logger.debug(
            f'{get_function_name()}: TypeError - The radius must be numeric type.')

        raise TypeError("The radius must be numeric type.")
    if r < 0:
        logger.debug(
            f'{get_function_name()}: ValueError - The radius can not be negative.')

        raise ValueError("The radius can not be negative.")
    result = pi * (r**2)
    logger.debug(f'{get_function_name()}: {result}.')
    return result


# main
if __name__ == '__main__':
    print(f'circles.py begins...')
    logger.debug(f'circles.py begins...')
    logger.debug(f'Logging Level: {log_level}')
    for i in range(5):
        print(f'radius={i}, circle area={circle_area(i)}')
