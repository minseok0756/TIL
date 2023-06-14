import numpy as np
import pandas as pd

## 2. DataFrame의 기술통계관련 함수
'''
  1. 최대(소)값         ==>  df.max(), df.min()
     누적최대(소)값,     ==>  df.cummax(), df.cummin()
      최대(소)값label   ==>  df.idxmax(), df.idxmin()
  2. (누적)합계         ==>  df.sum(), df.cumsum()
      평균              ==>  df.mean()
      중앙값            ==>  df.median()
      (누적)곱          ==>  df.prod(), df.cumprod()
  3. 사분위             ==>  df.quantile()
     분산               ==>  df.var()
      표준편차           ==>  df.std()
  4. count(갯수)         ==>  df.count()
  5. 통합 통계           ==>  df.describe()
  6. DataFrame 정보      ==> df.info()

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

# 1. 행을 축으로 최대/최소값 구하기
x = df.max(axis=0) # axis=0 위/아래
print(x)
'''
col1    15.0
col2    16.0
col3    12.0
dtype: float64
'''

x = df.min(axis=0)
print(x)
'''
col1     4.0
col2     6.0
col3    10.0
dtype: float64
'''


# 2. 컬럼을 축으로 최대/최소값 구하기
x = df.max(axis=1) # axis=1 왼쪽/오른쪽
print(x)
'''
A    16.0
B    11.0
C    12.0
D    12.0
E    15.0
dtype: float64
'''

x = df.min(axis=1)
print(x)
'''
A    4.0
B    6.0
C    9.0
D    5.0
E    6.0
dtype: float64
'''

# 3. 행을 축으로 누적최대/누적최소값 구하기
x = df.cummax(axis=0)
print(x)
'''
   col1  col2  col3
A     4  16.0    10
B     6  16.0    11
C     9   NaN    12
D     9  16.0    12
E    15  16.0    12
'''

x = df.cummin(axis=0)
print(x)
'''
   col1  col2  col3
A     4  16.0    10
B     4   8.0    10
C     4   NaN    10
D     4   6.0    10
E     4   6.0    10
'''

# 4. 컬럼을 축으로 누적최대/누적최소값 구하기
x = df.cummax(axis=1)
print(x)
'''
   col1  col2  col3
A   4.0  16.0  16.0
B   6.0   8.0  11.0
C   9.0   NaN  12.0
D   5.0   6.0  12.0
E  15.0  15.0  15.0
'''

x = df.cummin(axis=1)
print(x)
'''
   col1  col2  col3
A   4.0   4.0   4.0
B   6.0   6.0   6.0
C   9.0   NaN   9.0
D   5.0   5.0   5.0
E  15.0   6.0   6.0
'''

# 5. 행을 축으로 최대/최소값에 해당하는 인덱스라벨 구하기
x = df.idxmax(axis=0)
print(x)
'''
col1    E
col2    A
col3    C
dtype: object
최소값을 갖는 라벨이 여러개일 경우 가장 위에있는 라벨이 반환됨
'''

x = df.idxmin(axis=0)
print(x)
'''
col1    A
col2    D
col3    A
dtype: object
'''

# 6. 컬럼을 축으로 최대/최소값에 해당하는 컬럼라벨 구하기
x = df.idxmax(axis=1)
print(x)
'''
A    col2
B    col3
C    col3
D    col3
E    col1
dtype: object
'''
x = df.idxmin(axis=1)
print(x)
'''
A    col1
B    col1
C    col1
D    col1
E    col2
dtype: object
'''

# 7. 행을 축으로 총합/누적총합 구하기
x = df.sum(axis=0)
print(x)
'''
col1    39.0
col2    36.0
col3    57.0
dtype: float64
'''

x = df.cumsum(axis=0)
print(x)
'''
A     4  16.0    10
B    10  24.0    21
C    19   NaN    33
D    24  30.0    45
E    39  36.0    57
'''

# 8. 컬럼을 축으로 총합/누적총합 구하기
x = df.sum(axis=1)
print(x)
'''
A    30.0
B    25.0
C    21.0
D    23.0
E    33.0
dtype: float64
'''

x = df.cumsum(axis=1)
print(x)
'''
   col1  col2  col3
