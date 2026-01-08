import asyncio
from pymongo import AsyncMongoClient

async def main():
    client = AsyncMongoClient("mongodb://localhost:27017")

    collection = client["empresa"]["funcionarios"]

    # Contagem EXATA (varre a coleção)
    total_exato = await collection.count_documents({})

    # Contagem ESTIMADA (usa metadados internos - mais rápida)
    # Valor aproximado para grandes coleções
    total_estimado = await collection.estimated_document_count()

    print(f"Total exato de documentos: {total_exato}")
    print(f"Total estimado de documentos: {total_estimado}")

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())