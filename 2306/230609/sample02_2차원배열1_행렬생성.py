import numpy as np

'''
    2차원배열 - 행렬 생성

    1) np.array(중첩리스트) 이용
      arr2D = np.array([[],[]])
     
    2) 1차원 --> 2차원으로 변경(중요)
      arr1D.shape = (행, 열)  ==> 행 * 열 = ndarray크기(size)와 일치
      arr1D.shape = (행, -1)  ==> 행크기에 의해서 열크기가 자동 지정됨
      arr1D.shape = (-1, 열)  ==> 열크기에 의해서 행크기가 자동 지정됨
'''
# 1) np.array(중첩리스트) 이용
arr1 = [[1,2,3],[4,5,6]]
arr2D = np.array(arr1)
print("1. 2차원 행렬 생성: \n", arr2D, type(arr2D))  # <class 'numpy.ndarray'>

# 2) 1차원을 2차원으로 변경, shape 속성 사용
arr1D = np.array([1,2,3,4,5,6])
print(arr1D)  # [1 2 3 4 5 6]
arr1D.shape=(2, 3)
# arr1D.shape=(2, -1) # 행크기에 의해서 열크기가 자동 지정됨
# arr1D.shape=(-1, 3)   # 열크기에 의해서 행크기가 자동 지정됨
print("2. 1차원을 2차원으로 변경: \n", arr1D) # [[1 2 3][4 5 6]]
print()

# 다차원 shape 이해하기
arr1D = np.array([1,2,3,4,5,6])
arr1D.shape = (2,3,1)
# arr1D.shape = (3,1,2)
print(arr1D)
