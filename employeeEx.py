"""
這個程式是一個員工管理系統的示範，主要功能包括：

1. 類別設計:
   - 定義了 Employee 類別來管理員工資訊
   - 包含員工的基本屬性：名字 (first) 和姓氏 (last)
   - 提供兩個屬性方法：
     - email: 生成員工的電子郵件地址（自動轉換為小寫）
     - fullname: 生成員工的完整姓名

2. 日誌系統:
   - 使用 Python 內建的 logging 模組來記錄系統日誌
   - 日誌等級設置為 INFO，只會記錄 INFO 及以上等級的日誌
   - 日誌檔案會存放在 logger 目錄下的 employee.log 檔案中
   - 使用 'w' 模式覆寫日誌檔案，而不是追加模式

3. 測試示範:
   - 創建了三個測試員工物件：John Smith、Corey Schafer 和 Jane Doe
   - 在主程式中示範了不同等級的日誌訊息：
     - DEBUG (不會顯示，因為等級太低)
     - INFO
     - WARNING
     - ERROR
     - CRITICAL

這個程式主要用來示範：
- 如何正確使用類別和物件導向程式設計
- 如何設置和使用日誌系統
- 如何使用屬性裝飾器 (@property) 來實現 getter 方法
- 如何處理檔案路徑和目錄操作

注意事項:
1. 由於日誌等級設置為 'INFO'，所以不會顯示除錯訊息
2. 日誌檔案以 'w' 模式開始，這意味著會覆寫檔案，而不是預設的追加模式
3. 員工電子郵件地址會自動轉換為小寫
"""
import logging
from pathlib import Path

# 設置日誌記錄系統
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # 設置日誌等級為 INFO

# 定義日誌格式
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# 使用 pathlib 來獲取當前檔案的目錄
base_dir = Path(__file__).parent
log_dir = base_dir / 'logger'  # 日誌檔案存放目錄

# 如果日誌目錄不存在，則創建它
log_dir.mkdir(exist_ok=True)

# 指定日誌檔案路徑
log_file = log_dir / 'employee.log'
file_handler = logging.FileHandler(log_file, mode='w')  # 使用 'w' 模式覆寫日誌檔案
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    """員工類別，用於管理員工的基本資訊
    
    Attributes:
        first (str): 員工名字
        last (str): 員工姓氏
    """

    def __init__(self, first: str, last: str):
        """
        初始化員工物件
        
        Args:
            first (str): 員工名字
            last (str): 員工姓氏
        """
        self.first = first
        self.last = last
        logger.info(f'創建員工: {self.fullname} - {self.email}')

    @property
    def email(self) -> str:
        """生成員工電子郵件地址"""
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def fullname(self) -> str:
        """生成員工完整姓名"""
        return f'{self.first} {self.last}'

# 創建測試員工物件
test_employees = [
    Employee('John', 'Smith'),
    Employee('Corey', 'Schafer'),
    Employee('Jane', 'Doe')
]

if __name__ == '__main__':
    # 測試不同等級的日誌訊息
    logger.debug("這是一個無害的除錯訊息。")
    logger.info("仅供您参考。")
    logger.warning("我正在警告您。")
    logger.error("您剛剛試圖除以零？")
    logger.critical("系統無法連接網際網路。")
    
    print(f'請在 {log_file} 檔案末尾查看日誌資料...\n')
    print(f'''注意事項:
    1. 由於日誌等級設置為 'INFO'，所以不會顯示除錯訊息
    2. 日誌檔案以 'w' 模式開始，這意味著會覆寫檔案，而不是預設的追加模式
    3. 員工電子郵件地址會自動轉換為小寫
    ''')
