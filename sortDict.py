"""字典排序示範程式
這個程式示範如何使用 Python 對字典進行排序，包括：
1. 依鍵排序
2. 依值排序
3. 不同的排序方式和結果展示
"""

def sort_by_key(di):
	"""依字典的鍵進行排序
	
	Args:
		di (dict): 要排序的字典
		
	Returns:
		list: 排序後的鍵列表
	"""
	return sorted(di)

def sort_by_key_with_values(di):
	"""依字典的鍵進行排序，並保留鍵值對
	
	Args:
		di (dict): 要排序的字典
		
	Returns:
		list: 排序後的鍵值對列表
	"""
	return sorted(di.items(), key=lambda kv: (kv[0], kv[1]))

def sort_by_value(di):
	"""依字典的值進行排序
	
	Args:
		di (dict): 要排序的字典
		
	Returns:
		list: 排序後的鍵值對列表
	"""
	return sorted(di.items(), key=lambda kv: (kv[1], kv[0]))

def main():
	"""主函數，示範字典排序的各種方式"""
	# 原始字典
	di = {'name': 'Mike', 'job': 'programmer', 'age': '20', 'os': 'Mac'}
	print(f'原字典:\n{di}')
	print(f'\t類型: {type(di)}\n')

	# 1. 依鍵排序
	s_li = sort_by_key(di)
	print(f'1. 依字典用 sorted() 函式建立新的列表(依鍵遞增排序)...')
	print(f'\t其元素只含鍵，不含值:\n{s_li}')
	print(f'\t類型: {type(s_li)}\n')

	# 2. 依鍵排序並保留鍵值對
	s_li = sort_by_key_with_values(di)
	print(f'2. 依字典逐項用 sorted() 函式建立新的列表(依鍵遞增排序)...')
	print(f'\t其元素是含鍵及值元組:\n{s_li}')
	print(f'\t類型: {type(s_li)}\n')

	# 3. 依值排序
	s_li = sort_by_value(di)
	print(f'3. 依字典逐項用 sorted() 函式建立新的列表(依值遞增排序)...')
	print(f'\t其元素是含鍵及值元組:\n{s_li}')
	print(f'\t類型: {type(s_li)}\n')

if __name__ == '__main__':
	main()
