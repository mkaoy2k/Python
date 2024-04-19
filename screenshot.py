"""
This example takes a screen shot using 'pyautogui' module
"""

import pyautogui


# Initialize the folder where data is located
data_path = 'sample'  # relative to the current dir

# all data files in this example
file_write = f'{data_path}/screenshot.png'

myScreenshot = pyautogui.screenshot()   # 截圖
myScreenshot.save(file_write)         # 儲存
