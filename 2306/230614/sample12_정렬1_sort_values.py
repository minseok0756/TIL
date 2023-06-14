import numpy as np
import pandas as pd

## 1. 정렬
'''
   DataFrame 정렬

   1. 정렬
      df.sort_values(by=컬럼명, ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
      df.sort_values(by=[컬럼명, 컬럼명2], ascending=True, inplace=False, ignore_index=False, kind="quicksort", na_position="last")
    ascending=True : 오름차순
    na_position='last' : null값을 가장 마지막에 위치

'''
import seaborn as sns # df을 빌려오기위해 import했음

df = sns.load_dataset("mpg")
print("1. DataFrame")
df = df.head(10) # df의 위에서부터 10개 행 반환
                 # 기본값은 5
# df = df.tail(8) # df의 아래에서부터 8개 반환
df.index=list('HDAFCBEGIJ') # index변경
df[df['name']=='ford torino']=np.nan # 일부러 NaN값을 만들었음
                                     # 행값을 변경하는 것이기 때문에 df.loc[]를 생각할 수 있다.
                                     # 물론 df.loc[df['name']=='ford torino']=np.nan로도 같은 결과를 갖는다.
                                     # 하지만 조건이 주어진 boolean 색인으로도 생각할 수 있는데
                                     # 결과로 보아 boolean 색인은 df[]로 모두 처리할 수 있다.
                                     # 이러한 결과의 이유는 입력되는 boolean색인의 인덱스 때문인데
                                     # 행을 반환하고자 하는 조건식을 제대로 작성했으면 series의 인덱스는 df의 인덱스라벨과 같고
                                     # 열을 반환하고자 하는 조건식을 제대로 작성했으면 series의 인덱스는 df의 컬럼라벨과 같다.
                                     # 내부적으로 Series의 인덱스와 맞는 쪽으로 색인이된다.
print(df, df.shape) # (398, 9)

# 1. mpg 컬럼 오름차순 정렬
new_df = df.sort_values(by='mpg', ascending=True, inplace=False, na_position='last') # ascending과 inplace는 기본값이라 굳이 적을 필요 없음
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
'''

new_df = df.sort_values(by='mpg', ascending=True, inplace=False, na_position='first')
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
'''

# 2. 다중정렬, mpg, displacement컬럼 내림차순 정렬
new_df = df.sort_values(by=['mpg','displacement'], ascending=False, inplace=False, na_position='last') # ascending과 inplace는 기본값이라 굳이 적을 필요 없음
print(new_df)
'''
    mpg  cylinders  displacement  ...  model_year  origin                       name
A  18.0        8.0         318.0  ...        70.0     usa         plymouth satellite
H  18.0        8.0         307.0  ...        70.0     usa  chevrolet chevelle malibu
F  16.0        8.0         304.0  ...        70.0     usa              amc rebel sst
B  15.0        8.0         429.0  ...        70.0     usa           ford galaxie 500
J  15.0        8.0         390.0  ...        70.0     usa         amc ambassador dpl
D  15.0        8.0         350.0  ...        70.0     usa          buick skylark 320
I  14.0        8.0         455.0  ...        70.0     usa           pontiac catalina
E  14.0        8.0         454.0  ...        70.0     usa           chevrolet impala
G  14.0        8.0         440.0  ...        70.0     usa          plymouth fury iii
C   NaN        NaN           NaN  ...         NaN     NaN                        NaN
'''