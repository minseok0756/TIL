# ML/DL - 기초통계

두 데이터 사이의 관계를 나타내는 지표
- 공분산 
    - np.cov() - 리턴: 공분산 행렬
    - df.cov()
    - s.cov(other Series) - 값
- 상관계수
    - np.corrcoef() - 리턴: 상관 행렬
    - df.corr()
    - s.corr() - 값
<br>

2차원 데이터의 시각화
- 산점도
- 회귀직선
    - 회귀계수 구하기 - np.polyfit(data1, data2, 차수)
        - 회귀계수를 리스트로 리턴
    - 회귀직선 구하기 - np.poly1d()
        - 인자로 리스트를 사용
        - np.poly1d([1]) - 1
        - np.poly1d([1,2]) - x+2
        - nplpoly1d([1,2,3]) - x^2+2x+3
- 히트맵

<br>

엔스컴 - 동일한 지표를 갖는 서로 다른 데이터

---

[실습](http://localhost:8888/tree/%EA%B8%B0%EC%B4%88%ED%86%B5%EA%B3%84_0714)