A   4.0  20.0  30.0
B   6.0  14.0  25.0
C   9.0   NaN  21.0
D   5.0  11.0  23.0
E  15.0  21.0  33.0
'''

# 9. 행/컬럼을 축으로 평균 구하기
x = df.mean(axis=0)
print(x)
'''
col1     7.8
col2     9.0
col3    11.4
dtype: float64
'''

x = df.mean(axis=1)
print(x)
'''
A    10.000000
B     8.333333
C    10.500000
D     7.666667
E    11.000000
dtype: float64
'''

# 10. 행/컬럼을 축으로 중앙값 구하기
x = df.median(axis=0)
print(x)
'''
col1     6.0
col2     7.0
col3    12.0
dtype: float64
'''

x = df.median(axis=1)
print(x)
'''
A    10.0
B     8.0
C    10.5
D     6.0
E    12.0
dtype: float64
'''

# 11. 행을 축으로 곱/누적곱연산 구하기
x = df.prod(axis=0)
print(x)
'''
col1     16200.0
col2      4608.0
col3    190080.0
dtype: float64
'''

x = df.cumprod(axis=0)
print(x)
'''
    col1    col2    col3
A      4    16.0      10
B     24   128.0     110
C    216     NaN    1320
D   1080   768.0   15840
E  16200  4608.0  190080
'''

# 12. 컬럼을 축으로 곱/누적곱연산 구하기
x = df.prod(axis=1)
print(x)
'''
A     640.0
B     528.0
C     108.0
D     360.0
E    1080.0
dtype: float64
'''

x = df.cumprod(axis=1)
print(x)
'''
   col1  col2    col3
A   4.0  64.0   640.0
B   6.0  48.0   528.0
C   9.0   NaN   108.0
D   5.0  30.0   360.0
E  15.0  90.0  1080.0
'''

# 13. 행/컬럼을 축으로 분산 구하기
x = df.var(axis=0)
print(x)
'''
col1    19.700000
col2    22.666667
col3     0.800000
dtype: float64
'''

x = df.var(axis=1)
print(x)
'''
A    36.000000
B     6.333333
C     4.500000
D    14.333333
E    21.000000
dtype: float64
'''

# 13. 행/컬럼을 축으로 표준편차 구하기
x = df.std(axis=0)
print(x)
'''
col1    4.438468
col2    4.760952
col3    0.894427
dtype: float64
'''

x = df.std(axis=1)
print(x)
'''
A    6.000000
B    2.516611
C    2.121320
D    3.785939
E    4.582576
dtype: float64
'''

# 14. 행/컬럼을 축으로 갯수 구하기(기본적으로 null 제외)
x = df.count(axis=0)
print(x)
'''
col1    5
col2    4
col3    5
dtype: int64
'''

x = df.count(axis=1)
print(x)
'''
A    3
B    3
C    2
D    3
E    3
dtype: int64
'''

# 15. 통합 통계 데이터
x = df.describe()
print(x)
'''
            col1       col2       col3
count   5.000000   4.000000   5.000000
mean    7.800000   9.000000  11.400000
std     4.438468   4.760952   0.894427
min     4.000000   6.000000  10.000000
25%     5.000000   6.000000  11.000000
50%     6.000000   7.000000  12.000000
75%     9.000000  10.000000  12.000000
max    15.000000  16.000000  12.000000
'''

# 16. DataFrame 정보
x = df.info()
print(x)
'''
<class 'pandas.core.frame.DataFrame'>
Index: 5 entries, A to E
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   col1    5 non-null      int64
 1   col2    4 non-null      float64
 2   col3    5 non-null      int64
dtypes: float64(1), int64(2)
memory usage: 160.0+ bytes
None
'''