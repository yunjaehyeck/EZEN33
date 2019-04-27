from chap_2_saver.controller import TFController

if __name__ == '__main__':
    c = TFController()
    num1 = 5.0
    num2 = 10.0
    print('{}*{}={}'.format(num1, num2, c.calc(num1, num2)))