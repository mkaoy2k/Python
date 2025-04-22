"""
Python Lambda 函式範例

本程式通過兩個示例展示 Python 中 Lambda 函式的使用：

1. 基本 Lambda 函式使用：
   - 展示如何創建簡單的 Lambda 函式來印出訊息
   - 對比 Lambda 函式與一般函式的差異
   - 展示 Lambda 函式的物件類型和記憶體大小

2. Lambda 函式與 filter() 的搭配使用：
   - 展示如何使用 Lambda 函式搭配 Python 內建的 filter() 函式
   - 從數字列表中篩選出偶數
   - 展示 Lambda 函式在資料處理中的實際應用

主要特色：
- 比較一般函式與 Lambda 函式的差異
- Lambda 函式記憶體使用分析
- Lambda 函式與 filter() 函式搭配使用的實用範例
- 中文註解方便理解

"""
from sys import getsizeof

def main():
    # 例子1: 印出哈囉!
    def hello(title):
        print(f'一般函式：{title}')

    print(f'例子1: 印出哈囉...')
    hello('哈囉!')

    # 上面例子精簡成一行 Lambda 匿名函式
    my_lambda = (lambda title: print(f'匿名函式：{title}\n'))
    size = getsizeof(my_lambda)
    my_lambda('哈囉!')

    print(f'匿名函式的物件類别是：{type(my_lambda)}')
    print(f'匿名函式的物件大小是：{size}\n')

    # 例子2: Lambda 匿名函式印出偶數
    print(f'例子2: 印出偶數...')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'數字列表： {nums}')

    print(f'列表中偶數如下：')
    for even in filter(lambda n: n % 2 == 0, nums):
        print(f'===> {even}')

if __name__ == '__main__':
    main()
