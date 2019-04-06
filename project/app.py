import sqlite3
from member.service import MemberService
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', name='')


@app.route('/login', methods=['POST'])
def login():
    print('로그인 들어옴')
    userid = request.form['userid']
    password = request.form['password']
    print("컨트롤러 아이디 {}, 비번 {}".format(userid, password))
    service = MemberService()
    row = service.login(userid, password)
    view = ''
    if row is None:
        view = 'index.html'
    else:
        view = 'main.html'
    return render_template(view)


if __name__ == '__main__':
    app.run()
