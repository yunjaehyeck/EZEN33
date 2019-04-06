from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
# 랜덤포레스트 분류  알고리즘

import pandas as pd
import numpy as np
np.random.seed(0) # 랜덤값을 고정시키는 로직

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(df.head())

print(df.columns)

"""
[5 rows x 4 columns]
Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)'],
      dtype='object')
"""

df['species']=pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())

# print(df.columns)
"""
[5 rows x 5 columns]
Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)', 'species'],
      dtype='object')
"""

df['is_train'] = np.random.uniform(0,1,len(df))<=.75  # train set 75%
#print(df.columns)
"""
[5 rows x 5 columns]
Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)', 'species', 'is_train'],
      dtype='object')
"""

train, test = df[df['is_train'] == True],  df[df['is_train'] == False]

features = df.columns[:4] # 앞에서부터 4번째 컬럼(피처)까지 추출
print(features)

y = pd.factorize(train['species'])[0]
print(y)

 # ****
 # 학습단계
 # ****
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)
print(clf.predict(test[features]))
clf.predict_proba(test[features])[0:10]

# ****
# 정확도 평가
# ****
preds = iris.target_names[clf.predict(test[features])]
print(preds[0:5])

print(test['species'].head())

print('크로스탭 결과')
print(pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames =['Predicted Species']))

"""
Predicted Species  setosa  versicolor  virginica
Actual Species                                  
setosa                 13           0          0
versicolor              0           5          2
virginica               0           0         12
"""

print('피처별 중요도')
print(list(zip(train[features], clf.feature_importances_)))

""" 
피처별 중요도
[('sepal length (cm)', 0.11185992930506346),
 ('sepal width (cm)', 0.016341813006098178), 
 ('petal length (cm)', 0.36439533040889194),
  ('petal width (cm)', 0.5074029272799464)]
"""

"""
앙상블(ensemble)은 여러 머신러닝 모델을 연결하여 더 강력한 모델을 만드는 기법이다.
다양한 앙상블 기법중에서
랜덤 포레스트(random forest)와
그래티언트 부스팅(gradient boosting)결정 트리는
둘 다 모델을 구성하는 기본 요소로 결정 트리를 사용한다.

이 두 모델은 분류와 회귀 문제의 다양한 데이터셋에서 효과적이라고 입증되어있다.

< 랜덤 포레스트 >
결정 트리의 주요 단점은 훈련 데이터에 과대적합되는 경향이 있다는 것이었다.
랜덤 포레스트는 이 문제를 회피할 수 있는 방법이다.
랜덤 포레스트는기본적으로 여러 결정 트리의 묶음이라고 보면 된다.
각 트리는 비교적 예측을 잘 하구 있지만 일부에 과대 적합하다는 경향을 가지고 있음에 기초한다.
서로 다른 방향으로 과대적합된 트리를 많이 만들면 그 결과를 평균냄으로써 과대적합된 양을 줄일 수 있다.
이러한 전략은 구현하기 위해서는 결정 트리를 많이 만들어야 한다.
각각의 트리는 타깃 예측을 잘 해야하고 다른 트리와는 구별되어야 한다.
"""

