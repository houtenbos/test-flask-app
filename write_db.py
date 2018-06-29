import pymongo
import datetime
import time

try:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.test_collection
    print('connected to database')
except Exception as e:
    print('Error:')
    print(e)


while True:
    test_entry = {"msg":"Hello world",
                "date": datetime.datetime.now()}

    collection.insert(test_entry)
    time.sleep(60)

