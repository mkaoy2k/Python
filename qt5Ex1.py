"""
PyQt5 基本視窗程式範例

這個程式展示如何使用 PyQt5 建立一個基本的圖形使用者介面(GUI)應用程式。
主要功能：
- 建立一個主視窗
- 在視窗中添加標籤和按鈕
- 實現按鈕點擊事件處理

使用方式：
    直接執行此腳本即可啟動應用程式

依賴套件：
    PyQt5 >= 5.15.0
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """
    主視窗類別，繼承自 QMainWindow
    """
    def __init__(self):
        """
        初始化主視窗
        """
        super().__init__()
        self.setWindowTitle("PyQt5 範例")
        self.setGeometry(100, 100, 400, 200)  # x, y, 寬度, 高度
        
        # 建立中央部件和佈局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 建立標籤
        self.label = QLabel("歡迎使用 PyQt5！", self)
        layout.addWidget(self.label)
        
        # 建立按鈕
        button = QPushButton("點擊我", self)
        layout.addWidget(button)
        
        # 連接按鈕點擊事件
        button.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        """
        按鈕點擊事件處理函數
        """
        self.label.setText("按鈕已被點擊！")


def main():
    """
    主函數，程式進入點
    """
    # 建立應用程式實例
    app = QApplication(sys.argv)
    
    # 建立並顯示主視窗
    window = MainWindow()
    window.show()
    
    # 進入應用程式主循環
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
