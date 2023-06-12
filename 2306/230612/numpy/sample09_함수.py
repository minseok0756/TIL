import numpy as np

'''
    함수(function)
    1. 범용함수(universal function)
    - 데이터 요소단위(벡터연산처럼 원소단위)로 처리
    - 범용함수인지 확인 -> print(np.함수) 결과가 ufunc인지 확인
    
'''
# 단항 유니버셜 함수
# 1. np.abs: 절대값
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
print("1. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("2. np.abs(arr): " , np.abs(arr)) # [4.62 2.19 0.   1.57 3.4  4.06]

# 2. np.around: 0.5를 기준으로 올림 혹은 내림
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06, 4.5])
print("3. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06  4.5 ]
print("4. np.around(arr): " , np.around(arr)) # [-5. -2.  0.  2.  3.  4.  4.] # 4.5는 4.으로 반환

# 3. np.round: N 소수점 자릿수까지 반올림
arr = np.array([-4.62985, -2.19568, 0, 1.5754, 3.4056, 4.06898])
print("5. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("6. np.round(arr, 1): " , np.round(arr, 1)) # [-4.6 -2.2  0.   1.6  3.4  4.1]
print("6. np.round(arr, 3): " , np.round(arr, 3)) # [-4.63  -2.196  0.     1.575  3.406  4.069]

# 4. np.rint: 가장 가까운 정수로 올림 혹은 내림
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06, 4.5])
print("7. original: ", arr) # [-4.62 -2.19  0.    1.57  3.4   4.06  4.5 ]
print("8. np.rint(arr): ", np.rint(arr)) # [-5. -2.  0.  2.  3.  4.  4.] # 4.5는 4.으로 반환

# 5. np.fix: 0 방향으로 가장 가까운 정수로 올림 혹은 내림 -> np.trunc와 동일
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
print("9. original: ", arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("10. np.fix(arr): ", np.fix(arr)) # [-4. -2.  0.  1.  3.  4.]

# 6. np.ceil: 각 원소보다 크거나 같은 가장 작은 정수값으로 올림
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
print("11. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("12. np.ceil(arr): " , np.ceil(arr)) # [-4. -2.  0.  2.  4.  5.]

# 7. np.floor: 각 원소보다 작거나 같은 가장 큰 정수값으로 내림
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
print("13. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("14. np.floor(arr): " , np.floor(arr)) # [-5. -3.  0.  1.  3.  4.]

# 8. np.trunc: 각 원소의 소수점 부분은 잘라버리고 정수값만 남김 -> np.fix와 동일
arr = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])
print("15. original: " , arr) # [-4.62 -2.19  0.    1.57  3.4   4.06]
print("16. np.trunc(arr): " , np.trunc(arr)) # [-4. -2.  0.  1.  3.  4.]

# 9. np.sqrt: 제곱근
arr = np.array([1,4,9,16,25])
print("17. original: " ,arr) # [ 1  4  9 16 25]
print("18. np.sqrt(arr): " , np.sqrt(arr)) # [1. 2. 3. 4. 5.]

# 10. np.reciprocal : 각 요소의 역수
print("19. np.reciprocal 1: ", np.reciprocal([1,2,3]))  # 1/1 1/2 1/3 ==> [1 0 0]
print("20. np.reciprocal 2: ", np.reciprocal([1.,2.,3.]))  # 1/1 1/2 1/3 ==> [1.  0.5 0.33333333]
