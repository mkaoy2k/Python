"""
流程圖和記錄節點視覺化範例

此程式使用 Graphviz 創建兩個視覺化範例：
1. 流程圖：展示如何使用不同的節點形狀和樣式來表示不同的流程元素
   - 菱形表示開始/結束
   - 矩形表示過程
   - 圓形表示結束
   - 不同顏色和樣式來區分節點
   - 添加邊的標籤和樣式

2. 記錄節點：展示如何使用 record 節點形狀來表示結構化數據
   - 使用欄位分隔符來組織數據
   - 顯示多個記錄節點的關係
"""

from graphviz import Digraph
import logging
from pathlib import Path

# 設置日誌
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

def create_flowchart():
    """
    創建流程圖
    """
    dot = Digraph('graphEx3', format='png')
    
    # 設置節點
    dot.node('A', 'Start', shape='diamond', style='filled', fillcolor='green', fontcolor='black')
    dot.node('B', 'Process', shape='box', style='rounded,filled', fillcolor='lightblue', fontcolor='black')
    dot.node('C', 'End', shape='circle', style='filled', fillcolor='red')
    
    # 設置邊
    dot.edge('A', 'B', taillabel='步驟 1', color='purple', style='dashed', penwidth='2')
    dot.edge('B', 'C', taillabel='完成', color='black', arrowhead='vee')
    
    # 建立具有欄位的記錄節點
    dot.node('struct', shape='record', label='ID|名稱|類型')
    dot.node('struct1', shape='record', label='1|Alice|人')
    dot.node('struct2', shape='record', label='2|Bob|人')
    
    # 設置邊
    dot.edge('struct', 'struct1', xlabel='p1')
    dot.edge('struct', 'struct2', taillabel='p2')
    


    return dot

def main():
    """
    主函數，用於生成流程圖檔案
    """
    try:
        # 創建流程圖
        dot = create_flowchart()
        
        # 確保 sample 目錄存在
        sample_dir = Path(__file__).parent / 'sample'
        sample_dir.mkdir(exist_ok=True)
        
        # 生成圖形檔案
        graph_file = sample_dir / 'graphEx3.gv'
        dot.render(graph_file, view=True)
        
        logger.info(f"圖形已生成：{graph_file.with_suffix('.gv')} 和 {graph_file.with_suffix('.png')}")
        
    except Exception as e:
        logger.error(f"發生錯誤：{str(e)}")

if __name__ == "__main__":
    main()