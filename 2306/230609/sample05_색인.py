import numpy as np

'''
    1차원 배열 색인
    
    1. python의 인덱싱/슬라이싱 모두 가능
    
    2. fancy 색인
    
    3. boolean 색인
    ==> 반드시 색인대상과 길이가 같아야 된다.
    ==> python의 and/or/not 대신 &/|/~ 사용
'''
arr =np.arange(10)
print(arr) # [0 1 2 3 4 5 6 7 8 9]

# 1. 인덱싱
print(arr[0], arr[-1]) # 0 9

# 1. 슬라이싱
print(arr[1:5]) # [1 2 3 4]
print(arr[:5]) # [0 1 2 3 4]
print(arr[1:]) # [1 2 3 4 5 6 7 8 9]
print(arr[1:10:2]) # [1 3 5 7 9]
print(arr[:]) # [0 1 2 3 4 5 6 7 8 9]
print(arr[...]) # [0 1 2 3 4 5 6 7 8 9] [:]와 같은 결과(python은 지원 안됨)

# 2. fancy 색인
data = np.arange(10) * 100
print("1. original: ", data) # [  0 100 200 300 400 500 600 700 800 900]
# print(data[1,3,5]) # 에러 발생, 대괄호 두개 사용
print("2. data[[1,3,5]]: ", data[[1,3,5]]) # [100 300 500]
print("3. data[[8,1,5]]: ", data[[8,1,5]]) # [800 100 500] 먼저 지정한 인덱스가 먼저 나옴

# 3. boolean 색인 ==> 반드시 색인대상과 길이가 같아야 된다.
data = np.array([1,2,3,4,5])
print("1. original: " , data) # [1 2 3 4 5]
print("2. 벡터연산,  data%2==0: " , data%2==0) # [False  True False  True False]
print("3. boolean 색인, [True,True,True,True,False]: ",data[[True,True,True,True,False]]) # [1 2 3 4]
                                                                                         # True와 매핑이 되는 원소만 출력됨
print("4. boolean 색인 활용,data[data%2==0]: ",data[data%2==0])  # [2 4] 2)와3) 개념을 한꺼번에 적용
print("5. boolean 색인 활용,data[data > 3 ]: ",data[data > 3])  # [4 5]
print("6. boolean 색인의 & 연산자: " , data[(data%2==0) & (data >2)]) # [4]
print("7. boolean 색인의 | 연산자 " , data[(data%2!=0) | (data < 4)]) # [1 2 3 5]
print("8. boolean 색인 ~연산자: ",data[~(data > 3)])  # [1 2 3]

# 실습 : 특정 이름(홍길동) 검색
names = np.array(['세종',"홍길동","이순신","정조","홍길동"])
# 가. boolean 색인
print(names[names=='홍길동']) # ['홍길동' '홍길동']

# 나. list comprehension
print([x for x in names if x == '홍길동']) # ['홍길동', '홍길동']