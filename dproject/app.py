import sqlite3
from member.service import MemberService
from blood.service import BloodService
from calc.service import CalcService
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

@app.route('/move/<path>',methods=['GET'])
def move(path):
    print('{} 로 이동 '.format(path))
    return render_template('{}.html'.format(path))

@app.route('/blood',methods=['POST'])
def blood():
    weight = request.form['weight']
    age = request.form['age']
    print("컨트롤러 아이디 {}, 비번 {}".format(weight, age))
    service = BloodService('blood/data.txt')
    raw_data = service.create_raw_data()
    render_params = {}
    val1 = service.make_session(raw_data, weight, age)
    return render_template('blood.html', **render_params)


@app.route('/image_handling',methods=['POST'])
def image_handling():
    fname = request.form['fname']
    color = request.form['color']
    print("컨트롤러 아이디 {}, 비번 {}".format(fname, color))
    service = image_handling('image_handling/lena.jpg')
    raw_data = service.create_raw_data()
    render_params = {}
    val1 = service.make_session(raw_data, fname, color)
    return render_template('image.html', **render_params)

@app.route('/calc', method=['POST'])
def calc():
    print("계산기 진입")
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    print("{} {} {} =".format(num1, num2, opcode))
    service = CalcService
    val = service.calc(num1, num2, opcode)
    render_params = {}
    render_params['result'] = val
    return render_template('calc.html', **render_params)


if __name__ == '__main__':
    app.run()













