# BeautifulSoup 을 이용한 웹 크롤링 해보기
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

context = "C:/Users/ezen/PycharmProjects/"
driver = webdriver.Chrome(context+"chromedriver")  # chromedriver.exe 가 활성화 되어 있어야 함.
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')
print(soup.prettify())
all_divs = soup.find_all('div', attrs = {'class', 'tit3'})
products = [div.a.string for div in all_divs]
for product in products:
    print(product)
driver.close()


