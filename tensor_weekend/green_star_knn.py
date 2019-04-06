import mglearn
import matplotlib.pyplot as plt

mglearn.plots.plot_knn_regression(n_neighbors=1)

# n_neighbors=1 일 때 알고리즘

# plt.show()

"""
x축에 3개의 테스트 데이터를 녹색별로 표시한다.
최근접 이웃을 한개만 사용할 때 예측은 가장 가까운 데이터 포인트의 값으로 인식한다.
"""

mglearn.plots.plot_knn_regression(n_neighbors=3)
# plt.show()

from mglearn.datasets import make_wave
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

x, y = make_wave(n_samples=40)

x_train, x_test, y_train, y_test = \
     train_test_split(x, y, random_state=0, test_size=0.3)

knn_reg = KNeighborsRegressor(n_neighbors=3, n_jobs=-1)
# n_jobs = 사용할 코어의 수. -1 이면 모든 코어를 사용함
knn_reg.fit(x_train, y_train)

print("{:3f}".format(knn_reg.score(x_test, y_test)))

# 0.697183  # 정확도가 70%도 안된다. 더 높여야한다



