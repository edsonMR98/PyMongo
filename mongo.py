from pymongo import MongoClient
from bson.objectid import ObjectId
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

id = collection.insert_one({"name": "CDMX", "phone": "3141093387", "date": datetime.datetime.utcnow()}).inserted_id # Gets the _id inserted
print(id) # Prints its ObjectId (ObjectId type)
idStr = str(id)

#print(db.list_collection_names()) # Gets the collection names
print(collection.find_one()) # Gets the first document
print(collection.find_one({"_id": id})) # Gets the matched document
print(collection.find_one({"_id": idStr})) # Gets the matched document, idStr is str type and there are not a str type _id, Result = None
print(collection.find_one({"_id": ObjectId(idStr)})) # Gets the matched document, parse a str to ObjectId
print(collection.find_one({"name": "Yosa"})) # Gets the matched document