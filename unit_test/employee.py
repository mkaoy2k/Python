import requests


import logging
from pathlib import Path
import os
import traceback
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 設置日誌
logger = logging.getLogger(__name__)

# 設置日誌格式
formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')

# 設置 console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# 設置日誌檔案處理器
log_dir = Path(__file__).parent  # 使用當前文件的父目錄
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'employee.log'
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)

# 設置日誌等級
log_level = os.getenv("LOGGING", "INFO")
if log_level == "INFO":
    logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
else:
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

# 設置 console handler 的等級: INFO always
console_handler.setLevel(logging.INFO)

# 添加處理器到日誌器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]
class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        logger.debug(f'{get_function_name()}: Creating employee {first} {last} - {pay}')   
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        email = f'{self.first}.{self.last}@email.com'
        logger.debug(f'{get_function_name()}: email={email}')
        return email

    @property
    def fullname(self):
        fullname = f'{self.first} {self.last}'
        logger.debug(f'{get_function_name()}: fullname={fullname}')
        return fullname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        logger.debug(f'{get_function_name()}: pay={self.pay}')

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            logger.debug(f'{get_function_name()}:\n{response.text}')   
            return response.text
        else:
            logger.debug(f'{get_function_name()}: Bad Response!')
            return 'Bad Response!'

if __name__ == '__main__':
    print(f'Employee.py begins...')
    logger.debug(f'Employee.py begins...')
    logger.debug(f'Logging Level: {log_level}')
    
    # 創建測試員工物件
    test_employees = [
        Employee('Michael', 'Kao', 50000),
        Employee('Sue', 'Smith', 60000),
        Employee('John', 'Doe', 70000)
    ]

    for emp in test_employees:
        print(f'Employee: {emp.fullname}, Email: {emp.email}, Pay: {emp.pay}')