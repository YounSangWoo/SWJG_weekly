from flask import Flask, render_template, jsonify, request, redirect, url_for
import jwt, hashlib, datetime as dt, os

app = Flask(__name__)

SECRET_KEY = 'plzStopAllDie'

@app.route('/')
def home():
    access_token = request.cookies.get('access_token')
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
        return redirect(url_for('login'))
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login'))

@app.route('/main')
def main():
    access_token = request.cookies.get('access_token')
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=['HS256'])
        return render_template('main.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for('login'))
    except jwt.exceptions.DecodeError:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    username = request.form['id_']
    password = request.form['pw_']

    if username == 'test' and password == 'test':
        payload = {
            'id': username,
            'exp': dt.datetime.utcnow() + dt.timedelta(minutes=60 * 60 * 24)
        }
        access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': access_token})

    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)