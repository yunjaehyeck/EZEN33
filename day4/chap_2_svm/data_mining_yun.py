#  https://tensorflow.blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/2-3-7-%EC%BB%A4%EB%84%90-%EC%84%9C%ED%8F%AC%ED%8A%B8-%EB%B2%A1%ED%84%B0-%EB%A8%B8%EC%8B%A0/
#  BMI 계산
import random
ctx = '../data/'
def cal_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5 : return 'thin'
    if bmi < 25 : return 'normal'
    return 'fat'

fp = open(ctx+'bmi.csv', 'w', encoding='utf-8')  # w 는 write
fp.write('height, weight, label\r\n')
# 무작위 데이터 생성 - 사람의 개인 몸무개 값
cnt = {'thin': 0, 'normal': 0, 'fat': 0}  # 초기화

for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35, 100)
    label = cal_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))  # bmi.csv 파일에 결과값을 기록.
fp.close()
print('ok', cnt)










