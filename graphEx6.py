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
    
    回傳:
        Graphviz Digraph 物件
    """
    # 初始化有向圖，設置全局屬性
    dot = Digraph(
        name='software_architecture',
        format='png',
        graph_attr={
            'rankdir': 'TB',
            'splines': 'ortho',
            'bgcolor': 'lightgrey',
            'fontcolor': 'black',
            'fontsize': '12',
            'style': 'filled',
            'compound': 'true'
        },
        node_attr={'shape': 'record', 'style': 'filled', 'fillcolor': 'white', 'fontcolor': 'black'},
        edge_attr={'color': 'blue', 'penwidth': '1.5'}
    )

    # 前端層子圖
    with dot.subgraph(name='cluster_frontend') as frontend:
        frontend.attr(label='Frontend Layer', style='filled', fillcolor='lightblue', labelcolor='black')
        frontend.node('ui', r'{User Interface | React Components | Webpack}', fillcolor='skyblue')
        frontend.node('api_client', r'{API Client | REST Calls | Authentication}', fillcolor='skyblue')
        frontend.edge('ui', 'api_client', taillabel='sends requests', color='darkblue')

    # 後端層子圖
    with dot.subgraph(name='cluster_backend') as backend:
        backend.attr(label='Backend Layer', style='filled', fillcolor='lightgreen', labelcolor='black')
        backend.node('api', r'{API Gateway | Load Balancer | Rate Limiting}', fillcolor='limegreen')
        backend.node('service1', r'{Service 1 | Business Logic | Database Access}', fillcolor='limegreen')
        backend.node('service2', r'{Service 2 | Analytics | Caching}', fillcolor='limegreen')
        backend.edges([('api', 'service1'), ('api', 'service2')])
        backend.edge('service1', 'service2', taillabel='shares data', style='dashed', color='green')

    # 資料層子圖
    with dot.subgraph(name='cluster_db') as db:
        db.attr(label='Data Layer', style='filled', fillcolor='lightpink', labelcolor='black')
        db.node('db1', r'{Primary DB | PostgreSQL | Transactions}', shape='cylinder', fillcolor='salmon')
        db.node('db2', r'{Cache | Redis | Key-Value Store}', shape='cylinder', fillcolor='salmon')
        db.edge('db1', 'db2', taillabel='syncs', color='red')

    # 跨層邊
    dot.edge('api_client', 'api', lhead='cluster_backend', ltail='cluster_frontend', label='HTTP requests', color='purple')
    dot.edge('service1', 'db1', lhead='cluster_db', xlabel='reads/writes', color='darkred')
    dot.edge('service2', 'db2', lhead='cluster_db', xlabel='caches', style='dotted', color='darkred')

    # 圖例
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label='Legend', rank='sink', style='filled', fillcolor='lightyellow', labelcolor='black')
        legend.node('legend_node', r'Solid: Direct Call\nDashed: Async Data\nDotted: Optional', shape='note', fillcolor='yellow', labelcolor='black')

    return dot

def main():
    """
    主函數：處理檔案路徑和圖形渲染
    """
    try:
        # 創建圖形
        graph = create_software_architecture_graph()
        
        # 獲取腳本目錄並創建 sample 目錄
        script_dir = Path(__file__).parent
        sample_dir = script_dir / 'sample'
        sample_dir.mkdir(exist_ok=True)
        
        # 渲染並保存圖形
        output_file = sample_dir / 'graphEx6.gv'
        graph.render(str(output_file), view=True)
        print(f"Graph rendered as '{output_file.with_suffix('.png')}'")
        
    except Exception as e:
        print(f"發生錯誤：{str(e)}")
        raise

if __name__ == "__main__":
    main()
