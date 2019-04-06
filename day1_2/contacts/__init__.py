from contacts import Contacts

# 메인
if __name__ == '__main__':
    Contacts.Contacts.run()  # staticmethod 일 경우
    # c = Contacts() # staticmethod 아닌 self가 있을 경우
    # c.run()