import numpy as np
import pandas as pd

'''
    Series의 문자열 처리
    
    1. series.str.함수
    
    * 문자열 관련 함수
    1) python
        - 문자열.함수
    2) numpy
        - np.char.함수
        
    3) pandas
        - series.str.함수 
        
'''
info={"name":["Hello","Happy","Cat"],
      "age":[18,31, 33],
      "birthday":['1920/09/28','1910/03/26','2020/03/26']}
df = pd.DataFrame(info)
print(df)
'''
    name  age    birthday
0  Hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''

# 1. series.str.replace(old, new) => old -> new
df['name'] = df['name'].str.replace('Hello','hello')
print(df)
'''
    name  age    birthday
0  hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''

# 2. 인덱싱 및 slice
df['name'] = df['name'].str[:]
print(df)
'''
    name  age    birthday
0  hello   18  1920/09/28
1  Happy   31  1910/03/26
2    Cat   33  2020/03/26
'''

df['name'] = df['name'].str[::-1]
print(df)
'''
    name  age    birthday
0  olleh   18  1920/09/28
1  yppaH   31  1910/03/26
2    taC   33  2020/03/26
'''

df['name'] = df['name'].str[2:]
print(df)
'''
  name  age    birthday
0  leh   18  1920/09/28
1  paH   31  1910/03/26
2    C   33  2020/03/26
'''

df['name2'] = df['name'].str[0]
print(df)
'''
  name  age    birthday name2
0  leh   18  1920/09/28     l
1  paH   31  1910/03/26     p
2    C   33  2020/03/26     C
'''

# 3. upper, lower
df['name3'] = df['name'].str.upper()
print(df)
'''
  name  age    birthday name2 name3
0  leh   18  1920/09/28     l   LEH
1  paH   31  1910/03/26     p   PAH
2    C   33  2020/03/26     C     C
'''

df['name3'] = df['name'].str.lower()
print(df)
'''
  name  age    birthday name2 name3
0  leh   18  1920/09/28     l   leh
1  paH   31  1910/03/26     p   pah
2    C   33  2020/03/26     C     c
'''

# 4. contains
df['name4'] = df['name'].str.contains('a') # 'a'포함 하니?
print(df)
'''
  name  age    birthday name2 name3  name4
0  leh   18  1920/09/28     l   leh  False
1  paH   31  1910/03/26     p   pah   True
2    C   33  2020/03/26     C     c  False
'''

df['name5'] = df['name'].str.contains('a|e') # 'a' 또는 'e' 포함 하니?
print(df)
'''
  name  age    birthday name2 name3  name4  name5
0  leh   18  1920/09/28     l   leh  False   True
1  paH   31  1910/03/26     p   pah   True   True
2    C   33  2020/03/26     C     c  False  False
'''