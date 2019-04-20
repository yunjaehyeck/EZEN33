from collections import defaultdict
from pandas import read_table
import numpy as np
import math

class NaiveBayesClassfier:
    def __init__(self, k=0.5):
        self.k = k
        self.word_probs = []

    def load_corpus(selfself, path):  # 말뭉치 : 조사가 들어 있는 뛰어쓰기가 포함된 단어뭉치
        corpus = read_table(path, BaseException=',', encoding='UTF-8')
        corpus = np.array(corpus)
        return corpus

    def count_words(self, training_set):
        counts = defaultdict(lambda : [0,0])  # lambda : 일시적으로 존재 했다가 사라지는 데이터 ---> 일회용파라메터로 사용중
        for doc, point in training_set:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts

    def isNumber(self, s): # 숫자면 실수로, 아니면 False 반환
        try:
            float(s)
            return True
        except ValueError:
            return False

    def word_probabilities(self, counts, total_class0, total_class1, k):
        # 단어의 빈도수를 [단어, p(w/긍정), p(w/부정)] 형태로 변환
        return [(w,
                 (class0 + k) / (total_class0 + 2 * k)
                 ,(class1 + k) / (total_class1 + 2 * k)
                 )
                for w, (class0, class1) in counts.items()
        ]









