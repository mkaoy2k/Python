"""
PyQt5 與 SQLite 資料庫操作範例

這個程式展示如何使用 PyQt5 的 QSql 模組連接 SQLite 資料庫
並顯示資料表內容在 QTableView 中。

主要功能：
- 連接 SQLite 資料庫
- 載入指定資料表
- 在表格視圖中顯示資料

使用方式：
    1. 在 .env 檔案中設定 DB_PATH 和 DB_TABLE 環境變數
    2. 執行此腳本

依賴套件：
    PyQt5 >= 5.15.0
    python-dotenv
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt


class DatabaseViewer(QMainWindow):
    """
    資料庫檢視器視窗類別
    """
    def __init__(self, database_path, table_name):
        """
        初始化資料庫檢視器
        
        參數:
            database_path (str): SQLite 資料庫檔案路徑
            table_name (str): 要顯示的資料表名稱
        """
        super().__init__()
        self.setWindowTitle("SQLite 資料庫檢視器")
        self.setGeometry(100, 100, 800, 600)
        
        # 儲存資料庫連線資訊
        self.database_path = database_path
        self.table_name = table_name
        
        # 建立中央部件和佈局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # 建立按鈕區域
        button_layout = QHBoxLayout()
        
        # 新增儲存按鈕
        self.save_button = QPushButton("儲存變更")
        self.save_button.clicked.connect(self.save_changes)
        self.save_button.setEnabled(False)
        
        # 新增重新整理按鈕
        refresh_button = QPushButton("重新整理")
        refresh_button.clicked.connect(self.refresh_data)
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(refresh_button)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        
        # 初始化資料庫連接
        if not self._init_database(database_path, table_name):
            return
        
        # 建立表格視圖
        self.tableView = QTableView()
        self.tableView.setEditTriggers(QTableView.DoubleClicked | QTableView.EditKeyPressed)
        self.tableView.setSelectionBehavior(QTableView.SelectRows)
        main_layout.addWidget(self.tableView)
        
        # 設定模型
        self.model = QSqlTableModel()
        self.model.setTable(table_name)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)  # 設定編輯策略
        self.model.select()
        
        # 連接到資料變更信號
        self.model.dataChanged.connect(self.on_data_changed)
        
        # 設定表格屬性
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
    
    def on_data_changed(self, top_left, bottom_right, roles=None):
        """
        當資料變更時啟用儲存按鈕
        """
        self.save_button.setEnabled(True)
    
    def save_changes(self):
        """
        將變更儲存到資料庫
        """
        try:
            if self.model.submitAll():
                QMessageBox.information(self, "成功", "資料已成功儲存！")
                self.save_button.setEnabled(False)
            else:
                QMessageBox.critical(self, "錯誤", "儲存失敗：" + self.model.lastError().text())
                self.model.revertAll()  # 回復變更
        except Exception as e:
            QMessageBox.critical(self, "例外錯誤", f"儲存時發生錯誤：{str(e)}")
    
    def refresh_data(self):
        """
        重新載入資料
        """
        self.model.select()
        self.tableView.resizeColumnsToContents()
        self.save_button.setEnabled(False)
    
    def _init_database(self, database_path, table_name):
        """
        初始化資料庫連接
        
        參數:
            database_path (str): 資料庫檔案路徑
            table_name (str): 資料表名稱
            
        回傳:
            bool: 資料庫初始化是否成功
        """
        # 設定 SQLite 資料庫
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(database_path)
        
        if not db.open():
            error_msg = f"無法開啟資料庫：{db.lastError().text()}"
            QMessageBox.critical(self, "資料庫錯誤", error_msg)
            return False
            
        # 檢查資料表是否存在
        if table_name not in db.tables():
            error_msg = f"資料表 '{table_name}' 不存在於資料庫中"
            QMessageBox.critical(self, "資料表錯誤", error_msg)
            return False
            
        return True


def main():
    """
    主函數，程式進入點
    """
    # 載入 .env 檔案
    env_path = Path(__file__).parent / '.env'
    load_dotenv(dotenv_path=env_path)
    
    # 從環境變數取得資料庫設定
    database_path = os.getenv('DB_PATH')
    table_name = os.getenv('DB_TABLE')
    
    # 檢查環境變數是否設定
    if not database_path or not table_name:
        error_msg = "請在 .env 檔案中設定 DB_PATH 和 DB_TABLE 環境變數"
        print(error_msg)
        return
    
    # 檢查資料庫檔案是否存在
    if not os.path.exists(database_path):
        error_msg = f"找不到資料庫檔案: {database_path}"
        print(error_msg)
        return
    
    # 建立應用程式實例
    app = QApplication(sys.argv)
    
    # 建立並顯示主視窗
    window = DatabaseViewer(database_path, table_name)
    window.show()
    
    # 進入應用程式主循環
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
