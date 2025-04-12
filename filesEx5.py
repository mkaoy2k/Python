"""
這個程式示範了如何使用 Python 的文件讀取功能，特別是使用 read() 方法
以指定的位元數量來讀取文件內容。

主要功能：
1. 使用 pathlib 路徑處理來定位文件位置
2. 以 50 個位元為單位逐次讀取文件內容
3. 顯示讀寫頭的當前位置
4. 輸出每次讀取的內容

使用方法：
程式會自動讀取與本程式同目錄下的 'sample/test.txt' 文件
"""


from pathlib import Path

current_dir = Path(__file__).parent
fileName = current_dir / 'sample/test.txt'

with open(fileName, 'r') as f:
    print(f'讀寫頭現在位置 = {f.tell()}\n')

    # 一次讀出幾個位元
    size_to_read = 50
    f_contents = f.read(size_to_read)
    read_count = 1  # 初始化讀取計數器
    
    while len(f_contents) > 0:
        print(f'第 {read_count} 次讀取，一次讀出 {size_to_read} 個位元...\n===>{f_contents}<===\n')
        f_contents = f.read(size_to_read)
        read_count += 1  # 增加讀取計數
    print(f'===> {f.name} 讀取完畢！\n')

    print(f'讀寫頭現在位置 = {f.tell()}\n')
