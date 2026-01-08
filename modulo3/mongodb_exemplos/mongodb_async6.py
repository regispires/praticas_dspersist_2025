import asyncio
from pymongo import AsyncMongoClient

dados = [
    {"nome": "maria", "dep": "ti",            "salario": 5000},
    {"nome": "pedro", "dep": "ti",            "salario": 4000},
    {"nome": "jose",  "dep": "contabilidade", "salario": 2500},
    {"nome": "lucia", "dep": "rh",            "salario": 3000},
]

async def main():
    client = AsyncMongoClient("mongodb://localhost:27017")

    db = client["empresa"]
    collection = db["funcionarios"]

    # Inserção em lote (bulk insert)
    result = await collection.insert_many(dados)

    print(f"{len(result.inserted_ids)} documentos inseridos.")
    print("IDs:", result.inserted_ids)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())