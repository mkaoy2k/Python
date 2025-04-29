"""
這個程式示範如何使用schedule模組來安排定時任務
程式會每5-10秒隨機間隔執行一次咖啡休息提醒
"""
import schedule
import time
import datetime

def take_break():
    """
    定義休息提醒函數
    這個函數會印出休息提醒訊息和當前時間
    """
    print("該休息一下了")
    print(f'===>{datetime.datetime.now()}')

def main():
    """
    主函數，負責設定和執行定時任務
    """
    # 設定每5-10秒隨機間隔執行一次休息提醒
    schedule.every(5).to(10).seconds.do(take_break)
    
    print("開始執行定時任務...")
    print("(按 Ctrl+C 來停止程式)")
    
    try:
        # 持續檢查並執行待處理的定時任務
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程式已停止")

if __name__ == "__main__":
    main()
