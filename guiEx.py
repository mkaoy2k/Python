from re import I
import pyautogui
import pathlib

sampleDir = pathlib.Path(__file__).parent / "sample"
sampleDir.mkdir(parents=True, exist_ok=True)
screenFile = sampleDir / "screenshot.png"
myScreenshot = pyautogui.screenshot()   # 截圖
myScreenshot.save(screenFile)         # 儲存
print(f'\nCheck created screenshot at: {screenFile}\n')

# Screen functions
print(f'Resolution of my screen: {pyautogui.size()}')
print(f'Is the coordinate (100,100) on my screen: {pyautogui.onScreen(100, 100)}')
print(f'Is the coordinate (10000,10000) on my screen: {pyautogui.onScreen(10_000, 10_000)}\n')

# Mouse functions
print(f'Position of my mouse: {pyautogui.position()}')
pyautogui.moveTo(500, 500, duration=3)
print(f'Position of my mouse: {pyautogui.position()}')
pyautogui.moveRel(100, 100, duration=3)
print(f'Position of my mouse: {pyautogui.position()}')
