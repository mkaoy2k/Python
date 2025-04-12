"""
檔案存取模式測試範例

本程式展示 Python 中不同檔案存取模式的效果：
- r: 讀取模式（預設）
- w: 寫入模式（會覆蓋現有檔案）
- a: 追加模式（從檔案結尾開始寫入）
- r+: 讀寫模式（從檔案開頭開始）
- w+: 讀寫模式（會覆蓋現有檔案）
- a+: 讀寫模式（從檔案結尾開始）

注意事項：
1. 確保 sample/test.txt 檔案存在
2. 程式會嘗試所有模式，並顯示結果
3. 遇到錯誤時會顯示提示訊息
"""

from pathlib import Path

# 取得當前檔案所在的目錄
# Path(__file__).parent 會返回當前檔案的父目錄
# 例如：如果檔案在 /Users/michaelkao/My_Projects/Python/filesEx1.py
# 則 current_dir 會是 /Users/michaelkao/My_Projects/Python
current_dir = Path(__file__).parent

# 建立檔案路徑
# 使用 / 運算符來連接路徑，這是 Path 物件的標準用法
# 這樣可以確保跨平台相容性
fileName = current_dir / "sample/test.txt"

# 測試所有檔案存取模式
for mode in ["r", "w", "a", "r+", "w+", "a+"]:
    try:
        # 嘗試以指定模式開啟檔案
        f = open(fileName, mode)
        # 顯示檔案物件名稱和存取模式
        print(f'檔案物件名稱: {f.name}')
        print(f'檔案存取模式: {f.mode}\n')
        # 重要：記得關閉檔案以釋放資源
        f.close()
    except:
        # 如果發生錯誤，顯示提示訊息
        print(f'事有蹊蹺')
