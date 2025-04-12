"""
這個程式示範了檔案讀取的異常處理和性能監控。
主要功能：
1. 讀取指定的檔案並計時
2. 記錄操作日誌（包括錯誤和性能數據）
3. 處理檔案不存在等異常情況
4. 提供命令列參數支援

使用方法：
python exceptionEx.py [檔案路徑]
如果不指定檔案路徑，將使用預設值 "file_not_existed.jpg"

注意：
程式會在 logger 目錄下生成 problems.log 日誌檔案
"""

import logging
import time
import sys
from pathlib import Path

# 獲取本檔案所在目錄
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / 'logger'

# 確保日誌目錄存在
LOG_DIR.mkdir(exist_ok=True)

# 設置日誌系統
# 記錄檔案：logger/problems.log
# 記錄等級：DEBUG
logging.basicConfig(filename=LOG_DIR / 'problems.log',
                    level=logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """
    讀取檔案內容並計時
    
    參數:
    - path: 檔案路徑
    
    回傳:
    - 檔案內容（二進位格式）
    
    執行步驟：
    1. 記錄開始時間
    2. 嘗試以二進位模式開啟檔案
    3. 讀取檔案內容
    4. 如果檔案不存在，記錄錯誤並拋出異常
    5. 正常情況下關閉檔案
    6. 記錄結束時間並計算執行時間
    7. 記錄執行時間到日誌
    """
    # 記錄開始時間
    start_time = time.time()
    try:
        # 以二進位模式開啟檔案
        with open(path, mode="rb") as f:
            data = f.read()
    except FileNotFoundError as err:
        # 記錄錯誤並拋出異常
        logger.error(f"找不到檔案：{err}")
        raise
    finally:
        # 記錄結束時間並計算執行時間
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"讀取檔案 {path} 所需時間 = {dt:.6f} 秒")
        print(f"讀取檔案 {path} 所需時間 = {dt:.6f} 秒")
    
    return data

def main():
    """
    主程式函數
    
    1. 檢查命令列參數
    2. 如果沒有指定檔案路徑，使用預設值 "Olisan.JPG"
    3. 嘗試讀取檔案
    4. 處理可能的異常
    """
    try:
        # 檢查命令列參數
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = "file_not_existed.jpg"
            
        # 驗證檔案存在
        if not Path(file_path).exists():
            logger.error(f"找不到檔案：{file_path}")
            print(f"錯誤：找不到檔案 {file_path}")
            print(f"Usage:\npython exceptionEx.py  # 使用預設檔案\npython exceptionEx.py your_file.jpg  # 指定其他檔案")
            sys.exit(1)
            
        # 讀取檔案
        data = read_file_timed(file_path)
        print(f"成功讀取檔案：{file_path}")
        print(f'檔案大小：{len(data)} bytes')
        
    except Exception as e:
        logger.error(f"發生未預期的錯誤：{str(e)}")
        print(f"發生錯誤：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
