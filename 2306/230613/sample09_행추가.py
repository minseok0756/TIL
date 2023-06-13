import numpy as np
import pandas as pd

####################################################
#### 6. 행 추가 및 삭제
'''
   DataFrame 행(row) 추가
   
    0. 색인 = 값 -> 이미 있는 인덱스는 수정 / 없는 인덱스는 추가
        df.loc[인덱스] = 리스트
        df.loc[인덱스] = Series * 인덱스 주의(index=[컬럼명에 맞게 작성])
                    -> 리스트, Series만 가능한 것이 아님. (scalar값도 가능)
                    -> 추가될 DataFrame과 크기만 맞출 수 있으면 된다.
                    -> 유연하게 생각하자
        (iloc 사용 불가)
        
    1. 한번에 하나씩 추가 # 현 버전에서는 지원 안됨
                     # 1.3.0이후 버전에서는 지원 안됨
    new_df = df.append(df2, ignore_index=True)

    2. 한번에 여러개 추가
    new_df = pd.concat([df,df2,..], axis=0 , ignore_index=True)

'''
# 1. 한번에 여러개 추가
info={"Name":["유관순","안중근"],"age":[18,31],"birthday":['1920/09/28','1910/03/26']}
df = pd.DataFrame(info)

info2 = {"Name":["홍길동","강감찬"],"age":[22,43],"birthday":['1990/09/28','1980/03/26']}
df2 = pd.DataFrame(info2)

print(df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
'''

print(df2)
'''
  Name  age    birthday
0  홍길동   22  1990/09/28
1  강감찬   43  1980/03/26
'''

new_df = pd.concat([df,df2], axis=0, ignore_index=True) # axis기본값 0
# new_df = pd.concat([df,df2,df2,df2], axis=0, ignore_index=True) # 한꺼번에 여러개 df연결가능

print(new_df)
'''
  Name  age    birthday
0  유관순   18  1920/09/28
1  안중근   31  1910/03/26
2  홍길동   22  1990/09/28
3  강감찬   43  1980/03/26
'''