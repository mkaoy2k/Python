"""
球體體積計算模組

此模組提供計算球體體積的功能，包含基本的錯誤處理和日誌記錄功能。
主要功能包括：
- 計算球體體積
- 驗證輸入參數類型和值
- 記錄操作日誌
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

def sphere_vol(r):
    logging.debug(f'{get_function_name()}: started.')
    if type(r) not in [int, float]:
        logging.debug(
            f'\t{get_function_name()}: TypeError - The radius must be numeric type.')
        raise TypeError("The radius must be numeric type.")
    if r < 0:
        logging.debug(
            f'\t{get_function_name()}: ValueError - The radius can not be negative.')
        raise ValueError("The radius can not be negative.")

    logging.debug(f'{get_function_name()}: ended normally.')

    return (4.0 / 3.0 * pi * (r**3))

def main():
    """
    主函數，用於測試球體體積計算功能
    """
    try:
        # 測試正常情況
        radius = 5.0
        volume = sphere_vol(radius)
        logger.info(f"球體半徑: {radius}, 體積: {volume}")
        
        # 測試異常情況
        invalid_radius = "not a number"
        try:
            sphere_vol(invalid_radius)
        except TypeError as e:
            logger.info(f"測試 TypeError: {str(e)}")
            
        negative_radius = -2.0
        try:
            sphere_vol(negative_radius)
        except ValueError as e:
            logger.info(f"測試 ValueError: {str(e)}")
            
    except Exception as e:
        logger.error(f"發生未預期的錯誤: {str(e)}")

if __name__ == "__main__":
    main()
