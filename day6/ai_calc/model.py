import sqlite3
import tensorflow as tf

class CalcModel:

    def __init__(self):
        pass

    @staticmethod
    def create_add_model():

        w1 = tf.placeholder(tf.float32, name='w1')  # 외부에서 들어온 값을 숫자형으로(바뀌는값) 치환  --> 텐소용
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1':8.0, 'w2':2.0}   # 딕셔너리 타입으로 "훈련시키기 위한 값 설정 --> 워낙 단순해서 아무거나 넣아도 무관

        # 8 + 2 라는 연산을 수행을 해보고 그 결과를 확인하여 (학습) 하는 컨트롤.
        r = tf.add(w1, w2, name='op_add')  # 더하기 함수 호출. 텐소
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')  # 페이크 변수(훈련시키기 위한 함수)
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1:feed_dict['w1'], w2:feed_dict['w2']})   # 모델을 만든다. # 'w1':8.0 ,... 호출

        print('TF 덧셈결과 {}'.format(result))

        saver.save(sess, './saved_add/model', global_step=1000)  #  저장을 수행하는대 1000번을 수행하여  saved_add 폴더에 model이라는 이름으로 저장한다.

    def create_div_model(self):
        w1 = self._w1
        w2 = self._w2
        feed_dic = self._feed_dict

        r = tf.math.floordiv(w1, w2, name='op_div')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1:feed_dic['w1'], w2:feed_dic['w2']})

        print('TF 나눗셈결과 {}'.format(result))

        saver.save(sess, './saved_div/model', global_step=1000)

    def create_mul_model(self):

        w1 = self._w1
        w2 = self._w2
        feed_dic = self._feed_dict

        r = tf.multiply(w1, w2, name='op_mul')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1:feed_dic['w1'], w2:feed_dic['w2']})

        print('TF 곱셈결과 {}'.format(result))

        saver.save(sess, './saved_mul/model', global_step=1000)

    def create_sub_model(self):

        w1 = self._w1
        w2 = self._w2
        feed_dic = self._feed_dict

        r = tf.subtract(w1, w2, name='op_sub')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1:feed_dic['w1'], w2:feed_dic['w2']})

        print('TF 뺄셈결과 {}'.format(result))

        saver.save(sess, './saved_sub/model', global_step=1000)













