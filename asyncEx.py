"""Python 非同步程式設計示範

這個程式展示了如何使用 Python 的 asyncio 模組來實現非同步程式設計。
通過製作早餐的示例來說明非同步任務的執行方式。
"""

import asyncio
import time

async def brewCoffee():
    """非同步函數：沖泡咖啡
    
    模擬沖泡咖啡的過程，需要 3 秒的時間。
    """
    print("開始沖泡咖啡需要 3 秒的時間...")
    await asyncio.sleep(3)  # 模擬沖泡咖啡的時間
    print("咖啡沖泡完成！")
    return "咖啡已準備好"

async def toastBagel():
    """非同步函數：烤貝果
    
    模擬烤貝果的過程，需要 10 秒的時間。
    """
    print("開始烤貝果需要 10 秒的時間...")
    await asyncio.sleep(10)  # 模擬烤貝果的時間
    print("貝果烤好！")
    return "貝果已烤好"

async def main():
    """主程式：非同步任務協調器
    
    使用 asyncio.gather 來同時執行多個非同步任務，
    並計算總執行時間。
    """
    start_time = time.time()
    
    # 使用 asyncio.gather 同時執行多個非同步任務
    coffee, bagel = await asyncio.gather(
        brewCoffee(),
        toastBagel()
    )
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n早餐準備完成！")
    print(f"咖啡：{coffee}")
    print(f"貝果：{bagel}")
    print(f"總共用時：{total_time:.2f} 秒")

if __name__ == "__main__":
    """程式入口點
    
    使用 asyncio.run 來執行主程式。
    """
    print("開始準備早餐...")
    asyncio.run(main())
