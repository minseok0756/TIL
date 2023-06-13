import numpy as np
import pandas as pd

####################################################
#### 2. 인덱스 관리

'''
    인덱스(index) 관리
    0. 인덱스 변경
        df.index=[값, ...]
    
    1. df.set_index(기존컬럼, inplace=True|False)
        df.reset_index(drop=True|False, inplace=True|False)
    
    2. df.reindex(index=재배치하고싶은값)
    ==> 기존 인덱스 재배치
    
    3. ignore_index=True
    ==> df와 df2 연결시 인덱스도 그대로 연결되어 중복된다.
    이 때 인덱스는 빼고 연결하는 방법이다. 자동으로 인덱스가 생성됨
    (인덱스는 색인에 사용되어 중복되면 안되기 때문에 사용하는 방법)
    
'''
df = pd.DataFrame({"date":['2021','2022','2012','2023','2024'],
                   "City": ["Seoul", "Seoul", "Seoul", "Seoul", "Seoul"],
                   "Temperature": [32, 34, 32, 34, 53]
                   }, index=list('AECBD'))
print(df)
'''
   date   City  Temperature
A  2021  Seoul           32
E  2022  Seoul           34
C  2012  Seoul           32
B  2023  Seoul           34
D  2024  Seoul           53
'''

# 3) df병합시 기존 index값이 중복발생 ==> ignore_index=True 로 index값을 재설정
df1 = pd.DataFrame({'a':[12,2]},
                   index=[1,2])
df2 = pd.DataFrame({'a':[120,20]},
                   index=[1,2])

new_df = pd.concat([df1, df2])
print(new_df)
'''
     a
1   12
2    2
1  120
2   20
인덱스까지 그대로 연결됨
'''
new_df = pd.concat([df1, df2], ignore_index=True)
print(new_df)
'''
     a
0   12
1    2
2  120
3   20
인덱스는 무시하고 새로운 인덱스가 설정됨
'''

