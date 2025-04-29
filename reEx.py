"""
這個程式展示 Python re 模組中的主要功能和用法
主要功能包括：
1. 列出 re 模組中的所有公開類別和函數
2. 進行模式匹配的示範
3. 展示編譯模式的重複使用
4. URL 匹配的示範
"""

import re
from inspect import getmembers, isclass, isfunction

def main():
    """
    主函數，負責執行程式的主要邏輯
    
    這個函數會依次執行以下功能：
    1. 列出 re 模組中的所有公開類別
    2. 列出 re 模組中的所有公開函數
    3. 示範模式匹配在字串中的使用
    4. 示範模式匹配在句子中的使用（忽略大小寫）
    5. 示範編譯模式的重複使用
    """
    # 1. 列出 re 模組中的類別
    print("\n顯示 re 模組中的類別：")
    for (name, _) in getmembers(re, isclass):
        if not name.startswith("_"):
            print(f'\t{name}')

    # 2. 列出 re 模組中的函數
    print("\n顯示 re 模組中的函數：")
    for (name, _) in getmembers(re, isfunction):
        if not name.startswith("_"):
            print(f'\t{name}')

    # 3. 匹配模式在字串中的示範
    print("\n匹配模式在字串中的示範：")
    text_to_search = '''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

Corey Schafer.com
321-555-4321
123.555.1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

    pattern = re.compile(r'abc')
    matches = pattern.finditer(text_to_search)
    print("匹配 abc 模式的結果：")
    for match in matches:
        print(f"\t位置: {match.span()}, 內容: '{match.group()}'")

    # 4. 匹配模式在句子中的示範（忽略大小寫）
    print("\n匹配模式在句子中的示範（忽略大小寫）：")
    sentence = "The quick brown fox jumps over the lazy dog."
    pattern = re.compile(r'fox', re.IGNORECASE)
    matches = pattern.finditer(sentence)
    print("匹配 fox 模式的結果：")
    for match in matches:
        print(f"\t位置: {match.span()}, 內容: '{match.group()}'")

    # 5. 可重複使用的編譯模式示範
    print("\n可重複使用的編譯模式示範：")
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://twitter.com",
        "https://www.instagram.com"
    ]

    # 匹配 URL 模式
    url_pattern = re.compile(r'https://(www\.)?([a-zA-Z0-9]+)(\.[a-zA-Z]+)')
    print("匹配 URL 模式的結果：")
    for url in urls:
        matches = url_pattern.finditer(url)
        for match in matches:
            print(f"\n原始 URL: {url}")
            print(f"\t完整匹配: {match.group(0)}")
            print(f"\t主域名: {match.group(2)}")
            print(f"\t頂層域名: {match.group(3)}")

if __name__ == "__main__":
    main()
