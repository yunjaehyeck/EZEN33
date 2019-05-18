import tensorflow as tf
from flask_restful import reqparse
import numpy as np

class CabbageController:
    def __init__(self):
        pass

    def service_model():
        # Placeholder 는 외부에서 동적으로 주입받는 변수
        X = tf.placeholder(tf.float32, shape=[None, 4])  # Y는 관심없어, 다만 X는 4개.
        Y = tf.placeholder(tf.float32, shape=[None, 1])  # 결과값은 1개.
        # Variable 은 텐소 자체가 변경해 사용하는 변수
        W = tf.Variable(tf.random_normal([4, 1]), name='weight') # 공식 만들기 Y = wX+b
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b

        saver = tf.train.Saver()  # 데이터 가지고 오기.
        model = tf.global_variables_initializer()

        parser = reqparse.RequestParser()
        parser.add_argument('avg_temp', required=True, type=float)
        parser.add_argument('min_temp', required=True, type=float)
        parser.add_argument('max_temp', required=True, type=float)
        parser.add_argument('rain_fall', required=True, type=float)
        args = parser.parse_args()   # 파이썬이 인식할 수 있는 형태로 파싱

        avg_temp = float(args['avg_temp'])  # 파씽후. 다시 float로 변경.
        min_temp = float(args['min_temp'])
        max_temp = float(args['max_temp'])
        rain_fall = float(args['rain_fall'])

        with tf.Session() as sess:
            sess.run(model)
            save_path = 'cabbage/saved_model/model.ckpt'
            saver.restore(sess, save_path)
            data = ((avg_temp, min_temp, max_temp, rain_fall),)
            arr = np.array(data, dtype=np.float32)
            x_data = arr[0:4]
            dict = sess.run(hypothesis, feed_dict={X: x_data})

            print(dict[0])

        result = int(dict[0]) # 소숫점 이하 절삭

        return result

















