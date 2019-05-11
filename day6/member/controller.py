from member.model import MemberDAO

class MemberController:
    def __init__(self):
        self._dao = MemberDAO()  # 객체 생성(생성자)

    def login(self, userid, password):
        row = self._dao.login(userid, password)   # 컨트롤러에서 받아오는 row 객체를 통해 view -> init -> controller -> model -> DB 연결이 가능하도록 엮는다.
        view = ''
        if row is None:
            view = 'index.html' # 화면에서 들어온 입력값이 없다면
        else:
            view = 'home.html'  # 화면에서 들어온 입력값이 있다면

        return view  # 반환할 화면 view 명칭

    def ui_calc(self):

        view = 'ui_calc.html'

        return view




