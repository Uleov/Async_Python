import asyncio

async def job(name, delay, should_fail=False):
    await asyncio.sleep(delay)
    if should_fail:
        raise ValueError(f"сбой {name}")
    return f"успех {name}"

def on_done(t):
    name = t.get_name()
    if t.cancelled():
        print("отмена", name)
    elif t.exception() is not None:
        print("ошибка", name, t.exception())
    else:
        print("успех", name, t.result())

async def main():
    tasks = []
    
    t1 = asyncio.create_task(job("задача-1", 0.5), name="задача-1")
    t2 = asyncio.create_task(job("задача-2", 0.8, should_fail=True), name="задача-2")
    t3 = asyncio.create_task(job("задача-3", 0.3), name="задача-3")
    t4 = asyncio.create_task(job("задача-4", 1.0), name="задача-4")
    t5 = asyncio.create_task(job("задача-5", 0.6), name="задача-5")
    
    tasks.extend([t1, t2, t3, t4, t5])
    
    t5.cancel()
    
    for t in tasks:
        t.add_done_callback(on_done)
        print(t.get_name(), t.done())
        
    print("ожидание")
    await asyncio.gather(*tasks, return_exceptions=True)
    
    print("отчет")
    for t in tasks:
        name = t.get_name()
        if t.cancelled():
            status = "отменена"
        elif t.exception() is not None:
            status = f"ошибка {t.exception()}"
        else:
            status = f"успех {t.result()}"
        print(name, status)

if __name__ == "__main__":
    asyncio.run(main())
