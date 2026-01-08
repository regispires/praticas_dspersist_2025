import asyncio
from pymongo import AsyncMongoClient

async def main():
    uri = "mongodb://localhost:27017"
    client = AsyncMongoClient(uri)

    db = client["test_database"]
    collection = db["test_collection"]

    await collection.insert_one({"name": "João", "status": "Connected!"})
    result = await collection.find_one({"name": "João"})
    print(result)

    await client.close()

asyncio.run(main())