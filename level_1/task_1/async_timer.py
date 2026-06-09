import asyncio
import time
import argparse

async def run_timer(name, delay):
    print("старт", name)
    await asyncio.sleep(delay)
    print("финиш", name)

async def run_sequential(timers):
    start = time.perf_counter()
    for name, delay in timers:
        await run_timer(name, delay)
    return time.perf_counter() - start

async def run_concurrent(timers):
    start = time.perf_counter()
    tasks = [asyncio.create_task(run_timer(name, delay)) for name, delay in timers]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["sequential", "concurrent", "both"], default="both")
    args = parser.parse_args()
    
    timers = [("первый", 1.0), ("второй", 1.5), ("третий", 2.0)]
    
    if args.mode in ("sequential", "both"):
        print("последовательно")
        seq_time = await run_sequential(timers)
        print("время", seq_time)
        
    if args.mode in ("concurrent", "both"):
        print("конкурентно")
        con_time = await run_concurrent(timers)
        print("время", con_time)

if __name__ == "__main__":
    asyncio.run(main())
