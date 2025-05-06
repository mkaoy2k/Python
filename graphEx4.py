'''
Graphviz supports multiple layout engines (dot, neato, fdp, sfdp, circo, twopi, patchwork) for different graph types.
	• Engines:
		○ dot: Hierarchical (default for directed graphs).
		○ neato: Spring model (force-directed).
		○ fdp: Force-directed with reduced edge crossings.
		○ sfdp: Scalable force-directed for large graphs.
		○ circo: Circular layout.
		○ twopi: Radial layout.
	• Usage: Set dot.engine = 'neato' or similar.
	• Example:
'''

from graphviz import Graph
import logging
from pathlib import Path

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

def main():
    """
    主函數，用於生成圖形檔案
    """
    try:
        # 確保 sample 目錄存在
        sample_dir = setup_sample_dir()
        
        # 創建圖形
        dot = Graph('graphEx4', format='png')
        # 設置節點
        dot.node('A')
        dot.node('B')
        dot.node('C')
        dot.edges(['AB', 'BC', 'CA'])

        layouts = ['dot', 'neato', 'fdp', 'sfdp', 'circo', 'twopi', 'patchwork']
        for layout in layouts:
            graph_name = 'graphEx4_' + layout
            print(f"使用 {layout} 布局引擎生成圖形：{graph_name}")
            dot.engine = layout

            # 生成圖形檔案
            graph_file = sample_dir / graph_name + '.gv'
            dot.render(graph_file, view=False)            
            logger.info(f"使用 {layout} 布局引擎生成圖形：{graph_file.with_suffix('.gv')} 和 {graph_file.with_suffix('.png')}")
        
    except Exception as e:
        logger.error(f"發生錯誤：{str(e)}")

if __name__ == '__main__':
    main()
