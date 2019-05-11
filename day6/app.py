# app.py 파일은 한개만 존재하며 , 프로젝트 최상단에서 "라우팅" 시켜 준다.
from flask import Flask, render_template, request, jsonify
from member.controller import MemberController
from ai_calc.controller import CalcController
import re  # 정규식 라이브러리


# 플라스크를 이용하기 위한 기본 템플릿 코드
app = Flask(__name__)   # app는 플라스크로 정의 함.

@app.route('/')  # 데코레이터
def index():
    return render_template('index.html')

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
    print("app 호출 성공")
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

    weight = request.form['weight']
    age = request.form['age']

    print("weight:{}, age:{}".format(weight, age))

    return render_template('home.html')

###############
# 메인
###############
if __name__ == '__main__':
    app.run()

#########################################





