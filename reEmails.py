"""
這個程式使用正則表達式來匹配和驗證電子郵件地址
主要功能：
1. 使用兩種不同的正則表達式模式來匹配電子郵件地址
2. 顯示匹配結果
"""

import re

def match_emails(emails, pattern):
    """
    使用正則表達式匹配電子郵件地址
    
    參數:
        emails (str): 包含電子郵件地址的字串
        pattern (re.Pattern): 正則表達式模式
    
    返回:
        None: 直接打印匹配結果
    """
    matches = pattern.finditer(emails)
    for match in matches:
        print(f'\t{match}')

def main():
    """
    主函數，包含測試電子郵件地址和正則表達式模式
    """
    # 測試電子郵件地址
    emails = '''
    mkaoy2k@gmail.com
    mkaoy2k@university.edu
    mkaoy2k-321@my-work.net
    '''
    
    # 第一個模式：允許更多特殊字元
    print("第一個模式（允許更多特殊字元）:")
    pattern1 = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    print(f'模式：{pattern1}')
    match_emails(emails, pattern1)
    print()
    
    # 第二個模式：較嚴格的限制
    print("第二個模式（較嚴格的限制）:")
    pattern2 = re.compile(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}')
    print(f'模式：{pattern2}')
    match_emails(emails, pattern2)

if __name__ == "__main__":
    main()
