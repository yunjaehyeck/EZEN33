from member.database import Database
import numpy as np


class MemberService:

    def __init__(self):
        pass

    @staticmethod
    def login(userid, password):
        print("서비스 아이디 {}, 비번 {}".format(userid, password))
        db = Database()
        row = db.login(userid, password)
        return row

    @staticmethod
    def make_session(raw_data):
        x_data = np.array(raw_data[:, 2:4]. dtype=np.float32)
        y_data = np.array(raw_data[:. 4], dtype = np.float32)

        y_data = y_data.reshape((25,1))

        X = tf.placeholder(tf.float32, shape=[None, 2], name='x-input')
        Y = tf.placeholder(td.float32, shape=[None, 1], name='bias' )

        hypothesis = tf.matmul(X,W) + b

        cost = tf.reduce_mean(tf.square(hypothesis -Y))

        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)
        train = optimizer.minimize