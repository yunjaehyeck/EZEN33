"""
결정 트리decision tree는 분류와 회귀 문제에 널리 사용하는 모델입니다.
기본적으로 결정 트리는 결정에 다다르기 위해 예/아니오 질문을 이어 나가면서 학습합니다.
이 질문은 스무고개 놀이의 질문과 비슷합니다.
곰, 매, 펭귄, 돌고래라는 네 가지 동물을 구분한다고 생각해봅시다.
우리의 목표는 가능한 한 적은 예/아니오 질문으로 문제를 해결하는 것입니다.
날개가 있는 동물인지를 물어보면 가능성 있는 동물을 둘로 좁힐 수 있습니다.
대답이 “yes”이면 다음엔 독수리와 펭귄을 구분할 수 있는 질문을 해야 합니다.
예를 들면 날 수 있는 동물인지 물어봐야 합니다.
만약 날개가 없다면 가능한 동물은 곰과 돌고래가 될 것입니다.
이제 이 두 동물을 구분하기 위한 질문을 해야 합니다.
예를 들면 지느러미가 있는지를 물어봐야 합니다.
연속된 질문들을 [그림 2-22]처럼 결정 트리로 나타낼 수 있습니다.
이 그림에서 트리의 노드는 질문이나 정답을 담은 네모 상자입니다
(특히 마지막 노드는 리프leaf라고도 합니다). 엣지edge는 질문의 답과 다음 질문을 연결합니다.
머신러닝 식으로 말하면 세 개의 특성 “날개가 있나요?”, “날 수 있나요?”,
 지느러미가 있나요?”를 사용해 네 개의 클래스(매, 펭귄, 돌고래, 곰)를 구분하는 모델을 만든 것입니다.
  이런 모델을 직접 만드는 대신 지도 학습 방식으로 데이터로부터 학습할 수 있습니다.
결정 트리의 복잡도 제어하기
일반적으로 트리 만들기를 모든 리프 노드가 순수 노드가 될 때까지 진행하면
모델이 매우 복잡해지고 훈련 데이터에 과대적합됩니다.
순수 노드로 이루어진 트리는 훈련 세트에 100% 정확하게 맞는다는 의미입니다.
즉 훈련 세트의 모든 데이터 포인트는 정확한 클래스의 리프 노드에 있습니다.
[그림 2-26]의 왼쪽 그래프가 과대적합된 것으로 볼 수 있습니다.
클래스 0으로 결정된 영역이 클래스 1에 속한 포인트들로 둘러쌓인 것을 볼 수 있습니다.
 그 반대 모습도 보입니다. 이는 바람직한 결정 경계의 모습이 아닙니다.
 결정 경계가 클래스의 포인트들에서 멀리 떨어진 이상치outlier 하나에 너무 민감하기 때문입니다.
 과대적합을 막는 전략은 크게 두 가지입니다.
 트리 생성을 일찍 중단하는 전략(사전 가지치기pre-pruning)과
 트리를 만든 후 데이터 포인트가 적은 노드를 삭제하거나 병합하는 전략입니다
 (사후 가지치기post-pruning 또는 그냥 가지치기pruning). 사전 가지치기 방법은 트리의 최대 깊이나
 리프의 최대 개수를 제한하거나, 또는 노드가 분할하기 위한 포인트의 최소 개수를 지정하는 것입니다.
 scikit-learn에서 결정 트리는 DecisionTreeRegressor와 DecisionTreeClassifier에 구현되어 있습니다.
 scikit-learn은 사전 가지치기만 지원합니다.
유방암 데이터셋을 이용하여 사전 가지치기의 효과를 자세히 확인해보겠습니다.
항상 그랬듯이 먼저 데이터셋을 읽은 후 훈련 세트와 테스트 세트로 나눕니다.
그런 후에 기본값 설정으로 완전한 트리(모든 리프 노드가 순수 노드가 될 때까지 생성한 트리) 모델을 만듭니다.
random_state 옵션을 고정해 만들어진 트리를 같은 조건으로 비교합니다.
"""

import sklearn
from sklearn.tree import DecisionTreeClassifier
import sklearn.datasets
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()

# scikit-learn의 교차검증 기능
#독립 변수의 개수가 많은 빅데이터에서는 과최적화가 쉽게 발생한다.
#따라서 scikit-learn 의 model_selection 서브 패키지는 교차검증을 위한 다양한 명령을 제공한다.
#train_test_split 명령은 데이터를 학습용 데이터와 검증용 데이터로 분리한다. 사용법은 다음과 같다.

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, \
                    stratify = cancer.target, random_state=42) # 대문자 X는 확률변수

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)

print("훈련 세트의 정확도: {:.3f}".format(tree.score(X_train, y_train)))
print("테스트 세트의 정확도: {:.3f}".format(tree.score(X_test, y_test)))
