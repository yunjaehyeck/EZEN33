# app.py 파일은 한개만 존재하며 , 프로젝트 최상단에서 "라우팅" 시켜 준다.
from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
from blood.model import BloodModel #컨트롤러에 만들지 않아 바로 model호출 해 버림. (정식x)
from gradient_descent.controller import GradientDescentController
from iris.controller import IrisController
from cabbage.controller import CabbageController
from kospi.controller import KospiController
from stock_ticker.controller import StockTickerController
import re  # 정규식 라이브러리


# 플라스크를 이용하기 위한 기본 템플릿 코드
app = Flask(__name__)   # app는 플라스크로 정의 함.

@app.route('/')  # 데코레이터
def index():
    # return render_template('index.html')    # 로그인 예시 화면 (1)
    return render_template('home.html')  # 홈화면 예시 (2)

@app.route('/login', methods=['POST'])  # index 의 from 의 submit 폼 이룸.---> 포스트 전송
def login():
    # print('로그인 들어옴')

    userid = request.form['userid']   # html 의 form 테그의 userid 테그값 얻어 옴.
    password = request.form['password']
    # print('로그인 들어온 아이디 {}, 비번 {}'.format(userid, password))  # view단에서 을어온 html확인

    c = MemberController()
    c.login(userid, password)

    view = c.login(userid, password)

    return render_template(view)  # 화면(view:html)에 결과 보여주기

@app.route('/move/<path>')  # < > 은 변수 처리 된다(1). # // a 테그의 url 을 삽입 : /move/ui_calc
def move_ui_calc(path):  # < > 은 변수 처리 된다(2).
    print("/move/<app> 호출 성공")
    return render_template('{}.html'.format(path))  # view  파일명.  # < > 은 변수 처리 된다.(3)

"""
# 아래 함수들은 @app.route('/move/<path>')  함수로 대체하여 모두 삭제(주석처리) 함.
@app.route('/move/home')
def home():
    print("home --> app 호출 성공")
    return render_template('home.html')

@app.route('/move/ai_calc')
def move_ai_calc():
    return render_template('ai_calc.html')  # 화면(view:html)에 결과 보여주기

@app.route('/move/blood')
def move_blood():
    print('app > move_blood 로그인 들어옴')
    return render_template('blood.html')
"""


@app.route('/ui_calc')
def ui_calc():
    print("ui_calc --> app 호출 성공")

    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else:
        print('넘어온 식 {}'.format(stmt))
        patt = '[0-9]+'   # 한개 이상의 숫자
        op = re.sub(patt, '', stmt) # 공백제거
        print('넘어온 연산자 {}'.format(op))
        nums = stmt.split(op)

        result = 0

        if op == '+':
            result = int(nums[0])+int(nums[1])
        elif op == '-':
            result = int(nums[0]) - int(nums[1])
        elif op == '*':
            result = int(nums[0]) * int(nums[1])
        elif op == '/':
            result = int(nums[0]) / int(nums[1])
        else:
            pass

    return jsonify(result=result)

# /ai_calc
@app.route('/ai_calc', methods=['POST'])
def ai_calc():
    print('move_ai_calc 로그인 들어옴')

    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']

    # print('계산기에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))  # view단에서 을어온 html확인

    c = CalcController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = result

    return render_template('ai_calc.html', **render_params)  ## 지금 함수의 여러 번수들을 모두 params로 보냄

# /blood
@app.route('/blood', methods=['POST'])
def blood():

    print('-------------------- blood(1) ---------------------------')

    weight = request.form['weight']
    age = request.form['age']

    print("weight:{}, age:{}".format(weight, age))

    # 모델 호출
    # 컨트롤러가 해야 하는 부분.  ---> 학습 시킴
    model = BloodModel('./blood/data/data.text')  # 정답을 알려주고 시작하는 <지도학습> 임... "결과는 파일로"
    raw_data = model.create_raw_data()
    render_params = {}   # 결과값 받는곳
    value = model.create_model(raw_data,weight,age)
    render_params['result'] = value  # html의 resut 에 값 할당

    # render_template : 플라스크에서 html의 화면단에 표현
    # render_params : 플라스크에서 html에 보내 값.

    print('-------------------- blood(2) ---------------------------')

    return render_template('home.html', **render_params)  # ** 모든 파람값을 화면단에 전송

@app.route('/gradient_descent', methods=['GET','POST'])
def gradient_descent():
    ctrl = GradientDescentController()
    name = ctrl.service_model()

    return render_template('gradient_descent.html', name = name)

@app.route('/iris', methods=['GET','POST'])
def iris():
    ctrl = IrisController()
    result = ctrl.service_model()

    return render_template('iris.html', result = result)

@app.route('/cabbage', methods=['GET','POST'])
def cabbage():
    ctrl = CabbageController()
    result = ctrl.service_model()
    render_params = {}
    render_params['result'] = result

    return render_template('cabbage.html', **render_params)

@app.route('/kospi', methods=['GET','POST'])
def kospi():

    ctrl = KospiController()
    kospi = ctrl.service()
    render_params = {}
    render_params['result'] = kospi

    return render_template('kospi.html', **render_params)

@app.route('/stock_ticker', methods=['GET','POST'])
def stock_ticker():
    ctrl = StockTickerController()
    price = ctrl.service()
    render_params = {}
    render_params['result'] = price

    return render_template('stock_ticker.html', **render_params)



###############
# 메인
###############
if __name__ == '__main__':
    app.run()

#########################################





