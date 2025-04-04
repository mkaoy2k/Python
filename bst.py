""" 
這個實作定義了兩個類別：Node 和 BinarySearchTree。
Node 代表二元搜尋樹中的節點，
    包含一個值和指向其左子樹和右子樹的指標。

BinarySearchTree 代表二元搜尋樹本身，
    包含一個指向根節點的指標，以及兩個方法：
    用於插入新節點和搜尋具有特定值的節點。
"""
import random
import traceback
import logging

# 設定 logging 等級為 DEBUG
logging.basicConfig(level=logging.DEBUG)


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ 二元搜尋樹的三種常見遍歷順序：
    **中序**、**先序** 和 **後序**。
    中序遍歷
        包含訪問左子樹，然後是根節點，
        最後是右子樹。
        這種遍歷會以非遞減順序給出節點。
    先序遍歷
        包含先訪問根節點，然後是左子樹，
        最後是右子樹。
    後序遍歷
        包含先訪問左子樹，然後是右子樹，
        最後是根節點。
    """

    def print_keys_inorder(self):
        logging.debug(
            f'{get_function_name()}: {self.value}')

        if self.left is not None:
            self.left.print_keys_inorder()

        print(self.value, end=' ')

        if self.right is not None:
            self.right.print_keys_inorder()

    def print_keys_postorder(self):
        logging.debug(
            f'{get_function_name()}: {self.value}')

        if self.left is not None:
            self.left.print_keys_postorder()

        if self.right is not None:
            self.right.print_keys_postorder()

        print(self.value, end=' ')

    def print_keys_preorder(self):
        logging.debug(
            f'{get_function_name()}: {self.value}')

        print(self.value, end=' ')

        if self.left is not None:
            self.left.print_keys_preorder()

        if self.right is not None:
            self.right.print_keys_preorder()


class BinarySearchTree:
    def __init__(self):
        self.root = None

    """ 這個類別實現了兩個方法。
    1. insert 方法
        接受一個值並創建一個具有該值的新節點。
        如果樹是空的（即根節點為 None），
        新節點成為根節點。
        否則，該方法從根節點遍歷樹
        直到找到一個葉節點
        根據新節點的值，新節點應該插入的位置。
        該方法然後將該葉節點的左子樹或右子樹設為新節點，
        取決於新節點的值是否小於或大於
        葉節點的值。

    2. search 方法
        接受一個值並從根節點遍歷樹
        直到找到具有該值的節點。
        如果存在這樣的節點，該方法返回 True。
        如果該方法到達葉節點而未找到具有給定值的節點，
        它返回 False。
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
        """ 印出 self 子樹中的所有鍵值，有三種順序
        語法：
        <obj>.print_keys(order)
        返回：
            排序後的鍵值字串，如果 order = "Inorder"
            後序字串，如果 order = "Postorder"
            先序字串，如果 order = "Preorder"
            None: 無效的 order
        """
        current_node = self.root

        if order == "Inorder":
            current_node.print_keys_inorder()

        elif order == "Postorder":
            current_node.print_keys_postorder()

        elif order == "Preorder":
            current_node.print_keys_preorder()

        else:
            print(f'無效的順序：{order}')


if __name__ == '__main__':
    """ 範例程式碼，展示以下功能：

    1. 使用隨機數字建立二元搜尋樹，根節點的鍵值為 500
    2. 使用隨機鍵值插入節點到二元搜尋樹
    3. 以先序方式遍歷二元搜尋樹的鍵值
    4. 以中序方式遍歷二元搜尋樹的鍵值
    5. 以後序方式遍歷二元搜尋樹的鍵值
    """
    logging.basicConfig(level=logging.INFO)

    bst = BinarySearchTree()
    print(f'範例 1: 二元搜尋樹已初始化。')

    bn = bst.insert(500)
    print(f'===>根節點 {bn}，鍵值 = {bn.value}\n')

    print(f"範例 2: 插入節點...")
    for _ in range(9):
        bn = bst.insert(random.randint(100, 999))
        print(f'===>節點 {bn} 已插入，鍵值 = {bn.value}')
    print()

    print(f'範例 3: 以先序方式印出二元搜尋樹的鍵值')
    bst.print_keys("Preorder")
    print("\n")

    print(f'範例 4: 以中序方式印出二元搜尋樹的鍵值')
    bst.print_keys("Inorder")
    print("\n")

    print(f'範例 5: 以後序方式印出二元搜尋樹的鍵值')
    bst.print_keys("Postorder")
    print("\n")
