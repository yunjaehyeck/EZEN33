#  앙상블 기법 포함 https://cafe.naver.com/cariro/782 , 랜덤포레스트 (RandomForest) 포함 : 여려게를 묶어서 예측 정확도를 높임
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

np.random.seed(0)  # 랜덤값을 고정시키는 값.
iris = load_iris()  # 내장된 정브를 가지고 옴.
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# print(df)
# print(df.columns)
"""
Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)'],
      dtype='object')

"""

df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75  # 전체 데이터의 25% 를 학습데이터로 셈플링 함.
train, test = df[df['is_train']==True], df[df['is_train']==False]
features = df.columns[:4]  # 앞에서 4번째 컬럼까지 취해라
y = pd.factorize(train['species'])[0]

########################
# 러닝  -- sklearn 등의 모듈을 포팅해 와서 러닝을 간단히 수행시킬 수 있다.
########################
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)

print(clf.predict(test[features]))  # 내가 가지고 있는 어떠한 값에 대한 예측값 확인 중.

#######################
# 테스팅 (정확도 평가)
#######################
preds = iris.target_names[clf.predict(test[features])]
print(pd.crosstab(test['species'], preds, rownames=['Actural Species'], colnames=['Predicated Species']))
print('피처별 중요도')
print(list(zip(train[features], clf.feature_importances_)))  # 리스트 타입을 결합 : zip()





