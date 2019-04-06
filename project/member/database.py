import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite3.db')

    def create(self):
        cursor = self.conn.execute("DROP TABLE MEMBER")
        self.conn.commit()
        query = """
            CREATE TABLE IF NOT EXISTS MEMBER(
                USERID VARCHAR(10) PRIMARY KEY,
                PASSWORD VARCHAR(10),
                PHONE VARCHAR(10),
                REGDATE DATE DEFAULT CURRENT_TIMESTAMP 
            );
        """
        print(' 쿼리체크 ')
        print(query)
        self.conn.execute(query)
        self.conn.commit()

    def insert_many(self):
        data = [
            ('lee', '1', '010-1234'),
            ('kim', '1', '010-2345'),
            ('park', '1', '010-4567')
        ]
        stmt = "INSERT INTO MEMBER(USERID, PASSWORD, PHONE) VALUES(?, ?, ?)"
        self.conn.executemany(stmt, data)
        self.conn.commit()

    def fetch_one(self):
        cursor = self.conn.execute("SELECT * FROM MEMBER WHERE USERID LIKE 'lee'")
        row = cursor.fetchone()
        print('이씨')
        print(row)

    def fetch_all(self):
        cursor = self.conn.execute("SELECT * FROM MEMBER")
        rows = cursor.fetchall()
        count = 0
        for i in rows:
            count += 1

        print(count)

    def login(self, userid, password):
        sql = """
            SELECT * FROM MEMBER
            WHERE USERID LIKE ?
                AND PASSWORD LIKE ?
        """
        data = [
            userid,
            password
        ]
        cursor = self.conn.execute(sql, data)
        row = cursor.fetchone()
        print("조회한 회원의 상세 {}".format(row))
        return row














