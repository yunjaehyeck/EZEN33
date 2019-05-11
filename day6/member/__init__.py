from member.model import MemberDAO  # DAO 연결하기

if __name__ == '__main__':
    dao = MemberDAO() # 생성자 만들기.
    dao.create()  # 테이블 만들기.
    # dao.insert_many()  # 테이블에 Insert 수행

    print('로그인 정보 테스트')
    print(dao.login('lee','1'))










