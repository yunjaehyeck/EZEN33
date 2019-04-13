###############################
# 1주차 시작.
###############################
#
# 컨테이너를 만드는 파일
#

# 판다스 : 문자열   ,  넌파이 : 숫자   ---> 텍스트 분석에 쓰이는 데이터 형태.
import pandas as pd  # from 은 생략 : 내장함수(객체) 이므로 생략.
import matplotlib.pyplot as plt # 파이썬과 텐소 중에소 파이썬용으로 가지고 옴.  ---> 그래프
import seaborn as sns  # 여러 그래프를 중첩해서 보여주는 객체.  --> 교차분석
import numpy as np # 숫자

ctx = 'C:/Users/ezen/PycharmProjects/day1_2/titanic/data/' # 가져올 데이터 위치
train = pd.read_csv(ctx+'train.csv') # 판다스를 이용해 파일 내용을 텍스트 형태로 얻어 옴.
test = pd.read_csv(ctx+'test.csv')

# print(train.head()) # 파일내용 출력(확인용) --  head()함수는 상위 5개 파일만을 선택 함.
#df = pd.DataFrame(train)
#print(df.columns)

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
"""


"""
[Variable]                [Definition]    [Key]
PassengerId
Survived
Pclass
Name
Sex
Age
SibSp
Parch
Ticket
Fare
Cabin
Embarked

survival 생존여부         Survival        0 = No, 1 = Yes
pclass   승선권 클래스    Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
sex      성별             Sex    
Age      나이             Age in years    
sibsp    동반한 형제자매, 배우자수   # of siblings / spouses aboard the Titanic    
parch    동반한 부모, 자식 수   # of parents / children aboard the Titanic    
ticket   티켄 번호        Ticket number    
fare     티켓 요금        Passenger fare    
cabin    객실번호         Cabin number    
embarked 승선한 항구명    Port of Embarkation    
C = Cherbourg 쉐부로, Q = Queenstown 퀜스타운, S = Southampton 사우스햄톤

"""
"""
# 생존률

f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')

sns.countplot('Survived', data=train, ax=ax[1])
ax[1].set_title('Survived')
plt.show()  # 생존률 38.4% 사망률 61.6%
"""

"""
데이터는 훈련데이터(train.csv) , 목적데이터(test.csv) 두가지로 제공 됩니다.
목적데이터는 위 항목에서는 Survived 정보가 빠져있습니다.
그것은 정답이기 때문입니다.
"""

# 성별
"""
f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'][train["Sex"] == 'male'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
train['Survived'][train["Sex"] == 'female'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[1], shadow=True)
ax[0].set_title('Survived(Male)')
ax[1].set_title('Survived(Female)')

