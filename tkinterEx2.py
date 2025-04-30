"""
Tkinter 應用程式範例
這個程式示範了基本的 Tkinter GUI 界面，
- 包含兩個框架，每個框架都有輸入框和清單框
- 每個框架都有輸入和清除按鈕
"""

import tkinter as tk
from tkinter import ttk


def main():
    """
    應用程式的主要進入點。
    
    初始化 Application 類別的實例並啟動主要事件循環。
    """
    app = Application()
    app.mainloop()


class Application(tk.Tk):
    """
    主應用程式視窗類別。
    
    屬性:
        title: 視窗標題
    
    方法:
        __init__(): 初始化視窗並配置網格布局
    """
    def __init__(self):
        """
        初始化主應用程式視窗。
        
        設置視窗標題並配置網格布局，
        創建兩個輸入表單並添加到網格中。
        """
        super().__init__()
        self.title("簡單應用程式")

        # 設置網格權重
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        # 創建並配置第一個輸入表單
        frame = InputForm(self)
        frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # 創建並配置第二個輸入表單
        frame2 = InputForm(self)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


class InputForm(ttk.Frame):
    """
    輸入表單類別。
    
    屬性:
        entry: 輸入欄位
        entry_btn: 新增按鈕
        entry_btn2: 清除按鈕
        text_list: 列表框
    
    方法:
        __init__(): 初始化輸入表單
        add_to_list(): 將輸入文字添加到列表
        clear_list(): 清除列表中的所有項目
    """
    def __init__(self, parent):
        """
        初始化輸入表單。
        
        設置網格布局，創建輸入欄位和按鈕，
        並綁定相應的事件處理函數。
        
        參數:
            parent: 親元件
        """
        super().__init__(parent)

        # 設置網格權重
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # 創建輸入欄位
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, sticky="ew")

        # 綁定 Enter 鍵到添加函數
        self.entry.bind("<Return>", self.add_to_list)

        # 創建添加按鈕
        self.entry_btn = tk.Button(self, text="添加", command=self.add_to_list)
        self.entry_btn.grid(row=0, column=1)

        # 創建清除按鈕
        self.entry_btn2 = tk.Button(self, text="清除", command=self.clear_list)
        self.entry_btn2.grid(row=0, column=2)

        # 創建列表框
        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")

    def add_to_list(self, _event=None):
        """
        將輸入的文字添加到列表中。
        
        參數:
            _event: 事件物件（可選）
        """
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)

    def clear_list(self):
        """
        清除列表中的所有項目。
        """
        self.text_list.delete(0, tk.END)


if __name__ == "__main__":
    main()