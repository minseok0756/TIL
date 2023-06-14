import numpy as np
import pandas as pd

## 2. Series의 기술통계관련 함수
'''
  1. 최대(소)값         ==>  df['컬럼'].max(), df['컬럼'].min()

     누적최대(소)값,     ==>  df['컬럼'].cummax(), df['컬럼'].cummin()
      최대(소)값label   ==>  df['컬럼'].idxmax(), df['컬럼'].idxmin()
  2. (누적)합계         ==>  df['컬럼'].sum(), df['컬럼'].cumsum()
      평균              ==>  df['컬럼'].mean()
      중앙값            ==>  df['컬럼'].median()
      (누적)곱          ==>  df['컬럼'].prod(), df['컬럼'].cumprod()
  3. 사분위             ==>  df.quantile()
     분산               ==>  df['컬럼'].var()
      표준편차           ==>  df['컬럼'].std()
  4. count(갯수)         ==>  df['컬럼'].count()
  5. 통합 통계           ==>  df['컬럼'].describe()

    ==> DataFrame과 동일함

'''
df = pd.DataFrame({"col1" : [4 ,6, 9, 5, 15],
                   "col2" : [16, 8, np.nan, 6, 6],
                   "col3" : [10, 11, 12, 12, 12]},
                    index = list("ABCDE"))
print(df)
'''
   col1  col2  col3
A     4  16.0    10
B     6   8.0    11
C     9   NaN    12
D     5   6.0    12
E    15   6.0    12
'''

# 1. 최대/최소값 구하기
x = df['col1'].max()
print(x) # 15

x = df['col1'].min()
print(x) # 4

# 2. 누적최대/누적최소값 구하기
x = df['col1'].cummax()
print(x)
'''
A     4
B     6
C     9
D     9
E    15
Name: col1, dtype: int64
'''

x = df['col1'].cummin()
print(x)
'''
A    4
B    4
C    4
D    4
E    4
Name: col1, dtype: int64
'''

# 3. 최대/최소값에 해당하는 인덱스 구하기
x = df['col1'].idxmax()
print(x) # E

x = df['col1'].idxmin()
print(x) # A

# 4. 총합/누적총합 구하기
x = df['col1'].sum()
print(x) # 39

x = df['col1'].cumsum()
print(x)
'''
A     4
B    10
C    19
D    24
E    39
Name: col1, dtype: int64
'''

# 4. 평균 구하기
x = df['col1'].mean()
print(x) # 7.8

# 5. 중앙값 구하기
x = df['col1'].median()
print(x) # 6.0

# 6. 곱/누적곱연산 구하기
x = df['col1'].prod()
print(x) # 16200

x = df['col1'].cumprod()
print(x)
'''
A        4
B       24
C      216
D     1080
E    16200
Name: col1, dtype: int64
'''

# 7. 분산 구하기
x = df['col1'].var()
print(x) # 19.700000000000003


# 8. 표준편차 구하기
x = df['col1'].std()
print(x) # 4.43846820423443

# 9. 갯수 구하기(기본적으로 null 제외)
x = df['col1'].count()
print(x) # 5


# 10. 통합 통계 데이터
x = df['col1'].describe()
print(x)
'''
count     5.000000
mean      7.800000
std       4.438468
min       4.000000
25%       5.000000
50%       6.000000
75%       9.000000
max      15.000000
Name: col1, dtype: float64
'''

# 11. Series 정보
x = df['col1'].info()
print(x)
'''
<class 'pandas.core.series.Series'>
Index: 5 entries, A to E
Series name: col1
Non-Null Count  Dtype
--------------  -----
5 non-null      int64
dtypes: int64(1)
memory usage: 80.0+ bytes
None
'''