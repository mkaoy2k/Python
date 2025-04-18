"""
費氏堆（Fibonacci Heap）是一種支援高效攤還時間（amortized time）操作的堆（heap）資料結構，特點與原理如下：

1. 結構特性
    - 由多棵「樹」組成，每棵樹皆符合最小堆性質（min‐heap property）：父節點的鍵值 ≤ 子節點鍵值。
    - 所有樹的根節點串連成一個「循環雙向鏈表」（root list），可快速在根層間插入／移除節點。
    - 每個節點維護指向父、子、左兄弟、右兄弟的指標，以及「階（degree）」與「標記位（mark）」。
2. 懶惰合併與標記機制
    - 懶惰合併：插入（insert）與合併（merge）時，只將樹根加入 root list，不立即重整合併樹。
    - 標記機制：當對某節點執行 decrease_key 導致其鍵值小於父節點，會「剪下」（cut）該節點並移至 root list；若父節點已被剪過一次，則再對父節點做 cascading cut，保證樹形結構均衡。
3. 主要操作與攤還時間複雜度
    - find_min()：O(1) — 直接返回記錄的最小根節點。
    - insert(key)：O(1) — 建立新單節點樹，併入 root list。
    - merge(other_heap)：O(1) — 將兩個 root list 串聯，更新最小根。
    - decrease_key(node, new_key)：O(1) 攤還 — 若觸發剪切，會進行 cut 與 cascading cut，但整體攤還仍保持 O(1)。
    - extract_min()：O(log n) 攤還 — 移除最小根，將其所有子節點併入 root list，然後透過 consolidate（合併相同 degree 的樹）重整堆，保證樹的數量為 O(log n)。
使用情境
    費氏堆尤其適合需要大量 decrease_key 操作的演算法，如 Dijkstra 最短路徑、Prim 最小生成樹等，因其在減少鍵值時效率極高，可顯著降低演算法攤還成本。

此檔案實作費氏堆資料結構，提供以下操作：
- find_min(): O(1) 時間取得最小節點
- extract_min(): O(log n) 時間移除並回傳最小節點
- insert(key, value=None): O(1) 插入新節點
- merge(other_heap): O(1) 合併兩個堆
- decrease_key(node, new_key): O(1) 減少節點鍵值

透過懶惰合併與標記機制，實現上述攤還時間複雜度。
包含內部 Node 類別及輔助方法 (cut, cascading_cut, consolidate, heap_link 等)。
"""

import math

