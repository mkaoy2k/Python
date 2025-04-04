"""
範例程式碼，展示如何使用二元搜尋樹

這個範例程式碼展示了如何：
1. 從整數列表建立二元搜尋樹
2. 顯示二元搜尋樹資訊：
   1) 以中序方式印出鍵值
   2) 以後序方式印出鍵值
   3) 以先序方式印出鍵值
   4) 將鍵值排序並存儲在列表中
3. 查詢：
   1) 查詢二元搜尋樹中的最大節點
   2) 查詢二元搜尋樹中的最小節點
   3) 查詢子樹中的最大節點
   4) 查詢子樹中的最小節點
4. 根據鍵值查找節點：
   1) 查找具有匹配鍵值的節點
   2) 查找具有匹配鍵值的目標節點及其父節點（如果有的話）
5. 根據鍵值移除節點
6. 移除子樹
7. 移除整個樹
"""

from bsTree import BinaryTreeNode
import logging

# 設定 logging 等級為 DEBUG
logging.basicConfig(level=logging.DEBUG)

# 建立測試數據
test_numbers = [4, 1, 9, 5, 3, 7, 6, 8, 2, 5]
print(f'測試數據數量： {test_numbers} = {len(test_numbers)}\n')

# 1. 建立二元搜尋樹根節點
node_root = BinaryTreeNode(test_numbers.pop())
print(f'範例 1: 建立二元搜尋樹，根節點鍵值 = {BinaryTreeNode.root.key}')

# 2. 迴圈插入剩餘的節點
for key in test_numbers:
    bn = BinaryTreeNode(key)
    if node_root.insert_node(bn) == -1:
        print(f'範例 1: 重複鍵值 = {bn.key}')
        bn.free_node()
    else:
        print(f'範例 1: 已插入節點，位於 {bn}，鍵值 = {bn.key}')
print()

# 3. 印出鍵值
print(f'範例 2.1: 以中序方式印出鍵值：', end=' ')
node_root.print_keys("Inorder")
print()
print(f'範例 2.2: 以後序方式印出鍵值：', end=' ')
node_root.print_keys("Postorder")
print()
print(f'範例 2.3: 以先序方式印出鍵值：', end=' ')
node_root.print_keys("Preorder")
print()

# 4. 印出排序後的鍵值列表
print(
    f'範例 2.4: 排序整個二元搜尋樹的鍵值： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')
print(f'根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}\n')

# 5. 查詢最大和最小節點
node_max, _, _ = node_root.find_node_max()
print(f'範例 3.1: 全局最大鍵值 = {node_max.key} 位於 {node_max}')

node_min, _, _ = node_root.find_node_min()
print(f'範例 3.2: 全局最小鍵值 = {node_min.key} 位於 {node_min}\n')

# 6. 查詢子樹中的最大和最小節點
key = 3
node_found = node_root.find_node(key)
if node_found != -2:
    node_max, _, _ = node_found.find_node_max()
    print(
        f'範例 3.3: 鍵值 = {key} 的子樹中，局部最大鍵值 = {node_max.key} 位於 {node_max}')
    node_min, _, _ = node_found.find_node_min()
    print(
        f'範例 3.4: 鍵值 = {key} 的子樹中，局部最小鍵值 = {node_min.key} 位於 {node_min}\n')
    print(f'範例 4.1: 查找鍵值 = {key} 的節點')
    print(f'---> 找到 {node_found}，鍵值 = {node_found.key}\n')

else:
    print(f'---> 鍵值 = {key} 未找到\n')

key = 9
print(f'範例 4.2: 查找鍵值 = {key} 的節點及其父節點')
node_found, node_p, from_left = node_root.find_node_parent(key)
if node_found is None:
    print(f'---> 鍵值 = {key} 未找到。')
    if node_p is None:
        print(f'---> 父節點未找到。\n')
    else:
        print(f'---> 找到父節點 {node_p}，鍵值 = {node_p.key}\n')
else:
    print(f'---> 找到目標節點 {node_found}，鍵值 = {node_found.key}')
    if node_p is None:
        print(f'---> 父節點未找到。\n')
    else:
        print(f'---> 找到父節點 {node_p}，鍵值 = {node_p.key}\n')

# 7. 根據鍵值移除節點
key = 5
print(f'範例 5: 移除鍵值 = {key} 的節點')

node_removed = node_root.remove_node(key)
if node_removed == -2:
    print(f'鍵值 = {key} 未找到。\n')
else:
    print(f'節點 {node_removed}，鍵值 = {key} 移除成功。')
    print(f'排序後的鍵值列表： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')
    print(f'根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}\n')

# 8. 移除子樹
key = 9
node_found = node_root.find_node(key)
print(f'範例 6: 移除子樹，根節點位於 {node_found}，鍵值 = {node_found.key}')

node_found.remove_tree()
print(f'排序後的鍵值列表： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點\n')

# 9. 移除整個樹
print(f'範例 7: 移除整個二元搜尋樹，根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}')
node_root.remove_tree()
if BinaryTreeNode.root is None and BinaryTreeNode.count == 0:
    print(f'整個樹已移除。程式結束。')
