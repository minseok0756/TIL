import numpy as np

'''
    1. 차원감소(n차원 --> n-1차원)
    예) [[1 2 3]] (1,3) ==> [1 2 3] (3,)
        
    가. arr1D = np.squeeze(arr2D, axis=0)
       
'''
arr2D = np.arange(3).reshape(1,3)
print(arr2D, arr2D.shape) # [[0 1 2]] (1, 3)

arr1D = np.squeeze(arr2D,axis=0)
# shape값이 1인 축으로 축소할 수 있다.
# 따라서 axis에 값을 넣을 때 ndarray.shape값이 1인 인덱스를 넣어야한다.
print(arr1D, arr1D.shape) # [0 1 2] (3,)
