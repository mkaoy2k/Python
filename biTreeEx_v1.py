from biTree_v1 import BinaryTreeNode
import logging

"""
示例代碼，展示如何：
1. 從整數列表建立二元樹
2. 顯示樹的資訊：
   a) 使用 print_keys()
   b) 使用 sort_keys()
3. 查找：
   a) 樹中的最大節點
   b) 樹中的最小節點
4. 根據鍵值查找節點
5. 根據鍵值移除節點
6. 移除整棵樹
"""

# 設置日誌等級
logging.basicConfig(level=logging.DEBUG)

# 測試用的整數列表
numbers = [5, 4, 1, 9, 5, 3, 7, 6, 8, 2]

# 1. 建立二元樹
print("示例 1: 從整數列表建立二元樹")
print(f"原始數字列表： {numbers}")
print()

# 建立根節點
root = BinaryTreeNode(numbers[0])
print(f"示例 1.1: 建立根節點，鍵值為 {numbers[0]}")

# 插入剩餘的節點
for num in numbers[1:]:
    node = BinaryTreeNode(num)
    result = root.insert_node(node)
    if result == 0:
        print(f"示例 1.2: 成功插入節點，鍵值為 {num}")
    else:
        print(f"示例 1.2: 插入失敗，鍵值 {num} 已存在")
print()

# 顯示當前樹的狀態
print("示例 1.3: 當前樹的狀態")
print(f"節點數量： {BinaryTreeNode.count}")

print()

# 2. 顯示樹的資訊
print("示例 2: 顯示樹的資訊")

# 2.1 使用 print_keys()
print("示例 2.1: 使用 print_keys() 顯示鍵值")
root.print_keys()

# 2.2 使用 sort_keys()
print("示例 2.2: 使用 sort_keys() 顯示鍵值")
print(f"升序排列： {root.sort_keys()}")
print(f"降序排列： {root.sort_keys(reverse=True)}")
print()

# 3. 查找最大和最小節點
print("示例 3: 查找最大和最小節點")

# 3.1 查找最大節點
max_node = root.find_node_max()
print(f"示例 3.1: 最大節點的鍵值為 {max_node.key}")

# 3.2 查找最小節點
min_node = root.find_node_min()
print(f"示例 3.2: 最小節點的鍵值為 {min_node.key}")
print()

# 4. 根據鍵值查找節點
print("示例 4: 根據鍵值查找節點")

# 測試查找的鍵值
search_keys = [3, 9, 10]
for key in search_keys:
    node = root.find_node(key)
    if node == -2:
        print(f"示例 4.1: 鍵值 {key} 未找到")
    else:
        print(f"示例 4.2: 找到鍵值 {key} 的節點")
print()

# 5. 根據鍵值移除節點
print("示例 5: 根據鍵值移除節點")

# 測試移除的鍵值
remove_keys = [3, 9, 10]
for key in remove_keys:
    # 首先查找節點
    node = root.find_node(key)
    if node == -2:
        print(f"示例 5.1: 鍵值 {key} 未找到，無法移除")
    else:
        # 嘗試移除節點
        result = root.remove_node(key)
        if result == 0:
            print(f"示例 5.2: 成功移除鍵值 {key} 的節點")
            print(f"示例 5.2.1: 當前樹中的節點數量為 {BinaryTreeNode.count}")
            print("示例 5.2.2: 當前樹的鍵值：")
            root.print_keys()
        else:
            print(f"示例 5.3: 移除鍵值 {key} 的節點失敗")
print()

# 6. 移除整棵樹
print("示例 6: 移除整棵樹")
print(f"示例 6.1: 移除前，樹中的節點數量為 {BinaryTreeNode.count}")
print("示例 6.1.1: 移除前的樹形狀：")
root.print_keys()

# 移除整棵樹
BinaryTreeNode.discard_tree()

print(f"示例 6.2: 移除後，樹中的節點數量為 {BinaryTreeNode.count}")
print("示例 6.3: 整棵樹已被成功移除")
