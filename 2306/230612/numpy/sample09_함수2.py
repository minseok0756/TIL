import numpy as np

'''
    이항 유니버셜 함수(함수에 항이 두개들어감)

    1. np.add:  + 연산과 동일
    2. np.subtract:  - 연산과 동일
    3. np.multiply:  * 연산과 동일
    4. np.divide:  / 연산과 동일
    5. np.floor_divide:  // 연산과 동일 ( 몫 연산 )
    6. np.mod:  % 연산과 동일 ( 나머지 연산 )
    7. np.maximum:  인덱스별로 큰 값 반환
    8. np.power: ** 연산과 동일
    
'''
# 1. np.add:  + 연산과 동일
b = np.array([1, 2, 3, 4])
print("1. original: " , b ) # [1 2 3 4]
print("2. b+b: " , b+b ) # [2 4 6 8]
print("3. np.add(b,b): " , np.add(b,b) ) # [2 4 6 8]

# 2. np.subtract:  - 연산과 동일
b = np.array([1, 2, 3, 4])
print("1. original: " , b ) # [1 2 3 4]
print("2. b*2-b: " , b*2-b ) # [1 2 3 4]
print("3. np.subtract(b*2,b): " , np.subtract(b*2,b) ) # [1 2 3 4]

# 3. np.multiply:  * 연산과 동일
b = np.array([1, 2, 3, 4])
print("1. original: " , b ) # [1 2 3 4]
print("2. b*b: " , b*b ) # [ 1  4  9 16]
print("3. np.multiply(b,b): " , np.multiply(b,b) ) # [ 1  4  9 16]

# 4. np.divide:  / 연산과 동일
b = np.array([1, 2, 3, 4])
print("1. original: " , b ) # [1 2 3 4]
print("2. b/b: " , b/b ) # [1. 1. 1. 1.]
print("3. np.divide(b,b): " , np.divide(b,b) ) # [1. 1. 1. 1.]

# 5. np.floor_divide:  // 연산과 동일 ( 몫 연산 )
b = np.array([5,6,7,8])
b2 = np.array([3,3,3,3])
print("1. original: " , b ) # [5 6 7 8]
print("2. b//b2: " , b//b2 ) # [1 2 2 2]
print("3. np.floor_divide(b,b): " , np.floor_divide(b,b2) ) # [1 2 2 2]

# 6. np.mod:  % 연산과 동일 ( 나머지 연산 )
b = np.array([5,6,7,8])
b2 = np.array([3,3,3,3])
print("1. original: " , b ) # [5 6 7 8]
print("2. b%b2: " , b%b2 ) # [2 0 1 2]
print("3. np.mod(b,b2): " , np.mod(b,b2) ) # [2 0 1 2]
print("4. np.remainder(b,b2): " , np.remainder(b,b2) ) # [2 0 1 2]

# 7. np.maximum  인덱스별로 비교하여 큰 값 반환
b = np.array([5,6,7,8])
b2 = np.array([1,9,6,8])
print("1. original: " , b ) # [5 6 7 8]
print("2. np.maximum(b,b2): " , np.maximum(b,b2) ) # [5 9 7 8]
                                                   # 인덱스별로 비교하여 큰 값 반환
print("3. np.minimum(b,b2): " , np.minimum(b,b2) ) #  [1 6 6 8]
                                                   # 인덱스별로 비교하여 작은 값 반환
print("4. np.greater(b,b2): " , np.greater(b,b2) ) #  [ True False  True False]
                                                   # 인덱스별로 비교하여 크면 True 작거나 같으면 False
print("5. np.greater_equal(b,b2): " , np.greater_equal(b,b2) ) #  [ True False  True  True]
                                                               # 인덱스별로 비교하여 크거나 같으면 True 작으면 False
print("6. np.less(b,b2): " , np.less(b,b2) ) #  [False  True False False]
                                             # 인덱스별로 비교하여 작으면 True 크거나 같으면 False
print("7. np.less_equal(b,b2): " , np.less_equal(b,b2) ) #  [False  True False  True]
                                                         # 인덱스별로 비교하여 작거나 같으면 True 크면 False
print("8. np.equal(b,b2): " , np.equal(b,b2) ) #  [False False False  True]
                                               # 같으면 True 다르면 False
print("9. np.not_equal(b,b2): " , np.not_equal(b,b2) ) #  [ True  True  True False]
                                                       # 다르면 True 같으면 False

# 8. np.power : 제곱
print("1. np.power:" , np.power(2, 3))  # 8