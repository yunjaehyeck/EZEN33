from chap_3_db.db import Database


class Model:
    def __init__(self):
        pass

    def create_db(self) -> str:
        db = Database()  # DB 접속
        db.create()  # 테이블 생성
        # db.insert_many()
        count = db.count_all()  # insert 성공 여부 확인
        print('DB에 등록된 회원수 : {}', count)

        return count





