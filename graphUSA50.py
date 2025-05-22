"""
模組：美國50州相鄰關係圖生成器

概述：
這個模組使用 Graphviz 生成美國50個州的相鄰關係圖，展示各州之間的地理鄰近關係。

主要功能：
1. 地理區域劃分：
   - 東北 (Northeast)
   - 東南 (Southeast)
   - 中西部 (Midwest)
   - 西南 (Southwest)
   - 西部 (West)
   - 山區 (Mountain)

2. 節點信息：
   - 州名稱
   - 首府名稱
   - 所屬區域
   - 相鄰州份

3. 圖形特徵：
   - 由上到下佈局（rankdir='TB'）
   - 漸變背景色（lightblue:lightyellow）
   - 一致的字體大小和樣式
   - 清晰的邊緣標籤
   - 固定位置的圖例

4. 視覺優化：
   - 適當的節點間隔
   - 合理的圖形大小
   - 統一的節點形狀
   - 良好的邊緣路徑

使用方法：
調用 create_us_states_graph() 函數即可生成並保存圖形。

輸出：
生成 PNG 圖片文件，展示美國50個州的相鄰關係圖。
"""

from graphviz import Graph
from pathlib import Path

def create_us_states_graph():
    """
    創建美國50州相鄰關係圖形
    
    回傳:
        Graphviz Graph 物件
    """
    # 初始化無向圖，使用 neato 引擎
    dot = Graph(
        name='us_states',
        format='png',
        engine='neato',
        graph_attr={
            'rankdir': 'TB',  # 由上到下佈局
            'splines': 'polyline',  # 使用 polyline 以獲得更好的邊緣路徑
            'bgcolor': 'lightblue:lightyellow',  # 渐变背景
            'fontsize': '20',
            'style': 'filled',
            'label': 'US States Adjacency Graph\n(All 50 States)',
            'overlap': 'false',
            'sep': '1.0',  # 增加節點間隔
            'nodesep': '2.0',  # 增加同一層節點間隔
            'ranksep': '1.0',  # 增加不同層節點間隔
            'size': '15,25',  # 增加圖形大小
            'ratio': 'fill',  # 填充整個圖形區域
            'margin': '0.5',  # 增加邊緣間距
            'pad': '1.5',  # 增加圖形周圍的填充
            'esep': '1.5',  # 增加邊緣間隔
            'concentrate': 'true',  # 自動聚合邊緣
            'pack': 'true',  # 確保子圖之間的間隔
            'packmode': 'array',  # 使用 array 模式排列子圖
        },
        node_attr={
            'shape': 'ellipse',
            'style': 'filled',
            'fillcolor': 'white',
            'fontcolor': 'black',
            'fontsize': '20',
            'fontname': 'Arial',
            'penwidth': '1.2',
            'width': '1.5',
            'height': '0.8'
        },
        edge_attr={'color': 'darkgreen', 
                   'penwidth': '1.2', 
                   'arrowsize': '0.8', 
                   'fontsize': '20', 
                   'fontname': 'Arial', 
                   'fontcolor': 'black'}
    )

    # 所有50個州的數據，包括首府和鄰近州
    states_data = {
        # 西部
        'California': {'capital': 'Sacramento', 'region': 'West', 'neighbors': ['Oregon', 'Nevada', 'Arizona'], 'pos': '1,1'},
        'Oregon': {'capital': 'Salem', 'region': 'West', 'neighbors': ['California', 'Nevada', 'Idaho', 'Washington'], 'pos': '1,2'},
        'Washington': {'capital': 'Olympia', 'region': 'West', 'neighbors': ['Oregon', 'Idaho'], 'pos': '1,3'},
        'Idaho': {'capital': 'Boise', 'region': 'West', 'neighbors': ['Washington', 'Oregon', 'Nevada', 'Utah', 'Wyoming', 'Montana'], 'pos': '2,2'},
        'Utah': {'capital': 'Salt Lake City', 'region': 'West', 'neighbors': ['Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Nevada'], 'pos': '2,3'},
        
        # 山區
        'Montana': {'capital': 'Helena', 'region': 'Mountain', 'neighbors': ['Idaho', 'Wyoming', 'South Dakota', 'North Dakota'], 'pos': '2,4'},
        'Wyoming': {'capital': 'Cheyenne', 'region': 'Mountain', 'neighbors': ['Montana', 'South Dakota', 'Nebraska', 'Colorado', 'Utah', 'Idaho'], 'pos': '2,5'},
        'Colorado': {'capital': 'Denver', 'region': 'Mountain', 'neighbors': ['Wyoming', 'Nebraska', 'Kansas', 'Oklahoma', 'New Mexico', 'Utah'], 'pos': '2,6'},
        'Nebraska': {'capital': 'Lincoln', 'region': 'Mountain', 'neighbors': ['South Dakota', 'Iowa', 'Missouri', 'Kansas', 'Colorado', 'Wyoming'], 'pos': '3,7'},
        'Kansas': {'capital': 'Topeka', 'region': 'Mountain', 'neighbors': ['Nebraska', 'Missouri', 'Oklahoma', 'Colorado'], 'pos': '3,6'},
        
        # 西南
        'Arizona': {'capital': 'Phoenix', 'region': 'Southwest', 'neighbors': ['California', 'Nevada', 'Utah', 'Colorado', 'New Mexico'], 'pos': '3,3'},
        'New Mexico': {'capital': 'Santa Fe', 'region': 'Southwest', 'neighbors': ['Arizona', 'Utah', 'Colorado', 'Oklahoma', 'Texas'], 'pos': '3,4'},
        'Texas': {'capital': 'Austin', 'region': 'Southwest', 'neighbors': ['New Mexico', 'Oklahoma', 'Arkansas', 'Louisiana'], 'pos': '3,5'},
        'Nevada': {'capital': 'Carson City', 'region': 'Southwest', 'neighbors': ['Arizona', 'Utah', 'Idaho', 'Oregon', 'California'], 'pos': '3,2'},
        
        # 中西部
        'North Dakota': {'capital': 'Bismarck', 'region': 'Midwest', 'neighbors': ['Montana', 'South Dakota', 'Minnesota'], 'pos': '4,4'},
        'South Dakota': {'capital': 'Pierre', 'region': 'Midwest', 'neighbors': ['North Dakota', 'Montana', 'Wyoming', 'Nebraska', 'Iowa', 'Minnesota'], 'pos': '4,5'},
        'Iowa': {'capital': 'Des Moines', 'region': 'Midwest', 'neighbors': ['South Dakota', 'Nebraska', 'Missouri', 'Illinois', 'Wisconsin', 'Minnesota'], 'pos': '4,6'},
        'Minnesota': {'capital': 'Saint Paul', 'region': 'Midwest', 'neighbors': ['North Dakota', 'South Dakota', 'Iowa', 'Wisconsin'], 'pos': '4,7'},
        'Wisconsin': {'capital': 'Madison', 'region': 'Midwest', 'neighbors': ['Minnesota', 'Iowa', 'Illinois', 'Michigan'], 'pos': '4,8'},
        'Michigan': {'capital': 'Lansing', 'region': 'Midwest', 'neighbors': ['Wisconsin', 'Illinois', 'Indiana', 'Ohio'], 'pos': '4,9'},
        'Illinois': {'capital': 'Springfield', 'region': 'Midwest', 'neighbors': ['Wisconsin', 'Iowa', 'Missouri', 'Kentucky', 'Indiana'], 'pos': '4,10'},
        'Indiana': {'capital': 'Indianapolis', 'region': 'Midwest', 'neighbors': ['Michigan', 'Illinois', 'Kentucky', 'Ohio'], 'pos': '4,11'},
        'Ohio': {'capital': 'Columbus', 'region': 'Midwest', 'neighbors': ['Michigan', 'Indiana', 'Kentucky', 'West Virginia', 'Pennsylvania'], 'pos': '4,12'},
        
        # 東北
        'Maine': {'capital': 'Augusta', 'region': 'Northeast', 'neighbors': ['New Hampshire'], 'pos': '5,12'},
        'New Hampshire': {'capital': 'Concord', 'region': 'Northeast', 'neighbors': ['Maine', 'Vermont', 'Massachusetts'], 'pos': '5,11'},
        'Vermont': {'capital': 'Montpelier', 'region': 'Northeast', 'neighbors': ['New Hampshire', 'Massachusetts', 'New York'], 'pos': '5,10'},
        'Massachusetts': {'capital': 'Boston', 'region': 'Northeast', 'neighbors': ['New Hampshire', 'Vermont', 'Rhode Island', 'Connecticut', 'New York'], 'pos': '5,9'},
        'Rhode Island': {'capital': 'Providence', 'region': 'Northeast', 'neighbors': ['Massachusetts', 'Connecticut'], 'pos': '5,8'},
        'Connecticut': {'capital': 'Hartford', 'region': 'Northeast', 'neighbors': ['Massachusetts', 'Rhode Island', 'New York'], 'pos': '5,7'},
        'New York': {'capital': 'Albany', 'region': 'Northeast', 'neighbors': ['Vermont', 'Massachusetts', 'Connecticut', 'Pennsylvania', 'New Jersey'], 'pos': '5,6'},
        'Pennsylvania': {'capital': 'Harrisburg', 'region': 'Northeast', 'neighbors': ['New York', 'New Jersey', 'Delaware', 'Maryland', 'West Virginia', 'Ohio'], 'pos': '5,5'},
        'New Jersey': {'capital': 'Trenton', 'region': 'Northeast', 'neighbors': ['New York', 'Pennsylvania', 'Delaware'], 'pos': '5,4'},
        'Delaware': {'capital': 'Dover', 'region': 'Northeast', 'neighbors': ['New Jersey', 'Pennsylvania', 'Maryland'], 'pos': '5,3'},
        'Maryland': {'capital': 'Annapolis', 'region': 'Northeast', 'neighbors': ['Delaware', 'Pennsylvania', 'West Virginia', 'Virginia'], 'pos': '5,2'},
        'West Virginia': {'capital': 'Charleston', 'region': 'Northeast', 'neighbors': ['Ohio', 'Pennsylvania', 'Maryland', 'Virginia', 'Kentucky'], 'pos': '5,1'},
        
        # 東南
        'Virginia': {'capital': 'Richmond', 'region': 'Southeast', 'neighbors': ['West Virginia', 'Maryland', 'North Carolina', 'Kentucky', 'Tennessee'], 'pos': '6,1'},
        'North Carolina': {'capital': 'Raleigh', 'region': 'Southeast', 'neighbors': ['Virginia', 'Tennessee', 'Georgia', 'South Carolina'], 'pos': '6,2'},
        'South Carolina': {'capital': 'Columbia', 'region': 'Southeast', 'neighbors': ['North Carolina', 'Georgia'], 'pos': '6,3'},
        'Georgia': {'capital': 'Atlanta', 'region': 'Southeast', 'neighbors': ['South Carolina', 'North Carolina', 'Tennessee', 'Alabama', 'Florida'], 'pos': '6,4'},
        'Florida': {'capital': 'Tallahassee', 'region': 'Southeast', 'neighbors': ['Georgia', 'Alabama'], 'pos': '6,5'},
        'Alabama': {'capital': 'Montgomery', 'region': 'Southeast', 'neighbors': ['Florida', 'Georgia', 'Tennessee', 'Mississippi'], 'pos': '6,6'},
        'Mississippi': {'capital': 'Jackson', 'region': 'Southeast', 'neighbors': ['Alabama', 'Tennessee', 'Arkansas', 'Louisiana'], 'pos': '6,7'},
        'Louisiana': {'capital': 'Baton Rouge', 'region': 'Southeast', 'neighbors': ['Mississippi', 'Arkansas', 'Texas'], 'pos': '6,8'},
        'Kentucky': {'capital': 'Frankfort', 'region': 'Northeast', 'neighbors': ['Ohio', 'Indiana', 'Illinois', 'Tennessee', 'Virginia', 'West Virginia'], 'pos': '5,0'},
        'Oklahoma': {'capital': 'Oklahoma City', 'region': 'Southwest', 'neighbors': ['Texas', 'New Mexico', 'Colorado', 'Kansas', 'Arkansas', 'Missouri'], 'pos': '3,7'},
        'Arkansas': {'capital': 'Little Rock', 'region': 'Southeast', 'neighbors': ['Missouri', 'Tennessee', 'Mississippi', 'Louisiana', 'Texas', 'Oklahoma'], 'pos': '6,9'},
        'Missouri': {'capital': 'Jefferson City', 'region': 'Midwest', 'neighbors': ['Iowa', 'Illinois', 'Kentucky', 'Tennessee', 'Arkansas', 'Oklahoma', 'Kansas', 'Nebraska'], 'pos': '4,8'},
        'Tennessee': {'capital': 'Nashville', 'region': 'Southeast', 'neighbors': ['Kentucky', 'Virginia', 'North Carolina', 'Georgia', 'Alabama', 'Mississippi', 'Arkansas', 'Missouri'], 'pos': '6,10'}
    }

    # 創建不同區域的子圖
    regions = {
        'Northeast': 'lightcyan',
        'Southeast': 'lightblue',
        'Midwest': 'lightgreen',
        'Southwest': 'lightyellow',
        'West': 'lightgoldenrod',
        'Mountain': 'lightpink'
    }

    # 創建每個區域的子圖
    for region, color in regions.items():
        with dot.subgraph(name=f'cluster_{region.lower()}') as cluster:
            cluster.attr(
                label=region + ' 區域',
                style='filled',
                fillcolor=color,
                penwidth='2.0',
                fontsize='28',
                labelloc='l',  # 將標籤放在左上角
                fontname='Arial',
                fontcolor='black',
                margin='20',  # 增加邊緣間距
                nodesep='1.5',  # 增加節點間隔
                ranksep='1.5',  # 增加層次間隔
                size='10,10',  # 設定區域大小
                fixedsize='true'  # 確保大小固定
            )
            for state, data in states_data.items():
                if data['region'] == region:
                    cluster.node(state, f"{state}\n{data['capital']}", fillcolor='white', pos=data['pos'], fontsize='28', fontname='Arial', fontcolor='black')

    # 添加邊緣
    added_edges = set()
    for state, data in states_data.items():
        for neighbor in data['neighbors']:
            if (state, neighbor) not in added_edges and (neighbor, state) not in added_edges:
                dot.edge(state, neighbor, label='相鄰', fontsize='28', fontname='Arial', fontcolor='black')
                added_edges.add((state, neighbor))

    # 添加圖例子圖
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(
            label='圖例',
            rank='source',  # 將圖例放在最上方
            style='filled',
            fillcolor='lightyellow',
            penwidth='2.0',
            fontsize='12',
            fontname='Arial',
            fontcolor='black',
            pos='0,0!',  # 固定位置在左上角
            width='2',  # 調整寬度
            height='1',  # 調整高度
            fixedsize='true',  # 固定大小
            margin='0',  # 減少邊距
            labeljust='l'  # 標籤靠左對齊
        )
        legend.node('legend_node', '邊緣: 州之間的相鄰關係', shape='note', fillcolor='yellow', fontsize='28', fontname='Arial', fontcolor='black')

    return dot

def main():
    """
    主函數：處理檔案路徑和圖形渲染
    """
    try:
        # 創建圖形
        graph = create_us_states_graph()
        
        # 獲取當前檔案所在的目錄
        current_dir = Path(__file__).parent
        sample_dir = current_dir / 'sample'
        
        # 如果不存在，則創建 sample 目錄
        sample_dir.mkdir(exist_ok=True)
        
        # 保存圖形
        output_file = sample_dir / 'graphUSA50.gv'
        graph.render(str(output_file), view=True)
        print(f"圖形已生成為 '{output_file.with_suffix('.png')}'")
        
    except Exception as e:
        print(f"發生錯誤：{str(e)}")
        raise

if __name__ == "__main__":
    main()
