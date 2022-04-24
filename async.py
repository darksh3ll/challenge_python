import time
import asyncio


# Asyncio permet d’exécuter plusieurs sections de code (des fonctions, dites « coroutines »)
# de manière asynchrone. Quand une section de code termine (ou suspend) son exécution,
# alors Asyncio peut passer la main à une autre section de code à exécuter.

# async def print_this(s, time_ms):
#     while True:
#         await asyncio.sleep(time_ms)
#         print(s)
#
#
# loop = asyncio.get_event_loop()
# loop.create_task(print_this("1 secondes", 1))
# loop.create_task(print_this("10 secondes", 10))
#
# loop.run_forever()
# loop.close()


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(5, 'world')
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
