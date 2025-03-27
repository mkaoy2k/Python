"""用隨機亂數產生器來設計一個電腦讓我們猜數字遊戲"""
import random

print('讓我們猜數字遊戲開始...')

# 初始化遊戲變數
# 紀錄猜數的次數
counter = 0
# 儲存玩家的當前猜數
guess = 0

# 設定猜數的極限
limit = 5
print(f'猜 {limit} 次為限')

# 設定猜數的上下限
min_num = 100
max_num = 999

# 產生一個介於 min_num 和 max_num 之間的隨機數
answer = random.randint(min_num, max_num)

# 主要遊戲迴圈
while counter < limit:
    # 更新猜數範圍根據前一次猜數
    prompt = f'猜一正整數 ({min_num} - {max_num}): '
    
    try:
        # 取得玩家的猜數並轉換為整數
        guess = int(input(prompt))
        
        # 檢查猜數是否在有效範圍內
        if guess < min_num or guess > max_num:
            print(f'請輸入 {min_num} 到 {max_num} 之間的數字')
            continue
        
        counter += 1
        
        # 檢查猜數是否正確
        if guess == answer:
            print(f'恭喜猜中了 {answer}！共猜了 {counter} 次\n')
            break
        
        # 提供反饋以幫助玩家
        if guess > answer:
            max_num = guess
        else:
            min_num = guess
        
        # 顯示剩餘猜數次數
        if counter >= limit:
            print(f'對不起，您輸了！猜超過 {limit} 次，答案是 {answer}！\n')
            break
        else:
            print(f'沒中，請續猜！剩下 {limit - counter} 次\n')
    
    except ValueError:
        print('請輸入一個有效的數字')

print('遊戲結束\n')
