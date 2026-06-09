import asyncio

async def worker():
    try:
        while True:
            print("тик")
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        print("отмена")
        raise
    finally:
        print("очистка")

async def main():
    print("старт")
    task = asyncio.create_task(worker())
    await asyncio.sleep(2.0)
    
    print("стоп")
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("остановлен")

if __name__ == "__main__":
    asyncio.run(main())
