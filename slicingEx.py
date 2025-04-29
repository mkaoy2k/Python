"""
此程式示範 Python 中的列表和字串切片功能
包含正向和反向索引的範例，以及字串處理的應用
"""

def main():
    """
    主函數，示範列表和字串的切片操作
    """
    # 測試列表
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('測試列表:\n', my_list)
    
    # 基本索引範例
    print(f'\n基本索引範例')
    print('\t第一個元素:', my_list[0])
    print('\t最後一個元素:', my_list[-1])
    print('\t元素範圍 0-5:', my_list[0:6])
    print('\t元素範圍 5-9:', my_list[5:])
    
    # 間隔索引範例
    print(f'\n間隔索引範例')
    print('\t偶數:', my_list[2:-1:2])
    print('\t反向偶數:', my_list[-2:1:-2])
    print(f'\t反轉整個列表:{my_list[::-1]}')
    
    # 字串切片範例
    print(f'\n字串切片範例')
    sample_url = 'http://coreyms.com'
    print(f'\t測試字串:"{sample_url}"')
    
    # 字串處理範例
    print(f'\t反轉 URL:==>{sample_url[::-1]}<==')
    print(f'\t取得頂級網域名稱:{sample_url[-4:]}')
    print(f'\t移除 http://:{sample_url[7:]}')
    print(f'\t移除 http:// 和頂級網域名稱:{sample_url[7:-4]}')

if __name__ == '__main__':
    main()
