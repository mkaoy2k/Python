"""剪刀石頭布遊戲

這是一個剪刀石頭布遊戲，玩家需要贏得兩次才能獲勝。
每次出拳有三種可能的結果：平手、勝利或失敗。
遊戲規則：
- 石頭打敗剪刀
- 剪刀打敗布
- 布打敗石頭
- 如果雙方出拳相同，則平手
"""

import random

# 定義遊戲常數
SHAPE_NAMES = {
    0: "剪刀",
    1: "石頭",
    2: "布"
}

# 定義勝利規則（鍵：勝利者，值：輸家）
WIN_RULES = {
    0: 2,  # 剪刀打敗布
    1: 0,  # 石頭打敗剪刀
    2: 1   # 布打敗石頭
}

class SRPGame:
    """剪刀石頭布遊戲類別"""
    
    def __init__(self):
        """初始化遊戲"""
        self.comp_wins = 0
        self.player_wins = 0
        self.rounds = 0
        
    def get_computer_choice(self):
        """獲取電腦的選擇"""
        return random.randint(0, 2)
    
    def get_player_choice(self):
        """獲取玩家的選擇"""
        while True:
            print("\n請選擇：")
            for idx, shape in SHAPE_NAMES.items():
                print(f"{idx}: {shape}")
            
            try:
                choice = int(input("輸入數字選擇："))
                if choice in SHAPE_NAMES:
                    return choice
                print("無效的選擇，請重新輸入！")
            except ValueError:
                print("請輸入數字！")
    
    def determine_winner(self, comp_choice, player_choice):
        """判斷勝負
        
        Args:
            comp_choice (int): 電腦的選擇
            player_choice (int): 玩家的選擇
            
        Returns:
            tuple: (勝利者, 遊戲結果描述)
        """
        if comp_choice == player_choice:
            return None, "平手！"
            
        if WIN_RULES[player_choice] == comp_choice:
            self.player_wins += 1
            return "player", f"你贏了！{SHAPE_NAMES[player_choice]}打敗{SHAPE_NAMES[comp_choice]}"
            
        self.comp_wins += 1
        return "computer", f"電腦贏了！{SHAPE_NAMES[comp_choice]}打敗{SHAPE_NAMES[player_choice]}"
    
    def play_round(self):
        """進行一輪遊戲"""
        self.rounds += 1
        print(f"\n第 {self.rounds} 輪")
        
        comp_choice = self.get_computer_choice()
        player_choice = self.get_player_choice()
        
        print(f"\n電腦出了：{SHAPE_NAMES[comp_choice]}")
        print(f"你出了：{SHAPE_NAMES[player_choice]}")
        
        winner, result = self.determine_winner(comp_choice, player_choice)
        print(result)
        
        print(f"\n目前戰績：")
        print(f"你贏了 {self.player_wins} 次")
        print(f"電腦贏了 {self.comp_wins} 次")
        
        if self.player_wins >= 2 or self.comp_wins >= 2:
            return True
        return False
    
    def play_game(self):
        """開始遊戲"""
        print("""剪刀石頭布遊戲開始！
規則：
- 先贏兩次的一方獲勝
- 如果平手，繼續進行下一輪
- 電腦會隨機出拳""")
        
        while True:
            if self.play_round():
                break
        
        if self.player_wins >= 2:
            print("\n恭喜你獲勝！")
        else:
            print("\n電腦獲勝！")
        
        print("\n遊戲結束！")

if __name__ == "__main__":
    game = SRPGame()
    game.play_game()
