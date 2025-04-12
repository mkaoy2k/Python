"""
檔案讀取範例
============

本範例示範如何使用 Python 的 with context manager 安全地讀取檔案。
主要功能包括：
- 使用 pathlib.Path 進行路徑處理
- 使用 with 陳述句確保檔案資源正確釋放
- 顯示檔案相關資訊和內容

特點：
- 自動資源管理：with 陳述句確保檔案在使用完畢後自動關閉
- 安全性：即使發生例外情況，檔案也會被正確關閉
- 路徑處理：使用 pathlib 模組進行跨平台的路徑處理
"""

from pathlib import Path

def get_file_path():
    """
    取得檔案路徑
    
    Returns:
        Path: 檔案的完整路徑
    """
    current_dir = Path(__file__).parent
    return current_dir / 'sample/test.txt'

def read_file(file_path):
    """
    讀取檔案內容
    
    Args:
        file_path (Path): 要讀取的檔案路徑
    
    Returns:
        str: 檔案內容
    
    Raises:
        FileNotFoundError: 如果指定的檔案不存在
        PermissionError: 如果沒有足夠的權限讀取檔案
        IOError: 如果發生其他檔案操作錯誤
    """
    try:
        with open(file_path, 'r') as f:
            print(f'Context Manager 執行 with-block 開啓檔案...')
            print(f'===> 檔案是否關閉? {f.closed}')  # 檔案是否關閉
            contents = f.read()
            print(f'檔案物件名稱: {f.name}')
            print(f'檔案存取模式: {f.mode}\n')
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {file_path}")
        raise
    except PermissionError:
        print(f"錯誤：沒有足夠的權限讀取檔案 {file_path}")
        raise
    except IOError as e:
        print(f"錯誤：讀取檔案時發生錯誤：{str(e)}")
        raise
    print(f'Context Manager 執行 with-block 結束，自動關閉檔案')
    print(f'===> 檔案是否關閉? {f.closed}')  # 檔案是否關閉
    return contents

def main():
    """
    主程式函數
    """
    # 取得檔案路徑
    file_path = get_file_path()
    
    # 讀取檔案內容
    try:
        file_contents = read_file(file_path)
    except Exception as e:
        print(f"錯誤：{str(e)}")
        return
    
    # 顯示檔案內容
    print(f'檔案內容一次讀出:\n{file_contents}\n')

if __name__ == '__main__':
    main()
