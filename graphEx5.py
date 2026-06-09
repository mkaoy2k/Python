"""
這個程式示範如何使用 graphviz 建立一個有向圖，並控制節點的層級排列。

主要功能：
- 建立一個包含三個節點（A、B、C）的有向圖
- 將節點 A 和 B 設定為同一層級
- 新增邊 A->C 和 B->C，其中 A->C 不影響節點層級，B->C 權重較強
- 渲染圖形並儲存為 PNG 格式
"""

# 匯入 graphviz 模組的 Digraph 類別
from graphviz import Digraph

# 建立一個名為 graphEx5 的有向圖，輸出格式為 PNG
dot = Digraph('graphEx5', format='png')

# 將節點 A 和 B 設定為同一層級
# 建立子圖來控制節點的層級
with dot.subgraph() as s:
    # 設定子圖中的節點位於同一層級
    s.attr(rank='same')
    # 新增節點 A
    s.node('A')
    # 新增節點 B
    s.node('B')

# 新增節點 C
dot.node('C')
# 新增邊 A->C，設定 constraint='false' 表示此邊不影響節點層級
dot.edge('A', 'C', constraint='false')
# 新增邊 B->C，設定 weight='10' 表示此邊權重較強
dot.edge('B', 'C', weight='10')

# 渲染圖形並儲存到 sample/graphEx5.gv，view=True 表示自動開啟預覽
dot.render('sample/graphEx5.gv', view=True)
