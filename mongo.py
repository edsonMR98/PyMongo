from pymongo import MongoClient
import datetime

mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient.pymongo
collection = db.test

"""collection.insert_many(
    [
        {"name": "Edson", "phone": "3141093387", "date": datetime.datetime.utcnow()},
        {"name": "Yosa", "phone": "3141093387", "date": datetime.datetime.utcnow()}
    ]
)"""

id = collection.insert_one({"name": "Abraxas", "phone": "3141093387", "date": datetime.datetime.utcnow()}).inserted_id # Gets the _id inserted
print(id) # Prints its ObjectId

#print(db.list_collection_names()) # Gets the collection names
print(collection.find_one()) # Gets the first document
print(collection.find_one({"_id": id})) # Gets the matched document
print(collection.find_one({"name": "Yosa"})) # Gets the matched document