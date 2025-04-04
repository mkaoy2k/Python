from biTree_v2 import BinaryTreeNode
import logging

"""
範例程式碼，展示：
1. 從整數列表建立二元樹
2. 顯示二元樹資訊：
   1) 以中序方式印出鍵值
   2) 將鍵值排序並存儲在列表中
3. 查詢：
   1) 查詢二元樹中的最大節點
   2) 查詢二元樹中的最小節點
   3) 查詢子樹中的最大節點
   4) 查詢子樹中的最小節點
4. 根據鍵值查找節點：
   1) 查找具有匹配鍵值的節點
   2) 查找具有匹配鍵值的目標節點及其父節點（如果有的話）
5. 根據鍵值移除節點
6. 移除子樹
7. 移除整個樹
"""

# 設定 logging 等級為 DEBUG
logging.basicConfig(level=logging.DEBUG)

# 建立測試數據
numbers = [5, 4, 1, 9, 5, 3, 7, 6, 8, 2]
print(f'測試數據數量： {numbers} = {len(numbers)}\n')

# 1. 建立二元樹根節點
node_root = BinaryTreeNode(numbers.pop())
print(f'範例 1: 建立二元樹，根節點鍵值 = {BinaryTreeNode.root.key}')

# 2. 迴圈插入剩餘的節點
for key in numbers:
    bn = BinaryTreeNode(key)
    if node_root.insert_node(bn) == -1:
        print(f'範例 1: 重複鍵值 = {bn.key}')
        bn.free_node()
    else:
        print(f'範例 1: 已插入節點，位於 {bn}，鍵值 = {bn.key}')
print()

# 3. 印出鍵值
print(f'範例 2.1: 印出鍵值：', end=' ')
node_root.print_keys()
print()

# 4. 印出排序後的鍵值列表
print(
    f'範例 2.2: 排序整個二元樹的鍵值： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')
print(f'根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}\n')

# 5. 查詢最大和最小節點
node_max = node_root.find_node_max()
print(f'範例 3.1: 最大節點的鍵值為 {node_max.key}')

node_min = node_root.find_node_min()
print(f'範例 3.2: 最小節點的鍵值為 {node_min.key}')
print()

# 6. 根據鍵值查找節點
search_keys = [3, 9, 10]
for key in search_keys:
    node = node_root.find_node(key)
    if node == -2:
        print(f'範例 4.1: 鍵值 {key} 未找到')
    else:
        print(f'範例 4.2: 找到鍵值 {key} 的節點')
print()

# 7. 根據鍵值移除節點
remove_keys = [3, 9, 10]
for key in remove_keys:
    if node_root.remove_node(key) == 0:
        print(f'鍵值 {key} 移除成功。')
        print(f'排序後的鍵值列表： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點')
        print(f'根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}\n')
    else:
        print(f'鍵值 {key} 未找到。\n')

# 8. 移除子樹
key = 5  # 選擇一個存在的鍵值作為子樹的根節點
node_found = node_root.find_node(key)
if node_found != -2:
    print(f'範例 6: 移除子樹，根節點位於 {node_found}，鍵值 = {node_found.key}')
    node_found.remove_tree()
    print(f'排序後的鍵值列表： {BinaryTreeNode.root.sort_keys()}，共 {BinaryTreeNode.count} 個節點\n')
else:
    print(f'範例 6: 鍵值 {key} 未找到，無法移除子樹\n')

# 9. 移除整個樹
print(f'範例 7: 移除整個二元樹，根節點位於 {BinaryTreeNode.root}，鍵值 = {BinaryTreeNode.root.key}')
node_root.remove_tree()
if BinaryTreeNode.root is None and BinaryTreeNode.count == 0:
    print(f'整個樹已移除。程式結束。')
