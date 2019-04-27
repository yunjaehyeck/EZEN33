import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

class TitanicModel:
    def __init__(self):
        self._context = None
        self._fname = None
        self._train = None
        self._test = None

        self.test_id = None  # 테스트의 PK 대체키 저장용.

    ####################
    # Get
    ###################
    @property  # Get 역활
    def context(self) -> object: return self._context  # 람다식
    @property
    def fname(self) -> object: return self._fname
    @property
    def train(self) -> object: return self._train
    @property
    def test(self) -> object: return self._test
    @property
    def test_id(self, test) -> object: return self._test_id

    ####################
    # Set
    ####################
    @context.setter  # Set 역활
    def context(self, context): self._context = context
    @context.setter
    def fname(self, fname): self._fname = fname
    @context.setter
    def train(self, train): self._train = train
    @context.setter
    def test(self, test): self._test = test
    @context.setter
    def test_id(self, test_id): self._test_id = test_id


    ###################
    # 함수 - 모델
    ##################
    def new_file(self) -> str:   # 람다식 : str 로 반환
        return self._context + self._fname

    # 데이터 프레임으로 변환
    def new_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file)

    # 후크함수 : 일련의 동작의 패턴을 동기화 시킬 필요가 있을경우 반복적인것은 별도로 빼내서 함수화 함.
    # 외부에 이 함수만을 노출히켜서, 하위에 함수들을 규칙성없게 마구 호출해 사용하는 것을 방지 함.
    def hook_process(self, train, test) -> object:
        print('----------------------1. drop Cabin, Ticket 삭제 --------------------------')
        t = self.drop_feature(train, test, 'Cabin')  # Cabin을 지운 return 값을 가지고 후처리 해야 함.
        print('----------------------1-1. drop Cabin, Ticket 삭제 --------------------------')
        t = self.drop_feature(t[0], t[1], 'Ticket')  # 지워진 Cabin값을 기준으로 티켓값을 지움

        print('----------------------2. embarked 편집 -------------------------------')
        t = self.embarked_nominal(t[0], t[1]) # 티켓이 지워진

        print('----------------------3. title 편집 -------------------------------')
        t = self.title_nominal(t[0], t[1])

        print('----------------------4. name, PassengerId 삭제 -------------------------------')
        t = self.drop_feature(t[0], t[1], 'Name')

        # 키값을 되는 PassengerId를 아래에서 삭제해야 되므로 이를 대체할 pk 를 처리해 주어야 한다.(test_id)
        self._test_id = test['PassengerId']
        #

        t = self.drop_feature(t[0], t[1], 'PassengerId')

        print('----------------------5. age 편집 -------------------------------')
        t = self.age_ordinal(t[0], t[1])

        print('----------------------6. age 삭제 -------------------------------')
        t = self.drop_feature(t[0], t[1], 'Age')

        print('----------------------7. fare 편집 -------------------------------')
        t = self.fare_ordinal(t[0], t[1])

        print('----------------------8. fare 삭제 -------------------------------')
        t = self.drop_feature(t[0], t[1], 'Fare')

        print('----------------------9. sex 편집 -------------------------------')
        t = self.sex_nominal(t[0], t[1])

        # t[1] = t[1].drop('FareBand', axis=1)
        a = self.null_sum([1])
        print('널의 수량{ }'.format(a))

        # 테스트 결과값을 전역 변수에 저장.
        self._test = t[1]

        # 불필요한 피쳐들을 제거한 데이터를 리턴 받는다.
        return t[0]

    @staticmethod   # self를 사용하지 않을 경우 이 함수를 써야 한다. .. .생략시 --> 다이나믹
    def drop_feature(train, test, feature) -> []:    # 컬럼명 . 피처를 drop 할때는 train과 test도 함께 날려야 하는 셋트이다.
        train = train.drop([feature], axis = 1)
        test = test.drop([feature], axis = 1)
        return [train, test]  # 리턴값은 1개로 해야 하기에 두 값을 묶는다. (리스트 구조)

    # nominal : 문자를 숫자화 시키는 것을 의미하는대 그 숫자에 의미가 없는 임의로 주는 경우
    # oorminal : 문자를 숫자화 시키는 것을 의미하는대 그 숫자에 의미가 있는(rank등) 경우.
    @staticmethod
    def embarked_nominal(train, test) -> []:   # 승선
        s_city = train[train['Embarked'] == 'S'].shape[0]  # 스칼라
        c_city = train[train['Embarked'] == 'C'].shape[0]
        q_city = train[train['Embarked'] == 'Q'].shape[0]

        # print("S = ",s_city) #644
        # print("C = ",c_city) #168
        # print("Q = ",q_city) #77

        train = train.fillna({"Embarked": "S"})
        city_mapping = {"S": 1, "C": 2, "Q": 3}
        train['Embarked'] = train['Embarked'].map(city_mapping)
        test['Embarked'] = test['Embarked'].map(city_mapping)

        return [train, test]

    @staticmethod
    def title_nominal(train, test) -> []:  # 람다식 : 반환형은 리스트
        combine = [train, test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        # print(pd.crosstab(train['Title'],train['Sex']))

        for dataset in combine:
            dataset['Title'] \
                = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] \
                = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] \
                = dataset['Title'].replace('Mlle', 'Miss')
            dataset['Title'] \
                = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] \
                = dataset['Title'].replace('Mme', 'Mrs')
        train[['Title', 'Survived']].groupby(['Title'], as_index=False).mean()
        """
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
            dataset['Title'] = dataset['Title'].fillna(0)

        return [train, test]

    @staticmethod
    def sex_nominal(train, test) -> []:  # 람다식 : 리스트 반환
        combine = [train, test]
        sex_mapping = {"male": 0, "female": 1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        return [train, test]

    @staticmethod
    def age_ordinal(train, test) -> []:
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)

        age_title_mapping = {0: "Unknown", 1: "Young Adult", 2: "Student", 3: "Adult", 4: "Baby", 5: "Adult",
                             6: "Adult"}
        for x in range(len(train['AgeGroup'])):
            if train["AgeGroup"][x] == "Unknown":
                train["AgeGroup"][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test["AgeGroup"][x] == "Unknown":
                test["AgeGroup"][x] = age_title_mapping[test['Title'][x]]

        age_mapping = {'Baby': 1, 'Child': 2, 'Teenager': 3,
                       'Student': 4, "Young Adult": 5, "Adult": 6, 'Senior': 7}
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)

        return [train, test]

    #요금(좌석등급)
    @staticmethod
    def fare_ordinal(train, test) -> []:
        train['FareBand'] = pd.qcut(train['Fare'], 4, labels={1, 2, 3, 4})
        test['FareBand'] = pd.qcut(test['Fare'], 4, labels={1, 2, 3, 4})

        return [train, test]

    # 모델을 테스트하기 위한 함수.
    @staticmethod
    def create_model_dummy(train) -> []:
        model = train.drop('Survived', axis = 1)  # 모델에서 알고자 하는 답이 있는 부분을 제거 한다.  --> 제거 안하면 과적합 발생  :  100% 정답 맞춤
        dummy = train['Survived']
        return [model, dummy]

    @staticmethod
    def null_sum(train) -> int:
        sum = train.isnull().sum()
        return sum


    #################
    # 함수 - 훈련
    ################
    @staticmethod
    def create_random_variables(train) -> str:
        train2, test2 = train_test_split(train, test_size=0.3, random_state=0)
        target_col = ['Pclass', 'Sex', 'Embarked']
        train_X = train2[target_col]
        train_Y = train2['Survived']
        test_X = test2[target_col]
        test_Y = test2['Survived']

        features_one = train_X.values
        target = train_Y.values

        tree_model = DecisionTreeClassifier()
        tree_model.fit(features_one, target)
        dt_prediction = tree_model.predict(test_X)

        # 정확도 측정
        accuracy = metrics.accuracy_score(dt_prediction, test_Y)

        print('The accuracy of the Decision Tree is  ', accuracy)

        return accuracy

    # k_fold를 사용하여 데이터를 섞음..  --> 이 데이터 기반 나중에 검증 해야 함.
    @staticmethod
    def create_k_fold():
        k_fold = KFold(n_splits=10, shuffle=True, random_state=0)
        return k_fold

    # KNN 방식 검증
    def accuracy_by_knn(self, model, dummy) -> str:
        clf = KNeighborsClassifier(n_neighbors=13)
        scoring = 'accuracy'
        k_fold = self.create_k_fold()
        score = cross_val_score(clf, model, dummy, cv=k_fold, n_jobs=1, scoring=scoring)

        accuracy = round(np.mean(score)*100, 2)
        print(accuracy)

        return accuracy

    # 결정트리 방식 검증
    def accuracy_by_dt(self, model, dummy) -> str:
        clf = DecisionTreeClassifier()
        scoring = 'accuracy'
        k_fold = self.create_k_fold()
        score = cross_val_score(clf, model, dummy, cv=k_fold, n_jobs=1, scoring=scoring)

        accuracy = round(np.mean(score) * 100, 2)
        print(accuracy)  # 82.15

        return accuracy

    # 램덤포레스트 방식 검증
    def accuracy_by_rf(self, model, dummy) -> str:
        clf = RandomForestClassifier(n_estimators=13)  # 13개의 결정트리를 사용함
        scoring = 'accuracy'
        k_fold = self.create_k_fold()
        score = cross_val_score(clf, model, dummy, cv=k_fold, n_jobs=1, scoring=scoring)

        accuracy = round(np.mean(score) * 100, 2)
        print(accuracy)  # 82.15

        return accuracy

    # 나이브베이즈 방식 검증
    def accuracy_by_nb(self, model, dummy) -> str:
        clf = GaussianNB()
        scoring = 'accuracy'
        k_fold = self.create_k_fold()
        score = cross_val_score(clf, model, dummy, cv=k_fold, n_jobs=1, scoring=scoring)

        accuracy = round(np.mean(score) * 100, 2)
        print(accuracy)  # 82.15

        return accuracy

    # SVM 방식 검증
    def accuracy_by_svm(self, model, dummy) -> str:
        clf = SVC()
        scoring = 'accuracy'
        k_fold = self.create_k_fold()
        score = cross_val_score(clf, model, dummy, cv=k_fold, n_jobs=1, scoring=scoring)

        accuracy = round(np.mean(score) * 100, 2)
        print(accuracy)  # 82.15

        return accuracy




































