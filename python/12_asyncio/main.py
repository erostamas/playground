import asyncio
import aiohttp

#Coroutines are concurrent, scalable functions where the await keyword pauses execution, yielding control back to the event loop so that other tasks can run.
"""
file io, chat programs, tcp echo server, aiohttp, aiofiles, db access: asyncpg, aioredis, aiomysql

async for: __aiter__ and __anext__, async generators, async iterators

import asyncio

async def async_counter():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for num in async_counter():
        print(num)

asyncio.run(main())
"""

USERS = "https://jsonplaceholder.typicode.com/users"
POSTS = "https://jsonplaceholder.typicode.com/posts"
COMMENTS = "https://jsonplaceholder.typicode.com/comments"

from abc import ABC, abstractmethod

async def fetch_json(url):
    print(f"Fetching json from {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    # Run coroutines concurrently
    results = await asyncio.gather(
        fetch_json(USERS),
        fetch_json(POSTS),
        fetch_json(COMMENTS)
    )
    print(results)

asyncio.run(main())


class Job(ABC):
    @abstractmethod
    async def run(self):
        pass

class SleepJob(Job):
    async def run(self):
        print("Sleeping for 1 second")
        await asyncio.sleep(1)
        print("Done sleeping")