import numpy as np

'''
    2. 랜덤함수 이용
    가. np.random.seed(1234) # 랜덤값 고정
    나. np.random.random(size=(m,n)) : [0.0, 1.0]에서 (m,n)shape으로 임의의 값을 m*n 만큼 반환, float64
    다. np.random.rand(m,n) :  [0, 1)의 균등분포에서 (m,n)shape으로 m*n만큼 표본 추출, float64
    라. np.random.randn(m,n) :  표준정규분포에서 (m,n)shape으로 m*n만큼 표본 추출, float64
    마. np.random.randint(최소범위, 최대범위, size=(m,n)) : [최소, 최대) 범위안에서 (m,n) shape으로 임의의 m*n개 반환, int32
        np.random.randint(최대범위, size=n) :   [0, 최대) 범위안에서 (m,n) shape으로 임의의 m*n개 반환, int32

'''

# 1) 랜덤값 고정
np.random.seed(1234)

# 2) np.random.random(size=(행,열))
print("1. random(size=(행,열))")
arr = np.random.random(size=(2,3))
print(arr, type(arr), arr.dtype) # [[0.19151945 0.62210877 0.43772774] [0.78535858 0.77997581 0.27259261]] <class 'numpy.ndarray'> float64

# 3) np.random.rand(행, 열)
print("2. rand(행, 열)")
arr = np.random.rand(2,3)
# arr = np.random.rand((2,3)) # 에러 발생
                            # 마우스 오버해보면 패킹파라미터로 되어있다
                            # 따라서 random처럼 튜플로 지정하면 오류가 발생한다
print(arr, type(arr), arr.dtype) # [[0.27646426 0.80187218 0.95813935] [0.87593263 0.35781727 0.50099513]] <class 'numpy.ndarray'> float64

# 4) np.random.randn(행, 열)
print("3. randn(행, 열)")
arr = np.random.randn(2,3)
print(arr, type(arr), arr.dtype) # [[ 1.15003572  0.99194602  0.95332413] [-2.02125482 -0.33407737  0.00211836]] <class 'numpy.ndarray'> float64

# 5) np.random.randint(low, high, size=(행, 열))
print("4. randint(1,10,size=(행, 열))")
arr = np.random.randint(1,10, size=(2,3))
print(arr) # [[3 7 4] [8 1 1]]

# 5) np.random.randint(high, size=(행, 열))
print("4. randint(5, size=(행, 열)): ")
arr = np.random.randint(5, size=(2,3))
print(arr) # [[3 2 3] [4 1 3]]
