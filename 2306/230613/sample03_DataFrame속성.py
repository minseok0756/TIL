import numpy as np
import pandas as pd

'''
    DataFrame의 속성 정보 보기
    
    1. 컬럼정보
        DataFrame.columns
        DataFrame.keys()
        
    2. 인덱스(라벨) 정보
        DataFrame.index
        
    3. 값 정보 -> 다차원배열로 나온다.
        DataFrame.values
        DataFrame.to_numpy() - 권장 
        
'''
df = pd.DataFrame({"col1" : [4 ,5, 6],
                   "col2" : [7, 8, 9],
                   "col3" : [10, 11, 12]}, index=['A','B','C'])
# 1. 컬럼정보 보기
print(df.columns) # Index(['col1', 'col2', 'col3'], dtype='object')
print(df.keys()) # Index(['col1', 'col2', 'col3'], dtype='object')

# 2. 인덱스 정보 보기
print(df.index) # Index(['A', 'B', 'C'], dtype='object')

# 3. 값 정보 보기
print(df.values)
'''
[[ 4  7 10]
 [ 5  8 11]
 [ 6  9 12]]
'''
print(df.to_numpy())
'''
[[ 4  7 10]
 [ 5  8 11]
 [ 6  9 12]]
'''