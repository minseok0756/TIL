import numpy as np

'''
   유틸리티 함수 - axis 이용하여 행별 또는 열별로 연산

   1. np.max: 1, 2차원 최대
   2. np.min: 1, 2차원 최소
      
   3. np.argmax : 1, 2차원 최대값에 해당하는 인덱스 반환
   4. np.argmin : 1, 2차원 최소값에 해당하는 인덱스 반환

   5. np.sort :  1, 2차원 정렬

      - 2차원 배열인 경우
        axis=None 이면 flatten 되어 정렬
        axis=0 이면  행방향이기 때문에 컬럼단위로 정렬
        axis=1 이면  열방향이기 때문에 행단위로 정렬

   6. np.all, np.any ==> 논리값을 가진 다차원 배열을 하나의 논리값으로 처리할 때 사용

   7. 전치  (Transpose)

   8. 행렬곱( dot product(점곱), 곱해서 합 ) ==>  np.dot(a,b),  a @ b
'''

# 6. 최대/최소값
data = np.array([8, 2, 4, 5, 10, 1])
print("1. 1차원 배열 np.max(arr): ", np.max(data)) # 10
print("2. 1차원 배열 np.min(arr): ", np.min(data)) # 1

data = np.array(np.arange(16).reshape(4, 4))
print(data)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
'''
print("3. 2차원 배열, 각 열에서 최대값:", np.max(data, axis=0))  # 위 + 아래 [12 13 14 15]
print("4. 2차원 배열, 각 열에서 최소값:", np.min(data, axis=0))  # [0 1 2 3]
print("5. 2차원 배열, 각 행에서 최대값:", np.max(data, axis=1))  # 왼쪽 + 오른쪽 [ 3  7 11 15]
print("6. 2차원 배열, 각 행에서 최소값:", np.min(data, axis=1))  # [ 0  4  8 12]

# 7.  최대/최소값에 해당하는 인덱스 반환
data = np.array([8, 2, 4, 5, 10, 1])
print("1. 1차원 배열 최대 index값: ", np.max(data), np.argmax(data))  # 10 4
print("2. 1차원 배열 최소 index값: ", np.min(data), np.argmin(data))  # 1  5

data = np.array([[6, 2, 4], [10, 1, 54], [66, 3, 21]])
'''
[[ 6  2  4]
 [10  1 54]
 [66  3 21]]
'''
print("3. 2차원 배열, 각 열에서 최대 index값:", np.argmax(data, axis=0))  # [2 2 1]
print("4. 2차원 배열, 각 열에서 최소 index값:", np.argmin(data, axis=0))  # [0 1 0]
print("5. 2차원 배열, 각 행에서 최대 index값:", np.argmax(data, axis=1))  # [0 2 0]
print("6. 2차원 배열, 각 행에서 최소 index값:", np.argmin(data, axis=1))  # [1 1 1]

# python 정렬
'''
      1. sorted()
      - __builtins__객체의 함수
      - 정렬된 복사본 반환
      
      2. 객체.sort(reverse=True)
      - 객체의 함수
      - 자신이 정렬
'''
# 8.  1차원 정렬
data = np.array([8, 2, 4, 5, 10, 1])
print("1. 1차원 배열 sort 전: ", data)  # [ 8  2  4  5 10  1]
print("2. 1차원 배열 sort 후(오름차순): ", np.sort(data))  # [ 1  2  4  5  8 10]
print("3. 1차원 배열 sort 후(내림차순): ", np.sort(data)[::-1])  # [10  8  5  4  2  1]
print()

# 9. 2차원 정렬
data = np.array([[8, 2, 4, 5, 10, 1], [100, 67, 33, 77, 66, 90]])

data3 = np.sort(data, axis=None)  # flattened
print("6. axis=None(flattened):", data3)  # [  1   2   4   5   8  10  33  66  67  77  90 100]
print()
arr = np.array([[8, 2, 4], [100, 67, 33], [99, 44, 77]])
# [[  8   2   4]
#  [100  67  33]
#  [ 99  44  77]]
data4 = np.sort(arr, axis=0)  # 컬럼단위로 정렬
print(data4)
# [[  8   2   4]
#  [ 99  44  33]
#  [100  67  77]]
data4 = np.sort(arr, axis=1)  # 행단위로 정렬
print(data4)
# [[  2   4   8]
#  [ 33  67 100]
#  [ 44  77  99]]

# 5. np.all, np.any ==> 논리값을 가진 다차원 배열을 하나의 논리값으로 처리할 때 사용
print("1. 모든 값이 True 냐?: ", np.all([True, True]))  # True
x = np.array([1, 0, 0, 0])
print("2. np.all(arr): ", np.all(x))  # False
print("3. np.any(arr): ", np.any(x))  # True

# 6. np.all, np.any 활용
a = np.array([1, 2, 3, 4])
b = np.array([4, 3, 2, 1])
print(a>b) # [False False  True  True]
print("all a>b ?:", np.all(a > b))  # False

# 7. 전치  (Transpose)
arr = np.arange(15).reshape(3, 5)
print("1. original: ", arr)
print()
print("2. T:", arr.T)  # Transpose
print("3. transpose()", arr.transpose())  # Transpose

# 8. 행렬곱( dot product(점곱), 곱해서 합 ) ==>  np.dot(a,b),  a @ b
'''
  벡터 내적: 1차원인 벡터간의 곱연산후 합 의미
  행렬곱(점곱, dot product): 행렬간의 곱연산후 합 의미
'''
arr = np.arange(4).reshape(2,2)
print("1. original: ",arr)
print("2. np.dot(arr, arr2) - 행렬곱:  ",  np.dot(arr,arr))
print("4. arr @ arr2) - 행렬곱:  ",  arr @ arr )
arr = np.arange(4)
print("5. 벡터 내적: ", np.dot(arr, arr)) # 0*0 + 1*1 + 2*2 + 3*3 = 14