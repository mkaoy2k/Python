"""A show-hand game with 3 shapes: scissors, rock and paper.
In each show-hand, three possible outcomes: a draw, a win or a loss.
A player who shows rock will beat another player who shows scissors
but will lose to one who shows paper;
and a play of paper will lose to a play of scissors.
If both players choose the same shape, the show-hand is tied.
The winner of the game wins two show-hands out of three.
剪刀石頭布遊戲，平手再戰，先贏兩戰是羸家"""

import random

def u_win(comp_guess_idx, ur_guess_idx):
    """Compare two integers (0-2)
    0: 剪刀
    1: 石頭
    2: 布
    Return 'True' if you win, or 'False' if you loose, 'None' for tie/even."""

    if comp_guess_idx == ur_guess_idx:
        return None

    elif comp_guess_idx == 2 and ur_guess_idx == 0:
        return True

    elif comp_guess_idx == 0 and ur_guess_idx == 2:
        return False

    elif comp_guess_idx < ur_guess_idx:
        return True

    else:
        return False


# Main progem
guesses = ['剪刀', '石頭', '布']
menu = """
0: 剪刀
1: 石頭
2: 布
"""

# 三戰兩勝，平手不算
best_max = 2
count, count_u, count_c = 0, 0, 0

print(f'比賽開始...三戰兩勝，平手不算')
while count_u < best_max and count_c < best_max:
    count += 1
    print(f'第 {count} 戰開始...')

    # computer pick one here randomly
    comp_guess = random.choice(guesses)
    comp_guess_idx = guesses.index(comp_guess)

    # display menu for you
    print(f'{menu}')

    # make your guess 0-2
    ur_guess_idx = int(input("請選相應號碼: "))
    if ur_guess_idx not in [0, 1, 2]:
        print(f'\t電腦選{comp_guess_idx}<--->你選{ur_guess_idx}')
        print(f'你來亂的吼！選0,1,2 好嗎?\n')
        print(f'目前比數 電腦 {count_c}:{count_u} 你\n')
        continue

    ur_guess = guesses[ur_guess_idx]

    winner = u_win(comp_guess_idx, ur_guess_idx)
    if winner == None:
        print(f'===> 第 {count} 戰結果: 我們平手')

    elif winner:  # is you, i.e. == True:
        print(f'===> 第 {count} 戰結果: 恭喜你贏了！')
        count_u += 1

    else:
        print(f'===> 第 {count} 戰結果: 喔你輸了！')
        count_c += 1

    print(f'===> 電腦出{comp_guess}<--->你出{ur_guess}')
    print(f'===> 目前比數 電腦 {count_c}:{count_u} 你\n')


if count_u == best_max:
    print(f'===> 比賽結束 你勝 {count_u}:{count_c} 共 {count} 戰\n')
else:
    print(f'===> 比賽結束 你敗 {count_u}:{count_c} 共 {count} 戰\n')

print(f'有空再來玩！\n')
