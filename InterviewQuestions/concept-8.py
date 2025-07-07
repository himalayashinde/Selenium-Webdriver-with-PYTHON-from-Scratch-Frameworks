import asyncio
import time


def task(name):
    print(f"Starting {name}")

    time.sleep(2)

    print(f"Finished {name}")

task("Himalaya")
task("Shinde")

async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")


async def main():
    await asyncio.gather(task("Rahul"),task("Shetty"))


asyncio.run(main())