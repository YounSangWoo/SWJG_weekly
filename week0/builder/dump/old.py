import requests
from flask import Flask, render_template, redirect, url_for, make_response
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

@app.route("/", methods=["POST", "GET"])
def home():
    # 쿠키가 있을 경우
    if request.cookies.get('access_token'):
        print("cookie")
        access_token = request.cookies.get('access_token')
        url = 'http://127.0.0.1:5000/protected'
        head = {'Authorization': 'Bearer ' + access_token}

        # render main with header
        return render_template('main.html')

    # 쿠키가 없을 경우
    else:
        # 로그인 버튼 클릭 시
        if request.method == "POST":
            print("post")
            username = request.form['id_']
            password = request.form['pw_']

            # 로그인 실패
            if username != "test" or password != "test":
                return render_template('login.html')
            # 로그인 성공
            else:
                access_token = create_access_token(identity=username)
                res = make_response(render_template('main.html'))
                res.set_cookie('access_token', access_token)

                # render main with header
                return res

        # 기본 렌더링, 첫 접속 시
        else:
            print("no cookie, no post")
            return render_template('login.html')

    # # 로그인에서 로그인 할 경우
    # if request.method == "POST":
    #     username = request.form['id_']
    #     password = request.form['pw_']
    #
    #     # 로그인 실패
    #     if username != "test" or password != "test":
    #         return render_template('hello_flask.html')
    #
    #     # 로그인 성공
    #     access_token = create_access_token(identity=username)
    #     token = jsonify(access_token=access_token)
    #     url = 'http://127.0.0.1:5000/protected'
    #     head = {'Authorization': 'Bearer ' + access_token}
    #
    #     success = requests.get(url, headers=head)
    #     print(success)
    #     return render_template('main.html')
    #
    # # 쿠키가 있을 경우
    # if request.cookies.get('access_token'):
    #     access_token = request.cookies.get('access_token')
    #     url = 'http://127.0.0.1:5000/protected'
    #     head = {'Authorization': 'Bearer ' + access_token}
    #
    #     respone = requests.get(url, headers=head)
    #
    #     r = make_response(render_template('main.html'))
    #
    #
    # # 기본 페이지 렌더링
    # return render_template('login.html')


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login_confirm", methods=["POST"])
def login():
    username = request.form['id_']
    password = request.form['pw_']
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    token = jsonify(access_token=access_token)
    url = 'http://127.0.0.1:5000/protected'
    head = {'Authorization': 'Bearer ' + access_token}

    success = requests.get(url, headers=head)

    #######################################
    # response = redirect(url_for('protected'), access_token)
    # response.headers['Authorization'] = 'Bearer ' + access_token
    # print(response.headers)
    return ''


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/main", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    # return jsonify(logged_in_as=current_user), 200
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)


# jwt : https://fenderist.tistory.com/141
# https://qkqhxla1.tistory.com/968

# jwt header : https://stackoverflow.com/questions/13825278/python-request-with-authentication-access-token
# https://learning.postman.com/docs/sending-requests/authorization/#bearer-token

# cookie : https://stackoverflow.com/questions/46661083/how-to-set-cookie-in-python-flask
