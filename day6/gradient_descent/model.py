import tensorflow as tf

class GradientDescentModel:
    def __init__(self):
        pass

    def create_model(self):
        X = [1., 2., 3.]   # 대분자는 확률변수 = 값의 확정없이 1. , 2. , 3. 중에 하나로 들어갈 예정의 불확정 함수
        Y = [1., 2., 3.]

        m = n_samples = len(X)
        W = tf.placeholder(tf.float32)
        hypothesis =  tf.multiply(X, W) # 가설설정   Y = wX + b
        cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2))/m   # 확율이기에 정확하지 않기 때문에 근사값들로 수렴 시킴.
        W_val = []
        cost_val = []
        save_file = './saved_model/model.ckpt'  # checkpoint
        _ = tf.Variable(initial_value='fake_variable')
        saver = tf.train.Saver()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            for i in range(-30, 50):
                W_val.append(i * 0.1)  # U 자형 차트를 그리기 위한 공식
                cost_val.append(sess.run(cost, feed_dict={W: i* 0.1}))

            saver.save(sess, save_file) # 앞의 with 값을 모델로 만들어 파일로 생성하라.

        print('Model Saved !!')






















