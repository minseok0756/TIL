import numpy as np
import pandas as pd

###########################################
### 2.  병합(merge)
'''
    병합(merge)

   1. inner 병합

      나. 비공통 컬럼 이용
          new_df = pd.merge(df, df2, how='inner', left_on="컬럼명", right_on="컬럼명")
          new_df = pd.merge(df, df2, how='inner', left_on="컬럼명", right_on="컬럼명")
          
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

new_df = pd.merge(df1, df2, how='inner', left_on='x1', right_on='y1')
print(new_df)
'''
  x1  x2 y1 x3
0  A   1  A  T
1  B   2  B  F
'''