plt.show()  # 남성 생존률 18.9%  사망률 81.1%   # 여성 생존률 74.2% 사망률 25.8%
"""

#승선권 Pclass
"""
f, ax = plt.subplots(1, 2, figsize=(18, 8))
train['Survived'][train["Sex"] == 'male'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived(Male)')
ax[1].set_title('Survived(Female)')

df_1 = [train['Sex'],train['Survived']]
df_2 = train['Pclass']
df = pd.crosstab(df_1, df_2, margins=True)

#print(df.head())
"""
"""
Pclass             1    2    3  All
Sex    Survived                    
female 0           3    6   72   81
       1          91   70   72  233
male   0          77   91  300  468
       1          45   17   47  109
All              216  184  491  891
"""

"""
f, ax = plt.subplots(2, 2, figsize=(20, 15))
sns.countplot('Embarked', data=train, ax=ax[0,0])
ax[0,0].set_title('No. of Passengers Boarded')

sns.countplot('Embarked', hue='Sex', data=train, ax=ax[0,1])
ax[0,1].set_title('Male - Female for Embarked')

# 배를 탄 항구 "Embarked"
sns.countplot('Embarked', hue='Survived', data=train, ax=ax[1,0])
ax[1,0].set_title('Pclass vs Survived')

sns.countplot('Pclass', data=train, ax=ax[1,1])
ax[1,1].set_title('Embarked vs PClass')

plt.show()
"""
"""
위 데이터를 보면 절반 이상의 승객이 ‘Southampton’에서 배를 탔으며, 여기에서 탑승한 승객의 70% 가량이 남성이었습니다. 현재까지 검토한 내용으로는 남성의 사망률이 여성보다 훨씬 높았기에 자연스럽게 ‘Southampton’에서 탑승한 승객의 사망률이 높게 나왔습니다.
또한 ‘Cherbourg’에서 탑승한 승객들은 1등 객실 승객의 비중 및 생존률이 높은 것으로 보아서 이 동네는 부자동네라는 것을 예상할 수 있습니다.
"""

# 결측치 제거

#train.info()
"""
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
"""

# print(train.isnull().sum())

"""
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
"""

"""
def var_chart(feature):
    survived = train[train['Survived'] == 1][feature].value_counts()  #생존자들.
    dead = train[train['Survived'] == 0][feature].value_counts()
    df = pd.DataFrame([survived, dead])
    df.index = ['survived', 'dead']
    df.plot(kind='bar', stacked=True, figsize=(10,5))
    plt.show()

# var_chart('Sex')
# var_chart('Pclass')
# var_chart('SibSp')
# var_chart('Parch')
# var_chart('Embarked')
"""

###############################
# 2주차 시작.
###############################
"""
# Carbin, Ticket 값 삭제 : null 값이 많아 데이터 외곡이 있을 것으로 판단 하여 제거
train = train.drop(['Cabin'], axis = 1)
test = test.drop(['Cabin'], axis = 1)
train = train.drop(['Ticket'], axis = 1)
test = test.drop(['Ticket'], axis = 1)
"""
# 삭제 확인  -- 빅데이터이니. 전체를 돌리면 다운이 발생할 수 있으므로. 상위값만 확인 할수 있게 하는 습관을 들이자.
# print(train.head())
# print(test.head())

# Embarked 값 가공

s_city = train[train['Embarked']=='S'].shape[0]   # 0차원 : 선을 의미 ===> 스칼라
c_city = train[train['Embarked']=='C'].shape[0]
q_city = train[train['Embarked']=='Q'].shape[0]

# print("S = " ,s_city) #644
# print("C = " ,c_city) #168
# print("Q = ",q_city) #77

train = train.fillna({"Embarked":"S"})  # 데이터를 Key:value 로 넣어라.  --> 앞에서 S 값이 가장 많아 이렇게 판단 함.
city_mapping = {"S":1, "C":2, "Q":3}
train['Embarked'] = train['Embarked'].map(city_mapping)
test['Embarked'] = test['Embarked'].map(city_mapping)

# print(train.head())
# print(test.head())



combine = [train, test]  # 두개를 묶어 샛팅
for dataset in combine:
    # 서민 찾아 내기 로직.
    dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)  # 정규식 : 영문글자가 있어야 하는대 반드시 필요하고 " . " 은 제외 시킨다.
out1 = pd.crosstab(train['Title'], train['Sex'])  # 텍스트 분석 라이브러리 판다(pd) .

# print(out1) # 결과 확인하니 유의미한거 확인

for dataset in combine :
    dataset['Title'] = dataset['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer'],'Rare')
    dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
out2 = train[['Title','Survived']].groupby(['Title'], as_index=False).mean()

# print(out2)

""" 결과를 분석해 보자.
    Title  Survived
0  Master  0.575000
1    Miss  0.701087
2      Mr  0.156673
3     Mrs  0.793651
4      Ms  1.000000
5    Rare  0.250000
6   Royal  1.000000
"""

title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0) # fillna
print(train.head())



train = train.drop(['Name', 'PassengerId'], axis = 1)
test = test.drop(['Name','PassengerId'], axis = 1)
combine = [train, test]
out3 = train.head()
# print(out3)


sex_mapping = {"male": 0, "female": 1}
for dataset in combine:
    dataset['Sex'] = dataset['Sex'].map(sex_mapping)

# Age 가공하기
train['Age'] = train['Age'].fillna(-0.5) # null 일경우 -0.5로 채워 넣어라  --> bins 에서 -1 과 0 사이에 위치시켜 'Unknown' 으로 잡아준 것임.
test['Age'] = test['Age'].fillna(-0.5)
bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]   # 넌파이(np)
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']

train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels) # 데이터를 잘라내라.
test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)

out4 = train.head()
# print(out4)

age_title_mapping = {0: "Unknown", 1: "Young Adult", 2:"Student", 3:"Adult", 4:"Baby", 5:"Adult", 6:"Adult"}  # 텍스트 값을 숫자로 변환하여 분석 하기위한 변경 ----> 분석을 위해서는 숫자로 치환 필요.
# age_title_mapping = {1: "Young Adult", 2:"Student", 3:"Adult", 4:"Baby", 5:"Adult", 6:"Adult"}

for x in range(len(train['AgeGroup'])):
    if train["AgeGroup"][x] == "Unknown":
        train["AgeGroup"][x] = age_title_mapping[train['Title'][x]]

for x in range(len(test['AgeGroup'])):
    if test["AgeGroup"][x] == "Unknown":
        test["AgeGroup"][x] = age_title_mapping[test['Title'][x]]

out5 = train.head()
# print(out5)

# Fare 처리
train['FareBand'] = pd.qcut(train['Fare'], 4, labels={1, 2, 3, 4})  # 4등분 하라.
test['FareBand'] = pd.qcut(test['Fare'], 4, labels={1, 2, 3, 4})

train = train.drop(['Fare'], axis = 1)
test = test.drop(['Fare'], axis = 1 )

##############################################
# 데이터 모델링 시작
##############################################

train_data = train.drop('Survived', axis = 1)
target = train['Survived']
out7 = train_data.shape
out8 = target.shape
out9 = train.info

print(out7)
print(out8)
print(out9)

########### 실제 훈련 시키기 전까지 데이터 전처리 완료.





















