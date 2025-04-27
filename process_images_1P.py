"""
使用單一進程處理圖片的範例
這個程式會讀取圖片，應用高斯模糊效果，並調整圖片大小。
所有處理完的圖片會被儲存到 img_processed 目錄中。
"""

import time
from PIL import Image, ImageFilter
from pathlib import Path
import os

# 圖像輸入目錄和輸出目錄
INPUT_DIR = Path('photo')
OUTPUT_DIR = Path('img_processed')

# 圖像尺寸設定
TARGET_SIZE = (1200, 1200)

# 圖像處理參數
GAUSSIAN_BLUR_RADIUS = 15

def get_image_files(directory: Path) -> list:
    """
    獲取指定目錄中的所有圖像文件

    Args:
        directory: 圖像文件所在的目錄

    Returns:
        圖像文件的完整路徑列表
    """
    return [str(file) for file in directory.glob('*.jpg')]


def process_image(img_path: str) -> None:
    """
    處理單張圖像，包括高斯模糊和縮放

    Args:
        img_path: 圖像文件的完整路徑
    """
    try:
        # 開啟圖像
        with Image.open(img_path) as img:
            # 應用高斯模糊
            img = img.filter(ImageFilter.GaussianBlur(GAUSSIAN_BLUR_RADIUS))
            
            # 調整圖像大小
            img.thumbnail(TARGET_SIZE)
            
            # 獲取文件名
            filename = os.path.basename(img_path)
            
            # 創建輸出目錄（如果不存在）
            OUTPUT_DIR.mkdir(exist_ok=True)
            
            # 儲存處理後的圖像
            img.save(OUTPUT_DIR / filename)
            print(f'已處理: {img_path}')
    except Exception as e:
        print(f'處理圖像 {img_path} 時發生錯誤: {str(e)}')

def main():
    """
    主程式函數
    負責初始化設定並呼叫圖片處理函數
    """
    # 記錄開始時間
    start_time = time.perf_counter()

    image_files = get_image_files(INPUT_DIR)
    for img_name in image_files:
        # 處理每張圖片
        process_image(img_name)

    # 記錄結束時間
    end_time = time.perf_counter()

    # 輸出總花費時間
    print(f'處理完成，總耗時: {end_time - start_time:.2f} 秒')

if __name__ == '__main__':
    main()
