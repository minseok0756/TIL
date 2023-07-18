# ML

머신러닝 지도 학습 프로세스
- 데이터 전처리
    - 데이터 클린징
    - 결손값 처리(Null/NaN 처리)
        - 평균값 대체
        - 드롭
        - ('N'과 같은) 고정값으로 변경
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

이미지 전처리
1. 사이즈 조정 - 사이즈 통일
2. 인코딩
3. RGB or 회색 선택

<br>

데이터 인코딩
- 머신러닝 알고리즘의 모든 데이터는 숫자형으로 표현되어야 함
- 문자형 카테코리형 속성은 모두 숫자값으로 변환/인코딩되어야 함

- 레이블(Label) 인코딩
    - 카테고리 피처를 코드형 숫자값으로 변환
    - from sklearn.preprocessing import LabelEncoder
    - encoder = LabelEncoder()
    - encoder.fit(items) - Fit label encoder
    - encoder.transform(items) - Transform labels to normalized encoding
    - encoder.inverse_transform([3,5,2,3,1,0]) - Transform labels back to original encoding
    - 속성
        - .classes_ - 0번부터 순서대로 인코딩 값에 대한 원본값
    - 단점 - 인코딩된 레이블에 숫자의 크고 작음 특성이 작용함
        - 냉장고는 1, 믹서기는 2로 변환된 경우 2가 1보다 크므로 믹서기에 더 가중치가 부여되거나 더 중요하게 인식할 가능성이 있다
    - 따라서 레이블 인코딩은 선형회귀와 같은 ML 알고리즘에는 적용되면 안된다.
        - 트리 계열 알고리즘은 문제 없음
    - 해결 - 원-핫 인코딩

- 원-핫(One-Hot) 인코딩
    - 피처 값의 유형에 따라 새로운 피처를 추가해 고유 값에 해당하는 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방식
    - 입력값으로 2차원 데이터 필요
        - labels = labels.reshape(-1,1)
    - 원-핫 인코딩
        - oh_encoder = OneHotEncoder()
        - oh_encoder.fit(labels)
        - oh_labels = oh_encoder.transform(labels)
    - pandas one-hot encoding
        - pd.get_dummies()

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
    - scaler = MinMaxScaler()
    - Scaler클래스의 fit(), transform() 인자에 2차원 이상 데이터만 가능
        - scaler.fit(iris_df)
        - scaler.transform(iris_df)

- 표준화(Standardization)
    - 표준화는 데이터 피처 각각의 평균이 0이고 분산이 1인 가우시안 정규 분포를 가진 값으로 변환
    - 변수의 평균을 0, 표준편차를 1로 만들어 표준정규분포의 특징을 갖도록 함
    - 표준화는 가중치(weight) 학습을 더 쉽게 할 수 있도록 함
    - 𝑿_𝑺𝒕𝒂𝒏𝒅𝒂𝒓𝒅𝒊𝒛𝒂𝒕𝒊𝒐𝒏 = (𝑿 − 𝒎𝒆𝒂𝒏(𝑿))/𝒔𝒕𝒅 (𝑿)
    - from sklearn.preprocessing import StandardScaler
    - scaler = StandardScaler()
    - Scaler클래스의 fit(), transform() 인자에 2차원 이상 데이터만 가능
        - scaler.fit(iris_df)
        - iris_scaled = scaler.transform(iris_df)  

- fit(), transform() / fit_transform() 주의사항
    - fit()은 데이터 변환을 위한 기준 정보(최댓값, 최솟값 등)를 설정하며
    - transform()은 설정된 정보를 이용해 데이터를 변환한다
    - 예를 들어 MinMaxScaler.fit(iris_df)를 실행하면 iris_df데이터의 max,min값이 설정된다.
    - MinMaxScaler.transform(iris_df2)를 실행하면 iris_df2데이터의 max,min값이 아닌 설정되어있던 irir_df데이터의 max,min으로 iris_df2데이터를 정규화한다.
    - 저장되어있는 정보를 변경하려면 변경하고자 하는 데이터로 fit()하면 된다.
    - MinMaxScaler.fit(iris_df2)
    - fit_transform() 함수는 두번 실행할 것을 한번에 실행할 수 있다는 장점이있지만
    - 매번 fit()함수를 사용하여 저장되어있는 정보를 매번 수정하게 된다
    - 따라서 올바른 결과를 가져올 수 없다.

        <br>

    - fit_transform()함수보다는 fit(), transform() 함수 사용 권장
    - 선 스케일링, 후 데이터 분리 권장
        - 선 데이터 분리의 경우
        - fit() 함수를 여러번 쓰지 않는것에 주의해야 한다
        - 데이터가 나누어지면 스케일링 시 필요한 최대값, 최소값, 평균, 표준편차 등을 제대로 측정할 수 없다

---

[실습](http://localhost:8888/tree/ML_0718)