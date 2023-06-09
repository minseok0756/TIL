import numpy as np

'''
    행렬 추가 및 삽입
    1. ndarray 추가

      문법:
        arr = np.append(arr, values, axis=None)

      - 추가된 새로운 배열을 반환
      - axis=None 이면 flatten 된후에 추가된다.
        axis=0 이면 행 추가. 반드시 shape가 일치해야 된다.
        axis=1 이면 열 추가. 반드시 shape가 일치해야 된다.

     2. ndarray 삽입

       문법:
         arr = np.insert(arr, idx|fancy, value,  axis ).

         - fancy 사용시 value와 shape가 일치해야 된다.
'''
arr = np.array([[1,2,3],[4,5,6]])
'''
[[1 2 3]
 [4 5 6]]
'''

# 1. append 함수
# 1) axis=None 지정한 추가
# 2차원에서 axis 지정하지 않으면 flatten 되어 추가됨.
# 따라서 dimension 일치하지 않아도 된다.
xxx = np.append(arr, [100,200,300,400])
print(xxx)  # [  1   2   3   4   5   6 100 200 300 400]

# 2) axis=0 지정한 추가 ==> 행 추가
# 반드시 shape이 일치해야 한다
xxx = np.append(arr, [[100,200,300]], axis=0)
# xxx = np.append(arr, [100,200,300], axis=0) # 에러 발생 shape 불일치
print(xxx)
'''
[[  1   2   3]
 [  4   5   6]
 [100 200 300]]
'''

# 3) axis=1 지정한 추가 ==> 열 추가
# 반드시 shape이 일치해야 한다
xxx = np.append(arr, [[100],[200]], axis=1)
print(xxx)
'''
[[  1   2   3 100]
 [  4   5   6 200]]
'''

####################################################################
####################################################################
arr = np.array([[1,2,3],[4,5,6]])
'''
[[1 2 3]
 [4 5 6]]
'''

# 2. insert 함수
# 1) axis=None 지정한 삽입
# 2차원에서 axis 지정하지 않으면 flatten 되어 추가됨.
# 따라서 dimension 일치하지 않아도 된다.
xxx = np.insert(arr, 0,  [100,200,300,400])
print(xxx)  # [100 200 300 400   1   2   3   4   5   6]

# 2) axis=0 지정한 삽입 ==> 행 삽입
# 반드시 shape이 일치해야 한다
xxx = np.insert(arr, 0,  [[100,200,300]], axis=0)
print(xxx)
'''
[[100 200 300]
 [  1   2   3]
 [  4   5   6]]
'''

# 3) axis=1 지정한 삽입 ==> 열 삽입
# 반드시 shape이 일치해야 한다
xxx = np.insert(arr, 0, [[100],[200]], axis=1)
print(xxx)
'''
[[100 200   1   2   3]
 [100 200   4   5   6]]
'''

xxx = np.insert(arr, [0], [[100],[200]], axis=1)
print(xxx)
'''
[[100   1   2   3]
 [200   4   5   6]]
'''

#####################################################################################
print('#'*30)
xxx = np.insert(arr, 0, [100,200], axis=1)
print(xxx)

xxx = np.insert(arr, 0, [[100,200]], axis=1)
print(xxx)

xxx = np.insert(arr, 0, [[100],[200]], axis=1)
print(xxx)

xxx = np.insert(arr, [0], [100,200], axis=1)
print(xxx)

xxx = np.insert(arr, [0], [[100,200]], axis=1)
print(xxx)

xxx = np.insert(arr, [0], [[100],[200]], axis=1)
print(xxx)