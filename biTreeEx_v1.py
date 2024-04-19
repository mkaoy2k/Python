from biTree_v1 import biNode
import glog as log

""" Example code, demonstrating:
    1. Build a binary tree from a list of integers
    2. Showing btree info:
        1) print_keys()
        2} sort_keys()
    3. Finding out
        1) max node of the btree
        2) min node of the btree
    4. Finding a node given a key
    5. Removing a node given a key
    6. Discard the whole tree
"""

# log.setLevel("DEBUG")
numbers = [5, 4, 1, 9, 5, 3, 7, 6, 8, 2]
print(f'Number of items in {numbers} = {len(numbers)}\n')

# create root of binary tree
node_root = biNode(numbers.pop())
print(f'Example 1: Built a binary tree with root key = {biNode.root.key}')

# To iterate from the rest elements in the list
for key in numbers:
    bn = biNode(key)
    if node_root.insert_node(bn) == -1:
        print(f'Example 1: duplicated key = {bn.key}')
        bn.free_node()
    else:
        print(f'Example 1: Node at {bn} inserted with key = {bn.key}')
print()

# print the sorted keys
print(f'Example 2.1: printing keys of the whole btree:', end=' ')
node_root.print_keys()
print()

# To print the sorted keys in a list
print(
    f'Example 2.2: sorting keys of the whole btree: {biNode.root.sort_keys()} with {biNode.count} node(s)')
print(f'root at {biNode.root} with key = {biNode.root.key}\n')

# To print the max node and key
node_max = node_root.find_node_max()
print(f'Example 3.1: maximum key of the btree = {node_max.key} at {node_max}')

# To print the min node and key
node_min = node_root.find_node_min()
print(f'Example 3.2: minimum key = {node_min.key} at {node_min}\n')

# Example: To find a node from btree given a key
key = 7
print(f'Example 4: Finding a node with key = {key}')
node = node_root.find_node(key)
if node != -2:
    print(f'node type: {type(node)} at {node} with key= {node.key}\n')

# Example: To remove a node from btree given a key
key = 7

# find the node with the key
# return -2 if key not found
node_target = node_root.find_node(key)
if node_target == -2:
    print(f'key= {key} not found.\n')
else:
    print(f'Example 5: Removing target node at {node_target} with key = {key}')

    if node_root.remove_node(node_target) == 0:
        print(f'key = {key} removed successfully.')
        print(f'{biNode.root.sort_keys()} with {biNode.count} node(s)')
        print(f'root at {biNode.root} with key = {biNode.root.key}\n')
    else:
        print(f'key= {key} remove_node() failed.\n')

# Discarding the whole tree
print(
    f'Example 6: Discarding btree, root at {biNode.root} with key = {biNode.root.key}')
biNode.discard_tree()
print(f'The whole tree discarded. Program terminated.')
