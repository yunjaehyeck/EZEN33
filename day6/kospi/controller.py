from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse



class KospiController:

    def __init__(self):
        pass

    def service(self):

        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, type=str)
        args = parser.parse_args()

        print('url값 : {}'.format(args.url))
        page = urlopen(args.url)
        soup = BeautifulSoup(page, 'html.parser')

        print(soup.prettify())  # 크롤링한 전체 내용 보기.

        kospi = soup.find('span', id = 'KOSPI_now')  # span 엔레먼트에 id가 KOSPI_now 인 컨트롤을 찾는다.

        return kospi.string










