from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://chaeyi0318:test@cluster0.xa9ngty.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('default.html')

@app.route('/list.html',methods=['GET'])
def mbti():
    mbti = request.args.get('user')
    return render_template('list.html',mbti=mbti)

@app.route('/index.html',methods=['GET'])
def mbti1():
    mbti = request.args.get('user')
    return render_template('index.html',mbti=mbti)

@app.route('/list.html')
def homea():
    return render_template('list.html')

@app.route('/index.html')
def homes():
    return render_template('index.html')

@app.route('/default.html')
def homed():
    return render_template('default.html')

@app.route('/write.html')
def homef():
    return render_template('write.html')

@app.route("/mbti", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    mbti_receive = request.form['mbti_give']
    title_num_receive = request.form['title_num_give']

    mbti_list = list(db.mbtis_comment.find({}, {'_id': False}))
    count = repr(len(mbti_list) + 1)
    doc = {
        'num': count,
        'comment':comment_receive,
        'mbti':mbti_receive,
        'title_num' :title_num_receive
    }
    db.mbtis_comment.insert_one(doc)

    return jsonify({'msg':'댓글 작성 완료!'})

@app.route("/mbti_show", methods=["post"])
def comment_get():
    title_num_receive = request.form['title_num_give']
    mbtis = list(db.mbtis_comment.find({'title_num':title_num_receive}, {'_id': False}))
    return jsonify({'mbtis':mbtis})

@app.route("/board_one", methods=["post"])
def board_get():
    num = request.form['titlenum_give']
    boards = list(db.mbtis_title.find({'num':num}, {'_id': False}))
    return jsonify({'boards':boards})

@app.route("/board", methods=["GET"])
def homework_get():
    title_list = list(db.mbtis_title.find({}, {'_id': False}))
    topic_list = list(db.topic.find({}, {'_id': False}))

    return jsonify({'all_title': title_list, 'all_topic': topic_list})

@app.route("/create", methods=["post"])
def create_title():
    title_receive = request.form['title_give']
    # mbti_receive = request.form['mbti_give']
    content_receive = request.form['content_give']
    pw_receive = request.form['pw_give']

    create_list = list(db.mbtis_title.find({}, {'_id': False}))
    count = len(create_list) + 1

    doc = {
        'num': repr(count),
        'content': content_receive,
        # 'mbti': mbti_receive,
        'pw' : pw_receive,
        'title' : title_receive
    }
    db.mbtis_title.insert_one(doc)

    return jsonify({'msg':'게시글 작성 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)