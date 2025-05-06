"""
使用 Graphviz 生成軟體架構圖

這個程式會生成一個包含三個主要層次的軟體架構圖：
1. 前端層 (Frontend Layer) - 包含使用者介面和 API 客戶端
2. 後端層 (Backend Layer) - 包含 API 網關、服務和資料庫存取
3. 資料層 (Data Layer) - 包含主要資料庫和快取系統

圖表特色：
- 使用記錄型節點 (record nodes) 來表示複雜的元件結構
- 使用不同顏色來區分不同的層次
- 包含圖例來說明不同線型的意義
- 使用正交邊緣 (orthogonal edges) 來保持圖表的清晰度

輸出：
- 生成的圖表將保存在與程式相同的目錄下的 'sample' 子目錄中
- 圖表格式為 PNG
"""
from graphviz import Digraph
from pathlib import Path
import os

def create_software_architecture_graph():
    """
    創建軟體架構圖

    此函數會：
    1. 初始化 Graphviz 圖形，設置全局屬性
    2. 創建三個主要的子圖（層）：前端、後端和資料層
    3. 在每個層中添加相應的節點和邊
    4. 添加跨層的邊來表示不同層之間的互動
    5. 添加圖例來說明邊的意義
    6. 渲染並保存圖形
    """
    # 獲取腳本目錄並創建 sample 目錄
    script_dir = Path(__file__).parent
    sample_dir = script_dir / 'sample'
    sample_dir.mkdir(exist_ok=True)

    # 初始化有向圖，設置全局屬性
    dot = Digraph(
        name='software_architecture',
        format='png',
        graph_attr={
            'rankdir': 'TB',  # 由上至下布局
            'splines': 'ortho',  # 正交邊緣
            'bgcolor': 'lightgrey',  # 背景顏色
            'fontcolor': 'black',  # 字體顏色
            'fontsize': '12',  # 字體大小
            'style': 'filled',  # 填充樣式
            'compound': 'true'  # 啟用跨子圖的邊
        },
        node_attr={'shape': 'record', 'style': 'filled', 'fillcolor': 'white', 'fontcolor': 'black'},
        edge_attr={'color': 'blue', 'penwidth': '1.5'}
    )

    # 前端層子圖
    """
    前端層包含兩個主要節點：
    - UI：使用者介面、React 元件和 Webpack
    - API Client：API 客戶端、REST 請求和認證
    """
    with dot.subgraph(name='cluster_frontend') as frontend:
        frontend.attr(label='Frontend Layer', style='filled', fillcolor='lightblue', labelcolor='black')
        frontend.node('ui', r'{User Interface | React Components | Webpack}', fillcolor='skyblue')
        frontend.node('api_client', r'{API Client | REST Calls | Authentication}', fillcolor='skyblue')
        frontend.edge('ui', 'api_client', taillabel='sends requests', color='darkblue')

    # 後端層子圖
    """
    後端層包含三個主要節點：
    - API：API 網關、負載平衡和速率限制
    - Service 1：業務邏輯和資料庫存取
    - Service 2：分析和快取
    """
    with dot.subgraph(name='cluster_backend') as backend:
        backend.attr(label='Backend Layer', style='filled', fillcolor='lightgreen', labelcolor='black')
        backend.node('api', r'{API Gateway | Load Balancer | Rate Limiting}', fillcolor='limegreen')
        backend.node('service1', r'{Service 1 | Business Logic | Database Access}', fillcolor='limegreen')
        backend.node('service2', r'{Service 2 | Analytics | Caching}', fillcolor='limegreen')
        backend.edges([('api', 'service1'), ('api', 'service2')])
        backend.edge('service1', 'service2', taillabel='shares data', style='dashed', color='green')

    # 資料層子圖
    """
    資料層包含兩個主要節點：
    - Primary DB：主要資料庫、PostgreSQL 和交易
    - Cache：快取、Redis 和鍵值存儲
    """
    with dot.subgraph(name='cluster_db') as db:
        db.attr(label='Data Layer', style='filled', fillcolor='lightpink', labelcolor='black')
        db.node('db1', r'{Primary DB | PostgreSQL | Transactions}', shape='cylinder', fillcolor='salmon')
        db.node('db2', r'{Cache | Redis | Key-Value Store}', shape='cylinder', fillcolor='salmon')
        db.edge('db1', 'db2', taillabel='syncs', color='red')

    # 跨層邊
    """
    添加跨層的邊來表示不同層之間的互動：
    - API 客戶端到 API：HTTP 請求
    - Service 1 到 Primary DB：讀取/寫入
    - Service 2 到 Cache：快取
    """
    dot.edge('api_client', 'api', lhead='cluster_backend', ltail='cluster_frontend', label='HTTP requests', color='purple')
    dot.edge('service1', 'db1', lhead='cluster_db', xlabel='reads/writes', color='darkred')
    dot.edge('service2', 'db2', lhead='cluster_db', xlabel='caches', style='dotted', color='darkred')

    # 圖例
    """
    添加圖例來說明不同線型的意義：
    - 實線：直接呼叫
    - 虛線：異步資料
    - 點線：可選操作
    """
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label='Legend', rank='sink', style='filled', fillcolor='lightyellow', labelcolor='black')
        legend.node('legend_node', r'Solid: Direct Call\nDashed: Async Data\nDotted: Optional', shape='note', fillcolor='yellow', labelcolor='black')

    # 渲染並保存圖形
    dot.render(sample_dir / 'graphEx6.gv', view=True)
    print(f"Graph rendered as '{sample_dir / 'graphEx6.png'}'")

if __name__ == "__main__":
    create_software_architecture_graph()
