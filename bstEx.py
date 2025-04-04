"""
這個程式示範了二元搜尋樹中的刪除操作
"""

import logging

# 設定 logging 等級為 DEBUG
logging.basicConfig(level=logging.DEBUG)


class Node:
    """ 二元搜尋樹的節點類別 """
    def __init__(self, key):
        """ 初始化節點 """
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    """ 以中序方式遍歷二元搜尋樹 """
    if root is not None:
        inorder(root.left)
        logging.debug(root.key)
        inorder(root.right)


def insert(node, key):
    """ 在二元搜尋樹中插入新節點 """
    # 如果樹是空的，返回新節點
    if node is None:
        return Node(key)

    # 否則遞迴向下查找
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # 返回（未變更的）節點指標
    return node


def minValueNode(node):
    """ 給定一個非空的二元搜尋樹，返回具有最小鍵值的節點
    注意：不需要搜索整個樹
    """
    current = node

    # 循環向下找到最左的葉節點
    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):
    """ 給定一個二元搜尋樹和一個鍵，刪除該鍵並返回新的根 """
    # 基本情況
    if root is None:
        return root

    # 如果要刪除的鍵小於根的鍵，則它位於左子樹
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # 如果要刪除的鍵大於根的鍵，則它位於右子樹
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    # 如果鍵與根的鍵相同，則這是需要刪除的節點
    else:
        # 只有一個子樹或沒有子樹的節點
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # 兩個子樹的節點：
        # 取得中序後繼節點
        # （右子樹中最小的節點）
        temp = minValueNode(root.right)

        # 將中序後繼節點的內容複製到此節點
        root.key = temp.key

        # 刪除中序後繼節點
        root.right = deleteNode(root.right, temp.key)

    return root


if __name__ == '__main__':
    """ 主程式範例，建立並操作二元搜尋樹 """
    logging.basicConfig(level=logging.INFO)

    # 建立以下二元搜尋樹
    #          50
    #        /    \
    #       30    70
    #      / \   / \
    #     20 40 60 80 

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    logging.info("中序遍歷初始樹：")
    inorder(root)
    logging.info("")

    logging.info("\n刪除 20")
    root = deleteNode(root, 20)
    logging.info("刪除後的中序遍歷：")
    inorder(root)
    logging.info("")

    logging.info("\n刪除 30")
    root = deleteNode(root, 30)
    logging.info("刪除後的中序遍歷：")
    inorder(root)
    logging.info("")

    logging.info("\n刪除 50")
    root = deleteNode(root, 50)
    logging.info("刪除後的中序遍歷：")
    inorder(root)
    logging.info("程式示範結束\n")