class FibonacciHeap:

    # 內部節點類別
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = self.child = self.left = self.right = None
            self.degree = 0
            self.mark = False

        def __repr__(self):
            """Dump the Node"""
            str_dump = f'Dump key={self.key}\n'
            str_dump += f'===>value:\t{self.value}\n'
            # str_dump += f'===>parent:\t{self.parent}\n'
            # str_dump += f'===>child:\t{self.child}\n'
            # str_dump += f'===>left:\t{self.left}\n'
            # str_dump += f'===>right:\t{self.right}\n'
            str_dump += f'===>degree:\t{self.degree}\n'
            str_dump += f'===>mark:\t{self.mark}\n'

            return str_dump

    # 以雙向鏈結串列迭代節點
    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    # 根節點串列指標與最小節點
    root_list, min_node = None, None

    # 保持費氏堆總節點數
    total_nodes = 0

    # 以 O(1) 時間回傳最小節點
    def find_min(self):
        return self.min_node

    # 以 O(log n) 時間提取（刪除）最小節點
    # 攤還成本分析請見 (http://bit.ly/1ow1Clm)
    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child is not None:
                # 將子節點附加至根節點串列
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.merge_with_root_list(children[i])
                    children[i].parent = None
            self.remove_from_root_list(z)
            # 設定新的最小節點
            if z == z.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = z.right
                self.consolidate()
            self.total_nodes -= 1
        return z

    # 以 O(1) 時間將新節點插入至無序根節點串列
    # 回傳節點以供後續 decrease_key 使用
    def insert(self, key, value=None):
        n = self.Node(key, value)
        n.left = n.right = n
        self.merge_with_root_list(n)
        if self.min_node is None or n.key < self.min_node.key:
            self.min_node = n
        self.total_nodes += 1
        return n

    # 以 O(1) 時間修改堆中節點的鍵值
    def decrease_key(self, x, k):
        if k > x.key:
            return None
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    # 以 O(1) 時間透過串聯根節點串列合併兩個費氏堆
    # 新根節點串列的根節點為第一個串列的根節點，將第二個串列附加至其後
    def merge(self, h2):
        H = FibonacciHeap()
        H.root_list, H.min_node = self.root_list, self.min_node
        # 合併兩個堆時修正指標
        last = h2.root_list.left
        h2.root_list.left = H.root_list.left
        H.root_list.left.right = h2.root_list
        H.root_list.left = last
        H.root_list.left.right = H.root_list
        # 如有需要則更新最小節點
        if h2.min_node.key < H.min_node.key:
            H.min_node = h2.min_node
        # 更新總節點數
        H.total_nodes = self.total_nodes + h2.total_nodes
        return H

    # 若子節點鍵值小於其父節點
    # 剪裁子節點並移至根節點串列
    def cut(self, x, y):
        self.remove_from_child_list(y, x)
        y.degree -= 1
        self.merge_with_root_list(x)
        x.parent = None
        x.mark = False

    # 對父節點執行階層切割以保證時間複雜度
    def cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    # 合併相同階數的根節點以鞏固堆結構
    # 建立二項樹列表
    def consolidate(self):
        A = [None] * int(math.log(self.total_nodes) * 2)
        nodes = [w for w in self.iterate(self.root_list)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.key > y.key:
                    temp = x
                    x, y = y, temp
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # 找出新的最小節點 — 無需重建根節點串列
        # 因為根節點串列在移動過程中已不斷變動
        for i in range(0, len(A)):
            if A[i] is not None:
                if A[i].key < self.min_node.key:
                    self.min_node = A[i]

    # 實際將節點鏈結為另一節點的子節點
    # 同時更新子節點串列
    def heap_link(self, y, x):
        self.remove_from_root_list(y)
        y.left = y.right = y
        self.merge_with_child_list(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False

    # 將節點加入雙向鏈結的根節點串列
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node

    # 將節點加入根節點的雙向鏈結子節點串列
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    # 從根節點串列移除節點
    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left

    # 從子節點串列移除節點
    def remove_from_child_list(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left


# 測試範例已重構為 main() 函式，啟動程式請呼叫 main()
def main():
    """範例測試 FibonacciHeap 類別的基本操作"""
    # 建立 Fibonacci 堆並插入多個元素
    heap = FibonacciHeap()
    heap.insert(10)
    heap.insert(2)
    heap.insert(15)
    heap.insert(6)

    # 取得並顯示最小值
    min_node = heap.find_min()
    print(f'最小值: {min_node}')  # 2

    # 連續移除最小節點並顯示
    removed = heap.extract_min()
    print(f'移除節點: {removed}')   # 2
    removed = heap.extract_min()
    print(f'移除節點: {removed}')   # 6

    # 建立第二個堆並插入元素
    other_heap = FibonacciHeap()
    other_heap.insert(100)
    other_heap.insert(56)

    # 合併兩個堆，並對一個節點進行減少鍵值操作
    merged_heap = heap.merge(other_heap)
    node = merged_heap.root_list.right  # 隨機取得一個節點
    merged_heap.decrease_key(node, 1)

    # 顯示合併後的根節點串列
    root_keys = [n.key for n in merged_heap.iterate(merged_heap.root_list)]
    print(f'根節點串列: {root_keys}\n')  # [10, 1, 56]

    # 再次移除最小節點並顯示
    removed = merged_heap.extract_min()
    print(f'移除節點: {removed}')  # 1

if __name__ == '__main__':
    main()
