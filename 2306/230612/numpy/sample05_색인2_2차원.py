import numpy as np

'''
    2차원 배열 색인
    ==> 기본적으로 arr[행, 열] 형식을 따른다.
    
    1. python의 인덱싱/슬라이싱 모두 가능
    
    2. fancy 색인
    
    3. boolean 색인
    ==> 반드시 색인대상과 길이가 같아야 된다.
        실행결과는 1차원으로 반환됨.(True값만 반한되어 size가 망가지기 때문)
    ==> python의 and/or/not 대신 &/|/~ 사용
'''
# 1) 인덱싱 및 슬라이싱
arr = np.array([[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]])
print("1. original: ", arr)
'''
[[   1    2    3]
 [  10   20   30]
 [ 100  200  300]
 [1000 2000 3000]]
'''
print("2. 1행만 반환1",    arr[0]) # [1 2 3]
print("2. 1행만 반환2",    arr[0,...]) # 위 와 동일
print("3. 마지막 행만 반환",    arr[-1]) # [1000 2000 3000]

print("3. 1행의 1열 반환 " , arr[0,1]) # 2
print("4. 1행의 마지막 열 반환 " ,arr[0, -1]) # 3
print("5. 1행의 2열이후 반환 " ,arr[0, 1:]) # [2 3]

print("6. 1열만 반환1 " , arr[:, 0]) # [   1   10  100 1000]
print("6. 1열만 반환2 " , arr[..., 0]) # [   1   10  100 1000]
print("7. 2열이후 반환 " , arr[:, 1:])
# [[   2    3]
#  [  20   30]
#  [ 200  300]
#  [2000 3000]]

print("8. 2행이후 2열이후 반환 " , arr[1:, 1:])
# [[  20   30]
#  [ 200  300]
#  [2000 3000]]

# 2) fancy 색인
arr = np.array([[1,2,3],[10,20,30],[100,200,300]])
print("1. original: ", arr)
'''
[[  1   2   3]
 [ 10  20  30]
 [100 200 300]]
'''
print("2. 1행과 3행만 반환", arr[[0, 2]])
# [[  1   2   3]
#  [100 200 300]]

print("3. 1행과 3행에서 2열만 반환: ", arr[[0, 2], [1]]) #  [  2 200]
print("4. 1행과 3행에서 2열 이후 반환", arr[[0, 2], 1:])
# [[  2   3]
#  [200 300]]

print("5. 2열과 3열만 반환", arr[:, [1, 2]])
# [[  2   3]
#  [ 20  30]
#  [200 300]]

# 3) boolean 색인
arr = np.array([[1,2,3],[10,20,30],[100,200,300]])
print("1. original: ", arr)
'''
[[  1   2   3]
 [ 10  20  30]
 [100 200 300]]
'''
print("2. arr%2==0: ", arr%2==0)
# [[False  True False]
#  [ True  True  True]
#  [ True  True  True]]

print("3. arr[arr%2==0]: ", arr[arr%2==0]) # [  2  10  20  30 100 200 300]
print("4. arr[(arr%2!=0) | (arr < 100)] " , arr[(arr%2!=0) | (arr < 100)]) # [ 1  2  3 10 20 30]
