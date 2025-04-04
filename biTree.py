"""
這個版本的二元搜尋樹實現了除錯代碼。
請參閱 bsTree.py 以獲取生產代碼版本
"""

import random
import traceback
import logging as log

def get_function_name():
    """取得目前函數名稱"""
    return traceback.extract_stack(None, 2)[0][2]


class BinaryTreeNode:
    """使用者自定義的二元樹節點類別
    
    這個二元搜尋樹具有以下特性：
    1. 可以通過插入節點或從列表建立二元搜尋樹
    2. 所有節點按照鍵值升序排列（中序遍歷）
    3. 每個節點最多可以有兩個子節點
    4. 可以將二元搜尋樹轉換為升序或降序的列表
    5. 可以從二元搜尋樹中移除任意節點
    
    可能返回的錯誤代碼：
    -1: 節點鍵值重複
    -2: 節點鍵值未找到
    -3: 根節點未找到
    -4: 未知錯誤
    -5: 父節點無法定位
    """

    # 類別變數
    count = 0  # 節點總數
    root = None  # 根節點

    def __init__(self, value, left=None, right=None):
        """初始化節點
        
        參數：
        value: 節點的鍵值
        left: 左子節點 (預設為 None)
        right: 右子節點 (預設為 None)
        """
        self.key = value
        self.left = left
        self.right = right
        BinaryTreeNode.count += 1
        if BinaryTreeNode.count == 1:
            # 第一個節點成為根節點
            BinaryTreeNode.root = self

    def free_node(self):
        """釋放節點記憶體
        
        回傳：
        0: 成功釋放
        """
        del self
        BinaryTreeNode.count -= 1
        if BinaryTreeNode.count <= 0:
            # 二元樹已清空
            BinaryTreeNode.root = None
            BinaryTreeNode.count = 0
        return 0

    def insert_node(self, node):
        """在二元樹中插入節點
        
        參數：
        node: 要插入的節點
        
        回傳：
        0: 成功插入
        -1: 鍵值重複，忽略插入
        """
        if node.key == self.key:
            return -1   # 鍵值重複

        if node.key < self.key:
            if self.left is None:
                self.left = node
                return 0
            else:
                if self.left.insert_node(node) == -1:
                    return -1
        else:
            if self.right is None:
                self.right = node
                return 0
            else:
                if self.right.insert_node(node) == -1:
                    return -1
        return 0

    def remove_node(self, key):
        """從二元樹中移除具有指定鍵值的節點
        
        參數：
        key: 要移除的節點的鍵值
        
        回傳：
        0: 成功移除
        -2: 節點未找到
        -4: 未知錯誤
        """
        try:
            # 1. 特殊情況：移除根節點
            if key == BinaryTreeNode.root.key:
                return self._remove_root()
            
            # 2. 一般情況：移除非根節點
            dad, kid, is_left = self.find_node_parent(key)
            if dad is None:
                return -2  # 節點未找到

            # 3. 根據子節點情況進行移除
            if kid.left is None and kid.right is None:
                # 節點沒有子節點，直接移除
                self._remove_leaf(dad, kid, is_left)
            elif kid.left is None:
                # 節點只有右子節點
                self._remove_one_child(dad, kid, is_left, True)
            elif kid.right is None:
                # 節點只有左子節點
                self._remove_one_child(dad, kid, is_left, False)
            else:
                # 節點有兩個子節點，需要找到替換節點
                self._remove_two_children(kid)

            BinaryTreeNode.count -= 1
            return 0

        except Exception as e:
            log.error(f"移除節點時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    def _remove_root(self):
        """移除根節點的輔助函數"""
        if BinaryTreeNode.root.left is None and BinaryTreeNode.root.right is None:
            # 根節點沒有子節點，直接移除
            BinaryTreeNode.root = None
            BinaryTreeNode.count = 0
            return 0

        if BinaryTreeNode.root.right is not None:
            # 從右子樹中找到最小節點作為替換
            replace_node = BinaryTreeNode.root.right.find_node_min()
            if replace_node.parent is None:
                # 右子樹的最小節點就是右子節點
                BinaryTreeNode.root.right = replace_node.right
            else:
                # 將替換節點的右子樹接在父節點上
                parent.left = replace_node.right
        else:
            # 只有左子樹，直接用左子節點替換
            replace_node = BinaryTreeNode.root.left
            BinaryTreeNode.root.left = None

        # 更新根節點
        BinaryTreeNode.root.key = replace_node.key
        return 0

    def _remove_leaf(self, dad, kid, is_left):
        """移除葉節點的輔助函數"""
        if is_left:
            dad.left = None
        else:
            dad.right = None

    def _remove_one_child(self, dad, kid, is_left, is_right_child):
        """移除只有一個子節點的節點的輔助函數
        
        參數：
        is_right_child: 布林值，表示要保留的子節點是否為右子節點
        """
        if is_right_child:
            # 保留右子節點
            if is_left:
                dad.left = kid.right
            else:
                dad.right = kid.right
        else:
            # 保留左子節點
            if is_left:
                dad.left = kid.left
            else:
                dad.right = kid.left

    def _remove_two_children(self, kid):
        """移除有兩個子節點的節點的輔助函數"""
        # 從右子樹中找到最小節點作為替換
        replace_node = kid.right.find_node_min()
        if replace_node.parent is None:
            # 右子樹的最小節點就是右子節點
            kid.right = replace_node.right
        else:
            # 將替換節點的右子樹接在父節點上
            replace_node.parent.left = replace_node.right

        # 更新節點的鍵值
        kid.key = replace_node.key

    def find_dad_kid(self, key):
        """在二元樹中查找指定鍵值的節點及其父節點
        
        參數：
        key: 要查找的鍵值
        
        回傳：
        三個參數：
        dad: 父節點
        kid: 子節點
        is_left: 布林值，表示子節點是否為父節點的左子節點
        -5: 如果找不到父節點
        -4: 未知錯誤
        """
        if self.key == key:
            return None, self, True  # 找到目標節點，沒有父節點

        if key < self.key:
            if self.left is None:
                return None, None, True
            else:
                dad, kid, is_left = self.left.find_dad_kid(key)
                if dad is None:
                    return self, kid, True
                return dad, kid, is_left
        else:
            if self.right is None:
                return None, None, False
            else:
                dad, kid, is_left = self.right.find_dad_kid(key)
                if dad is None:
                    return self, kid, False
                return dad, kid, is_left

    def find_node(self, key):
        """在二元樹中查找指定鍵值的節點
        
        參數：
        key: 要查找的鍵值
        
        回傳：
        找到的節點物件
        -2: 如果未找到
        """
        if self.key == key:
            return self
        elif key < self.key:
            if self.left is None:
                return -2
            return self.left.find_node(key)
        else:
            if self.right is None:
                return -2
            return self.right.find_node(key)

    def find_node_max(self):
        """在二元樹中查找具有最大鍵值的節點"""
        if self.right is None:
            return self
        return self.right.find_node_max()

    def find_node_min(self):
        """在二元樹中查找具有最小鍵值的節點"""
        if self.left is None:
            return self
        return self.left.find_node_min()

    def print_keys(self, order):
        """
        以指定順序列印子樹中的所有鍵值
        
        參數：
        order: 遍歷順序（"Inorder", "Postorder", "Preorder"）
        
        回傳：
        排序後的鍵值字串
        None: 無效的順序
        """
        try:
            if order == "Inorder":
                return self.print_keys_inorder()
            elif order == "Postorder":
                return self.print_keys_postorder()
            elif order == "Preorder":
                return self.print_keys_preorder()
            else:
                return None
        except Exception as e:
            log.error(f"列印鍵值時發生錯誤: {str(e)}")
            return None

    def print_keys_inorder(self):
        """
        以中序遍歷方式列印子樹中的所有鍵值
        """
        try:
            result = []
            if self.left is not None:
                result.extend(self.left.print_keys_inorder().split())
            result.append(str(self.key))
            if self.right is not None:
                result.extend(self.right.print_keys_inorder().split())
            return " ".join(result)
        except Exception as e:
            log.error(f"中序列印鍵值時發生錯誤: {str(e)}")
            return ""

    def print_keys_postorder(self):
        """
        以後序遍歷方式列印子樹中的所有鍵值
        """
        try:
            result = []
            if self.left is not None:
                result.extend(self.left.print_keys_postorder().split())
            if self.right is not None:
                result.extend(self.right.print_keys_postorder().split())
            result.append(str(self.key))
            return " ".join(result)
        except Exception as e:
            log.error(f"後序列印鍵值時發生錯誤: {str(e)}")
            return ""

    def print_keys_preorder(self):
        """
        以先序遍歷方式列印子樹中的所有鍵值
        """
        try:
            result = []
            result.append(str(self.key))
            if self.left is not None:
                result.extend(self.left.print_keys_preorder().split())
            if self.right is not None:
                result.extend(self.right.print_keys_preorder().split())
            return " ".join(result)
        except Exception as e:
            log.error(f"先序列印鍵值時發生錯誤: {str(e)}")
            return ""
    def append_key(self, key_list, reverse=False):
        """內部遞迴函數，用於收集鍵值
        
        參數：
        key_list: 用於存儲鍵值的列表
        reverse: 布林值，決定是否反向排序
        
        回傳：
        0: 成功
        """
        if reverse is False:
            if self.left is not None:
                self.left.append_key(key_list, reverse)
            key_list.append(self.key)
            if self.right is not None:
                self.right.append_key(key_list, reverse)
        else:
            if self.right is not None:
                self.right.append_key(key_list, reverse)
            key_list.append(self.key)
            if self.left is not None:
                self.left.append_key(key_list, reverse)
        return 0

    def sort_keys(self, reverse=False):
        """遍歷二元樹並取得鍵值列表
        
        參數：
        reverse: 布林值，決定是否反向排序
        
        回傳：
        排序後的鍵值列表
        """
        key_list = []
        self.append_key(key_list, reverse)
        return key_list

    def sort_nodes(self, reverse=False):
        """遍歷二元樹並取得節點列表
        
        參數：
        reverse: 布林值，決定是否反向排序
        
        回傳：
        排序後的節點列表
        """
        node_list = []
        self.append_node(node_list, reverse)
        return node_list

    def append_node(self, node_list, reverse=False):
        """內部遞迴函數，用於收集節點
        
        參數：
        node_list: 用於存儲節點的列表
        reverse: 布林值，決定是否反向排序
        
        回傳：
        0: 成功
        """
        if reverse is False:
            if self.left is not None:
                self.left.append_node(node_list, reverse)
            node_list.append(self)
            if self.right is not None:
                self.right.append_node(node_list, reverse)
        else:
            if self.right is not None:
                self.right.append_node(node_list, reverse)
            node_list.append(self)
            if self.left is not None:
                self.left.append_node(node_list, reverse)
        return 0

    def remove_tree(self):
        """遞迴移除整個二元樹
        
        回傳：
        0: 成功
        """
        if self.left is not None:
            log.debug(f'移除左子節點，鍵值 = {self.left.key}')
            self.remove_node(self.left.key)
            log.debug(f'剩餘節點: {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')

        if self.right is not None:
            log.debug(f'移除右子節點，鍵值 = {self.right.key}')
            self.remove_node(self.right.key)
            log.debug(f'剩餘節點: {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')

        # 移除自己
        if self == BinaryTreeNode.root:
            BinaryTreeNode.root = None
        return 0

    def find_node_parent(self, key):
        """
        在二元樹中查找指定鍵值的節點及其父節點
        
        參數：
        key: 要查找的鍵值
        
        回傳：
        三個參數：
        node_found: 找到的節點
        node_p: 父節點
        is_left: 布林值，表示子節點是否為父節點的左子節點
        """
        if key == self.key:
            # 找到目標節點，沒有父節點
            return None, self, True

        if key < self.key:
            if self.left is None:
                return None, None, True
            else:
                node_p, node_found, is_left = self.left.find_node_parent(key)
                if node_p is None:
                    return self, node_found, True
                return node_p, node_found, is_left
        else:
            if self.right is None:
                return None, None, False
            else:
                node_p, node_found, is_left = self.right.find_node_parent(key)
                if node_p is None:
                    return self, node_found, False
                return node_p, node_found, is_left

    @classmethod
    def discard_tree(cls):
        """釋放整個二元樹的記憶體
        
        回傳：
        0: 成功
        """
        if cls.count <= 0:
            return 0
        
        # 從根節點開始移除
        if cls.root is not None:
            cls.root.remove_tree()
            cls.root = None
            cls.count = 0
        return 0


if __name__ == '__main__':
    """範例程式碼，展示如何使用二元樹：
    1. 建立根節點 (鍵值 = 500)
    2. 隨機插入 9 個鍵值在 100-999 之間的節點
    3. 顯示二元樹資訊
    4. 將二元樹轉換為升序列表
    5. 將二元樹轉換為降序列表
    6. 移除整個二元樹
    """
    # 設定 log 等級
    log.basicConfig(level=log.DEBUG)
    
    node_root = BinaryTreeNode(500)
    print(f'範例 1: 二元樹根節點，位於 {node_root}，鍵值 = {node_root.key}\n')

    for _ in range(9):
        bn = BinaryTreeNode(random.randint(100, 999))
        if node_root.insert_node(bn) == -1:
            print(f'範例 2: 重複鍵值 = {bn.key}')
            bn.free_node()  # 重複鍵值
        else:
            print(f'範例 2: 已插入節點，位於 {bn}，鍵值 = {bn.key}')
    print()

    print(f'範例 3: 二元樹節點數量 = {BinaryTreeNode.count}')
    print('範例 3: 印出鍵值:')
    # print keys
    print(f'Example 3.1: printing keys Inorder:', end=' ')
    print(node_root.print_keys("Inorder"))
    print()
    print(f'Example 3.2: printing keys Postorder:', end=' ')
    print(node_root.print_keys("Postorder"))
    print()
    print(f'Example 3.3: printing keys Preorder:', end=' ')
    print(node_root.print_keys("Preorder"))
    print()

    # 將二元樹轉換為列表
    new_list = node_root.sort_keys()
    print(f'範例 4: 升序鍵值列表:\n {new_list}\n')
    rev_list = node_root.sort_keys(reverse=True)
    print(f'範例 5: 降序鍵值列表:\n {rev_list}\n')

    # 移除整個二元樹
    print(f'範例 6: 移除二元樹，根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}')
    BinaryTreeNode.discard_tree()
    print('範例 6: 已移除整個二元樹。程式結束。')
