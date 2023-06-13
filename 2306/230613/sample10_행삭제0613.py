import numpy as np
import pandas as pd

####################################################
#### 6. 행 추가 및 삭제
'''
   DataFrame 행 삭제

   1. new_df = df.drop(index=[인덱스명(라벨), 인덱스명(라벨)])

   2. new_df = df.drop([인덱스명, 인덱스명], axis=0)

'''
df = pd.DataFrame({"이름":['홍길동','이순신','유관순','강감찬'],
                   "국어":[30, 26, 11, 10],
                   "수학":[20, 12, 20, 12]
                 }, index=[1,2,3,4])

print(df)
'''
    이름  국어  수학
1  홍길동  30  20
2  이순신  26  12
3  유관순  11  20
4  강감찬  10  12
'''

df.drop(index=[1,2], inplace=True)
print(df)
'''
    이름  국어  수학
3  유관순  11  20
4  강감찬  10  12

'''

df.drop([3], inplace=True, axis=0)
print(df)
'''
    이름  국어  수학
4  강감찬  10  12
'''
