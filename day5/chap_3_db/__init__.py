from chap_3_db.controller import Controller

if __name__ == '__main__':
    c = Controller()

    count = c.count_members()
    print('총 회원수 >>>>>>> {} '.format(count))
