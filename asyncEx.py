import asyncio
import time

async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(10)
    print("End toastBagel()")
    return "Bagel toasted"
    
async def main():
    start_time = time.time()
    
    # # option 1: use asyncio.gather() to dispatch coroutines
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch
    
    # option 2: use asyncio.create_task() to dispatch coroutines
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    
    result_coffee = await coffee_task
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"await coffee time: {elapsed_time:.2f} seconds")
    
    result_bagel = await toast_task
    end_time = time.time()    
    elapsed_time = end_time - start_time
    print(f"await toast time: {elapsed_time:.2f} seconds")
        
    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")
    
if __name__ == "__main__":
    asyncio.run(main())
    
