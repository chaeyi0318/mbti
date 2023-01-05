from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://chaeyi0318:test@cluster0.xa9ngty.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {

}

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/board", methods=["GET"])
def homework_get():
    title_list = list(db.board.find({}, {'_id':False}))
    print(title_list)
    topic_list = list(db.topic.find({}, {'_id':False}))
    print(topic_list)

    return jsonify({'all_title': title_list, 'all_topic': topic_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)