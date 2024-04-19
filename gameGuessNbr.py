"""用隨機亂數產生器來設計一個電腦讓我們猜數字遊戲"""
import random

print('電腦讓我們猜數字遊戲開始...')

# 猜數的次數 設初值
counter = 0
guess = 0

# 猜數的極限 設初值
limit = 5
print(f'猜 {limit} 次為限')

# 猜數的上下限 設初值
min_num = 100
max_num = 999

answer = random.randint(min_num, max_num)

while counter < limit:

    counter += 1   # counter 加一
    prompt = f'猜一正整數 ({min_num} - {max_num}): '
    guess = int(input(prompt))

    if guess == answer:
        print(f'恭喜猜中了 {answer}！共猜了 {counter} 次\n')
        break
    elif guess > answer:
        max_num = guess
    else:
        min_num = guess

    if counter >= limit:
        print(f'對不起，您輸了！猜超過 {limit} 次，答案是 {answer}！\n')
        break
    else:
        print(f'沒中，請續猜！剩下 {limit - counter} 次\n')

print('遊戲結束\n')
