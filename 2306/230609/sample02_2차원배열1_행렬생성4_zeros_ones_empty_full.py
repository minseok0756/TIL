import numpy as np

'''
    3. 특정값으로 설정

    가.  np.zeros(shape) : shape만큼  0.0 으로 채움. 기본 type은 float64
                        만약 정수형으로 저장하기 위해서는 dtype=np.int32 지정한다.
    나.  np.ones(shape) : shape만큼  1.0 으로 채움. 기본 type은 float64
                        만약 정수형으로 저장하기 위해서는 dtype=np.int32 지정한다.

    다.  np.empty(shape) : 초기화하지 않았기 때문에 임의의(arbitrary) 값으로 채움.

        Returns
        -------
        out : ndarray
            Array of uninitialized (arbitrary) data of the given shape, dtype, and
            order.  Object arrays will be initialized to None.

    라. np.full(shape, 값) : shape만큼 지정된 값으로 채움 
'''

# 1. np.zeros((행, 열))
# shape만큼 0으로 채움. 기본 type은 float64
print("1. np.zeros((행, 열)):")
# data = np.zeros((2,3)) # [[0. 0. 0.] [0. 0. 0.]] float64
data = np.zeros((2,3), dtype=np.int32) # [[0 0 0] [0 0 0]] int32
print(data, data.dtype)

# 2. np.ones((행, 열))
# shape만큼  1.0 으로 채움. 기본 type은 float64
print("2. np.ones((행, 열)):")
# data = np.ones((2,3)) # [[1. 1. 1.] [1. 1. 1.]] float64
data = np.ones((2,3), dtype=np.int32) # [[1 1 1] [1 1 1]] int32
print(data , data.dtype)

# 3. np.empty((행, 열))
# shape 만큼 임의의 값으로 채워짐 ==> 임의의 값으로 초기화 시킨 것
print("3. np.empty((행, 열))")
data = np.empty((2,9))
# data = np.empty((2,9), dtype=np.int32)
print(data , data.dtype )

# 4. np.full((행, 열), 값)
# shape 만큼 지정된 값으로 채워짐
print("4. full((행, 열), 10)")
data = np.full((2,3), 10)
print(data) # [[10 10 10] [10 10 10]]