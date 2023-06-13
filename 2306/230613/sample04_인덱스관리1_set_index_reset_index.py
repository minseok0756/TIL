import numpy as np
import pandas as pd

####################################################
#### 2. 인덱스 관리

'''
    인덱스(index) 변경
    - DataFrame의 기존컬럼을 index로 변경
    - inplace=True|False 에 따라서 복사여부 결정
     
    문법:
    - df.set_index(기존컬럼, inplace=True|False)
           
    - df.reset_index( drop=False, inplace=True ) # 기존 index를 컬럼으로 변경하고 새로운 index 생성
    - df.reset_index( drop=True, inplace=True ) # 기존 index를 삭제하고 새로운 index 생성
    
'''
df = pd.DataFrame({"date":['2021','2022'],
                   "City": ["Seoul", "Seoul"],
                   "Temperature": [32, 34]
                   })
print("1. 원본 DataFrame")
print(df)
'''
   date   City  Temperature
0  2021  Seoul           32
1  2022  Seoul           34
'''

# 1) 기존 컬럼을 인덱스로 변경
print("기존 컬럼을 인덱스로 변경")
df.set_index('date', inplace=True)
print(df)
'''
       City  Temperature
date                    
2021  Seoul           32
2022  Seoul           34
'''
print(df.index) # Index(['2021', '2022'], dtype='object', name='date')

# 2) 기존 인덱스를 컬럼으로 변경하고 새로운 인덱스 생성
# df.reset_index(drop=False, inplace=True)
print(df)
'''
   date   City  Temperature
0  2021  Seoul           32
1  2022  Seoul           34
'''

# 3) 기존 인덱스를 삭제하고 새로운 인덱스 생성
df.reset_index(drop=True, inplace=True)
print(df)
'''
    City  Temperature
0  Seoul           32
1  Seoul           34
'''