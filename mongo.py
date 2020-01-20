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

"""id = collection.insert_one({"name": "CDMX", "phone": "3141093387", "date": datetime.datetime.utcnow()}).inserted_id # Gets the _id inserted (1 document)
print(id) # Prints its ObjectId (ObjectId type)
idStr = str(id)"""

"""ids = collection.insert_many(
    [
        {"name": "Colima", "phone": "3141093387", "date": datetime.datetime.utcnow()},
        {"name": "Manza", "phone": "3141093387", "date": datetime.datetime.utcnow()}
    ]
)"""

#print(db.list_collection_names()) # Gets the collection names
#print(collection.find_one()) # Gets the first document
#print(collection.find_one({"_id": id})) # Gets the matched document
#print(collection.find_one({"_id": idStr})) # Gets the matched document, idStr is str type and there are not a str type _id, Result = None
#print(collection.find_one({"_id": ObjectId(idStr)})) # Gets the matched document, parse a str to ObjectId
#print(collection.find_one({"name": "Yosa"})) # Gets the matched document
#print(ids.inserted_ids) # gets the _id inserted (2+ documets)
for doc in collection.find(): # Prints all the collection docuemnts
    print(doc)

for doc in collection.find({"name": "CDMX"}): # Prints all collections documents matched
    print(doc)

print(collection.count_documents({})) # Gets the number of documents
print(collection.count_documents({"name": "Manza"})) # Gets the number of documents matched