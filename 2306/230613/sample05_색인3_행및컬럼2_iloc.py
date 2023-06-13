import numpy as np
import pandas as pd

####################################################
#### 3. 조회

'''
    3) 행 및 컬럼 조회

   DataFrame 의 행과 컬럼 조회 

    1. 행 인덱스의 label 이용 
      ==> 기본 문법은 df.loc[행label, 컬럼label]
      ==> 행label은 인덱스라벨,fancy,슬라이싱,boolean 모두 가능 
      ==> 컬럼label은 인덱스라벨,fancy,슬라이싱,boolean 모두 가능 
      
    2. 행 인덱스의 위치 이용
    ==> 기본 문법은 df.iloc[행위치, 컬럼위치]
    
'''
df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
'''
     0     1     2
     col1  col2  col3
0  A     4     7    10
1  B     5     8    11
2  C     6     9    12
3  D     6     9    12
4  E     1     2    10
'''

# 1. 인덱싱
print(df.iloc[0, 0]) # 4 스칼라값

# 2. 인덱싱 + fancy
print(df.iloc[[0,1], 0]) # Series 반환
'''
A    4
B    5
Name: col1, dtype: int64
'''

# 3. fancy + fancy
print(df.iloc[[0,1], [0,1]]) # DataFrame 반환
'''
   col1  col2
A     4     7
B     5     8
'''

# 4. slice + fancy
print(df.iloc[1:, [0,1]]) # DataFrame 반환
'''
   col1  col2
B     5     8
C     6     9
D     6     9
E     1     2
lavel이기 때문에 E까지 포함
'''

# 5. slice + slice
print(df.iloc[1:, 1:]) # DataFrame 반환
'''
   col2  col3
B     8    11
C     9    12
D     9    12
E     2    10
lavel이기 때문에 E와 col3까지 포함
'''

# 6. boolean + slice
# 일반적으로 비교연산자와 논리연산자를 이용하여 boolean색인한다.
print(df.iloc[[True,False,True,False,True], 1:]) # DataFrame 반환
'''
   col2  col3
A     7    10
C     9    12
E     2    10
'''