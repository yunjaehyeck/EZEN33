#  결정 트리decision tree는 분류와 회귀 문제에 널리 사용하는 모델
import pandas as pd
import os
import matplotlib.pyplot as plt
import mglearn
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

import numpy as np

# activate tenso1
# pip install mglearn

ram_price = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH, "ram_price.csv"))
plt.semilogy(ram_price.date, ram_price.price)
plt.xlabel('년')
plt.ylabel('가격')

# plt.show()

data_train = ram_price[ram_price['date'] < 2000]
data_test = ram_price[ram_price['date'] >= 2000]

x_train = data_train['date'][:,np.newaxis] #  train data 를 1열로 만든다.
y_train = np.log(data_train['price'])
tree = DecisionTreeRegressor().fit(x_train, y_train)  # 이 함수를 사용하는 방법 교육이 핵심
lr = LinearRegression().fit(x_train, y_train) # 이 함수를 사용하는 방법 교육이 핵심

x_all = ram_price['date'].values.reshape(-1, 1)  # x_all 을  1열로 만듬
pred_tree = tree.predict(x_all)
price_tree = np.exp(pred_tree)  # log  값 되돌리기
pred_lr = lr.predict(x_all)
price_lr = np.exp(pred_lr) # log 값 되돌리기
plt.semilogy(ram_price['date'], pred_tree, label='tree predict', ls = '-', dashes=(2, 1))
plt.semilogy(ram_price['date'], pred_lr, label='linear regression predict', ls=':')
plt.semilogy(data_train['date'], data_train['price'], label='train data', alpha=0.4)
plt.semilogy(data_test['date'], data_test['price'], label='test data')
plt.legend(loc = 1)
plt.xlabel('year', size = 15)
plt.ylabel('price', size = 15)
plt.show()


