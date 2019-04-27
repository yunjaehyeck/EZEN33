# 데이터베이스 연결(SQL Lite3) 하여 진행.  --> 기본 내장되어 있어 별도 설치 필요 없음.
import sqlite3

class Database:
    def __init__(self):
        self._conn = sqlite3.connect('./sqlite.db')

    # 테이블 만들기
    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Persons (
            userid varchar(10) primary key,
            password varchar(10),
            name varchar(10),
            phone varchar(15),
            address varchar(10),
            regdate date default current_timestamp 
        );
        """
        print('쿼리 체크: {}'.format(sql))
        self._conn.execute(sql)
        self._conn.commit()

    # 한줄 insert
    def insert_one(self, userid, password, name, phone, address):
        sql = """
            INSERT INTO Persons( userid, password, name, phone, address)
                VALUES( ?, ?, ?, ?, ?);
        """
        self._conn.execute(sql, userid, password, name, phone, address)  # 한번만 실행
        self._conn.commit()

    # 여러줄 insert # 쿼리에서는 튜플 () 로 데이터 튜플처리
    def insert_many(self):
        data = [
                ('lee','1','이순신', '000-0000-0000','사당')
                ,('hong','1','홍길동', '111-1111-1111','강남')
                ,('kim','1','김길수','222-2222-2222','부산')
        ]
        sql = """
            INSERT INTO Persons( userid, password, name, phone, address)
                VALUES( ?, ?, ?, ?, ?);
        """
        self._conn.executemany(sql, data)  # 데이터 구조가 튜플이 아니면 오류남. 다시 강조.
        self._conn.commit()

    # 한줄 select
    def fetch_one(self, userid) -> object:
        sql = """
            SELECT * FROM Persons WHERE userid LIKE ? ;
        """
        cursor = self._conn.execute(sql, userid)   # cursor 는 DB에서 얻오온 값의 목록을 의미한다.
        row = cursor.fetchone()
        return row

    # 여러줄 select
    def fetch_all(self) -> object:
        sql = """
            SELECT * FROM Persons;
        """
        cursor = self._conn.execute(sql)   # cursor 는 DB에서 얻오온 값의 목록을 의미한다.
        rows = cursor.fetchall()
        return rows

    # 갯수 구하기
    def count_all(self) -> object:
        sql = """
            SELECT count(*) FROM Persons;
        """
        cursor = self._conn.execute(sql)   # cursor 는 DB에서 얻오온 값의 목록을 의미한다.
        row = cursor.fetchone()
        return row

    # update
    def update(self, userid, password):
        sql = """
            UPDATE Persions
               SET password = ?
             WHERE userid = ? ;
        """
        self._conn.execute(sql, password, userid)
        self._conn.commit()

    # delete
    def remove(self):
        sql = """
            DELETE FROM Persions 
             WHERE userid = ? ;
        """
        self._conn.execute(sql, userid)
        self._conn.commit()



