"""
This implementation consists of two classes, `Node` and `BinomialHeap`.
Each `Node` contains a key value and pointers to its parent and children nodes. The `BinomialHeap` class is implemented with a list `trees` which contains the individual trees that make up the heap.

This implementation can be improved for efficiency, but it should provide 
a basic understanding of how a binomial heap works in Python.
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []

    def __repr__(self):
        """Dump Binomial Node"""
        str_dump = f'Dump Node key={self.key}\n'
        str_dump += f'===> parent={self.parent}\n'

        return str_dump
class BinomialHeap:
    def __init__(self):
        self.trees = []
    
    def find_min(self):
        """
        The `find_min` method 
        returns the minimum key node in the heap.
        """
        if not self.trees:
            return None
        min_node = min(self.trees, key=lambda x: x.key)
        return min_node

    def insert(self, key):
        """
        The `insert` method 
        creates a new node, 
        adds it to a new heap, and 
        merges the new heap with the existing heap.
        """
        new_node = Node(key)
        new_heap = BinomialHeap()
        new_heap.trees.append(new_node)
        self.merge(new_heap)
    
    def extract_min(self):
        """
        The `extract_min` method 
        removes the minimum key node from the heap, 
        sets its children to a new heap, 
        merges the new heap with the existing heap,
        return the minimum key node.
        """
        if not self.trees:
            return None
        min_node = min(self.trees, key=lambda x: x.key)
        
        self.trees.remove(min_node)
        new_heap = BinomialHeap()
        new_heap.trees = min_node.children[:]
        self.merge(new_heap)
        return min_node
    
    def merge(self, other_heap):
        """
        The `merge` method 
        merges two heaps by concatenating their tree lists and 
        sorting the list by the number of children in each tree. 
        This ensures that trees of the same order are combined correctly.
        """
        self.trees += other_heap.trees
        self.trees.sort(key=lambda x: len(x.children))
        self.combine_trees()
    
    def combine_trees(self):
        """
        The `combine_trees` method 
        iterates over the sorted list of trees and 
        combines trees of equal order by making one tree the child of the other.
        """
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
# Functional Test
if __name__ == '__main__':
    H = BinomialHeap()

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
    print(f'{m}')  # 2

    q = H.extract_min()
    print('Extract min of 2 expected')
    print(f'{q}')   # 2

    q = H.extract_min()
    print('Extract min of 6 expected')
    print(f'{q}')   # 6

