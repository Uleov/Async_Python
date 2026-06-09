import asyncio
import argparse
import random

active_count = 0
max_active = 0
active_lock = asyncio.Lock()

async def run_job(job_id, delay, sem):
    global active_count, max_active
    async with sem:
        async with active_lock:
            active_count += 1
            if active_count > max_active:
                max_active = active_count
                
        print("старт", job_id)
        try:
            await asyncio.sleep(delay)
        finally:
            print("финиш", job_id)
            async with active_lock:
                active_count -= 1

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    
    if args.limit <= 0:
        print("неверный лимит")
        return
        
    sem = asyncio.Semaphore(args.limit)
    
    random.seed(42)
    jobs = [(i, random.uniform(0.1, 0.5)) for i in range(1, 21)]
    
    print("старт", args.limit)
    
    tasks = [asyncio.create_task(run_job(job_id, delay, sem)) for job_id, delay in jobs]
    await asyncio.gather(*tasks)
    
    print("макс", max_active)

if __name__ == "__main__":
    asyncio.run(main())
