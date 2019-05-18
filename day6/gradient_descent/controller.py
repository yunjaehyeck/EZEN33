import tensorflow as tf
import matplotlib.pyplot as plt

class GradientDescentController:

    def __init__(self):
        pass

    def service_model(self):

        X = [1., 2., 3.]   # 대분자는 확률변수 = 값의 확정없이 1. , 2. , 3. 중에 하나로 들어갈 예정의 불확정 함수
        Y = [1., 2., 3.]

        m = n_samples = len(X)
        W = tf.placeholder(tf.float32)
        hypothesis =  tf.multiply(X, W) # 가설설정   Y = wX + b
        cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2))/m   # 확율이기에 정확하지 않기 때문에 근사값들로 수렴 시킴.
        W_val = []
        cost_val = []

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(-30, 50):
                W_val.append(i * 0.1)
                cost_val.append(sess.run(cost, {W: i * 0.1}))

        plt.plot(W_val, cost_val, 'ro')
        plt.ylabel('cost')
        plt.xlabel('W')
        plt.savefig('./static/img/gradient_descent.svg')  # 결과 이미지를 해당 위치에 저장

        return "경사하강법(gradient_descent)"







