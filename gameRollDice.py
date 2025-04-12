"""擲骰子遊戲

使用隨機數生成器模擬擲骰子的遊戲，並顯示對應的骰子圖片。
"""

import random
import sys
import subprocess

try:
    from PIL import Image
    from pathlib import Path
except ImportError:
    print("\n找不到必要的 PIL 模組。")
    print("正在嘗試自動安裝 Pillow...\n")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        from PIL import Image
        from pathlib import Path
        print("\nPillow 已成功安裝！")
    except Exception as e:
        print(f"\n安裝失敗：{str(e)}")
        print("請手動執行以下命令安裝 Pillow：")
        print("pip install Pillow")
        sys.exit(1)

# 定義骰子圖片路徑
current_dir = Path(__file__).parent
DICE_PATH = current_dir / 'sample'

def load_dice_images():
    """載入所有骰子圖片
    
    Returns:
        list: 包含 6 個骰子圖片的清單
    """
    dice_images = []
    for i in range(1, 7):  # 1 到 6 點的骰子
        image_path = DICE_PATH / f"dice{i}.jpg"
        try:
            dice_images.append(Image.open(image_path))
        except FileNotFoundError:
            print(f"找不到骰子圖片: {image_path}")
            return None
    return dice_images

def roll_dice():
    """模擬擲骰子並顯示結果
    
    使用者可以選擇繼續擲骰子或結束遊戲。
    """
    # 載入骰子圖片
    dice_images = load_dice_images()
    if dice_images is None:
        print("遊戲無法開始，請確認骰子圖片檔案存在")
        return

    print("\n歡迎來到擲骰子遊戲！")
    print("-" * 30)
    print("按 Enter 鍵繼續擲骰子")
    print("輸入 'q' 退出遊戲")
    print("-" * 30)

    while True:
        user_input = input("\n繼續擲骰子？(按 Enter 鍵繼續, 或輸入 q 退出): ")
        
        if user_input.lower() == 'q':
            print("\n感謝遊玩！再見！")
            break
            
        # 產生隨機數字 (1-6)
        dice_number = random.randint(1, 6)
        print(f"\n擲出了 {dice_number} 點！")
        
        # 顯示對應的骰子圖片
        dice_images[dice_number - 1].show()

def main():
    """遊戲主程式"""
    try:
        roll_dice()
    except KeyboardInterrupt:
        print("\n遊戲已中斷。感謝遊玩！")

if __name__ == '__main__':
    main()
