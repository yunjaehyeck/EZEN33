from calc import Calc


def main():
    calc = Calc.Calc(3, 7)
    print("{} + {} = {}".format(calc.first, calc.second, calc.sum()))


# 메인
if __name__ == '__main__':
    main()