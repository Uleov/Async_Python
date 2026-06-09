import asyncio
import sys

if sys.version_info >= (3, 11):
    timeout = asyncio.timeout
else:
    class timeout:
        def __init__(self, delay):
            self.delay = delay
            self.task = None
            self.cancelled = False

        async def __aenter__(self):
            self.task = asyncio.current_task()
            self.loop = asyncio.get_running_loop()
            self.h = self.loop.call_later(self.delay, self._timeout)
            return self

        def _timeout(self):
            self.cancelled = True
            self.task.cancel()

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            self.h.cancel()
            if exc_type is asyncio.CancelledError and self.cancelled:
                raise asyncio.TimeoutError() from None
            return False

async def slow_op(seconds):
    try:
        print("старт", seconds)
        await asyncio.sleep(seconds)
        print("финиш", seconds)
        return f"результат {seconds}"
    finally:
        print("очистка", seconds)

async def main():
    print("wait_for")
    try:
        res1 = await asyncio.wait_for(slow_op(3.0), timeout=1.0)
        print("результат", res1)
    except asyncio.TimeoutError:
        print("таймаут")
        
    print("timeout")
    try:
        async with timeout(1.0):
            res2 = await slow_op(3.0)
            print("результат", res2)
    except asyncio.TimeoutError:
        print("таймаут")

    print("быстро")
    try:
        async with timeout(2.0):
            res3 = await slow_op(0.5)
            print("результат", res3)
    except asyncio.TimeoutError:
        print("таймаут")

if __name__ == "__main__":
    asyncio.run(main())
