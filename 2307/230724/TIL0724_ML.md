### 붓꽃 품종 예측하기
데이터 로드
(데이터프레임으로 변환)
데이터 세트 분리
DecisionTreeClassifier 객체생성
학습 - .fit(x_train, y_train)
예측 - .predict(x_test)
성능 평가(정확도) - accuracy_score(y_test, pred)

## Estimator 이해 및 fit(), predict() 메서드
분류 알고리즘 - ~Classifier클래스
회귀 알고리즘 - ~Regressor클래스
합쳐서 - Estimator클래스

fit() - 지도학습에서 학습 / 비지도 학습에서는 입력 데이터의 형태에 맞춰 데이터를 변환하기 위해 사전 구조를 맞추는 작업
transform() - fit()으로 사전 구조를 맞추면 이후 입력 데이터에 대한 실제 작업을 수행

## 교차검증
KFold(n_splits)
KFold.split() - 학습용/검증용으로 데이터를 분할할 수 있는 인덱스를 반환
- 리턴 - train_index, test_index
- for문으로 사용

Stratiified K 폴드
불균형한 분포도를 가진 레이블 데이터 집합을 위한 방식
불균형한 데이터를 K 폴드방식으로 교차검증할 시 레이블의 비율을 제대로 반영하지 못하는 경우가 쉽게 발생함
stratiifiedKFOld(n_splits)
skfodl.split(data, label)
***일반적으로 분류에서의 교차 검증은 stratified K폴드를 사용해야함***
회귀에서는 지원되지 않음

cross_val_score(estimator, x, y, scoring, cv)
편리한 교차검증 - 위의 교차검증은 수동으로 교차검증을 진행. cross_val_score()는 한번에 자동으로 수행(세트 분리, 반복적인 학습/예측/평가)
estimator = ~classifier 인 경우 자동으로 stratified K폴드 방식으로 데이터 세트 분리 / ~Regressor 인 경우 K 폴드방식(회귀방식은 Stratified K폴드 방식을 지원하지 않기 때문)
리턴 - scoring 파라미터로 지정된 성능 지표 측정값을 배열 형태로 반환

GridSearchCV(estimator, param_grid, scoring, cv, refit)
- 교차 검증과 최적 하이퍼 파라미터 튜닝을 한 번에 수행
- 파라미터 집합을 만들어 내부에서 순차적으로 입력하면서 최적의 파라미터 조합을 도출함
    - 파라미터 집합은 딕셔너리 형태로 파라미터 명칭은 문자열 키값, 파라미터 값은 리스트형으로 설정
    - 교차 검증을 기반으로 함
- 수행시간이 오래 걸림

1. 학습데이터를 GridSearchCV 객체에 인자로 입력
2. GridSearchCV객체의 fit 메서드를 수행하면 학습 데이터를 cv에 기술된 폴딩 세트로 분할해 param_grid에 기술된 하이퍼 파라미터를 순차적으로 변경하면서 학습/평가를 수행하고 그 결과를 cv_results_ 속성에 기록한다
- cv_results_를 데이터프레임으로 변환하면 더 쉽게 볼 수 있음(원래 딕셔너리 형태임)

- best_params_ / best_score_ 속성
    - 최고성능의 파라미터 값 / 그 때의 평가 결과값
- best_estimator_
    - refit = True이면 GridSearchCV가 최적 성능을 나타내는 하이퍼 파라미터로 Estimator를 학습해 best_estimator_로 저장
    
- ***일반적으로 학습 데이터를 GridSearchCV를 이용해 최적 하이퍼 파라미터 튜닝을 수행한 뒤에 별도의 테스트 세트에서 이를 평가하는 것이 일반적인 머신러닝 모델 적용 방법임***














































