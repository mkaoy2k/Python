"""
範例程式碼，展示 Python 中元組的各種常用操作，包括：
- 元組的元素操作（出現次數、索引位置）
- 列表與元組之間的轉換
- 字串與元組的轉換
"""

def main():
    """
    主函數，示範元組的各種操作
    """
    # 建立數字元組
    numbers = (1, 9, 8, 1, 2, 4, 7, 1)
    print(f'數字元組: {numbers}\n')
    
    # 檢查元素出現次數
    item_new = 1
    print(f'1. 元組中 {item_new} 出現次數: {numbers.count(item_new)}\n')
    
    # 找出元素第一次出現的位置
    print(f'2. 元組中 {item_new} 第一次出現的索引: {numbers.index(item_new)}\n')
    
    # 建立課程元組
    courses = ('歷史', '物理', '電腦', '物理')
    print(f'課程元組: {courses}\n')
    
    # 元組轉換為字串
    course_str = ' - '.join(courses)
    print(f'3. 元組轉字串: {course_str}\n')
    
    # 字串轉換為列表，再轉換為元組
    new_list = course_str.split(' - ')
    new_tuple = tuple(new_list)
    print(f'4. 字串轉元組: {new_tuple}\n')

if __name__ == '__main__':
    main()
