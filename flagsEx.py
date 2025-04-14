"""
命令行參數範例

此程式展示如何使用 absl.flags 來處理命令行參數。
支援的參數包括：
- name: 使用者姓名
- age: 使用者年齡
- debug: 設定除錯模式
- job: 工作狀態（running 或 stopped）
"""

from absl import app
from absl import flags

# 定義旗標變數
FLAGS = flags.FLAGS

# 定義命令行參數
flags.DEFINE_string(
    'name', 'Michael Kao',
    '使用者姓名。預設值為 Michael Kao。'
)
flags.DEFINE_integer(
    'age', None,
    '使用者年齡。必須為非負數。',
    lower_bound=0
)
flags.DEFINE_boolean(
    'debug', False,
    '是否啟用除錯模式。預設為關閉。'
)
flags.DEFINE_enum(
    'job', 'running', ['running', 'stopped'],
    '工作狀態。可選值為 running 或 stopped。'
)

def main(argv):
    """
    主函數，處理命令行參數並顯示相應訊息

    Args:
        argv: 非旗標參數列表
    """
    # 顯示除錯訊息
    print(f'啟用除錯模式: {FLAGS.debug}\n非旗標參數: {argv}\n') if FLAGS.debug else None
     
    # 顯示生日祝福
    print(f'生日快樂 "{FLAGS.name}"')

    # 如果提供了年齡參數，顯示年齡和工作狀態
    if FLAGS.age is not None:
        print(f'\t您 {FLAGS.age} 歲\n\t您的工作狀態是 {FLAGS.job}\n')

if __name__ == '__main__':
    """
    程式入口點
    
    範例命令：
    python flagsEx.py a b c --debug -name '1 3 4 2' -age 2 -job 'stopped'
    
    輸出：
    啟用除錯模式: True
    非旗標參數: ['flagsEx.py', 'a', 'b', 'c']

    生日快樂 "1 3 4 2"
        您 2 歲
        您的工作狀態是 stopped
    """
    app.run(main)
