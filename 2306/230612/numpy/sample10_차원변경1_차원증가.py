import numpy as np

'''
    1. 차원증가(1차원 --> 2차원)
    예) [1 2 3] (3,) ==> [[1 2 3]] (1,3)
        
    가. arr1D.reshape((행, 열))
    나. np.expand_dims(arr1D, axis=0)
    다. arr1D[np.newaxis, ...]
        arr1D[np.newaxis, :]
'''
# 가. arr1D.reshape((행, 열))
arr1D = np.array([1, 2, 3])
print(arr1D, arr1D.shape) # [1 2 3] (3,)

# arr2D = arr1D.reshape((1,3))
arr2D = arr1D.reshape((1,-1))
print(arr2D, arr2D.shape) # [[1 2 3]] (1, 3)

# 나. np.expand_dims(arr1D, axis=0) -> axis는 추가할 축을 의미
arr1D = np.array([1, 2, 3])
# arr2D = np.expand_dims(arr1D, axis=0) # # [[1 2 3]] (1, 3)
arr2D = np.expand_dims(arr1D, axis=1)
'''
[[1]
 [2]
 [3]] (3, 1)
'''
print(arr2D, arr2D.shape)

# 다. arr1D[np.newaxis, ...] -> np.newaxis는 추가할 축을 의미
#     arr1D[np.newaxis, :]
arr1D = np.array([1, 2, 3])
# arr2D = arr1D[np.newaxis, ...]  # [[1 2 3]] (1, 3)
arr2D = arr1D[..., np.newaxis]
'''
[[1]
 [2]
 [3]]
'''
print(arr2D, arr2D.shape)