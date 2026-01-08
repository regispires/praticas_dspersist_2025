import asyncio
import time
from pymongo import AsyncMongoClient

client = AsyncMongoClient("mongodb://localhost:27017")
collection = client.mydatabase.mycollection

names = [f"user{i}" for i in range(10000)]

async def fetch(name):
    return await collection.find_one({"name": name})

async def main():
    start = time.time()

    results = await asyncio.gather(
        *(fetch(name) for name in names)
    )

    end = time.time()
    print(f"Tempo total assíncrono: {end - start:.2f} segundos")
    print(len(results))

asyncio.run(main())