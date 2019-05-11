import tensorflow as tf
import numpy as np

class BloodModel:
    def __init__(self, fname):
        # fname : 훈련시키기 위한 (모델생성) 데이터
        self.fname = fname

    def create_raw_data(self):
        tf.set_random_seed(777)
        raw_data = np.genfromtxt(self.fname, skip_header=36)

        return raw_data

    @staticmethod
    def create_model(raw_data, weight, age):
        x_data = np.array(raw_data[:, 2:4], dtype=np.float32)
        y_data = np.array(raw_data[:, 4], dtype=np.float32)
        y_data = y_data.reshape(25, 1)

        # placeholder 는 외부에서 주입되는 데이터를 텐소플로우의 데이터 적제 형으로 변경 하는 작업.
        X = tf.placeholder(tf.float32, shape=[None, 2], name='x-input')
        Y = tf.placeholder(tf.float32, shape=[None, 1], name='y-input')

        # 대문자로 쓸 경우 확률변수로 취급 됨.
        # Y = W ( 모델-투입되는 수 )  b
        # variable 은 텐소가 결정하는 값 이다.
        W = tf.Variable(tf.random_normal([2,1]), name='weight')  # 가중치 >  2개의 변수를 넣음.
        b = tf.Variable(tf.random_normal[1], name='bias') # 편차값

        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))  # 예측된 값과 실제값의 평균을 최소화 시켜서 서로 가깝게 수렴 시킨다.
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)
        train = optimizer.minimize(cost)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        cost_history = []

        for step in range(2000):
            cost_val, hy_val, _ = sess.run([
                cost
                ,hypothesis
                ,train
            ], feed_dict={X: x_data, Y: y_data})

            if step % 10 == 0:  # 결과값중 셈플링 해서 결과값을 보겠다.
                print(step, "Cost : ", cost_val)
                cost_history.append(sess.run(cost, feed_dict={X: x_data, Y: y_data}))

        val = sess.run(hypothesis, feed_dict={X: [[weight, age]]})

        print('혈중 지방농도: {}'.format(val))

        result = ''
        if val < 150:
            result = '정상'
        elif 150 <= val  < 200:
            result = '경계역 중성지방혈증'
        elif 200 <= val < 500:
            result = '정상'
        elif 500 <= val < 1000:
            result = '정상'
        elif 1000 <= val :
            result = '췌장염 발병 가능성 고도화'

        return result







