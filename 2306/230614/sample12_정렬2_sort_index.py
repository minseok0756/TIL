import numpy as np
import pandas as pd

## 1. 정렬
'''
   DataFrame 정렬

   1. 정렬
      df.sort_values(by=컬럼명, ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
      df.sort_values(by=[컬럼명, 컬럼명2], ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
    ascending : 오름차순 / 내림차순
    na_position="last" : null값을 가장 마지막에 위치
    
   2. 행 라벨(인덱스) 및 컬럼 라벨(컬럼명) 정렬
      new_df = df.sort_index(axis=0|1)

'''
import seaborn as sns

df = sns.load_dataset("mpg")
print("1. DataFrame")
df = df.head(10)
df.index=list('HDAFCBEGIJ')
df[df['name']=='ford torino']=np.nan
print(df, df.shape)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
'''

# 1. 행 라벨 정렬
new_df = df.sort_index(axis=0)
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
'''

new_df = df.sort_index(axis=0, ascending=False)
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
'''

new_df = df.sort_index(axis=0, ascending=False, na_position='first')
print(new_df) # df.sort_index는 index정렬이기 때문에 na_position='first'가 적용되지 않는다.
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
'''

# 2. 컬럼 라벨 정렬
new_df = df.sort_index(axis=1)
print(new_df)
'''
   acceleration  cylinders  ...  origin  weight
H          12.0        8.0  ...     usa  3504.0
D          11.5        8.0  ...     usa  3693.0
A          11.0        8.0  ...     usa  3436.0
F          12.0        8.0  ...     usa  3433.0
C           NaN        NaN  ...     NaN     NaN
B          10.0        8.0  ...     usa  4341.0
E           9.0        8.0  ...     usa  4354.0
G           8.5        8.0  ...     usa  4312.0
I          10.0        8.0  ...     usa  4425.0
J           8.5        8.0  ...     usa  3850.0
'''

new_df = df.sort_index(axis=1, ascending=False)
print(new_df)
'''
   weight origin  ... cylinders  acceleration
H  3504.0    usa  ...       8.0          12.0
D  3693.0    usa  ...       8.0          11.5
A  3436.0    usa  ...       8.0          11.0
F  3433.0    usa  ...       8.0          12.0
C     NaN    NaN  ...       NaN           NaN
B  4341.0    usa  ...       8.0          10.0
E  4354.0    usa  ...       8.0           9.0
G  4312.0    usa  ...       8.0           8.5
I  4425.0    usa  ...       8.0          10.0
J  3850.0    usa  ...       8.0           8.5
'''