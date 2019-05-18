import numpy as np
import tensorflow as tf
from keras.models import load_model
from flask_restful import reqparse
from sklearn import datasets
from keras import backend as K

class IrisController:
    def __init__(self):
        global model, graph, target_names
        K.clear_session()
        model = load_model('./iris/saved_model/iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_names

    def service_model(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sepal_length', required=True, type=float)  # 필수 값으로 지정
        parser.add_argument('sepal_width', required=True, type=float)  # 필수 값으로 지정
        parser.add_argument('petal_length', required=True, type=float)  # 필수 값으로 지정
        parser.add_argument('petal_width', required=True, type=float)  # 필수 값으로 지정
        args = parser.parse_args()  # 외부에서 값을 입력 받음.

        features = [args['sepal_length']
                    ,args['sepal_width']
                    ,args['petal_length']
                    ,args['petal_width']
                ]

        features = np.reshape(features, (1, 4))

        with graph.as_default():
            Y_pred = model.predict_classes(features)  # 예측값

        result = {'species ' : target_names[Y_pred[0]]}  # 예측값 중에서 0번째(가장 확율이 높은) 여석을 선택.

        return result







