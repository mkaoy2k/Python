"""
Python 非同步程式設計示範

這個程式展示了如何使用 Python 的 asyncio 模組來實現非同步程式設計。
通過製作早餐的示例來說明非同步任務的執行方式。

主要功能：
1. 非同步沖泡咖啡
2. 非同步烤貝果
3. 使用 asyncio.gather 同時執行多個任務
"""

import asyncio
import time

async def brewCoffee() -> str:
    """
    非同步函數：沖泡咖啡
    
    模擬沖泡咖啡的過程，需要 3 秒的時間。
    
    Returns:
        str: 咖啡準備完成的訊息
    """
    print("\t開始沖泡咖啡需要 3 秒的時間...")
    await asyncio.sleep(3)  # 模擬沖泡咖啡的時間
    print("\t咖啡沖泡完成！")
    return "咖啡已準備好!"

async def toastBagel() -> str:
    """
    非同步函數：烤貝果
    
    模擬烤貝果的過程，需要 10 秒的時間。
    
    Returns:
        str: 貝果烤好後的訊息
    """
    print("\t開始烤貝果需要 10 秒的時間...")
    await asyncio.sleep(10)  # 模擬烤貝果的時間
    print("\t貝果烤好！")
    return "貝果已烤好了!"

async def main() -> None:
    """
    主程式：非同步任務協調器
    
    使用 asyncio.gather 來同時執行多個非同步任務，
    並計算總執行時間。
    
    Returns:
        None
    """
    print("\n開始準備早餐...")
    start_time = time.time()
    
    # 使用 asyncio.gather 同時執行多個非同步任務
    coffee, bagel = await asyncio.gather(
        brewCoffee(),
        toastBagel()
    )
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n早餐準備完成！")
    print(f"煮咖啡的結果：{coffee}")
    print(f"烤貝果的結果：{bagel}")
    print(f"總共耗時：{total_time:.2f} 秒")

if __name__ == "__main__":
    """
    程式入口點
    
    使用 asyncio.run 來執行主程式。
    """
    asyncio.run(main())
