"""
使用 Graphviz 生成二元樹圖形的範例程式

這個程式會:
1. 建立一個簡單的二元樹結構
2. 使用 Graphviz 將樹形結構視覺化
3. 將生成的圖形儲存到 sample 目錄中

注意事項:
- 需要安裝 graphviz 套件
- 生成的圖形會自動開啟預設的圖片檢視器
- bstGraph.gv 會儲存圖形的原始描述，可以使用 Graphviz 編輯器(eg. DOT插件)顯示
- bstGraph.png 會儲存圖形的圖片檔案
"""
from graphviz import Digraph
from pathlib import Path

# 確保 sample 目錄存在，用於儲存生成的圖形檔案
def setup_sample_dir():
    sample_dir = Path(__file__).parent / 'sample'
    sample_dir.mkdir(exist_ok=True)
    return sample_dir

# 生成簡單的二元樹
# @param n 當前節點的值
# @param parent 父節點的值（如果存在）
def add_node(dot, n, parent=None):
    # 建立當前節點
    dot.node(str(n))
    
    # 如果有父節點，建立連接線
    if parent is not None:
        dot.edge(str(parent), str(n))
    
    # 限制樹的深度（最多 3 層）
    # 左子節點 = 當前節點 * 2
    # 右子節點 = 當前節點 * 2 + 1
    if n < 4:
        add_node(dot, 2*n, n)      # 左子節點
        add_node(dot, 2*n + 1, n)  # 右子節點

def main():
    # 建立 Graphviz 圖形物件，指定格式為 png
    dot = Digraph('bstGraph', format='png')
    
    # 確保 sample 目錄存在
    sample_dir = setup_sample_dir()
    
    # 從根節點 1 開始建立樹
    add_node(dot, 1)
    
    # 生成並顯示圖形，檔案儲存於 sample 目錄中
    dot.render(str(sample_dir / 'bstGraph.gv'), view=True)

if __name__ == "__main__":
    main()
