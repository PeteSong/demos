import asyncio
import secrets


async def hello() -> None:
    print("hello")
    await asyncio.sleep(2)
    print("world")


async def task(name: str, delay: int) -> None:
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")


async def producer(queue: asyncio.Queue[int]) -> None:
    for _ in range(5):
        item = secrets.randbelow(100)
        await queue.put(item)
        print(f"Produced {item}")
        await asyncio.sleep(secrets.randbelow(5) + 1)


async def consumer(queue: asyncio.Queue[int]) -> None:
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()
        await asyncio.sleep(secrets.randbelow(5) + 1)


async def main() -> None:  # pragma: no cover
    await hello()

    await asyncio.gather(task("task01", 2), task("task2", 3), task("task3", 1))

    queue: asyncio.Queue[int] = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await producer_task
    await queue.join()
    consumer_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
