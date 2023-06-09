import numpy as np

'''
    1. ndarray 삭제
    문법:                          색인
        arr = np.delete(arr, idx|fancy|slice, axis )

      - 순방향 역방향 모두 가능
      - 삭제된 새로운 배열을 반환 (in-place(False))
      - axis=None 이면 flatten 적용됨. => 다차원 -> 1차원
      - slice인 경우에는  np.s_[]  형식 사용한다.
      
    2. 값으로 삭제

    - np.where( (arr==5) | (arr==8)) 활용하여 일치하는 인덱스를 먼저 찾고 인덱싱 방법으로 삭제한다.
    - np.delete(arr, np.where())
'''
# 1. idx 삭제
print("1. idx로 삭제")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr,0)
new_arr = np.delete(arr,1)
# new_arr = np.delete(arr,-1) # [9 8 7 5 4]
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 5 4 3]

# 1. fancy 삭제
# [idx, idx2, idx3, ...] 여러 idx 지정하는 방식
# numpy만 지원됨
print("2. fancy 삭제")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, [0,3,5] ) # fancy 인덱싱
# new_arr = np.delete(arr, [0,3,5, -2] ) # [8 7]
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [8 7 4]

# 1. slice 삭제
# 반드시 np.s_[] 형식 사용
print("3. slice 삭제,  np.s_[::2]")
arr = np.array([9,8,7,5,4,3])
new_arr = np.delete(arr, np.s_[0:4] ) # slice 삭제
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [4 3]

# 2. 값으로 삭제하는 방법
arr = np.array([9,8,7,5,4,3])
print(np.where(arr == 5)) # (array([3], dtype=int64),)
print(np.where((arr == 5)|(arr==8))) # (array([1, 3], dtype=int64),)

xx = np.delete(arr, np.where(arr == 5)) # 5 값 삭제,
print(arr) #[9 8 7 5 4 3]
print(xx) # [9 8 7 4 3]

arr = np.array([9,8,7,5,4,3])
xx = np.delete(arr, np.where((arr==5)|(arr==8))) # 5 와 8 값 삭제,
print(arr) #[9 8 7 5 4 3]
print(xx) # [9 7 4 3]
