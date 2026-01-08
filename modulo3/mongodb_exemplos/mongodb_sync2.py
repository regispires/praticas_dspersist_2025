from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
collection = client.mydatabase.mycollection

names = [f"user{i}" for i in range(10000)]

start = time.time()

results = []
for name in names:
    results.append(collection.find_one({"name": name}))

end = time.time()

print(f"Tempo total síncrono: {end - start:.2f} segundos")
