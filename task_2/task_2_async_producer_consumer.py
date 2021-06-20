import asyncio
import random


async def producer(number):
    while True:
        await queue.put(round(number + random.random() * 2))
        print('Produced done!')
        await asyncio.sleep(random.random() * 5)


async def consumer(number):
    while True:
        value = await queue.get()
        print(f'Consumed {number}, {value}')


queue = asyncio.Queue()
loop = asyncio.get_event_loop()

for i in range(6):
    loop.create_task(producer(i))

for i in range(20):
    loop.create_task(consumer(i))

loop.run_forever()
