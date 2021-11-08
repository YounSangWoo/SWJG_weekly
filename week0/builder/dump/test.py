from flask import Flask, render_template, request, url_for, redirect, make_response

app = Flask(__name__, static_url_path='/static')

@app.route('/hello_flask')
def hello_flask():
    return render_template('hello_flask.html')


@app.route('/')
def home():
    if request.cookies.get('test'):
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

# action in form and type in input attr in HTML
@app.route('/login_confirm', methods=['POST'])
def login_confirm():
    id_ = request.form['id_']
    pw_ = request.form['pw_']
    if id_ == 'test' and pw_ == 'test':
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('test', 'test')
        return resp
    else:
        return redirect(url_for('login'))


@app.route('/index')
def index():
    return render_template('index.html')


host_addr = "0.0.0.0"
port_num = "8080"
if __name__ == "__main__":
    app.run(host_addr, port_num, debug=True)


# login page : https://github.com/jaeseok3/flask_for_blog