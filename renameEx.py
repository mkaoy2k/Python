"""
批量重命名檔案的程式
這個程式會將指定目錄中的檔案名稱從 '標題-課程-編號' 格式
轉換為 '編號-標題' 格式。

使用方法：
    1. 確保檔案在正確的目錄中
    2. 程式會自動過濾不需要的檔案（如 .DS_Store）
    3. 將檔案名稱重命名為新的格式
"""

from pathlib import Path
import os

def rename_files(directory):
    """
    重命名指定目錄中的所有檔案
    
    Args:
        directory (str): 要處理的目錄路徑
    """
    try:
        os.chdir(directory)
        print(f"當前目錄：{os.getcwd()}")

        # 遍歷目錄中的所有檔案
        for f in os.listdir():
            # 過濾不需要的檔案
            if f == '.DS_Store':
                continue

            try:
                # 分割檔案名稱和擴展名
                f_name, f_ext = os.path.splitext(f)
                
                # 分割檔案名稱的各個部分
                f_title, f_course, f_number = f_name.split('-')
                
                # 移除空白並格式化
                f_title = f_title.strip()
                f_course = f_course.strip()
                
                # 驗證編號是否為數字
                number_part = f_number.strip()[1:]
                if not number_part.isdigit():
                    raise ValueError(f"編號部分 '{number_part}' 不是有效的數字")
                    
                # 去除編號前的符號'#'並補零
                f_number = number_part.zfill(2)  
                
                # 生成新的檔案名稱
                new_name = f'{f_number}-{f_course}-{f_title}{f_ext}'
                
                # 顯示舊名稱和新名稱
                print(f'舊名稱:\t{f}\n\t新名稱:\t{new_name}')
                
                # 重命名檔案
                os.rename(f, new_name)
                
            except Exception as e:
                print(f"==> 警告：跳過檔案 {f}，原因：{str(e)}")
                continue
            
    except Exception as e:
        print(f"==> 發生錯誤：{str(e)}")

def main():
    """
    主程式函數
    設定要處理的目錄並呼叫重命名函數
    """
    # 使用 pathlib 找到 video 目錄
    current_dir = Path(__file__).resolve().parent
    target_directory = current_dir / 'video'
    
    if not target_directory.exists():
        print(f"錯誤：找不到目錄 {target_directory}")
        return
    
    rename_files(str(target_directory))

if __name__ == '__main__':
    main()
