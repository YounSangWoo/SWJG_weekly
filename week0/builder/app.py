import hmac

from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
import jwt
import hashlib
import datetime as dt
from datetime import datetime
import os
from bson.objectid import ObjectId

app = Flask(__name__)
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://dog:1234@3.36.126.56', 27017)
db = client.partylist

SECRET_KEY = 'Hello, welcome to the jungle'


############# main #############
@app.route('/')
def home():
    if request.cookies.get('mytoken'):

        token_receive = request.cookies.get('mytoken')

        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

            now = str(dt.datetime.now()).replace('-', '').replace(':','').replace(" ", '')[:14]

            return render_template('main.html',  allpartylist = getAllListID(), user = payload['OID'], username = payload['name'], time=now)

        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.exceptions.DecodeError:
            return redirect(url_for('login'))

    else:
        return redirect(url_for('login'))

################### This is part of jaehyun ###################
@app.route('/all_list', methods=['GET'])
def read_all_list():
    result = getAllListID()
    return jsonify({'result': 'success', 'alllists': result})

def getAllListID():
    result = objectIdDecoder(list(db.partylist.find({})))
    return result

def objectIdDecoder(list):
    results=[]
    for document in list:
        document['_id'] = str(document['_id'])
        temp = document['userlist']
        document['cur_num'] = len(temp)
        userNames = []
        for id in document['userlist']:
            item = getUser({'_id' : id})
            userNames.append(item['name'])
        document['userlist'] = userNames
        results.append(document)
    return results

def getUser(findIndex):
    for i, j in findIndex.items():
        key = i
        value = j.replace("'","\"")
    if (key == '') or (value == ''):
        return None
    value = value[10:-2]
    if (key == '') or (value == ''):
        return None
    value = ObjectId(value)
    json = db.user.find_one({key : value})
    result = objectIdDecoderUser(json)
    return result

def objectIdDecoderUser(user):
    result = user
    result['_id'] = str(result['_id'])
    return result

################### end ###################

# @app.route('/main')
# def main():
#     if request.cookies.get('mytoken'):
#
#         token_receive = request.cookies.get('mytoken')
#
#         try:
#             payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#             return render_template('main.html')
#
#         except jwt.ExpiredSignatureError:
#             return redirect(url_for('login'))
#         except jwt.exceptions.DecodeError:
#             return redirect(url_for('login'))
#
#     else:
#         return redirect(url_for('login'))

############# login #############

@app.route('/login')
def login():
    return render_template('login.html')

############# join #############
@app.route('/join')
def join():
    return render_template('join.html')

############# make party #############
@app.route('/makeparty')
def makeparty():
    if request.cookies.get('mytoken'):

        token_receive = request.cookies.get('mytoken')

        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
            return render_template('makeparty.html', username = payload['name'])

        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.exceptions.DecodeError:
            return redirect(url_for('login'))

    else:
        return redirect(url_for('login'))

@app.route('/api/makeparty', methods=['GET'])
def api_make_party():
    title_receive = request.values['title_give']
    comment_receive = request.values['comment_give']
    datetime_receive = makeDate(request.values['datetime_give'])
    maxNum_receive = request.values['maxNum_give']

    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    name = payload['name']

    oid_str = payload['OID']
    print("check", name)
    userlist = ObjectId(oid_str)
    userlist = repr(userlist)
    ls = []
    ls.append(userlist)

    db.partylist.insert_one({
        'author': name,
        'title': title_receive,
        'detail': comment_receive,
        'dueDate': datetime_receive,
        'maxNum': int(maxNum_receive),
        'userlist' : ls
    })
    return jsonify({'result' : 'success'})

def makeDate(datetime_receive):
    ls = datetime_receive.split(' ')

    ls1 = str(ls[0]).split('.')
    ls2 = str(ls[2]).split(':')


    if str(ls[1]) == '오후':
        if int(ls2[0]) != 12:
            ls2[0] = int(ls2[0]) + 12

    ls = ls1 + ls2

    result = []
    for item in ls:
        result.append(int(item))

    result = dt.datetime(result[0], result[1], result[2], result[3], result[4])
    print(result)
    return result


