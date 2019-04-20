# https://d2.naver.com/helloworld/8344782
# 사진 판별
# python - m pop install opencv-python
import cv2

class Lena:
    def __init__(self, fname):
        self.fname = fname
    def execute(self):
        print("cv2 버전: {}".format(cv2.__version__))
        original = cv2.imread(self.fname, cv2.IMREAD_COLOR)
        gray = cv2.imread(self.fname, cv2.IMREAD_GRAYSCALE)
        unchange = cv2.imread(self.fname, cv2.IMREAD_UNCHANGED)

        print('original shap is {}'.format(original.shape))

        cv2.imshow('Original', original)
        cv2.imshow('Gray', gray)
        cv2.imshow('Unchange', unchange)

        cv2.waitKey(0)   # 대기시간 없이 종료.


