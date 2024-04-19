"""例子：寫入 TXT 新檔案和加入 TXT 舊檔案"""
solarSystem = (
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune")

# 寫入 plenets.txt 新檔案
fileName = 'sample/planets.txt'

with open(fileName, "w") as f:
    for planet in solarSystem:
        print(planet, file=f)
print(f'寫入 {f.name} 新檔案')

# 加入 plenets.txt 舊檔案
with open("planets.txt", "a") as f:
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

print(f'加入 {fileName} 舊檔案')
