import os
from flask import Flask
import pymongo

app = Flask(__name__)

mongo_url = os.environ['MONGO_URL']
print(mongo_url)
client = pymongo.MongoClient(mongo_url)
db = client.test_database
collection = db.test_collection


@app.route('/')
def hello_world():
    try:
        entries = collection.find()

        msg = ''
        date = ''
        posts = []

        for entry in entries:
            if 'msg' in entry:
                msg = entry['msg']
            if 'date' in entry:
                date = entry['date']
            post = msg + '<br>' + str(date)
            posts.append(post)

        head = '<html>'
        end = '</html>'
        content = ''
        for post in posts:
            content += '<br>' + post + '<br>'
        page = head + content + end
    except Exception as e:
        print('Error hello_world:')
        print(e)
        page = 'error!'
    return page

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(port)
    app.run(host='127.0.0.1', port=port)

