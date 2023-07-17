# ML

[사이킷런](https://scikit-learn.org/stable/)

머신러닝 기초 용어
- 피처(Feature), 속성 - 데이터 세트의 일반 속성
- 레이블, 클래스, 타겟(값), 결정(값) - 데이터 학습을 위해 주어지는 정답 데이터

<br>

머신러닝 지도 학습 프로세스
- 데이터 전처리
    - 데이터 클린징
    - 결손값 처리(Null/NaN 처리)
    - 데이터 인코딩(레이블 인코딩, 원-핫 인코딩)
    - 데이터 스케일링
    - 이상치 제거
    - Feature 선택, 추출 및 가공
- 데이터세트 분리 - train_test_split()(내부적으로 k-fold 교차검증 실행, 파라미터 최적화까지)
    - 학습 데이터
    - 테스트 데이터
- 모델 학습 - fit()
    - 학습 데이터를 기반으로 ML 알고리즘을 적용해 모델을 학습
- 예측 수행 - predict()
    - 학습된 ML 모델을 이용해 테스트 데이터 분류를 예측
- 평가
    - 예측된 결과값과 테스트 데이터의 실제 결과값을 비교해 ML 성능 평가

<br>

1. 데이터세트 분리
- X_train, X_test, y_train, y_test = train_test_split(data, label, test_size, random_state)
    - 내부적으로 교차검증 및 파라미터 최적화 실행
2. 모델 학습
- dt_clf = DecisionTreeClassifier()
- dt_clf.fit(X_train, y_train)
3. 예측 수행
- pred = dt_clf.predict(X_test)
4. 평가
- accuracy_score(y_text, pred)

<br>

데이터 인코딩
- 머신러닝 알고리즘의 모든 데이터는 숫자형으로 표현되어야 함
- 문자형 카테코리형 속성은 모두 숫자값으로 변환/인코딩되어야 함
- 레이블(Label) 인코딩
    - #####################################
- 원-핫(One-Hot) 인코딩
    - 피처 값의 유형에 따라 새로운 피처를 추가해 고유 값에 해당하는 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방식

<br>

피처 스케일링
- 범위(Scale)가 다른 변수들의 범위(Scale)를 비슷하게 맞추기 위한 목적
    - 연속형 변수가 다양한 범위(Scale)로 존재할 때 제곱 오차 계산 시 왜곡 발생
        - X1은 1에서 10 사이 스케일, X2는 1000에서 100만 사이 스케일
        - 스케일이 더 큰 변수에 맞추어서 가중치를 최적화하는 문제 발생

- 정규화(Normalization)
    - 정규화는 서로 다른 피처의 크기를 통일하기 위해 크기를 변환
    - 변수의 스케일을 0 ~ 1 사이 범위로 맞춤(min-max scaling)
    - 𝑿_𝑵𝒐𝒓𝒎𝒂𝒍𝒊𝒛𝒂𝒕𝒊𝒐𝒏 = (𝑿 − 𝒎𝒊𝒏(𝑿))/(𝒎𝒂𝒙 𝑿 − 𝒎𝒊𝒏(𝑿))
    - from sklearn.preprocessing import MinMaxScaler

- 표준화(Standardization)
    - 표준화는 데이터 피처 각각의 평균이 0이고 분산이 1인 가우시안 정규 분포를 가진 값으로 변환
    - 변수의 평균을 0, 표준편차를 1로 만들어 표준정규분포의 특징을 갖도록 함
    - 표준화는 가중치(weight) 학습을 더 쉽게 할 수 있도록 함
    - 𝑿_𝑺𝒕𝒂𝒏𝒅𝒂𝒓𝒅𝒊𝒛𝒂𝒕𝒊𝒐𝒏 = (𝑿 − 𝒎𝒆𝒂𝒏(𝑿))/𝒔𝒕𝒅 (𝑿)
    - from sklearn.preprocessing import StandardScaler

<br>

교차검증(Cross Validation)
- 학습 데이터
    - 학습 데이터
    - 검증 데이터

<br>

K폴드(K-Fold) 교차 검증
- 학습데이터를 k등분한 후 골고루 한 번씩 검증데이터로 사용하여 총 k번 교차검증한다.
- 최종평가는 k번 검증의 평균값
- KFold(n_splits) - 객체 생성
- for train_index, test_index in KFold.split(data)를 이용하여 수동으로 훈련데이터 검증데이터 분리

<br>

Stratified K 폴드
- 불균형한(imbalanced) 분포도를 가진 레이블 데이터 집합을 위한 방식
- 학습데이터와 검증 데이터 세트의 분포도가 레이블과 유사하도록 검증 데이터 추출
- StratifiedKFold(n_splits) - 객체 생성
- for train_index, test_index in KFold.split(data, label)를 이용하여 수동으로 훈련데이터 검증데이터 분리

<br>

cross_val_score(estimator, data, label, scoring, cv)
- 간편한 교차 검증
- 폴드 세트 추출, 학습/예측, 평가 한번에 수행
- Return - Array of scores of the estimator for each run of the cross validation

<br>

GridSearchCV(estimator, param_grid, scoring, refit, cv)
- 최적의 파라미터를 도출하기위해 사용
- .fit(train_data, train_label)
- .cv_results_
- .best_params_
- .predict(test_data)
- accuracy_score(test_label, pred)
- Returns - Result of the decision function for `X` based on the estimator with the best found parameters.

---

[실습](http://localhost:8888/tree/ML_0717)