from flask import Flask
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.test_collection


@app.route('/')
def hello_world():
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

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)