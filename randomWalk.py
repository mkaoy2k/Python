"""本程式模擬隨機漫步問題，研究在隨機行走的情況下，
   何時可以回到起點而不需要打車。使用兩種不同的方法進行模擬：
   1. 基本隨機漫步（random_walk）
   2. 向量移動方式（random_walk_v2）
"""
import random

def random_walk(n):
    """執行 n 步基本隨機漫步
    
    Args:
        n (int): 步數
        
    Returns:
        tuple: 最終座標 (x, y)
        
    詳細說明：
        本函數使用東(E)、西(W)、南(S)、北(N)四個方向
        來模擬隨機漫步，每次隨機選擇一個方向移動。
    """
    x, y = 0, 0
    for i in range(n):
        step = random.choice(['E', 'W', 'S', 'N'])
        if step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
        elif step == 'S':
            y -= 1
        else:
            y += 1
    return (x, y)

def random_walk_v2(n):
    """執行 n 步向量移動方式的隨機漫步
    
    Args:
        n (int): 步數
        
    Returns:
        tuple: 最終座標 (x, y)
        
    詳細說明：
        本函數使用向量方式來模擬隨機漫步，
        每次隨機選擇一個方向向量移動。
        可能的向量：[(0,1)北, (0,-1)南, (1,0)東, (-1,0)西]
    """
    x, y = 0, 0
    for _ in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

def main():
    """程式進入點：執行隨機漫步測試並顯示結果
    
    主要功能：
    1. 進行 25 次 10 步的隨機漫步測試
    2. 計算在 10,000 次模擬中，不同步數下
       能在 5 個區塊內返回起點的機率
    """
    print('基本隨機漫步測試...')
    for _ in range(25):
        walk = random_walk(10)
        print(f'{walk} \n\t距離起點 = {abs(walk[0]) + abs(walk[1])}')

    print('\n向量移動方式測試...')
    for _ in range(25):
        walk = random_walk_v2(10)
        print(f'{walk} \n\t距離起點 = {abs(walk[0]) + abs(walk[1])}')

    number_of_walks = 10_000
    blocks_limit = 5
    print('\n分析不同步數下，不打車回起點的機率...')
    for walk_len in range(1, 36):
        no_taxi = 0  # 距離起點 <= 5 個區塊的次數
        for _ in range(number_of_walks):
            x, y = random_walk_v2(walk_len)
            if abs(x) + abs(y) <= blocks_limit:
                no_taxi += 1
        no_taxi_percentage = float(no_taxi) / number_of_walks
        print(f'走 {walk_len} 步: {100 * no_taxi_percentage:.2f}% 時可以不打車')

if __name__ == '__main__':
    main()

"""Last observation about the result: 31 or 33
Q: Why any even walk length has lower chance to walk home without taxi
than 2 adjacent odd walk lengths?"""
