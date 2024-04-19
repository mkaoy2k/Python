""" 
This implementation defines two classes: Node and BinarySearchTree. 
Node represents a node in the binary search tree, 
    with a value and pointers to its left and right children. 

BinarySearchTree represents the binary search tree itself,
    with a pointer to the root node, and 2 methods which are:
    to insert new nodes and search for nodes with a given value.
"""
import random
import traceback
import glog as log


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ Three common traversal orders for a binary search tree:
    **inorder**, **preorder**, and **postorder**.
    Inorder traversal
        involves visiting the left subtree, then the root,
        and finally the right subtree.
        This traversal gives nodes in non-decreasing order.
    Preorder traversal
        involves visiting the root first, then the left subtree,
        and finally the right subtree.
    Postorder traversal
        involves visiting the left subtree first, then the right subtree,
        and finally the root.
    """

    def print_keys_inorder(self):

        log.debug(
            f'{get_function_name()}: {self.value}')

        if self.left is not None:
            self.left.print_keys_inorder()

        print(self.value, end=' ')

        if self.right is not None:
            self.right.print_keys_inorder()

    def print_keys_postorder(self):

        log.debug(
            f'{get_function_name()}: {self.value}')

        if self.left is not None:
            self.left.print_keys_postorder()

        if self.right is not None:
            self.right.print_keys_postorder()

        print(self.value, end=' ')

    def print_keys_preorder(self):

        log.debug(
            f'{get_function_name()}: {self.value}')

        print(self.value, end=' ')

        if self.left is not None:
            self.left.print_keys_preorder()

        if self.right is not None:
            self.right.print_keys_preorder()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    """ There are two methods implemented with this class.
    1. insert method
        takes a value and creates a new node with that value.
        If the tree is empty (i.e., the root node is None),
        the new node becomes the root.
        Otherwise, the method traverses the tree from the root node
        until it finds a leaf
        node where the new node should be inserted based on its value.
        The method then sets the left or right child of that leaf node to the new node,
        depending on whether the new node's value is less than or greater than
        the leaf node's value.

    2. search method
        takes a value and traverses the tree from the root node
        until it finds a node with that value.
        If such a node exists, the method returns True.
        If the method reaches a leaf node without finding a node with the given value,
        it returns False.
    """

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        return new_node
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        return new_node
                    current_node = current_node.right
        return new_node

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def print_keys(self, order):
        """ Print all the keys within self sub-tree in 3 orders
        Syntax:
        <obj>.print_keys(order)
        return:
            sorted string of keys if order = "Inorder"
            postorder string if order = "Postorder"
            preorder string if order = "Preorder"
            None: invalide order
        """
        current_node = self.root

        if order == "Inorder":
            current_node.print_keys_inorder()

        elif order == "Postorder":
            current_node.print_keys_postorder()

        elif order == "Preorder":
            current_node.print_keys_preorder()

        else:
            print(f'Invalid order: {order}')


if __name__ == '__main__':
    """ Example code, demonstrating the followings:

    1. Build a binary search tree with random numbers with the key of root is 500
    2. Insert nodes into a binary search tree with random keys
    3. Traverse keys of binary search tree in Preorder
    4. Traverse keys of binary search tree in Inorder
    5. Traverse keys of binary search tree in Postorder
    """
    log.setLevel("INFO")
    # log.setLevel("DEBUG")

    bst = BinarySearchTree()
    print(f'Example 1: Binary Search Tree initiated.')

    bn = bst.insert(500)
    print(f'===>Root {bn} with key = {bn.value}\n')

    print(f"Example2: Inserting nodes ...")
    for _ in range(9):
        bn = bst.insert(random.randint(100, 999))
        print(f'===>Node {bn} inserted with key = {bn.value}')
    print()

    print(f'Example 3: Print keys of Binary Search Tree in Preorder')
    bst.print_keys("Preorder")
    print("\n")

    print(f'Example 4: Print keys of Binary Search Tree in Inorder')
    bst.print_keys("Inorder")
    print("\n")

    print(f'Example 5: Print keys of Binary Search Tree in Postorder')
    bst.print_keys("Postorder")
    print("\n")
