import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc   # 한글 파일 께짐 현상 처리
import seaborn as sns
from sklearn import preprocessing

ctx = '../data/'
filename = 'crime_police.csv'
# 텍스트 인코딩 타입을 지정 함.
df_crime_police = pd.read_csv(ctx+filename, sep=',', encoding='utf-8')
# aggfunc 는 평균값 리턴
df_police = pd.pivot_table(df_crime_police, index='구별', aggfunc=np.sum)
# 컬럼스
# print(df_crime_police.columns)
# print(df_police.columns)

"""
Index(['Unnamed: 0', '관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생',
       '강간 검거', '절도 발생', '절도 검거', '폭력 발생', '폭력 검거', '구별'],
      dtype='object')
Index(['Unnamed: 0', '강간 검거', '강간 발생', '강도 검거', '강도 발생', '살인 검거', '살인 발생'], dtype='object')

"""

df_police['강간검거율'] = df_police['강간 검거'] / df_police['강간 발생'] * 100
df_police['강도검거율'] = df_police['강도 검거'] / df_police['강도 발생'] * 100
df_police['살인검거율'] = df_police['살인 검거'] / df_police['살인 발생'] * 100
df_police['절도검거율'] = df_police['절도 검거'] / df_police['절도 발생'] * 100
df_police['폭력검거율'] = df_police['폭력 검거'] / df_police['폭력 발생'] * 100

# 불필요한 컬럼 삭제.
df_police.drop(['강간 검거','강도 검거','살인 검거','절도 검거','폭력 검거'], 1)

# print(df_police.columns)

# 검거율이 100이 넘는 것이 있는데... 기간상의 오류
ls_rate = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
for i in ls_rate:
    df_police.loc[df_police[i] > 100, i] = 100
df_police.rename(columns = {'강간 발생' : '강간'
                            ,'강도 발생' : '강도'
                            ,'살인 발생' : '살인'
                            ,'절도 발생' : '절도'
                            ,'폭력 발생' : '폭력'
                            }, inplace=True)
ls_crime = ['강간','강도','살인','절도','폭력']

x = df_police[ls_crime].values
min_max_scalar = preprocessing.MinMaxScaler()
"""
스케일링은 선형변환을 적용하여 전체 자료의 분포를  평균 0 , 분산 1이 되도록 만드는 과정
"""
x_scaled = min_max_scalar.fit_transform(x.astype(float))
df_police_norm = pd.DataFrame(x_scaled, columns=ls_crime, index=df_police.index)

df_police_norm[ls_rate] = df_police[ls_rate]
df_cctv_pop = pd.read_csv(ctx+'cctv_pop.csv', encoding='UTF-8', sep=',', index_col='구별')
# 0~ 1 사이의 값으로 변경 함.
df_police_norm[['인구수','CCTV']] = df_cctv_pop[['인구수','소계']]  # 소계 -> CCTV 이름 변경

df_police_norm['범죄'] = np.sum(df_police_norm[ls_crime], axis=1)
df_police_norm['검거'] = np.sum(df_police_norm[ls_rate], axis=1)

font = 'C:/Windows/Fonts/malgun.ttf'
font_name =font_manager.FontProperties(fname=font).get_name()
rc('font', family=font_name)
sns.pairplot(df_police_norm, vars=['강도', '살인', '폭력'], kind='reg', height=3)
sns.pairplot(df_police_norm, x_vars=['인구수', 'CCTV'], y_vars=['살인','강도'], kind='reg', height=3)

tmp_max = df_police_norm['검거'].max()
df_police_norm['검거'] = df_police_norm['검거'] / tmp_max * 100
df_police_norm_sort = df_police_norm.sort_values(by='검거', ascending=False)  # 내림차순 정렬
plt.figure(figsize=(10, 10))

sns.heatmap(df_police_norm_sort[ls_rate], annot=True, fmt='f', linewidths=5)
plt.title('범죄 검거 비율')

ls_crime = ['강간', '강도', '살인', '절도', '폭력', '범죄']
df_police_norm['범죄'] = df_police_norm['범죄'] / 5
df_police_norm_sort = df_police_norm.sort_values(by='범죄', ascending=False)
plt.figure(figsize=(10, 10))
sns.heatmap(df_police_norm_sort[ls_crime], annot=True, fmt='f', linewidths=5)
plt.title('범죄비율')
df_police_norm.to_csv(ctx+'police_norm.csv', sep=',', encoding='utf-8')

plt.show()
