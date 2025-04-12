"""
這個程式示範如何使用 Python 創建和附加文字檔案。
主要功能包括：
1. 創建新的文字檔案並寫入太陽系行星名稱
2. 在現有檔案中附加行星說明文字
3. 使用 pathlib 模組處理檔案路徑

程式會在當前目錄下的 'sample' 子目錄中創建 planets.txt 檔案，
並在其中附加行星名稱列表和詳細說明。
"""
solarSystem = (
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune")

from pathlib import Path

current_dir = Path(__file__).parent
fileName = current_dir / 'sample/planets.txt'

with open(fileName, "w") as f:
    for planet in solarSystem:
        print(planet, file=f)
print(f'創建 {f.name} 新檔案完成\n')

# 附加行星說明到 planets.txt 舊檔案
with open(fileName, "a") as f:
    print(80 * "=", file=f)
    comment = """成為太陽系行星的天體有8個：
    1. 水星 (Mercury)
    2. 金星 (Venus)
    3. 地球 (Earth)
    4. 火星 (Mars)
    5. 木星 (Jupiter)
    6. 土星 (Saturn)
    7. 天王星 (Uranus)
    8. 海王星 (Neptune)"""

    print(comment, file=f)

print(f'附加行星說明到 {fileName} 舊檔案完成\n')
