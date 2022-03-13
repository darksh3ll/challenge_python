from time import sleep
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


async def say_hello(s, time_s):
    while True:
        await asyncio.sleep(time_s)
        print(s)


loop = asyncio.get_event_loop()
loop.create_task(say_hello("1", 1))
loop.create_task(say_hello("2", 1))
loop.run_forever()
loop.close()
