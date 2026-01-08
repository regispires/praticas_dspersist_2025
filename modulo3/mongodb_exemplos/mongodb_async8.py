import asyncio
from pymongo import AsyncMongoClient

async def main():
    client = AsyncMongoClient("mongodb://localhost:27017")
    collection = client["empresa"]["funcionarios"]

    # Busca o primeiro documento da coleção (ordem natural)
    doc = await collection.find_one()
    print("Primeiro documento:")
    print(doc)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())