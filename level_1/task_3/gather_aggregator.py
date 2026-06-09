import asyncio
import time
import random

async def fetch_source(name):
    delay = random.uniform(0.5, 2.0)
    print("старт", name)
    await asyncio.sleep(delay)
    print("финиш", name)
    return f"данные {name}"

async def main():
    random.seed(42)
    names = ["а", "б", "в", "г", "д", "е"]
    
    start = time.perf_counter()
    print("старт")
    results = await asyncio.gather(*[fetch_source(n) for n in names])
    elapsed = time.perf_counter() - start
    
    print("результаты")
    for res in results:
        print(res)
        
    print("время", elapsed)

if __name__ == "__main__":
    asyncio.run(main())
