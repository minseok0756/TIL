import numpy as np
import pandas as pd

###########################################
### 2.  병합(merge)
'''
    병합(merge)

    2. outer 병합
              
          나. 비공통컬럼 이용
              pd.merge(df, df2,  how“left|right|outer”,  left_on=“컬럼명”,  right_on=“컬럼명” )
                 .query("조건식")
                 .drop(columns=[컬럼,.])
                 .rename(columns={컬럼:컬럼})
'''
# 2) 비공통컬럼
df1 = pd.DataFrame({"x1":['A','B','C'],
                    "x2":[1, 2, 3]})

df2 = pd.DataFrame({"y1":['A','B','D'],
                    "x3":['T','F','T']})

print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''

print(df2)
'''
  y1 x3
0  A  T
1  B  F
2  D  T
'''

new_df = pd.merge(df1, df2, how='left', left_on='x1', right_on='y1')
print(new_df)
'''
  x1  x2   y1   x3
0  A   1    A    T
1  B   2    B    F
2 *C  *3 *NaN *NaN
'''

new_df = pd.merge(df1, df2, how='right', left_on='x1', right_on='y1')
print(new_df)
'''
    x1   x2 y1 x3
0    A  1.0  A  T
1    B  2.0  B  F
2 *NaN *NaN *D *T
'''

new_df = pd.merge(df1, df2, how='outer', left_on='x1', right_on='y1')
print(new_df)
'''
    x1   x2   y1   x3
0    A  1.0    A    T
1    B  2.0    B    F
2   *C *3.0 *NaN *NaN
3 *NaN *NaN   *D   *T
'''

'''
    outer 병합도 컬럼과 인덱스 / 인덱스와 인덱스 가능하다
    하지만 실습은 안함.
'''