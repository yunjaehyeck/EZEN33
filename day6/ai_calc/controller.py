from ai_calc.model import CalcModel
import tensorflow as tf

class CalcController:

    def __init__(self, num1, num2, opcode):
        # self._calc = CalcModel()  # 모델 생성자.  --> 이미 model.py에서 모델 file을 생성했으므로. 위 폴더의 파일들이 모델이 되어야 한다.
        self._num1 = num1
        self._num2 = num2
        self._opcode = opcode

    def calc(self):
        num1 = self._num1
        num2 = self._num2
        opcode = self._opcode

        print('컨트롤러에 들어온 num1 = {}, num2 = {}, opcode = {}'.format(num1, num2, opcode))  # view단에서 을어온 html확인

        sess = tf.Session()
        # 모델에서 학습시킨 결과값의 메타(로그) 정보들을 텐소플로우의 graph로 분석 시작.
        saver = tf.train.import_meta_graph('./ai_calc/saved_'+opcode+'/model-1000.meta')  # 더하기
        saver.restore(sess, tf.train.latest_checkpoint('ai_calc/saved_'+opcode+'/')) # checkpoint 는 . 모델합습시 발생한 이력 정보 넣어둔 파일

        graph = tf.get_default_graph()
        w1 = graph.get_tensor_by_name('w1:0')  # w1을 호출하고 바로 0으로 초기화
        w2 = graph.get_tensor_by_name('w2:0')
        feed_dict = {w1: num1, w2: num2}

        op_to_restore = graph.get_tensor_by_name('op_'+opcode+':0') # 이름 부여하고 0으로 초기화
        result = sess.run(op_to_restore, feed_dict)  # 새로운 feed_dict 값 대입

        print('최종결과 : {}'.format(result))

        return result  # app.py로 리턴 시킴.










