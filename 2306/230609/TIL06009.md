## 과정 프리뷰

### 1. SQL

### 2. Python

### 3. numpy
- 외부 라이브러리
- 다차원배열과 관련된 문법
    - 생성, 색인, 연산
- python 리스트와 유사

### 4. pandas
- 외부 라이브러리
- DataFrame 관리
    - 그룹핑, 병합 등

### 5. 시각화(그래프)
- **Matplotlib**, seaborn 

### 6. 간단한 데이터 분석
- 코로나 데이터 이용

### 7. 기초 통계
- 머신러닝, 딥러닝에 기반이 되는 내용

### 8. 웹
- 정적특징
    - html(구조), css(색상, 배치, 정렬, 스타일)
- 동적특징
    - **JavaScript()**

### 9. 웹 크롤링
- 이미 민들어진 html에서 필요한 데이터 가져온다
- beatifulsoup 라이브러리

### 10. Django
- 파이썬 기반의 웹 페이지(동적기능 포함) 만들기

---

## [Numpy](https://numpy.org/devdocs/reference/index.html)

### 용어정리
- 다차원배열
    - 1차원 : 벡터
    - 2차원 : 행렬
    - 3차원이상 : 텐서

### [실습](./)

---

## 리뷰
###  1. Numpy  
- 다차원 배열 관리

### 2. 다차원배열
- 1차원 : [벡터]
- 2차원 : [[행렬]]
- 3차원이상 : [[[텐서]]]

### 3-1. 1차원 배열 생성
- ***np.array(리스트)***  
    - ndarray 속성 : ndarray.ndim/shape/dtype/size  
- 랜덤함수  
    - np.random()/rand()/randn()/randint()/choice()/shuffle()
- 특정값  
    - np.zeros/ones/empty/full  
- 범위  
    - ***np.arange***  
- 동일한 간격  
    - ***np.linspace***

### 3-2. 1차원 삭제
- np.delete(arr, 색인)
    - 색인 : 인덱싱, 슬라이싱, ***fancy***
- np.where()

### 3-3. 1차원 삽입, 추가
- np.append()
- np.insert(arr, 색인)  
    - 색인 : 인덱싱, 슬라이싱, fancy 

### 4-1. 2차원 배열 생성
- np.array(중첩리스트)
    - ndarray 속성 : ndarray.ndim/shape/dtype/size  
- ndarray.shape=(m,n)
- 랜덤함수
    - np.random()/rand()/randn()/randint()
- 범위 + reshape
    - np.arange().reshape

### 4-2. 2차원 배열 삭제
- np.delete(arr, 색인, ***axis***)
    - 색인 : 인덱싱, 슬라이싱, fancy

### 4-3. 2차원 배열 삽입, 추가
- np.append(arr, values, ***axis***)
- np. insert(arr, 색인, value, ***axis***)

### 5. 타입변경
- np.array(dtype=np.dtype)
- ndarray.astype(np.dtype)

### 6. 벡터연산
- 다차원배열 사칙연산 다차원배열
- 다차원배열 사칙연산 스칼라
    - 브로드캐스팅
- 비교연산자

### 7. 색인
- 1차원 배열
    - 인덱싱, 슬라이싱, fancy색인, boolean색인