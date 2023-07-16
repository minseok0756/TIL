# ML/DL - 기초통계

통계: 집단에 대한 특징 확인
- 대표적 특징 
    - 모여있는 정도(중심화 경향치) - 평균
        - 집단의 공통점에 focus
    - 떨어져있는 정도(산포도) - 분산
        - 집단의 차이점에 focus

<br>

변수의 종류
- 질적변수
- 양적변수
- 척도수준
    - 명목척도
    - 순서척도
    - 등간척도
    - 비율척도
- 이산형변수
- 연속형변수

<br>

데이터 중심의 지표
- 평균값 - np.mean() / df.mean() / s.mean()
- 중앙값 - np.median() / df.median() / s.median()
- 절사평균 
    - 양쪽을 자르고 나머지로 평균
    - 이상값에 영향을 덜 받음
    - 정보의 손실이 적음
- 최빈값 - df.mode() / s.mode()

<br>

데이터의 산포도 지표
- 분산 - np.var() / df.var() / s.var()
- 표준편차 - np.std() / df.std() / s.std()
- 범위
- 사분위 범위 
    - np.percentile(..., 75) - np.percentile(..., 25)
    - np.quantile(..., 0.75) - np.quantile(..., 0.25)
    - df.quantile(0.75)-df.quantile(0.25)
    - s.quantile(0.75)-s.quantile(0.25)

<br>

데이터의 정규화
- 표준화
- 편차값

<br>

데이터의 시각화
- 도수분포표 
- 히스토그램

---

[실습](http://localhost:8888/tree/%EA%B8%B0%EC%B4%88%ED%86%B5%EA%B3%84_0713)