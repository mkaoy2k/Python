"""
範例程式碼，展示 Python 中元組的各種常用操作，包括：
- 元組的基本屬性（長度、最大值、最小值、總和）
- 列表與元組之間的轉換
"""

def main():
    """主函數，展示元組操作示範"""
    # 建立一個數字元組
    numbers = (9, 8, 1, 2, 4, 7)
    print(f'數字元組: {numbers}\n')

    # 1. 取得元組長度
    print(f'1. 元組長度: {len(numbers)}\n')

    # 2. 取得元組中的最大值
    print(f'2. 元組中最大元素: {max(numbers)}\n')

    # 3. 取得元組中的最小值
    print(f'3. 元組中最小元素: {min(numbers)}\n')

    # 4. 計算元組中所有元素的總和
    print(f'4. 元組總計: {sum(numbers)}\n')

    # 5. 列表與元組轉換示範
    courses_list = ['歷史', '物理', '電腦', '物理']
    courses_tuple = tuple(courses_list)
    print(f'課程列表: {courses_list}\n')
    print(f'5. 列表轉元組: {courses_tuple}\n')
    print(f'\t元組轉列表: {list(courses_tuple)}\n')

if __name__ == '__main__':
    main()
