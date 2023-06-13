import numpy as np
import pandas as pd

####################################################
#### 3. 조회

'''
    컬럼 선택(SQL의 projection 기능)

    - [] : 인덱싱 연산자, 컬럼(들)을 선택하는 목적
                
    - 단일컬럼 조회 : Series로 반환(index와 값 으로 구성됨)
    df['컬럼명']
    df.컬럼명
                
    - 다중컬럼 조회 : DataFrame으로 반환
    df[['컬럼명', '컬럼명']]
                
    - slice, boolean 안되더라
'''
# 1. 싱글 및 멀티 컬럼 조회
df = pd.DataFrame({"col1" : [4 ,5, 6, 6],
                   "col2" : [7, 8, 9, 9],
                   "col3" : [10, 11, 12, 12]},
                   index = list("ABCD"))
print(df)
'''
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
D     6     9    12
'''

print("1. col1 컬럼만 조회")
print(df.col1 )     # Series 반환
'''
A    4
B    5
C    6
D    6
Name: col1, dtype: int64 -> Series포맷
'''

print("2. col1 컬럼만 조회")
print(df['col1'])  # Series 반환
'''
A    4
B    5
C    6
D    6
Name: col1, dtype: int64
'''

print("3. col1와 col2 컬럼 조회")
print(df[['col2', 'col1']])  # fancy 형태로 사용 , # DataFrame 반환
'''
   col2  col1
A     7     4
B     8     5
C     9     6
D     9     6
df에 적힌 순서대로 출력됨
'''

print("4. col1 컬럼만 여러번 조회")
print(df[['col1','col1','col1']])  # DataFrame 반환
'''
   col1  col1  col1
A     4     4     4
B     5     5     5
C     6     6     6
D     6     6     6
'''