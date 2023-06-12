import numpy as np

'''
   유틸리티 함수 - axis 이용하여 행별 또는 열별로 연산

    1. np.prod: 1, 2차원 배열 모든 원소의 곱계산인 product
    2. np.cumprod: 배열 원소간 누적 곱하기

    1. np.sum: 1, 2차원 배열 원소간 합
    2. np.cumsum: 배열 원소간 누적 합하기

    2. np.mean ==> 평균
    3. np.var ==> 분산 
    4. np.std ==> 표준 편차 

'''
# 1. np.prod: 1차원 배열 원소간 곱계산인 product
b = np.array([1, 2, 3, 4])
print("1. original: ", b)  # [1 2 3 4]
print("2. np.prod(arr): ", np.prod(b))  # 1*2*3*4 = 24

# 2. np.prod: 2차원 배열 원소간 곱계산인 product
c = np.array([[1, 2], [3, 4], [5, 6]])
print("3. original: ", c)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("4. np.prod(axis=0): ", np.prod(c, axis=0))  # [15 48]    위 * 아래 ( axis=0 인 행축 기준 )
print("5. np.prod(axis=1): ", np.prod(c, axis=1))  # [ 2 12 30] 왼쪽 * 오른쪽 ( axis=1인 열축 기준 )

# 3. np.nanprod: NaN 을 1로 간주하고 배열 원소 간 곱처리
# NaN 표현 : np.nan (NaN : Not a Number - 데이터로 사용할 수 없는 값)
c = np.array([[1, 2], [3, np.nan]])
print("6.original: ", c)
print("7. np.prod(axis=0): ", np.prod(c, axis=0))  # [ 3. nan]      위 * 아래 ( axis=0 인 행축 기준 )
print("8. np.prod(axis=1): ", np.prod(c, axis=1))  # [ 2. nan]      왼쪽 * 오른쪽 ( axis=1인 열축 기준 )
print("9. np.nanprod(axis=0): ", np.nanprod(c, axis=0))  # [3. 2.]  위 * 아래
print("10. np.nanprod(axis=1): ", np.nanprod(c, axis=1))  # [2. 3.] 왼쪽 * 오른쪽

# 4. np.cumprod: 배열 원소간 누적 곱하기
c = np.array([[1, 2], [3, 4], [5, 6]])
print("11. original: ", c)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("12. np.cumprod(axis=0): ", np.cumprod(c, axis=0))  # [[ 1 2][ 1*3 2*4] [1*3*5 2*4*6]]
'''
[[ 1  2]
 [ 3  8]
 [15 48]]
'''
print("13. np.cumprod(axis=1): ", np.cumprod(c, axis=1))  # [[ 1 1*2] [3 3*4] [5 5*6]]
'''
[[ 1  2]
 [ 3 12]
 [ 5 30]]
'''

# 단항 유니버셜 함수3 - sum, nansum, cumsum (모두 중요)

# 1. np.sum: 1차원 배열 원소간 합
b = np.array([1, 2, 3, 4])
# print("average:" , np.average(b))
print("1. original: ", b)  # [1 2 3 4]
print("2. np.sum: ", np.sum(b))  # 1+2+3+4 = 10, 스칼라 값으로 배월 원소 간 합을 반환
print("3. np.sum(keepdims=True): ", np.sum(b, keepdims=True))  # [10] , 1차원 배열로 배열 원소 간 합을 반환

# 2. np.sum: 2차원 배열 원소간 합
c = np.array([[1, 2], [3, 4], [5, 6]])
print("4. original: ", c)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("5. np.sum(axis=0): ", np.sum(c, axis=0))  # [ 9 12]    위 + 아래  ( axis=0 인 행축 기준 )
print("6. np.sum(axis=1): ", np.sum(c, axis=1))  # [ 3  7 11] 왼쪽 + 오른쪽 ( axis=1인 열축 기준 )

# 3. np.nansum: NaN 을 0로 간주하고 배열 원소 간 합처리
c = np.array([[1, 2], [3, np.nan]])
print("7. original: ", c)
print("8. np.sum(axis=0): ", np.sum(c, axis=0))  # [ 4. nan]       위 + 아래
print("9. np.sum(axis=1): ", np.sum(c, axis=1))  # [ 3. nan]       왼쪽 + 오른쪽
print("10. np.nansum(axis=0): ", np.nansum(c, axis=0))  # [4. 2.]  위 + 아래
print("11. np.nansum(axis=1): ", np.nansum(c, axis=1))  # [3. 3.]  왼쪽 + 오른쪽

# 4. np.cumsum: 배열 원소간 누적 합하기
c = np.array([[1, 2], [3, 4], [5, 6]])
print("12. original: ", c)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("13. np.cumsum(axis=0): ", np.cumsum(c, axis=0)) # [[ 1 2][1+3 2+4][1+3+5 2+4+6]]
'''
[[ 1  2]
 [ 4  6]
 [ 9 12]]
'''
print("14. np.cumsum(axis=1): ", np.cumsum(c, axis=1))  # [[ 1 1+2][3 3+4][5 5+6]]
'''
[[ 1  3]
 [ 3  7]
 [ 5 11]]
'''

# 5. np.mean ==> 평균, 이상치(outlier)에 영향을 많이 받음
# python: 제공안됨 ==> sum()/len()
# sql: avg()
print("9.  1차원 배열 np.mean(arr) : ", np.mean([1, 2, 3, 4]))  # 2.5
print("10. 2차원 배열 np.mean(arr, axis=0): ",
      np.mean([[1, 2, 3, 4], [1, 2, 3, 4]], axis=0))  # [1. 2. 3. 4.]
print("11. 2차원 배열 np.mean(arr, axis=1):",
      np.mean([[1, 2, 3, 4], [1, 2, 3, 4]], axis=1))  # [2.5 2.5]

# 6. np.median ==> 중앙값 (내부적으로 정렬 후 가운데 있는 값 반환), 이상치에 영향을 덜 받음
arr = np.array([6, 8, 3, 5, 1])
print("홀수 중앙값:", np.median(arr)) # 5.0
arr = np.array([6,8,3,5,1,9])
print("짝수 중앙값:", np.median(arr)) # 5.5 -> 5와 6의 평균

# 7. np.var ==> 분산
# 분산 : 평균을 기준으로 퍼져있는 정도
print("12. 1차원 배열 np.var(arr): ", np.var([1, 20, 3, 40]))  # 246.5
print("13. 2차원 배열 np.var(arr, axis=0): ",
      np.var([[1, 20, 3, 40], [4, 6, 7, 80]], axis=0))  # [  2.25  49.     4.   400.
print("14. 2차원 배열 np.var(arr, axis=1): ",
      np.var([[1, 20, 3, 40], [4, 6, 7, 80]], axis=1))  # [ 246.5    1037.1875]

# 8. np.std ==> 표준 편차
print("15. 1차원 배열 np.std(arr): ", np.std([1, 20, 3, 40]), np.sqrt(np.var([1, 20, 3, 40])))  # 15.700318468107582 15.700318468107582
print("16. 2차원 배열 np.std(arr, axis=0): ",
      np.std([[1, 20, 3, 40], [4, 6, 7, 80]], axis=0))  # [ 1.5  7.   2.  20. ]
print("17. 2차원 배열 np.std(arr, axis=1): ",
      np.std([[1, 20, 3, 40], [4, 6, 7, 80]], axis=1))  # [15.70031847 32.20539551]