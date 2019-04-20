from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

ctx = '../data/'

cvs = pd.read_csv(ctx+'bmi.csv')
label = cvs['label']
w = cvs['weight'] / 100 # 최대 100 kg
h = cvs['height'] / 200 # 최대 2m

wh = pd.concat([w, h], axis=1)  # 하나의 차원으로 합침 : w + h

# 학습데이터와 테스트데이터 분리
data_train, data_test, label_train, label_test = train_test_split(wh, label)
clf = svm.SVC()
clf.fit(data_train, label_train)
predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 : ", ac_score)
print("리포트 : \n", cl_report)

"""



"""