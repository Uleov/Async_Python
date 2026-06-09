import asyncio

async def task_step(i):
    await asyncio.sleep(0.2)
    if i % 3 == 0:
        raise ValueError(f"ошибка в задаче {i}")
    return f"результат {i}"

async def main():
    coros_1 = [task_step(i) for i in range(1, 7)]
    
    print("стандартный")
    try:
        results = await asyncio.gather(*coros_1)
        print("успешно", results)
    except ValueError as e:
        print("ошибка", e)
        
    print("с ошибками")
    coros_2 = [task_step(i) for i in range(1, 7)]
    results = await asyncio.gather(*coros_2, return_exceptions=True)
    
    successes = []
    failures = []
    
    for r in results:
        if isinstance(r, Exception):
            failures.append(str(r))
        else:
            successes.append(r)
            
    print("успешно")
    for s in successes:
        print(s)
        
    print("ошибки")
    for f in failures:
        print(f)
        
    print("успех", len(successes), "упало", len(failures))

if __name__ == "__main__":
    asyncio.run(main())
