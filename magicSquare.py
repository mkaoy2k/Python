"""
生成奇數階幻方的程式

這個程式可以生成任意奇數階的幻方矩陣，並顯示其幻和。
幻方的特點是：
1. 每行、每列和兩條對角線的數字之和都相等
2. 使用連續的自然數填充
3. 只能生成奇數階的幻方

使用方法：
直接運行此程式，將自動生成並顯示奇數階的幻方
"""

def genOddSquare(n):
    """
    生成奇數階幻方
    
    參數:
    n (int): 幻方的階數，必須為奇數
    
    動作:
    如果 n 不是奇數，則引發 ValueError
    """
    # 檢查 n 是否為奇數
    if n % 2 == 0:
        raise ValueError(f"n 必須為奇數，但輸入的是 {n}")
    
    # 創建 n x n 的矩陣，初始值為0
    magicSquare = [[0 for x in range(n)] for y in range(n)]

    # 初始化數字1的位置
    i = n // 2  # 初始行位置
    j = n - 1   # 初始列位置

    # 填充幻方矩陣
    num = 1
    while num <= (n * n):
        # 處理邊界情況
        if i == -1 and j == n:  # 超出上邊和右邊
            j = n - 2
            i = 0
        else:
            # 處理超出右邊的情況
            if j == n:
                j = 0
            # 處理超出上邊的情況
            if i < 0:
                i = n - 1

        # 檢查當前位置是否已被佔用
        if magicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        # 移動到下一個位置
        j = j + 1
        i = i - 1

    # 顯示結果
    print(f"{n}階幻方")
    print(f"幻和 = {n * (n * n + 1) // 2}\n")

    # 顯示幻方矩陣
    for i in range(0, n):
        for j in range(0, n):
            print(f'{magicSquare[i][j]:2d}', end=' ')
            if j == n - 1:
                print()

def main():
    """
    主函數，生成並顯示多個奇數階的幻方
    """
    # 生成從3到9的所有奇數階幻方
    for odd in range(3, 10, 2):
        genOddSquare(odd)
        print('*' * 20)

if __name__ == '__main__':
    main()
