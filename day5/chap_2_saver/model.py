import tensorflow as tf

class TFModel:
    def __init__(self):
        self._num1 = 0.0
        self._num2 = 0.0

    @property
    def num1(self): return self._num1
    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self): return self._num2
    @num2.setter
    def num2(self, num2): self._num2 = num2

    def exec(self) ->float:

        print("-----------model > exec -------------------")

        num1 = self._num1
        num2 = self._num2

        var = tf.Variable([num1], dtype=tf.float32)
        con = tf.constant([num2], dtype=tf.float32)
        session = tf.Session()
        init = tf.global_variables_initializer()

        session.run(init)

        result = session.run(var * con)
        saver = tf.train.Saver()
        saver.save(session, './data/model.ckpt')

        return result



