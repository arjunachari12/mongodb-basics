from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access a database
db = client["mydatabase1"]

# Access a collection
collection = db["mycollection"]

# Insert a document
collection.insert_one({"name": "Alice", "age": 30})

# Find documents
result = collection.find_one({"name": "Alice"})
print(result)
