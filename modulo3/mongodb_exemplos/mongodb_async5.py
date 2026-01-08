import asyncio
from pymongo import AsyncMongoClient

async def main():
    client = AsyncMongoClient("mongodb://localhost:27017")

    collection = client["empresa"]["funcionarios"]

    doc = { "nome": "joao", "dep": "contabilidade", "salario": 2000 }

    result = await collection.insert_one(doc)
    print("Documento inserido com id:", result.inserted_id)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())