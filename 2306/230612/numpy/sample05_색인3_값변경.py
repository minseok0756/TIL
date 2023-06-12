import numpy as np

'''
    색인을 활용한 데이터 변경
    1. 인덱싱
    2. 슬라이싱
    3. fancy
    4. boolean
    
'''
arr = np.arange(10)
print(arr) # [0 1 2 3 4 5 6 7 8 9]

# 1. 인덱싱 이용한 값 변경
arr[0] = 100
print(arr) # [100   1   2   3   4   5   6   7   8   9]

# 2. 슬라이싱 이용한 값 변경 => 브로드 캐스팅
arr[1:4] = 200
print(arr) # [100 200 200 200   4   5   6   7   8   9]

# 3. fancy 색인 이용한 값 변경
arr[[-1,-2,-3]] = 50
print(arr) # [100 200 200 200   4   5   6  50  50  50]

# 4. boolean 색인 이용한 값 변경
arr[arr>=100] = 0
print(arr) # [ 0  0  0  0  4  5  6 50 50 50]

# 5. 모든 값 변경 ==> 1
arr[:]=1
arr[...] = 1
print(arr) # [1 1 1 1 1 1 1 1 1 1]