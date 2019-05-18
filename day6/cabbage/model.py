import tensorflow as tf
from pandas.io.parsers import read_csv
import numpy as np

class CabbageModel:

    def __init__(self):
        pass

    def create_model(self):
        model = tf.global_variables_initializer()
        data = read_csv('data/price_data.csv', sep=',')
        xy = np.array(data, dtype=np.float32)
        x_data = xy[:, 1:-1]
        y_data = xy[:, [-1]]
        X = tf.placeholder(tf.float32, shape=[None, 4]) # 4개 받아서
        Y = tf.placeholder(tf.float32, shape=[None, 1])  # 1개로 답함.
        W = tf.Variable(tf.random_normal([4,1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hypothesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hypothesis - Y))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)  # 오차를 최소화 하라.

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for step in range(100000):
                cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})  # 000_ 들어가는 것은 페이크 변수(임시변수)
                if step % 500 ==0:
                    print('#', step, " 손실비용", cost_)
                    print("_ 배추가격 : ", hypo_[0])

            saver = tf.train.Saver()  # 학습결과 저장
            save_path = './saved_model/model.ckpt'
            saver.save(sess, save_path)  # 파일로 저장.
































