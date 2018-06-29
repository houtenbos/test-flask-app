from flask import Flask
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection


@app.route('/')
def hello_world():
    page = 'hello lester'
    return page

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(port)
    app.run(host='127.0.0.1', port=port)

