"""
Implementin a Binary Heap using Python list.
"""
class BinaryHeap:
    def __init__(self):
        """
        Initializes an empty heap list.
        """
        self.heap = []

    def __repr__(self):
        """Dump Binary Heap"""
        str_dump = f'Dump Binary Heap={self.heap}\n'

        return str_dump
    
    def parent(self, i):
        """
        Returns the index of the parent node of the node at index `i`.
        """
        return (i - 1) // 2

    def leftChild(self, i):
        """
        Returns the index of the left child of the node at index `i`.
	    """
        return 2*i + 1

    def rightChild(self, i):
        """
        Returns the index of the right child of the node at index `i`.
        """
        return 2*i + 2

    def find_min(self):
        """
        Returns the minimum value in the heap.
        """
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def insert(self, value):
        """
        Inserts a new value into the heap and 
        maintains the heap property by calling `heapifyUp`.
        """
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def extract_min(self):
        """
        Removes and returns the minimum value in the heap and 
        maintains the heap property by calling `heapifyDown`.
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
        Maintains the heap property after adding a new value to the heap. 
        If the parent node has a value that is greater than the current node, 
        the current node is swapped with the parent node.
        And the process is repeated until the parent node is smaller than 
        the current node.
        """
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapifyDown(self, i):
        """
        Maintains the heap property after removing a value from the heap. 
        The current node is swapped with its smallest child node 
        until it is smaller than both of its children 
        or it reaches a leaf node.
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
    print('===> 10 inserted')
    H.insert(2)
    print('===> 2 inserted')
    H.insert(15)
    print('===> 15 inserted')
    H.insert(6)
    print('===> 6 inserted')

    m = H.find_min()
    print('Find min of 2 expected')
    print(f'{m} from {H}')  # 2

    q = H.extract_min()
    print('Extract min of 2 expected')
    print(f'{q} from {H}')   # 2

    q = H.extract_min()
    print('Extract min of 6 expected')
    print(f'{q} from {H}')   # 6


