import numpy as np
import pandas as pd
## 1. 널(null) 값 조회
'''
     널(null) 값 조회 : None, NaN or NA as null
                        -> python에는 None, NaN, NA가 있다. 모두 합쳐 null이라 부르자
                        -> 하지만 python에 실제 null값이 있는건 아니다.

    1.  Pandas 함수 이용
     1)  bool = pd.isna(스칼라|Series|df)
     2)  bool = pd.isnull(스칼라|Series|df)
     3)  bool = pd.notnull(스칼라|Series|df)

    2.  DataFrame 함수 이용
     1)  bool = df.isnull()
         bool = df[컬럼명].isnull()
         bool = df[[컬럼,컬럼2]].isnull()
     2)  bool = df.isna()
         bool = df[컬럼명].isna()
         bool = df[[컬럼,컬럼2]].isna()
     3)  bool = df.notnull()
         bool = df[컬럼명].notnull()
         bool = df[[컬럼,컬럼2]].notnull()
         
'''
df = pd.DataFrame({ "col1" : [1 ,1, 1, None, 1],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 3, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
None값도 NaN으로 출력된다.
'''

# pandas함수 이용
# 1. df 대상
print(pd.isna(df))
print(pd.isnull(df))
'''
    col1   col2   col3  col4
1  False  False   True  True
2  False  False  False  True
3  False  False  False  True
4   True  False  False  True
5  False   True  False  True
NaN값이 True로 출력
'''
print(pd.notnull(df))
'''
    col1   col2   col3   col4
1   True   True  False  False
2   True   True   True  False
3   True   True   True  False
4  False   True   True  False
5   True  False   True  False
NaN이면 False 출력
'''

# 2. 특정 컬럼(Series) 대상
print(pd.isna(df['col1']))
print(pd.isnull(df['col1']))

'''
1    False
2    False
3    False
4     True
5    False
Name: col1, dtype: bool
'''

# 3. 특정 컬럼들(DataFrame) 대상
print(pd.isna(df[['col1','col2']]))
print(pd.isnull(df[['col1','col2']]))
'''
    col1   col2
1  False  False
2  False  False
3  False  False
4   True  False
5  False   True

'''
print('#'*100)

# DataFrame 함수 이용
# 1. df 대상
print(df.isnull())
print(df.isna())
'''
    col1   col2   col3  col4
1  False  False   True  True
2  False  False  False  True
3  False  False  False  True
4   True  False  False  True
5  False   True  False  True
'''

# 2. 특정 컬럼(Series) 대상
print(df['col1'].isnull())
'''
1    False
2    False
3    False
4     True
5    False
Name: col1, dtype: bool
'''

# 3. 특정 컬럼들(DataFrame) 대상
print(df[['col1', 'col2']].isnull())
'''
    col1   col2
1  False  False
2  False  False
3  False  False
4   True  False
5  False   True
'''