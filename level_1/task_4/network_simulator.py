import asyncio
import time
import random

async def download(url):
    delay = random.uniform(0.3, 1.2)
    print("старт", url)
    await asyncio.sleep(delay)
    size = len(url) * 100
    print("финиш", url)
    return {"url": url, "delay": delay, "size": size}

async def run_sequential(urls):
    start = time.perf_counter()
    results = []
    for url in urls:
        res = await download(url)
        results.append(res)
    elapsed = time.perf_counter() - start
    return elapsed, results

async def run_concurrent(urls):
    start = time.perf_counter()
    tasks = [asyncio.create_task(download(url)) for url in urls]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    return elapsed, results

async def main():
    random.seed(42)
    urls = [
        "сайт_а.рф", "сайт_б.рф", "сайт_в.рф", "сайт_г.рф",
        "сайт_д.рф", "сайт_е.рф", "сайт_ж.рф", "сайт_з.рф"
    ]
    
    print("последовательно")
    seq_time, seq_results = await run_sequential(urls)
    
    print("конкурентно")
    con_time, con_results = await run_concurrent(urls)
    
    print("результаты")
    for res in con_results:
        print(res["url"], res["delay"], res["size"])
        
    sum_delays = sum(res["delay"] for res in con_results)
    print("сумма", sum_delays)
    print("последовательно", seq_time)
    print("конкурентно", con_time)

if __name__ == "__main__":
    asyncio.run(main())
