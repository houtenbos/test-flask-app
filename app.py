import os
from flask import Flask
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
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
        return page
    except Exception as e:
        print('Error:')
        print(e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(port)
    app.run(host='127.0.0.1', port=port)

