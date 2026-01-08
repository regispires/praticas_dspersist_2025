import asyncio
from pymongo import AsyncMongoClient

client = AsyncMongoClient("mongodb://localhost:27017")
db = client["test"]

async def main():
    collections = await db.list_collection_names()
    print("Coleções:", collections)
    await client.close()

asyncio.run(main())