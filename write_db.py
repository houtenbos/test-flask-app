import pymongo
import datetime
import time

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection

while True:
    test_entry = {"msg":"Hello world",
                "date": datetime.datetime.now()}

    collection.insert(test_entry)
    time.sleep(60)

