"""
簡單的 Tkinter 應用程式範例
這個程式示範了基本的 Tkinter GUI 界面，包含輸入框和清單框
"""

import tkinter as tk
from tkinter import ttk

class SimpleApp:
    """
    簡單的 Tkinter 應用程式類別
    
    Attributes:
        root: Tkinter 主視窗
        entry: 輸入框元件
        text_list: 清單框元件
    """
    
    def __init__(self, root):
        """
        初始化 SimpleApp 類別
        
        Args:
            root: Tkinter 主視窗
        """
        self.root = root
        self.root.title("簡單應用程式")
        self.setup_layout()
        
    def setup_layout(self):
        """
        設置應用程式的佈局
        包含兩個框架，每個框架都有輸入框和清單框
        """
        # 設置主視窗的網格配置
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=1)

        # 第一個框架
        frame1 = ttk.Frame(self.root)
        frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.setup_frame(frame1)

        # 第二個框架
        frame2 = ttk.Frame(self.root)
        frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.setup_frame(frame2, use_ttk=False)

    def setup_frame(self, frame, use_ttk=True):
        """
        設置單個框架的元件
        
        Args:
            frame: 要設置的框架
            use_ttk: 是否使用 ttk 元件
        """
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        # 輸入框
        entry = ttk.Entry(frame) if use_ttk else tk.Entry(frame)
        entry.grid(row=0, column=0, sticky="ew")
        entry.bind("<Return>", self.add_to_list)

        # 新增按鈕
        button = ttk.Button(frame, text="新增", command=self.add_to_list) if use_ttk else tk.Button(frame, text="新增", command=self.add_to_list)
        button.grid(row=0, column=1)

        # 清單框
        text_list = tk.Listbox(frame)
        text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def add_to_list(self, event=None):
        """
        將輸入框的文字新增到清單框中
        
        Args:
            event: 事件物件（可選，用於處理鍵盤事件）
        """
        # 找到目前焦點的輸入框
        entry = self.root.focus_get()
        if isinstance(entry, (ttk.Entry, tk.Entry)):
            text = entry.get()
            if text:
                # 找到對應的清單框
                text_list = entry.grid_info()["in"].grid_slaves(row=1, column=0)[0]
                text_list.insert(tk.END, text)
                entry.delete(0, tk.END)

def main():
    """
    主程式函數
    創建並啟動 Tkinter 應用程式
    """
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()