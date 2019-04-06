from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from wordcloud import WordCloud

import pandas as pd # 판다스 사용
import re
import nltk
# nltk.download()  # 최초 1회 nltk 모듈을 받고, 주석에 기록한다.
import matplotlib.pyplot as plt


okt = Okt()
okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)


from nltk.tokenize import word_tokenize

ctx = 'C:/Users/ezen/PycharmProjects/day2/data/'
filename = ctx + 'kr-Report_2018.txt'

with open(filename, 'r', encoding='utf-8') as f:
    texts = f.read()
# print(texts[:300])

texts = texts.replace('\n', ' ')   # 해당줄의 줄바꿈 내용 제거
tokenizer = re.compile('[^ ㄱ-힣]+')   # 한글과 띄어쓰기를 제외한 모든 글자를 선택
texts = tokenizer.sub('', texts)   # 한글과 띄어쓰기를 제외한 모든 부분을 제거

# print(texts[:7])

tokens    = word_tokenize(texts)
tokens[:7]

# 불용어 단어 처리
noun_token = []
for token in tokens:
    token_pos = okt.pos(token)
    temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == "Noun"]
    if len(''.join(temp)) > 1:
        noun_token.append("".join(temp))
texts = " ".join(noun_token)
# print(texts[:300])

with open(ctx+'stopwords.txt','r',encoding='UTF-8') as f:
    stopwords = f.read()

stopwords = stopwords.split(',')

# print(stopwords[:10])

text = [text for text in tokens if text not in stopwords]
freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)

# print(freqtxt[:30])

okt.pos('가치창출') # 뛰어쓰기 오류도 자동처리
okt.pos('갤러시') # 오타는 갤럭시로 처리

wcloud = WordCloud(ctx + 'D2Coding.ttf', relative_scaling=0.2, background_color='white').generate("".join(texts))

plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
plt.show()






