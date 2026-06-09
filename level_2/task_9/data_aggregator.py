import asyncio

async def weather():
    await asyncio.sleep(0.3)
    return {"температура": 20, "ветер": 5}

async def rates():
    await asyncio.sleep(0.5)
    raise RuntimeError("сервер валют недоступен")

async def news():
    await asyncio.sleep(0.2)
    return {"заголовок": "важные новости"}

async def safe_fetch(name, coro):
    try:
        data = await coro
        return {"name": name, "status": "ok", "data": data}
    except Exception as e:
        return {"name": name, "status": "error", "error": str(e)}

async def main():
    print("старт")
    
    results = await asyncio.gather(
        safe_fetch("погода", weather()),
        safe_fetch("курсы", rates()),
        safe_fetch("новости", news())
    )
    
    summary = {
        "данные": {},
        "ошибки": {}
    }
    
    for res in results:
        name = res["name"]
        if res["status"] == "ok":
            summary["данные"][name] = res["data"]
        else:
            summary["ошибки"][name] = res["error"]
            
    print("отчет")
    print("успешно")
    for name, data in summary["данные"].items():
        print(name, data)
        
    print("ошибки")
    for name, err in summary["ошибки"].items():
        print(name, err)

if __name__ == "__main__":
    asyncio.run(main())
