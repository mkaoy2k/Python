"""
雙集群圖和 HTML 表格節點視覺化範例

此程式使用 Graphviz 創建一個包含兩個主要部分的視覺化範例：
1. 雙集群圖：展示如何使用 subgraph 來組織節點和邊
   - Cluster 1: 包含節點 A 和 B
   - Cluster 2: 包含節點 C 和 D
   - 連接兩個集群的邊

2. HTML 表格節點：展示如何使用 HTML 標籤來創建複雜的節點
   - 使用 TABLE 標籤來組織數據
   - 包含標題行和多個數據行
   - 使用 CSS 樣式來格式化表格
"""

from graphviz import Digraph
from pathlib import Path
import logging

# 設置日誌
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

def setup_sample_dir():
    """
    確保 sample 目錄存在，用於儲存生成的圖形檔案
    """
    sample_dir = Path(__file__).parent / 'sample'
    sample_dir.mkdir(exist_ok=True)
    return sample_dir

def create_subgraph(dot):
    """
    創建包含兩個集群的有向圖形
    """

    # Cluster 1
    with dot.subgraph(name='cluster_1') as c1:
        c1.attr(label='Cluster 1', style='filled', fillcolor='lightgrey')
        c1.node('A', 'Node A')
        c1.node('B', 'Node B')
        c1.edges(['AB'])

    # Cluster 2
    with dot.subgraph(name='cluster_2') as c2:
        c2.attr(label='Cluster 2', color='blue')
        c2.node('C', '節點 C')
        c2.node('D', '節點 D')
        c2.edges(['CD'])

    # 連接集群
    dot.edge('B', 'C')
    
    # HTML 節點
    dot.node('E', label='''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR>
                <TD COLSPAN="2"><B>標題</B></TD>
            </TR>
            <TR>
                <TD>欄位 1</TD>
                <TD>欄位 2</TD>
            </TR>
        </TABLE>
    >''')
    dot.node('F', label='''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR>
                <TD COLSPAN="1"><B>標題</B></TD>
            </TR>
            <TR>
                <TD>行 1</TD>
            </TR>
            <TR>
                <TD>行 2</TD>
            </TR>
        </TABLE>
    >''')
    dot.edge('E', 'F')
 
    return dot

def main():
    """
    主函數，用於生成圖形檔案
    """
    try:
        # 確保 sample 目錄存在
        sample_dir = setup_sample_dir()
        
        # 創建圖形
        dot = Digraph('graphEx2', format='png')
        dot = create_subgraph(dot)
        
        # 生成圖形檔案
        graph_file = sample_dir / 'graphEx2.gv'
        dot.render(graph_file, view=False)
        
        logger.info(f"圖形已生成：{graph_file.with_suffix('.gv')} 和 {graph_file.with_suffix('.png')}")
        
    except Exception as e:
        logger.error(f"發生錯誤：{str(e)}")

if __name__ == "__main__":
    main()