############# mypage #############
@app.route('/mypage')
def mypage():
    if request.cookies.get('mytoken'):

        token_receive = request.cookies.get('mytoken')

        try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

            result = getAllListID()
            writing = []
            participation = []

            print(payload['name'])
            for item in result:
                if item['author'] == payload['name']:
                    writing.append(item)
                else:
                    for i in item['userlist']:
                        if payload['name'] in i:
                            participation.append(item)

            print(participation)

            return render_template('mypage.html', username = payload['name'], my_participation_partylist=participation, my_writing_partylist=writing, userID=payload['OID'])

        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.exceptions.DecodeError:
            return redirect(url_for('login'))

    else:
        return redirect(url_for('login'))


# db에서 로그인 정보를 찾고, 성공시 토큰 발행
@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    pw_ = hashlib.sha256((pw_receive + SECRET_KEY).encode('utf-8')).hexdigest()

    result = db.user.find_one({'ID': id_receive, 'PW': pw_})


    if result is not None:
        payload = {
            'id': id_receive,
            'name' : result['name'],
            'OID' : str(result['_id']),
            'exp': dt.datetime.utcnow() + dt.timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# db에서 아이디가 있는지 조회
@app.route('/api/idCheck', methods=['GET'])
def api_id_check():
    id_receive = request.values['id_give']
    result = db.user.find_one({'ID': id_receive})

    if result is None:
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'fail'})


# 회원가입에서 정보를 db에 저장
@app.route('/api/makeUser', methods=['POST'])
def makeUser():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']
    hostedlist = []
    joinedlist = []

    crypt_pw = hashlib.sha256((pw_receive+SECRET_KEY).encode('utf-8')).hexdigest()

    db.user.insert_one({
        'name' : name_receive,
        'ID' : id_receive,
        'PW' : crypt_pw,
        'hostedlist' : hostedlist,
        'joinedlist' : joinedlist
    })

    return jsonify({'result' : 'success'})

@app.route('/api/addParticipation', methods = ['GET'])
def add_Participation():
    result = jsonify({'result' : 'fail', 'msg' : '수정에 실패했습니다.'})

    party_id_receive = request.values['party_id_give']
    user_id_receive = request.values['user_id_give']


    # convert str to Object
    OID = ObjectId(party_id_receive)
    cur = db.partylist.find_one({'_id' : OID})
    userlist = cur['userlist']

    for item in userlist:
        if user_id_receive in item:
            result = jsonify({'result': 'fail', 'msg': '이미 신청한 파티입니다.'})
            return result

    userlist.append(repr(ObjectId(user_id_receive)))
    db.partylist.update({'_id' : OID}, {'$set' : {'userlist' : userlist}})

    result = jsonify({'result': 'success'})
    return result

@app.route('/api/deleteParty', methods=['GET'])
def api_delete_party():
    OID_party_receive = request.values['party_id_give']
    try:
        OID = ObjectId(OID_party_receive)
        db.partylist.delete_one({'_id' : OID})
    except:
        return jsonify({'result' : 'fail', 'msg' : 'can not delete party'})
    return jsonify({'result' : 'success'})

@app.route('/api/deleteParticipation', methods=['GET'])
def delete_Participation():

    OID_party_receive = request.values['party_id_give']
    OID_user_receive = request.values['user_id_give']


    try:
        OID = ObjectId(OID_party_receive)
        result = db.partylist.find_one({'_id': OID})
        userlist = result['userlist']

        target = ""

        for item in userlist:
            if OID_user_receive in item:
                target = item

        userlist.remove(target)

        db.partylist.update({'_id': OID}, {'$set': {'userlist': userlist}})

    except:
        return jsonify({'result' : 'fail', 'msg' : 'can not delete party'})

    return jsonify({'result' : 'success'})

@app.route('/api/updateParty', methods=['GET'])
def api_update_party():

    OID_party_receive = request.values['party_id_give']
    OID = ObjectId(OID_party_receive)

    title_receive = request.values['title_give']
    comment_receive = request.values['comment_give']
    datetime_receive = makeDate(request.values['datetime_give'])
    maxNum_receive = request.values['maxNum_give']

    print(title_receive)
    print(comment_receive)
    print(datetime_receive)
    print(maxNum_receive)



    try:
        db.partylist.update({'_id': OID},
                            {'$set': {
                                    'title': title_receive,
                                    'detail': comment_receive,
                                    'dueDate': datetime_receive,
                                    'maxNum': int(maxNum_receive),
                                }
        })
    except:
        return jsonify({'result' : 'fail', 'msg' : '수정 실패'})

    return jsonify({'result' : 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
