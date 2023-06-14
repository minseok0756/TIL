import numpy as np
import pandas as pd
## 2. 널(null) 값 삭제
'''
     null 값 삭제
     
     df.dropna(axis, how, inplace)
    - axis 0|1
    - how 'all|any' - 기본값 any
        - how = 'all' : 모두 NaN일시 삭제
          how = 'any' : 하나라도 NaN이면 삭제
    - inplace True|False
    
     1. 행 삭제
        new_df = df.dropna(axis=0|'index', inplace=False)
        new_df = df.dropna(axis=0|'index', how="any|all" , inplace=False)) 

     2. 열 삭제
        new_df = df.dropna(axis=1|'column', inplace=False)
        new_df = df.dropna(axis=1|'column', how="any|all" , inplace=False))
        
'''
df = pd.DataFrame({ "col1" : [1 ,1, 1, 1, np.nan],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [3, np.nan, np.nan, np.nan, np.nan],
                    "col4" : [np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   NaN
2   1.0   2.0   NaN   NaN
3   1.0   2.0   NaN   NaN
4   1.0   2.0   NaN   NaN
5   NaN   NaN   NaN   NaN
'''

# 1. 행 삭제
new_df = df.dropna(axis=0) # how의 기본값은 any
print(new_df)
'''
Empty DataFrame
Columns: [col1, col2, col3, col4]
Index: []
'''

new_df = df.dropna(axis=0, how='all')
print(new_df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   2.0
2   1.0   2.0   NaN   NaN
3   1.0   2.0   NaN   NaN
4   1.0   2.0   NaN   NaN
다섯번째행 삭제
'''

# 2. 열 삭제
new_df = df.dropna(axis=1)
print(new_df)
'''
Empty DataFrame
Columns: []
Index: [1, 2, 3, 4, 5]
'''

new_df = df.dropna(axis=1, how='all')
print(new_df)
'''
   col1  col2  col3
1   1.0   2.0   3.0
2   1.0   2.0   NaN
3   1.0   2.0   NaN
4   1.0   2.0   NaN
5   NaN   NaN   NaN
col4가 삭제
'''