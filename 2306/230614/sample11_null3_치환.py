import numpy as np
import pandas as pd
## 3. 널(null) 값 변경
'''
    null 값 변경
    - null값이 있는 행/컬럼을 삭제하는 경우 분포에 영향을 끼칠 수 있음
    - 또한 통계량 정보를 유지할 수 없음
    - 위 상황이 발생하는 경우에 값을 삭제하지 않고 변경한다.
    
    1. 변경
    - df.fillna(value, method='bfill|ffill|None', inplace=False, limit=n )
        
'''
df = pd.DataFrame({ "col1" : [1 ,1, 1, 1, np.nan],
                    "col2" : [2, 2, 2, 2, np.nan],
                    "col3" : [3, 3, 3, 3, np.nan],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   1.0   2.0   3.0   NaN
5   NaN   NaN   NaN   NaN
'''

# 1. 전체 df의 null값을 임의의 값으로 변경 -> 일반적으로 평균값으로 변경
new_df = df.fillna(0)
print(new_df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   *0.0
2   1.0   2.0   3.0   *0.0
3   1.0   2.0   3.0   *0.0
4   1.0   2.0   3.0   *0.0
5   *0.0  *0.0  *0.0  *0.0
'''

# 2. 컬럼마다 다르게 null값을 임의의 값으로 변경
new_df = df.fillna({'col1':-1, 'col2':-2})
print(new_df)
'''
   col1  col2  col3  col4
1   1.0   2.0   3.0   NaN
2   1.0   2.0   3.0   NaN
3   1.0   2.0   3.0   NaN
4   1.0   2.0   3.0   NaN
5  *-1.0 *-2.0   NaN   NaN
'''

#####################################################################
df = pd.DataFrame({ "col1" : [1 ,np.nan, 3, 4, np.nan],
                    "col2" : [1 ,np.nan, 3, 4, np.nan],
                    "col3" : [1 ,2, np.nan, 4, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3
1   1.0   1.0   1.0
2   NaN   NaN   2.0
3   3.0   3.0   NaN
4   4.0   4.0   4.0
5   NaN   NaN   NaN
'''
# 3. null값의 앞에있는 값으로 변경(forward)
new_df = df.fillna(method='ffill')
print(new_df)
'''
   col1  col2  col3
1   1.0   1.0   1.0
2   *1.0  *1.0  2.0
3   3.0   3.0   *2.0
4   4.0   4.0   4.0
5   *4.0  *4.0  *4.0
'''

# 4. null값의 뒤에있는 값으로 변경(back)
new_df = df.fillna(method='bfill')
print(new_df)
'''
   col1  col2  col3
1   1.0   1.0   1.0
2   *3.0  *3.0  2.0
3   3.0   3.0   *4.0
4   4.0   4.0   4.0
5   NaN   NaN   NaN
'''