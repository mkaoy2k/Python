"""
這個模組展示了 Python os 模組的基本使用範例
主要功能包括：
1. 目錄操作 (建立、刪除、改名)
2. 目錄遍歷
3. 檔案系統資訊查詢
4. 目錄路徑操作

"""

import os
from datetime import datetime
from pathlib import Path

def main():
    # 列出 os 模組的所有方法
    print('列出 os 模組的所有方法:')
    print(dir(os))
    print()

    # 列出當前工作目錄路徑
    print('列出當前工作目錄路徑:')
    print(os.getcwd())
    print()

    # 更改當前工作目錄到相對路徑的 samples 目錄
    # 使用 Path(__file__).parent 取得當前腳本所在的目錄
    # 建立 samples 子目錄並切換到該目錄
    script_dir = Path(__file__).parent
    sample_dir = script_dir / 'sample'
    sample_dir.mkdir(exist_ok=True)  # 確保目錄存在
    print('更改當前工作目錄到:', sample_dir)
    os.chdir(sample_dir)
    print(os.getcwd())
    print()

    # 列出當前目錄下的所有子目錄
    print(f'列出 {sample_dir} 目錄下的所有子目錄:')
    print([entry.name for entry in os.scandir() if entry.is_dir()])
    print()

    # 建立目錄結構
    dir1 = 'Demo-dir'
    dir1sub = 'Sub-dir'
    dirpath = Path(dir1) / dir1sub

    # 建立多層目錄結構
    if not dirpath.exists():
        dirpath.mkdir(parents=True)
        print(f'{dir1} 目錄建立在 {os.getcwd()}')
        
        # 只列出子目錄
        subdirs = [entry.name for entry in os.scandir() if entry.is_dir()]
        print(f'子目錄列表: {subdirs}')
        print()

        print(f'{dir1sub} 目錄建立在 {dir1}')
        
        # 只列出子目錄
        subdirs = [entry.name for entry in os.scandir(dir1) if entry.is_dir()]
        print(f'子目錄列表: {subdirs}')
        print()

    # 列出目錄詳細資訊
    print('列出目錄詳細資訊:', dir1)
    mod_time = os.stat(dir1).st_mtime
    print(f'\t{os.stat(dir1)}\n\t修改時間: {datetime.fromtimestamp(mod_time)}')
    print()

    # 刪除目錄
    if dirpath.exists():
        dirpath.rmdir()
        print(f'{dir1sub} 目錄從 {dir1} 刪除')
        print(os.listdir(dir1))
        print()

    # 重命名目錄
    dir2 = 'Demo-other-dir'
    if Path(dir1).exists() and not Path(dir2).exists():
        Path(dir1).rename(dir2)
        print(f'{dir1} 目錄重命名為 {dir2}')
        print([entry.name for entry in os.scandir() if entry.is_dir()])
        print()

    # 遍歷目錄樹
    print(f'{sample_dir} 目錄樹遍歷:')
    for dirpath, dirname, filename in os.walk(sample_dir):
        print(f'當前路徑:\t{dirpath}')
        print(f'目錄:\t{dirname}')
        print(f'檔案:\t{filename}')
        print()

    # 清理臨時目錄
    if Path(dir1).exists():
        print(f'刪除 {dir1} 目錄')
        Path(dir1).rmdir()
    if Path(dir2).exists():
        print(f'刪除 {dir2} 目錄')
        Path(dir2).rmdir()

    # 返回原始目錄
    os.chdir(script_dir)
    print(f'返回原始目錄: {os.getcwd()}')

if __name__ == '__main__':
    main()
