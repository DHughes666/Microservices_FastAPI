import asyncio 
import time

async def main():
    for i in range(1, 6):
        await myfunc(i)
        print ('In main', i)

async def myfunc(i):
    print ('In myfunc', i)
    time.sleep(2)

asyncio.run(main())