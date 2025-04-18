"""
BinomialHeap（二項堆）的核心概念與此實作方式：

二項堆的概念
    - 由多棵「二項樹」（Binomial Tree）組成，每棵樹的階（degree）即節點子樹數量。
    - 不同階的樹最多各一棵，組合起來就能代表任意數量的節點。
    - 支援常見堆操作：插入（insert）、尋找最小值（find_min）、合併（merge）、移除最小值（extract_min），時間複雜度多為 O(log n)。
此實作結構
    1. Node 類別
        - 屬性：
            - key：儲存節點鍵值。
            - parent：指向父節點。
            - children：子節點列表，長度即此樹的階。
        - 方法：
            - repr：輸出節點鍵值與父節點資訊，方便除錯。
2. BinomialHeap 類別
    - 屬性：
        - trees：一個根節點列表，存放各階的二項樹根。
    - 方法：
        - find_min()：掃描 trees 找出鍵值最小的根節點並回傳。
        - insert(key)：
            - 建立單一節點的新堆（階為 0）。
            - 與原堆呼叫 merge 合併。
        - merge(other_heap)：
            - 將兩堆的根列表串接後依「樹階」（即子節點數）排序。
            - 呼叫 combine_trees，將相同階的樹合併成更高階的樹。
        - combine_trees()：
            - 依序檢查排序後的根列表，若遇到連續兩棵同階的樹，將鍵值較大的作為鍵值較小者的子樹，階數＋1；重複直到沒有相同階的樹為止。
        - extract_min()：
            - 找出並移除根列表中的最小鍵節點。
            - 將該節點的子樹（children）反向視作新堆，與剩餘的根列表呼叫 merge。
            - 回傳該最小節點。
特點與效能
    - 插入與移除最小值皆可在 O(log n) 時間內完成，合併則最優僅需 O(1)（只調整指標），實作上採排序＋合併策略故約 O(log n)。
    - 資料結構對於大量合併操作特別友善，適用於需要頻繁合併的場景（例如多路佇列合併）。
實作
    - 由兩個類別 Node 與 BinomialHeap 組成。
    - Node 物件包含鍵值、父節點指標與子節點列表。
    - BinomialHeap 類別使用 trees 列表儲存多個二項樹。

此實作示範二項堆的基本操作：尋找最小值、插入、合併、提取最小值等。
可進一步優化效能，但目前實作足以理解其核心機制。
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def __repr__(self):
        """輸出節點資訊：鍵值與父節點"""
        str_dump = f'Dump Node key={self.key}\n'
        str_dump += f'===> parent={self.parent}\n'

        return str_dump
class BinomialHeap:
    def __init__(self):
        self.trees = []
    
    def find_min(self):
        """尋找並回傳堆中鍵值最小的節點"""
        if not self.trees:
            return None
        min_node = min(self.trees, key=lambda x: x.key)
        return min_node

    def insert(self, key):
        """插入新鍵，建立新堆並與現有堆合併"""
        new_node = Node(key)
        new_heap = BinomialHeap()
        new_heap.trees.append(new_node)
        self.merge(new_heap)
    
    def extract_min(self):
        """移除並回傳堆中鍵值最小的節點，將其子節點重建為新堆後與當前堆合併"""
        if not self.trees:
            return None
        min_node = min(self.trees, key=lambda x: x.key)
        
        self.trees.remove(min_node)
        new_heap = BinomialHeap()
        new_heap.trees = min_node.children[:]
        self.merge(new_heap)
        return min_node
    
    def merge(self, other_heap):
        """合併兩個二項堆，將樹列表合併後依樹階排序，確保相同階數的樹能正確合併"""
        self.trees += other_heap.trees
        self.trees.sort(key=lambda x: len(x.children))
        self.combine_trees()
    
    def combine_trees(self):
        """遍歷已排序的樹列表，將相同階數的樹合併，讓較大鍵的樹成為較小鍵樹的子節點"""
        if not self.trees:
            return
        combined = [self.trees.pop(0)]
        for tree in self.trees:
            if tree.key < combined[-1].key:
                combined.append(tree)
            else:
                combined[-1].children.append(tree)
                tree.parent = combined[-1]
        self.trees = combined[:]

def main():
    """測試 BinomialHeap 的基本操作：插入、尋找最小值與提取最小值"""
    H = BinomialHeap()
    # 插入測試
    H.insert(10)
    print('===> 10 inserted')
    H.insert(2)
    print('===> 2 inserted')
    H.insert(15)
    print('===> 15 inserted')
    H.insert(6)
    print('===> 6 inserted')

    # 尋找最小值
    m = H.find_min()
    print('Find min of 2 expected')
    print(f'{m}')

    # 提取最小值
    q = H.extract_min()
    print('Extract min of 2 expected')
    print(f'{q}')
    q = H.extract_min()
    print('Extract min of 6 expected')
    print(f'{q}')

if __name__ == '__main__':
    main()
