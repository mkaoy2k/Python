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


def deleteNode(root, key):
    """ 給定一個二元搜尋樹和一個鍵，刪除該鍵並返回新的根 """
    # 基本情況
    if root is None:
        return root

    # 遞迴呼叫要刪除節點的祖先
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root

    elif key > root.key:
        root.right = deleteNode(root.right, key)
        return root

    # 當根節點是要刪除的節點時

    # 如果根節點是葉節點
    if root.left is None and root.right is None:
        return None

    # 如果其中一個子樹是空的
    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp

    # 如果兩個子樹都存在
    succParent = root

    # 找到後繼節點
    succ = root.right

    # 向左遞迴找到最左的節點
    while succ.left is not None:
        succParent = succ
        succ = succ.left

    # 刪除後繼節點。由於後繼節點總是其父節點的左子節點，
    # 我們可以安全地將後繼節點的右子樹設為其父節點的左子樹。
    # 如果沒有後繼父節點，
    # 則將後繼節點的右子樹設為根節點的右子樹（即 succParent == root）
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    # 將後繼節點的值複製到根節點
    root.key = succ.key

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
    logging.info(f'根節點位於 {root}，鍵值 = {root.key}\n')

    logging.info("中序遍歷初始樹：")
    inorder(root)

    logging.info("\n刪除 20")
    root = deleteNode(root, 20)
    logging.info("刪除後的中序遍歷：")
    inorder(root)

    logging.info("\n刪除 30")
    root = deleteNode(root, 30)
    logging.info("刪除後的中序遍歷：")
    inorder(root)

    logging.info("\n刪除 50")
    root = deleteNode(root, 50)
    logging.info("刪除後的中序遍歷：")
    inorder(root)

    logging.info("\n程式示範結束")
