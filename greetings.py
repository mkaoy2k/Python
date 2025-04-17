"""
greetings.py

本檔案示範如何使用 FastAPI 建立一個簡單的 Web API，並包含互動式命令列輸入與多種問候函式。

主要內容說明：
1. 使用 FastAPI 建立一個 Web 應用，當用戶端以 GET 請求造訪根目錄 ("/") 時，會回傳 {"message": "Hello, World!"}。
2. 將回傳訊息的功能封裝於 print_hello3() 函式中，方便在 API 與主程式重複使用。
3. 定義 input_name() 函式，讓使用者可以於命令列互動式輸入名字。
4. 於 __main__ 區塊中，示範如何在命令列下執行各種問候函式與互動功能。
5. 若以 uvicorn greetings:app --reload 執行，則會啟動 FastAPI 伺服器，提供 Web API 服務。

適用情境：
- 學習 FastAPI 基本用法
- 熟悉 Python 函式的封裝與重複利用
- 練習命令列互動與 Web API 並存的程式結構
提供兩種方式來實現命令列互動打招呼功能：

1. 字串格式化方法
   - 使用 Python 的 format() 方法來格式化字串
   - 適用於 Python 2.x 和 3.x 版本

2. f-字串方法
   - 使用 Python 3.x 的 f-string 指令來格式化字串
   - 提供更簡潔的字串格式化方式

使用範例：
```python
# 使用預設值
print_hello1(input_name())

# 自定義問候語
print_hello2(input_name(), greeting="你好", welcome="歡迎光臨")
```

注意事項：
- 程式使用中文輸入介面
- 支援 Python 3.x 版本
- f-string 方法僅適用於 Python 3.x 版本

作者：Michael Kao
日期：2025-04-15
"""

# 打招呼Web 應用
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return print_hello3()

def input_name(name=None):
    """ 呼叫輸入函式 input(<提示字串>)，
    Python 能印出一段提示字串，然後等使用者輸入資訊，按 enter 鍵後，返回名字字串。

    用法：
        input_name('<你的名字>')

    1. <你的名字>忽略時，會要求輸入。
    2. 輸入空白時，預設值是'尤勇'
    """

    if name == None:
        # <你的名字>忽略時，呼叫 input(<提示字串>)函式
        name = input("請問你的名字叫: ")
    else:
        if name == '':
            name = '尤勇'   # 輸入空白時，用預設值
    return name


def print_hello1(name,
                 greeting='哈囉',
                 welcome='歡迎'
                 ):
    """
    以字串物件的 'format' 方法列印

    用法：
        print_hello1(greeting, name)
    """
    message1 = '{}, {}. {}!'.format(
        greeting,
        name,
        welcome)
    print(message1)


def print_hello2(name,
                 greeting='哈囉',
                 welcome='歡迎'
                 ):
    """
    Python 版本3以後才有的以'f-字串指令'列印

    用法：
        print_hello2(greeting, name)
    """
    message2 = f'{greeting}, {name}. {welcome}!'
    print(message2)

def print_hello3():
    return {"message": "Hello, World!"}

if __name__ == '__main__':
    greeting='哈囉'
    welcome='歡迎'
    print(f'{greeting}, {input_name()}. {welcome}!')
    print(f'{greeting}, {input_name(name="")}. {welcome}!')
    print(f'{greeting}, {input_name(name="Michael")}. {welcome}!')

    print_hello1(name='Michael 1')
    print_hello2(name='Michael 2')
    print_hello3()