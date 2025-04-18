"""
二元堆（Binary Heap）的概念與操作：

什麼是二元堆？
    二元堆是一種完全二元樹（Complete Binary Tree），所有層都被填滿，最後一層從左至右依序填入節點。
    可分「最小堆」（Min‑Heap）與「最大堆」（Max‑Heap）：
        最小堆：每個父節點的值 ≤ 其左右子節點的值 → 根節點為最小值
        最大堆：每個父節點的值 ≥ 其左右子節點的值 → 根節點為最大值
陣列實作
    使用 Python list（一維陣列）儲存樹節點，從索引 0 開始：
        節點 i 的父索引：parent = (i - 1) // 2
        左子索引：left = 2*i + 1
        右子索引：right = 2*i + 2
核心操作
    1. insert(value)
        先將新元素 append 到陣列尾，
        再呼叫 heapifyUp：若該節點小於（最大堆則大於）父節點，則「上浮」交換，直到結構合法。
    2. find_min() / find_max()
        直接回傳陣列第 0 處（根節點）的值。
    3. extract_min() / extract_max()
        - 取出根節點值作為結果，
        - 用最後一個元素填補根節點，並 pop 掛尾端，
        - 呼叫 heapifyDown：若根節點比子節點「更大」（最小堆）或「更小」（最大堆），則與較小／大的子節點交換，重複直到合法。
時間複雜度
    - insert：O(log n)
    - extract_min/extract_max：O(log n)
    - find_min/find_max：O(1)
應用場景
    - 優先佇列（Priority Queue）
    - 排序演算法：Heap Sort
    - 線上演算法中維持動態最小／最大值
透過二元堆，你可以在對大資料流進行插入與取出最值時，保有對數級的效率
    - 適合需要動態維護極值的場合
實作二元最小堆（Binary Heap）
    使用 Python list 作為底層資料結構。
提供以下操作：
- insert：插入新元素，並透過 heapifyUp 維持最小堆性質。
- find_min：查詢最小值。
- extract_min：移除並回傳最小值，並透過 heapifyDown 調整堆結構。
- parent、leftChild、rightChild：取得父節點及左右子節點索引。
- __repr__：輸出目前堆內容。
"""
class BinaryHeap:
    def __init__(self):
        """
        初始化空的堆列表。
        """
        self.heap = []

    def __repr__(self):
        """輸出堆內容"""
        str_dump = f'堆內容={self.heap}\n'

        return str_dump
    
    def parent(self, i):
        """
        回傳父節點索引。
        """
        return (i - 1) // 2

    def leftChild(self, i):
        """
        回傳左子節點索引。
	    """
        return 2*i + 1

    def rightChild(self, i):
        """
        回傳右子節點索引。
        """
        return 2*i + 2

    def find_min(self):
        """
        回傳堆中最小值。
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, value):
        """
        插入新元素，並透過 heapifyUp 維持最小堆性質。
        """
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def extract_min(self):
        """
        移除並回傳最小值，並透過 heapifyDown 調整堆結構。
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return min_value

    def heapifyUp(self, i):
        """
        維持最小堆性質，當父節點值大於當前節點值時，進行交換。
        """
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapifyDown(self, i):
        """
        維持最小堆性質，當前節點值大於子節點值時，進行交換。
        """
        while self.leftChild(i) < len(self.heap):
            min_child = self.leftChild(i)
            if self.rightChild(i) < len(self.heap) and self.heap[self.rightChild(i)] < self.heap[min_child]:
                min_child = self.rightChild(i)
            if self.heap[i] <= self.heap[min_child]:
                break
            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
# Functional Test
if __name__ == '__main__':
    H = BinaryHeap()

    H.insert(10)
    print('===> 10 插入')
    H.insert(2)
    print('===> 2 插入')
    H.insert(15)
    print('===> 15 插入')
    H.insert(6)
    print('===> 6 插入')

    m = H.find_min()
    print('查詢最小值，預期 2')
    print(f'{m} from {H}')  # 2

    q = H.extract_min()
    print('移除最小值，預期 2')
    print(f'{q} from {H}')   # 2

    q = H.extract_min()
    print('移除最小值，預期 6')
    print(f'{q} from {H}')   # 6
