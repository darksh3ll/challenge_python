import asyncio


def gg():
    print("ffddsfdsf")


async def hello():
    await asyncio.sleep(5)
    print("hello")


async def main():
    await asyncio.sleep(1)
    print('... World!')


async def foo():
    await asyncio.sleep(10)
    print("foo")


# Python 3.7+
asyncio.run(hello())
asyncio.run(foo())
asyncio.run(main())
gg()
