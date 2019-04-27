from chap_1_titanic_oop.controller import TitanicController
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


if __name__ == '__main__':
    c = TitanicController()  # 모델링
    c.test_random_variables()  # 텐소플로우 사용
    c.test_by_sklearn()  # 사이키런 모듈 사용
    c.submit()


