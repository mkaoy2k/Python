"""
loopEx.py - Python循環結構示範
本程式展示了Python中的各種循環結構，包括for循環、while循環、break和continue語句，以及嵌套(nested)循環。
"""

def main():
    """主函數 - 示範各種循環結構"""
    # 數字列表示範
    nums = [1, 2, 3, 4, 5]
    print('數字列表:', nums)
    print('\t正在遍歷每個項目...')

    # 基本for循環
    for num in nums:
        print(f'\t{num}')

    # break和continue在循環中的使用
    print('\n\t從for循環中跳出...')
    for num in nums:
        if num == 3:
            print(f'\t{num} 找到了！')
            break
        print(f'\t{num}')

    print('\n\t在for循環中跳過...')
    for num in nums:
        if num == 3:
            print(f'\t{num} 找到了！')
            continue
        print(f'\t{num}')

    # 嵌套for循環
    print('\n\t兩層嵌套循環...')
    for num in nums:
        for letter in 'abc':
            print(f'\t{num} {letter}')

    # range()函數示範
    print('\n從0到9的for循環...')
    for i in range(10):
        print('   ', i)

    print('\n從1到10的for循環...')
    for i in range(1, 11):
        print('   ', i)

    # while循環示範
    print('\n從0到9的while循環...')
    x = 0
    while x < 10:
        print(f'\t{x}')
        x += 1

if __name__ == '__main__':
    main()
