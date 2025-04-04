import random
import logging

"""
這個版本的二元搜尋樹使用生產環境的程式碼實現。
請參閱 biTree.py 以查看除錯程式碼。
"""

class BinaryTreeNode:
    """
    二元搜尋樹的節點類別，具有以下特性：

    1. 可以通過插入節點、鍵值或鍵值列表來建立二元樹
    2. 不允許重複的鍵值
    3. 所有節點按照鍵值升序（中序）排列
    4. 每個節點最多只能有兩個子節點
    5. 可以將二元樹轉換為升序或降序的列表
    6. 可以從二元樹中移除任意節點
    7. 可以從二元樹中移除任意子樹
    8. 可以按照後序遍歷順序移除整個樹
    9. 可以從根節點開始遞迴地刪除整棵樹

    這個模組可能返回的錯誤碼：
    -1: 節點鍵值重複
    -2: 節點/鍵值未找到
    """

    # 類別變數
    count = 0  # 節點總數，初始值為0
    root = None  # 樹的根節點

    def __init__(self, key, value=None, left=None, right=None):
        """
        初始化節點
        
        參數：
        key: 節點的鍵值
        value: 節點的值（可選）
        left: 左子節點（可選）
        right: 右子節點（可選）
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
        BinaryTreeNode.count += 1
        if BinaryTreeNode.count == 1:
            # 第一個節點成為根節點
            BinaryTreeNode.root = self

    def free_node(self):
        """
        釋放節點
        
        回傳：
        0: 成功
        """
        try:
            # 解除節點的引用，讓 Python 自動進行垃圾回收
            self = None
            
            BinaryTreeNode.count -= 1
            if BinaryTreeNode.count <= 0:
                # 樹已空
                BinaryTreeNode.root = None
                BinaryTreeNode.count = 0
            
            return 0
            
        except Exception as e:
            logging.error(f"釋放節點時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    def insert_node(self, node):
        """
        在以 self 為根的二元樹中插入節點
        
        參數：
        node: 要插入的節點
        
        回傳：
        0: 成功
        -1: 鍵值重複
        """
        try:
            if node.key == self.key:
                return -1  # 鍵值重複

            if node.key < self.key:
                if self.left is None:
                    self.left = node
                    return 0
                else:
                    return self.left.insert_node(node)
            else:
                if self.right is None:
                    self.right = node
                    return 0
                else:
                    return self.right.insert_node(node)

        except Exception as e:
            logging.error(f"插入節點時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    def remove_node(self, key):
        """
        在以 self 為根的子樹中移除指定鍵值的節點
        
        參數：
        key: 要移除的節點的鍵值
        
        回傳：
        被移除的節點: 成功
        -2: 節點/鍵值未找到
        """
        try:
            if key == self.key:
                # 找到要移除的節點

                # 如果是葉節點
                if self.left is None and self.right is None:
                    self.free_node()
                    return self

                # 如果只有一個子節點
                if self.left is None:
                    temp = self.right
                    self.free_node()
                    return temp
                elif self.right is None:
                    temp = self.left
                    self.free_node()
                    return temp

                # 如果有兩個子節點，找到右子樹的最小值節點作為替代
                succ_parent = self
                succ = self.right

                while succ.left is not None:
                    succ_parent = succ
                    succ = succ.left

                # 刪除後繼節點
                if succ_parent != self:
                    succ_parent.left = succ.right
                else:
                    self.right = succ.right

                # 用後繼節點替換當前節點
                self.key = succ.key
                self.value = succ.value
                return self

            # 繼續在子樹中搜尋
            if key < self.key:
                if self.left is None:
                    return -2  # 節點未找到
                return self.left.remove_node(key)
            else:
                if self.right is None:
                    return -2  # 節點未找到
                return self.right.remove_node(key)

        except Exception as e:
            logging.error(f"移除節點時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    def find_node(self, key):
        """
        在以 self 為根的子樹中查找指定鍵值的節點
        
        參數：
        key: 要查找的鍵值
        
        回傳：
        找到的節點: 成功
        -2: 節點/鍵值未找到
        """
        try:
            if key == self.key:
                return self
            
            if key < self.key:
                if self.left is None:
                    return -2
                return self.left.find_node(key)
            else:
                if self.right is None:
                    return -2
                return self.right.find_node(key)

        except Exception as e:
            logging.error(f"查找節點時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    def find_node_max(self):
        """
        在以 self 為根的子樹中查找最大鍵值的節點
        
        回傳：
        1. 最大鍵值的節點
        2. 父節點（如果存在，否則為 None）
        3. 子節點（如果存在，否則為 None）
        """
        try:
            if self.right is None:
                return self, None, self.left
            
            parent = self
            current = self.right
            
            while current.right is not None:
                parent = current
                current = current.right
            
            return current, parent, current.left

        except Exception as e:
            logging.error(f"查找最大節點時發生錯誤: {str(e)}")
            return None, None, None

    def find_node_min(self):
        """
        在以 self 為根的子樹中查找最小鍵值的節點
        
        回傳：
        1. 最小鍵值的節點
        2. 父節點（如果存在，否則為 None）
        3. 子節點（如果存在，否則為 None）
        """
        try:
            if self.left is None:
                return self, None, self.right
            
            parent = self
            current = self.left
            
            while current.left is not None:
                parent = current
                current = current.left
            
            return current, parent, current.right

        except Exception as e:
            logging.error(f"查找最小節點時發生錯誤: {str(e)}")
            return None, None, None

    def find_node_parent(self, key):
        """
        在以 self 為根的子樹中查找指定鍵值的節點及其父節點
        
        參數：
        key: 要查找的鍵值
        
        回傳：
        1. 找到的節點（如果存在，否則為 None）
        2. 父節點（如果存在，否則為 None）
        3. 是否在父節點的左子樹（True/False）
        """
        try:
            if key == self.key:
                return self, None, False
            
            if key < self.key:
                if self.left is None:
                    return None, None, False
                return self.left.find_node_parent(key)
            else:
                if self.right is None:
                    return None, None, False
                return self.right.find_node_parent(key)

        except Exception as e:
            logging.error(f"查找節點父節點時發生錯誤: {str(e)}")
            return None, None, False

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
            logging.error(f"列印鍵值時發生錯誤: {str(e)}")
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
            logging.error(f"中序列印鍵值時發生錯誤: {str(e)}")
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
            logging.error(f"後序列印鍵值時發生錯誤: {str(e)}")
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
            logging.error(f"先序列印鍵值時發生錯誤: {str(e)}")
            return ""

    def sort_keys(self, reverse=False):
        """
        以中序遍歷方式獲取子樹中所有鍵值的排序列表
        
        參數：
        reverse: 是否反向排序（預設為 False）
        
        回傳：
        排序後的鍵值列表
        """
        try:
            key_list = []
            self.append_key(key_list, reverse)
            return key_list

        except Exception as e:
            logging.error(f"排序鍵值時發生錯誤: {str(e)}")
            return []

    def append_key(self, key_list, reverse=False):
        """
        將節點的鍵值添加到列表中
        
        參數：
        key_list: 要添加鍵值的列表
        reverse: 是否反向添加（預設為 False）
        """
        try:
            if reverse:
                if self.right is not None:
                    self.right.append_key(key_list, reverse)
                key_list.append(self.key)
                if self.left is not None:
                    self.left.append_key(key_list, reverse)
            else:
                if self.left is not None:
                    self.left.append_key(key_list, reverse)
                key_list.append(self.key)
                if self.right is not None:
                    self.right.append_key(key_list, reverse)

        except Exception as e:
            logging.error(f"添加鍵值時發生錯誤: {str(e)}")

    def sort_nodes(self, reverse=False):
        """
        以中序遍歷方式獲取子樹中所有節點的排序列表
        
        參數：
        reverse: 是否反向排序（預設為 False）
        
        回傳：
        排序後的節點列表
        """
        try:
            node_list = []
            self.append_node_inorder(node_list, reverse)
            return node_list

        except Exception as e:
            logging.error(f"排序節點時發生錯誤: {str(e)}")
            return []

    def append_node_inorder(self, node_list, reverse=False):
        """
        以中序遍歷方式將節點添加到列表中
        
        參數：
        node_list: 要添加節點的列表
        reverse: 是否反向添加（預設為 False）
        """
        try:
            if reverse:
                if self.right is not None:
                    self.right.append_node_inorder(node_list, reverse)
                node_list.append(self)
                if self.left is not None:
                    self.left.append_node_inorder(node_list, reverse)
            else:
                if self.left is not None:
                    self.left.append_node_inorder(node_list, reverse)
                node_list.append(self)
                if self.right is not None:
                    self.right.append_node_inorder(node_list, reverse)

        except Exception as e:
            logging.error(f"中序添加節點時發生錯誤: {str(e)}")

    def append_node_postorder(self, node_list):
        """
        以後序遍歷方式將節點添加到列表中
        
        參數：
        node_list: 要添加節點的列表
        """
        try:
            if self.left is not None:
                self.left.append_node_postorder(node_list)
            if self.right is not None:
                self.right.append_node_postorder(node_list)
            node_list.append(self)

        except Exception as e:
            logging.error(f"後序添加節點時發生錯誤: {str(e)}")

    def append_node_preorder(self, node_list):
        """
        以先序遍歷方式將節點添加到列表中
        
        參數：
        node_list: 要添加節點的列表
        """
        try:
            node_list.append(self)
            if self.left is not None:
                self.left.append_node_preorder(node_list)
            if self.right is not None:
                self.right.append_node_preorder(node_list)

        except Exception as e:
            logging.error(f"先序添加節點時發生錯誤: {str(e)}")

    def remove_tree(self):
        """
        釋放以 self 為根的子樹中的所有節點
        以後序遍歷方式移除所有節點（先移除子節點，再移除當前節點）
        
        回傳：
        0: 成功
        """
        try:
            # 如果當前節點不是根節點，需要先將子樹從主樹中切斷
            if self != BinaryTreeNode.root:
                node_found, node_p, from_left = BinaryTreeNode.root.find_node_parent(self.key)
                
                if node_p is not None:
                    if from_left:
                        node_p.left = None
                    else:
                        node_p.right = None

            # 使用後序遍歷方式收集所有節點
            list_stack = []
            self.append_node_postorder(list_stack)

            # 移除所有節點
            for node in list_stack:
                self.remove_node(node.key)

            return 0

        except Exception as e:
            logging.error(f"移除子樹時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

    @classmethod
    def insert_tree(cls, key):
        """
        創建節點並插入到二元樹中
        
        參數：
        key: 要插入的鍵值
        
        回傳：
        新節點: 成功
        已存在的節點: 鍵值重複
        """
        try:
            # 如果樹是空的，返回新節點
            if cls.root is None:
                return BinaryTreeNode(key)

            # 檢查樹中是否已有相同鍵值的節點
            node_found = cls.root.find_node(key)
            if node_found == -2:
                # 創建新節點
                node_new = BinaryTreeNode(key)
                
                # 將新節點插入樹中
                cls.root.insert_node(node_new)
                return node_new
            else:
                # 返回已存在的節點
                return node_found

        except Exception as e:
            logging.error(f"插入樹時發生錯誤: {str(e)}")
            return None

    @classmethod
    def discard_tree(cls):
        """
        釋放整棵二元樹的所有節點
        從根節點開始遞迴地刪除整棵樹
        
        回傳：
        0: 成功
        """
        try:
            if cls.root is None:
                return 0
            else:
                cls.root.remove_node(cls.root.key)

            if cls.root is not None:
                return cls.root.discard_tree()
            else:
                return 0

        except Exception as e:
            logging.error(f"釋放整棵樹時發生錯誤: {str(e)}")
            return -4  # 未知錯誤

if __name__ == '__main__':
    """
    範例代碼，展示如何：
    1. 使用隨機數字作為鍵值建立二元樹，其中：
       - 根節點的鍵值為 500
       - 其他節點的鍵值為 9 個 100 到 999 之間的隨機數
    2. 以三種不同的順序顯示樹的內容
    3. 將樹轉換為升序列表
    4. 將樹轉換為降序列表
    5. 移除整棵樹
    """
    
    # 建立根節點
    node_root = BinaryTreeNode.insert_tree(500)
    print(f'範例 1: 二元樹的根節點在 {node_root}，鍵值為 {node_root.key}\n')

    # 插入 9 個隨機鍵值的節點
    for _ in range(9):
        bn = BinaryTreeNode.insert_tree(random.randint(100, 999))
        print(f'範例 2: 在位置 {bn} 插入鍵值為 {bn.key} 的節點')
    print()

    # 顯示樹的狀態
    print(f'範例 3: 樹中的節點數量 = {BinaryTreeNode.count}')
    print(f'範例 3.1: 以中序方式顯示鍵值：')
    print(node_root.print_keys("Inorder"))
    print(f'範例 3.2: 以後序方式顯示鍵值：')
    print(node_root.print_keys("Postorder"))
    print(f'範例 3.3: 以先序方式顯示鍵值：')
    print(node_root.print_keys("Preorder"))

    # 將二元樹轉換為列表
    new_list = node_root.sort_keys()
    print(f'範例 4: 排序後的鍵值列表：\n {new_list}\n')
    
    rev_list = node_root.sort_keys(reverse=True)
    print(f'範例 5: 逆序排序的鍵值列表：\n {rev_list}\n')

    # 移除整棵樹
    print(f'範例 6: 移除整棵樹，根節點在 {BinaryTreeNode.root}，鍵值為 {BinaryTreeNode.root.key}')
    BinaryTreeNode.discard_tree()
    print(f'範例 6: 整棵樹已被移除。程式結束。')
