"""
批量圖像處理工具

使用多進程並行處理大量圖像，支援高斯模糊和縮放處理。
"""

import time
import concurrent.futures
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

def process_images_parallel(image_paths: list) -> None:
    """
    使用多進程並行處理圖像

    Args:
        image_paths: 要處理的圖像文件路徑列表
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, image_paths)

def main() -> None:
    """
    主函數：執行圖像批量處理
    """
    # 獲取開始時間
    start_time = time.perf_counter()
    
    try:
        # 獲取所有圖像文件
        image_files = get_image_files(INPUT_DIR)
        
        if not image_files:
            print("未找到圖像文件")
            return
        
        # 開始並行處理
        process_images_parallel(image_files)
        
        # 計算並顯示處理時間
        end_time = time.perf_counter()
        print(f'處理完成！總耗時: {end_time - start_time:.2f} 秒')
        
    except Exception as e:
        print(f'處理過程中發生錯誤: {str(e)}')

if __name__ == '__main__':
    main()
