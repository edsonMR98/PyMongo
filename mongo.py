from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime, pymongo

# Connection with MongoClient, getting database and collection
mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient.pymongo
collection = db.dictionary

# Inserting documents
"""collection.insert_many(
    [
        {"name": "Edson", "phone": "3141093387", "date": datetime.datetime.utcnow()},
        {"name": "Yosa", "phone": "3141093387", "date": datetime.datetime.utcnow()}
    ]
)"""

"""id = collection.insert_one({"name": "CDMX", "phone": "3141093387", "date": datetime.datetime.utcnow()}).inserted_id # Gets the _id inserted (1 document)
print(id) # Prints its ObjectId (ObjectId type)
idStr = str(id)"""

"""collection.insert_one({
    "tabla": "",
    "periodicidad": 0,
    "data":[
        {
            "Campo1": {
                "Clave": "",
                "Llave": "",
                "Tipo de Dato": "",
                "Tipo de Dato Estadistico": "",
                "Descripcion": "",
                "Estructura": "",
                "Longitud": "",
                "Dominio": "",
                "Alias": "",
                "Area": "",
                "Marca": "",
                "Pais": "",
                "Region": ""
            },
            "Campo2": {
                "Clave": "",
                "Llave": "",
                "Tipo de Dato": "",
                "Tipo de Dato Estadistico": "",
                "Descripcion": "",
                "Estructura": "",
                "Longitud": "",
                "Dominio": "",
                "Alias": "",
                "Area": "",
                "Marca": "",
                "Pais": "",
                "Region": ""
            }
        }
    ]
})"""

collection.update_one({}, {"$set": {"tabla": "Prueba"}})

"""ids = collection.insert_many(
    [
        {"name": "Colima", "phone": "3141093387", "date": datetime.datetime.utcnow()},
        {"name": "Manza", "phone": "3141093387", "date": datetime.datetime.utcnow()}
    ]
)"""

# Getting documents
#print(db.list_collection_names()) # Gets the collection names
#print(collection.find_one()) # Gets the first document
#print(collection.find_one({"_id": id})) # Gets the matched document
#print(collection.find_one({"_id": idStr})) # Gets the matched document, idStr is str type and there are not a str type _id, Result = None
#print(collection.find_one({"_id": ObjectId(idStr)})) # Gets the matched document, parse a str to ObjectId
#print(collection.find_one({"name": "Yosa"})) # Gets the matched document
#print(ids.inserted_ids) # gets the _id inserted (2+ documets)
x = 0
for doc in collection.find(): # Prints all the collection docuemnts. .find({}, {"_id": 1}) = Shows just _id field
    x += 1
    print(doc)
    #collection.update_one({"_id": doc["_id"]}, {"$set": {"id": x}}) # Adds new field each document

"""for doc in collection.find({"name": "CDMX"}): # Prints all collections documents matched
    print(doc)"""

# Counting documents
#print(collection.count_documents({})) # Gets the number of documents
#print(collection.count_documents({"name": "Manza"})) # Gets the number of documents matched

#print("\n")
# Range queries
# There are operators that are useful to create advanced queries
d = datetime.datetime(2020, 1, 20, 18, 44, 8, 929000)
#for doc in collection.find({"date": {"$lt": d}}).sort("name"): # $lt means less than
 #   print(doc)

# Index
#collection.create_index([("id", pymongo.ASCENDING)], unique=True) # Create a index on a key that rejects documents whose value for that key already exists in the index
#print(sorted(list(collection.index_information())))
#collection.insert_one({"name": "Tecoman", "phone": "3141093387", "date": datetime.datetime.utcnow(), "id": 18})
#collection.insert_one({"name": "Colima", "phone": "3141093387", "date": datetime.datetime.utcnow(), "id": 16})