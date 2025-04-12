"""
這個檔案展示了 Python 中特殊方法（dunder methods）的使用範例。
主要功能包括：
1. 特殊方法的使用範例：__init__, __setattr__, __getattr__, __str__, __lt__
2. 物件屬性的動態管理
3. 物件比較的自定義邏輯
4. 物件字串表示的自定義
5. 屬性訪問的追蹤和記錄

這個示範程式使用火星人（Martian）作為例子，展示了如何使用特殊方法來實現：
- 動態屬性管理
- 屬性訪問追蹤
- 物件比較邏輯
- 物件字串表示
- 屬性不存在時的處理

同時，這個程式還展示了如何使用 logging 來追蹤物件的行為和屬性訪問。
"""

import logging

# 設置 logging 格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class Martian:
    """火星人"""
    
    def __init__(self, fn, ln):
        self.logger = logging.getLogger('Martian')
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        if name == 'logger':
            super().__setattr__(name, value)
        else:
            self.logger.debug(f"設定屬性 {name} = {value}")
            super().__setattr__(name, value)

    def __getattr__(self, name):
        self.logger.debug(f"獲取屬性 '{name}'")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"找不到屬性名稱 '{name}'")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __lt__(self, other):
        self.logger.debug(f"比較 {self} 與 {other}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)


def main():
    # 印出類別的文件字串 (__doc__ 屬性)
    logger = logging.getLogger('main')
    logger.info(f'Printing __doc__:\n===>{Martian.__doc__}\n')

    # 印出物件的屬性字典 (__dict__ 屬性)
    m1 = Martian('Michael', 'Kao')
    m1.arrival_date = '2035-12-22'
    logger.info(f'Printing __dict__:\n===>{m1.__dict__}\n')

    # 取得屬性。注意：__getattr__() 不會被調用
    logger.info(f'First name = {m1.first_name}')
    logger.info(f'Last name = {m1.last_name}')

    # 使用 __getattr__() 取得計算屬性
    logger.info(m1.full_name)

    try:
        logger.info(m1.martian_name)
    except:
        logger.info(f"===> AttributeError caught\n")

    # 計算屬性不會存儲在 __dict__ 中
    logger.info(f'Printing __dict__:\n===>{m1.__dict__}\n')

    # 創建多個火星人實例並排序
    m2 = Martian("Henry", "Kao")
    m3 = Martian("Christine", "Kao")
    m4 = Martian("Judy", "Kao")
    m5 = Martian("Latte", "Dog")
    m6 = Martian("Olisan", "Dog")

    martians = [m1, m2, m3, m4, m5, m6]
    martians.sort()
    logger.info("火星人字母排序如下：")
    for i, m in enumerate(martians, 1):
        logger.info(f"===> {i}. {m}")

if __name__ == "__main__":
    main()
