""" 
列表排序範例
本程式示範 Python 中的兩種列表排序方式：
1. 使用 sorted() 函數創建新的排序列表
2. 使用 sort() 方法在原列表上進行排序
"""

def show_original_list(li):
    """顯示原始列表及其類型"""
    print(f'原列表:\n\t{li}')
    print(f'\t類型: {type(li)}\n')

def show_sorted_list(s_li, sort_type):
    """顯示排序後的列表及其類型
    
    Args:
        s_li (list): 排序後的列表
        sort_type (str): 排序類型描述
    """
    print(f'{sort_type}:\n\t{s_li}\n\t類型: {type(s_li)}\n')

def main():
    """主函數，示範各種列表排序方式"""
    print(f'列表排序範例...')
    
    # 基本數字列表
    li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    show_original_list(li)
    
    # 1. 使用 sorted() 函數建立新的遞增排序列表
    s_li = sorted(li)
    show_sorted_list(s_li, "1. 用 sorted() 函數建立新的列表(遞增排序)")
    
    # 2. 使用 sort() 方法在原列表上進行遞增排序
    li.sort()
    show_sorted_list(li, "2. 用 sort() 方法於原列表重新排序(遞增排序)")
    
    # 3. 遞減排序示範
    s_li = sorted(li, reverse=True)
    show_sorted_list(s_li, "3. 用 sorted() 函式建立新的列表(遞減排序)")
    
    # 4. 在原列表上進行遞減排序
    li.sort(reverse=True)
    show_sorted_list(li, "4. 用 sort() 方法於原列表重新排序(遞減排序)")
    
    # 5. 絕對值排序示範
    print(f'絕對值排序範例...')
    li = [-6, -5, -4, 1, 2, 3]
    show_original_list(li)
    
    s_li = sorted(li, key=abs)
    show_sorted_list(s_li, "5. 用 sorted() 函式建立新的列表(絕對值遞增排序)")

if __name__ == '__main__':
    main()
