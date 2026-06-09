import asyncio
import time

async def do_step(name, delay):
    print("старт", name)
    await asyncio.sleep(delay)
    print("финиш", name)
    return {"имя": name, "время": delay}

async def run_concurrent(steps):
    start = time.perf_counter()
    tasks = []
    for name, delay in steps:
        task = asyncio.create_task(do_step(name, delay))
        tasks.append(task)
    
    print("запланировано")
    
    results = []
    for task in tasks:
        res = await task
        results.append(res)
        
    elapsed = time.perf_counter() - start
    return elapsed, results

async def run_naive(steps):
    start = time.perf_counter()
    results = []
    for name, delay in steps:
        res = await do_step(name, delay)
        results.append(res)
    elapsed = time.perf_counter() - start
    return elapsed, results

async def main():
    steps = [
        ("первый", 0.5),
        ("второй", 0.3),
        ("третий", 0.7),
        ("четвертый", 0.2),
        ("пятый", 0.4)
    ]
    
    print("конкурентно")
    con_time, con_res = await run_concurrent(steps)
    print("время", con_time)
    
    print("последовательно")
    naive_time, naive_res = await run_naive(steps)
    print("время", naive_time)

if __name__ == "__main__":
    asyncio.run(main())
