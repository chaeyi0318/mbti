from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://chaeyi0318:test@cluster0.xa9ngty.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# title_list = list(db.board.find({}, {'_id': False}))
#
# count = len(title_list) + 1
#
# doc = {
#     'index': count,
#     'title': '제목12입니다.',
# }
#
# db.board.insert_one(doc)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/board", methods=["GET"])
def homework_get():
    title_list = list(db.board.find({}, {'_id':False}))
    topic_list = list(db.topic.find({}, {'_id':False}))

    db.board.find().limit(15)

    return jsonify({'all_title': title_list, 'all_topic': topic_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)