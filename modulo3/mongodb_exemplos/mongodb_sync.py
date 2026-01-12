from pymongo import MongoClient

url = "mongodb+srv://mongodbuser:mongodbpasswd123@cluster0.bycza.mongodb.net/?appName=Cluster0"
# url = "mongodb://localhost:27017/"
client = MongoClient(url)

db = client.mydatabase
collection = db.mycollection

# Inserir um documento
collection.insert_one({"name": "João", "age": 30})

# Buscar um documento
result = collection.find_one({"name": "João"})
print(type(result))
print(result)
