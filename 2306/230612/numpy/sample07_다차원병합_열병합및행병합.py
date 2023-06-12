import numpy as np

'''
    1. 다차원 열병합 ==> 수평축을 기준으로 열 병합(두 배열을 가로로 붙인다.)

    1. np.hstack((arr, arr2)) ==> 수평(horizontal)방향으로 병합
    2. np.concatenate((arr,arr2), axis=1 ) ==> axis=1인 컬럼방향으로 병합
    3. np.column_stack((arr, arr2)) ==> 컬럼(column)방향으로 병합
    -> 인자가 튜플형식인 것을 주의
    
    2. 다차원 행병합 ==> 수직축을 기준으로 행 병합(두 배열을 세로로 붙인다.)

    1. np.vstack((arr, arr2)) ==> 수직(vertical)방향으로 병합
    2. np.concatenate((arr,arr2), axis=0 ) ==> axis=0인 행방향으로 병합
    3. np.row_stack((arr, arr2)) ==> 행(row)방향으로 병합
'''
# 1. 다차원 열병합
arr = np.arange(9).reshape(3,3)
arr2 = arr * 2
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
# column_merge = np.hstack((arr,arr2)) # hstack 마우스오버에서 tup는 튜플을 의미
# column_merge = np.concatenate((arr,arr2) , axis=1)
column_merge= np.column_stack((arr, arr2))
print(column_merge)
'''
[[ 0  1  2  0  2  4]
 [ 3  4  5  6  8 10]
 [ 6  7  8 12 14 16]]
'''

# 2. 다차원 행병합
arr = np.arange(9).reshape(3,3)
arr2 = arr * 2
print(arr)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print(arr2)
'''
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''
# row_merge = np.vstack((arr,arr2))
# row_merge = np.concatenate((arr,arr2) , axis=0)
row_merge= np.row_stack((arr, arr2))
print(row_merge)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
'''