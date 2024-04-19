
"""用隨機亂數產生器來設計一個擲骰子遊戲"""
import random
# pip install pillow if 'PIL' Module is missing.
from PIL import Image


def roll_dice():
    # store jpg file path in a list
    list = []
    file_prefix = "../Python/sample/dice"
    for x in range(6):
        jpg = Image.open(f"{file_prefix}{x+1}.jpg")
        list.append(jpg)

    while True:
        roll = input("Continue to roll dices? (Hit ENTER key) : ")
        if roll == "":
            # 按 'enter' to continue...
            pass
        else:
            # else to terminate
            break

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"===>Dice rolled: {dice1} and {dice2}\n")
        list[dice1 - 1].show()
        list[dice2 - 1].show()


# Game Example: rolling two dices
if __name__ == '__main__':
    print(f"Game starting...")
    roll_dice()
    print(f"Game ended.")
