from flask import Flask, render_template, jsonify, request
import requests
from pymongo import MongoClient  
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbexam  


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    title_receive = request.form['title_give']  
    comment_receive = request.form['comment_give'] 
   
    memo = {'title': title_receive, 'comment': comment_receive}
    db.memo.insert_one(memo)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['PUT'])
def delete_article():
    # 1. 클라이언트로부터 데이터를 받기
    id_receive = request.form['_id_give']  # 클라이언트로부터 url을 받는 부분
    memo = {'_id': ObjectId(id_receive)}
    db.memo.remove(memo)

    return jsonify({'result': 'success'})

@app.route('/memo/1', methods=['PUT'])
def modify_article():
    # 1. 클라이언트로부터 데이터를 받기
    id_receive = request.form['_id_give'] 
    title_receive = request.form['title_give']  
    comment_receive = request.form['comment_give'] 
    memo = {'$set': {'title': title_receive, 'comment': comment_receive}}
    db.memo.update({'_id': ObjectId(id_receive)}, memo)

    return jsonify({'result': 'success'})


def getSpecificId():
  result = objectIdDecoder(list(db.memo.find({})))
  return result

def objectIdDecoder(list):
  results=[]
  for document in list:
    document['_id'] = str(document['_id'])
    results.append(document)
  return results

@app.route('/memo', methods=['GET'])
def read_articles():
    result = getSpecificId();
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)