import numpy as np
import pandas as pd

###########################################
### 2.  병합(merge)
'''
    병합(merge)

    2. outer 병합
          가. 공통컬럼 이용
              pd.merge(df, df2,  how=“left|right|outer”,  on=“컬럼명”)

              left : SQL의 left outer join과 동일 : left는 모두 출력
              right : SQL의 right outer join과 동일 : right는 모두 출력
              outer : SQL의 full outer join과 동일 : 모두 출력
              
          나. 비공통컬럼 이용
              pd.merge(df, df2,  how“left|right|outer”,  left_on=“컬럼명”,  right_on=“컬럼명” )
                 .query("조건식")
                 .drop(columns=[컬럼,.])
                 .rename(columns={컬럼:컬럼})

'''
# 1) 공통컬럼
df1 = pd.DataFrame({"x1":['A','B','C'],
                    "x2":[1, 2, 3]})

df2 = pd.DataFrame({"x1":['A','B','D'],
                    "x3":['T','F','T'],
                    "x4":['T1','F1','T1']})
print(df1)
'''
  x1  x2
0  A   1
1  B   2
2  C   3
'''
print(df2)
'''
  x1 x3  x4
0  A  T  T1
1  B  F  F1
2  D  T  T1
'''

new_df = pd.merge(df1, df2, how='left', on='x1')
print(new_df)
'''
  x1  x2   x3   x4
0  A   1    T   T1
1  B   2    F   F1
2 *C  *3 *NaN *NaN
'''

new_df = pd.merge(df1, df2, how='right', on='x1')
print(new_df)
'''
  x1   x2 x3  x4
0  A  1.0  T  T1
1  B  2.0  F  F1
2  D  NaN  T  T1
'''

new_df = pd.merge(df1, df2, how='outer', on='x1')
print(new_df)
'''
  x1   x2   x3   x4
0  A  1.0    T   T1
1  B  2.0    F   F1
2  C  3.0  NaN  NaN
3  D  NaN    T   T1
'''