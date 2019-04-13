# 한글 데이터파일을 처리하는 방법 제공.
# CCTV 설치 수와 범죄율의 연관관계를 확인하는 예제.
# 이름 부분에 의미를 부여 함. ex : dfxxx : 데이터 프레임(2차원)
import pandas as pd
import xlrd
import numpy as np

ctx = '../data/'
filename = ctx + 'CCTV_in_Seoul.csv'
df_cctv = pd.read_csv(filename, encoding='UTF-8')
#print(seoul_cctv.head())

df_cctv_idx = df_cctv.columns
#print(seoul_cctv_idx)

"""
Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')
"""

df_cctv.rename(columns={df_cctv.columns[0]: '구별'}, inplace=True)  # 컬럼명 이름 변경
# print(seoul_cctv.head())

df_pop = pd.read_excel(ctx + 'population_in_Seoul.xls', encoding="UTF-8", header=2, usecols='B, D, G, J, N')   # 엑셀 파일 처리
# print(seoul_pop)

df_pop.rename(columns={df_pop.columns[0]: '구별'
                            ,df_pop.columns[1]: '인구수'
                            ,df_pop.columns[2]: '한국인'
                            ,df_pop.columns[3]: '외국인'
                            ,df_pop.columns[4]: '고령자'
                           }
                  , inplace=True)
df_cctv.sort_values(by='소계', ascending=True).head(5)
df_pop.drop([0], inplace=True)
df_pop['구별'].unique()
df_pop['구별'].isnull()

df_pop.drop([26], inplace=True)  # null 제거

# 없는 피처를 추가하면 새로운 피처가 추가됨.(add) , 있는거 하면 (Select)
df_pop['외국인비율'] = df_pop['외국인'] / df_pop['인구수'] * 100
df_pop['고령자비율'] = df_pop['고령자'] / df_pop['인구수'] * 100

# [] 를 줌으로 써. 다음부터는 반드시 list 타입을 받도록 한다.  --> 다른 데이터 타입 입력 불가.
# 열을 삭제하여야 하므로 옵션 '1'을 준다. , inplace는 즉시 적용 여부 설정.
# 행은 : 0 , 열은 : 1
df_cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], 1, inplace=True)

# 두 데이터프레임을 합치는대. 그 키 값을 '구별' 로 하여 새로운 데이터프레임으로 할당
df_cctv_pop = pd.merge(df_cctv, df_pop, on='구별')

#print(df_cctv_pop)

"""
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
고령자비율 상관계수 [[ 1.         -0.28078554]
 [-0.28078554  1.        ]] 
 외국인비율 상관계수 [[ 1.         -0.13607433]
 [-0.13607433  1.        ]]
"""


# 인덱스 설정
df_cctv_pop.set_index('구별', inplace=True)
# 상관관계 분석
cor1 = np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2 = np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])
# print('고령자비율 상관계수 {} \n 외국인비율 상관계수 []'.format(cor1, cor2))

df_cctv_pop.to_csv(ctx+'df_cctv_pop.csv')

print(df_cctv_pop)

# 결론 . -0.2 로는 명확한 상관관계를 확인 할 수 없다. 그래서. 이 데이터를 crime_plice로 범죄율로