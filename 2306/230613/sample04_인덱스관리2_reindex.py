import numpy as np
import pandas as pd

####################################################
#### 2. 인덱스 관리

'''
    인덱스(index) 관리

    - df.reindex(index=재배치배열)
    ==> 기존 인덱스 재배치
    
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

# 2. 인덱스 재배치
new_df = df.reindex(index=list('ABCDE'))
print(new_df)
'''
   date   City  Temperature
A  2021  Seoul           32
B  2023  Seoul           34
C  2012  Seoul           32
D  2024  Seoul           53
E  2022  Seoul           34
인덱스가 A B C D E로 재배치됨
'''