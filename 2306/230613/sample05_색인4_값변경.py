import numpy as np
import pandas as pd

####################################################
#### 3. 조회

df = pd.DataFrame({"col1" : [4 ,5, 6, 6,1],
                   "col2" : [7, 8, 9, 9,2],
                   "col3" : [10, 11, 12, 12,10]},
                   index = list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4     7    10
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10
'''

# 1. A행의 모든 값 변경(인덱싱)
df.loc['A']=100
print(df)
'''
   col1  col2  col3
A   100   100   100
B     5     8    11
C     6     9    12
D     6     9    12
E     1     2    10
'''

# 2. B, c행의 모든 값 변경(fancy)
df.loc[['B','C']]=200
print(df)
'''
   col1  col2  col3
A   100   100   100
B   200   200   200
C   200   200   200
D     6     9    12
E     1     2    10
'''

# 3. D행의 col2 값을 900으로변경
df.loc['D','col2']=900
print(df)
'''
   col1  col2  col3
A   100   100   100
B   200   200   200
C   200   200   200
D     6   900    12
E     1     2    10
'''

# 4. D,E행의 col1,col3 값을 -1로변경
df.loc[['D','E'],['col1','col3']]= -1
print(df)
'''
   col1  col2  col3
A   100   100   100
B   200   200   200
C   200   200   200
D    -1   900    -1
E    -1     2    -1
'''

# 5. A:D행의 col2:col3 값을 -100로변경
df.loc['A':'D','col2':'col3']= -100
print(df)
'''
   col1  col2  col3
A   100  -100  -100
B   200  -100  -100
C   200  -100  -100
D    -1  -100  -100
E    -1     2    -1
'''

#########################################
# 6. iloc적용
df.iloc[[0,2],[0,2]]= -1000
print(df)
'''
   col1  col2  col3
A -1000  -100 -1000
B   200  -100  -100
C -1000  -100 -1000
D    -1  -100  -100
E    -1     2    -1
'''

# 7. boolean 색인 사용 가능
df.iloc[[True,True,True,True,True],[0,2]]= -2000
print(df)
'''
   col1  col2  col3
A -2000  -100 -2000
B -2000  -100 -2000
C -2000  -100 -2000
D -2000  -100 -2000
E -2000     2 -2000
'''