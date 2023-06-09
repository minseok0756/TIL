import numpy as np

'''
    2. 랜덤함수 이용
    가. np.random.seed(1234) # 랜덤값 고정
    나. np.random.random([size]) : [0.0, 1.0] 임의의 값을 n만큼 반환, float64, [size]=1
    다. np.random.rand([n]) :  [0, 1)의 균등분포에서 n만큼 표본 추출, float64, [n]=1
    라. np.random.randn([n]) :  표준정규분포에서 n만큼 표본 추출, float64, [n]=1
    마. np.random.randint(최소범위, 최대범위, [size]) : [최소, 최대) 범위안에서 임의의 size개 반환, int32, [size]=1
        np.random.randint(최대범위, size=n) :   [0, 최대) 범위안에서 임의의 size개 반환, int32
    바. np.random.choice(리스트)  : 주어진 리스트에서 임의의 값 1개 반환
    사. np.random.shuffle(리스트)  : 주어진 리스트를 shuffle 함.  in-place(True)로 동작됨.
    
'''
# 1) 랜덤값 고정
np.random.seed(1234)

# 2) np.random.random([size])
# [0.0, 1.0] 임의의 값을 n만큼 반환, float64, [n]=1
print("1. random(5)")
arr = np.random.random() # 0.1915194503788923
arr = np.random.random(5) # [0.62210877 0.43772774 0.78535858 0.77997581 0.27259261] <class 'numpy.ndarray'> float64
print(arr, type(arr), arr.dtype)

# 3) np.random.rand([n])
# [0, 1)의 균등분포에서 n만큼 표본 추출, float64, [n]=1
print("2. rand(5)")
arr = np.random.rand() # 0.2764642551430967
arr = np.random.rand(5) # [0.80187218 0.95813935 0.87593263 0.35781727 0.50099513] <class 'numpy.ndarray'> float64
print(arr, type(arr), arr.dtype)

# 4) np.random.randn([n])
# 표준정규분포에서 n만큼 표본 추출, float64, [n]=1
print("3. randn(5)")
arr = np.random.randn() # 1.150035724719818
arr = np.random.randn(5) # [ 0.99194602  0.95332413 -2.02125482 -0.33407737  0.00211836] <class 'numpy.ndarray'> float64
print(arr, type(arr), arr.dtype)

# 5) np.random.randint(low, high, size)
# [최소, 최대) 범위안에서 임의의 n개 반환, int32, [n]=1
print("4. randint(1,10,3)")
arr = np.random.randint(1,10,3) # 1~9
print(arr)

# 5) np.random.randint(high, size=n)
# [0, 최대) 범위안에서 임의의 n개 반환, int32, 복원추출
print("4. randint(5, size=4): ")
arr = np.random.randint(5, size=4) # 0~4
print(arr)

# 6) np.random.choice(리스트)
# 주어진 리스트에서 임의의 값 1개 반환
print("5. np.random.choice(['foo','bar','baz']")
choice_value = np.random.choice(['foo','bar','baz'])
print(choice_value) # foo

# 7) np.random.shuffle(리스트)
# 주어진 리스트를 shuffle 함.  in-place(True)로 동작됨. -> 자기 자신이 바뀜
#                           in-place(False)         -> 복사본이 만들어짐
print("6. np.random.shuffle(1,3,56,7,98])")
shuffle_value = [1,3,56,7,98]
np.random.shuffle(shuffle_value) # [98, 3, 1, 56, 7]
print(shuffle_value)