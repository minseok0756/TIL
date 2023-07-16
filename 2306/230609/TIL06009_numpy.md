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

<br>

### 2. 다차원배열
- 1차원 : [벡터]
- 2차원 : [[행렬]]
- 3차원이상 : [[[텐서]]]

<br>

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

<br>

### 3-2. 1차원 삭제
- np.delete(arr, 색인)
    - 색인 : 인덱싱, 슬라이싱, ***fancy***
- np.where()

<br>

### 3-3. 1차원 삽입, 추가
- np.append()
- np.insert(arr, 색인)  
    - 색인 : 인덱싱, 슬라이싱, fancy 

<br>

### 4-1. 2차원 배열 생성
- np.array(중첩리스트)
    - ndarray 속성 : ndarray.ndim/shape/dtype/size  
- ndarray.shape=(m,n)
- 랜덤함수
    - np.random()/rand()/randn()/randint()
- 범위 + reshape
    - np.arange().reshape

<br>

### 4-2. 2차원 배열 삭제
- np.delete(arr, 색인, ***axis***)
    - 색인 : 인덱싱, 슬라이싱, fancy

<br>

### 4-3. 2차원 배열 삽입, 추가
- np.append(arr, values, ***axis***)
- np. insert(arr, 색인, value, ***axis***)

<br>

### 5. 타입변경
- np.array(dtype=np.dtype)
- ndarray.astype(np.dtype)

<br>

### 6. 벡터연산
- 다차원배열 사칙연산 다차원배열
- 다차원배열 사칙연산 스칼라
    - 브로드캐스팅
- 비교연산자

<br>

### 7. 색인
- 1차원 배열
    - 인덱싱, 슬라이싱, fancy색인, boolean색인