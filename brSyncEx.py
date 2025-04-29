"""
模擬早餐準備過程的同步示例
包含煮咖啡和烤貝果兩個任務
"""

import time


def brewCoffee():
    """
    模擬煮咖啡的過程，需要 3 秒的時間。
    
    Returns:
        str: 煮咖啡完成的訊息
    """
    print("\t開始煮咖啡需要 3 秒的時間...")
    time.sleep(3)
    print("\t煮咖啡完成!")
    return "咖啡準備好了!"

def toastBagel():
    """
    模擬烤貝果的過程，需要 10 秒的時間。
    Returns:
        str: 烤貝果完成的訊息
    """
    print("\t開始烤貝果需要 10 秒的時間...")    
    time.sleep(10)
    print("\t烤貝果完成!")
    return "貝果烤好了!"
    
def main():
    """
    主函數，執行早餐準備過程並計算總執行時間
    """
    print("\n開始準備早餐...")
    start_time = time.time()
    
    result_coffee = brewCoffee()
    result_bagel = toastBagel() 
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"煮咖啡的結果: {result_coffee}")
    print(f"烤貝果的結果: {result_bagel}")
    print(f"總共耗時: {elapsed_time:.2f} 秒")
    
if __name__ == "__main__":
    main()
