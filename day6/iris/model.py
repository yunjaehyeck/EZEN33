from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense

class IrisModel:
    def __init__(self):
        iris = datasets.load_iris()
        self._X = iris.data
        self._Y = iris.target

    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1,1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))  # relu 라는 알고리즘 사용.  # 4개의 정보(dim)을 이용해서 결론을 뽑을 것임.
        model.add(Dense(3, activation='softmax'))  # 차원 줄이기 수행  : 4가지 값을 이용해 결과값의 가능성을 줄여 나감.
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X, Y_1hot, epochs=300, batch_size=10)  # 반복횟수와 셈플 사이즈

        print('모델 트레이닝 완료')

        file_name = './saved_model/iris_model.h5'  # Keras 모델의 저장 확장자 (.h5)
        model.save(file_name)

        print('모델 저장 완료')




