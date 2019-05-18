from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class StockTickerController:

    def __init__(self):
        pass

    def service(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ticker', required=True, type=str)  # ticker 라는 name을 html에서 가지고옴.
        args = parser.parse_args()

        print('입력된 코드 : {}'.format(args.ticker))
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+args.ticker

        print('url-------->'+url)

        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')

        print(soup.prettify())  # 크롤링한 전체 내용 보기.

        kospi = soup.find('span', id = 'KOSPI_now')  # span 엔레먼트에 id가 KOSPI_now 인 컨트롤을 찾는다.

        return kospi.string

