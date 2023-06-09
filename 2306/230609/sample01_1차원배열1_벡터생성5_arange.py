import numpy as np

'''
    4. np.arange([start,] stop[, step] 함수
     ==> 파이썬의  range 함수와 동일한 기능 제공, 단, 지정된 값의 타입에 따라서 반환됨.

    가. 변수 = np.arrange(n)		#  [0,n) 범위의 정수 , 만약 n값이 실수이면 실수값 반환됨.
	나. 변수 = np.arrange(n,m)	#  [n,m) 범위의 정수
	다. 변수 = np.arrange(n, dtype=np.float32)   #  [0,n) 범위의 실수
        변수 = np.arrange( n실수값 )   #  [0, n) 범위의 실수   
'''
# 가
print("1. arange(10)")
data = np.arange(10)  # [0,10)형식으로 표현
print(data)  # [0 1 2 3 4 5 6 7 8 9]

# 나
print("2. arange(1,11)")
data = np.arange(1,11) # [1,11)형식으로 표현
print(data) # [ 1  2  3  4  5  6  7  8  9 10]

#
print("3. arange(1,11,2)")
data = np.arange(1,11,2) # start, end(exclusive), step
print(data) # [1 3 5 7 9]

# float값으로 설정하기
print("4. float으로 설정1")
data = np.arange(5, dtype=np.float32)
print(data) # [0. 1. 2. 3. 4.]

print("4. float으로 설정2")
# float값 지정하면 float 값 반환됨.
data = np.arange(5.)
print(data) # [0. 1. 2. 3. 4.]