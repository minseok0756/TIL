import numpy as np
import pandas as pd

# print(dir(pd.Series.str))
'''
[
'__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_doc_args', '_freeze', '_get_series_list', '_validate', '_wrap_result', 

'capitalize', 'casefold', 'cat', 'center', 'contains', 'count', 'decode', 'encode', 'endswith', 'extract', 'extractall', 'find', 'findall', 'fullmatch', 'get', 'get_dummies', 'index', 'isalnum', 
'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 'isupper', 'join', 'len', 'ljust', 'lower', 'lstrip', 'match', 'normalize', 'pad', 'partition', 'removeprefix', 
'removesuffix', 'repeat', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'slice', 'slice_replace', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
'wrap', 'zfill']
'''

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

# 실습 : name컬럼에서 a가 포함된 값 출력
print(df['name'][df['name'].str.contains('a')])
'''
1    paH
Name: name, dtype: object
'''

# 4. startswith, endswith
df['name6'] = df['name'].str.startswith('H')
print(df)
'''
  name  age    birthday name2 name3  name4  name5  name6
0  leh   18  1920/09/28     l   leh  False   True  False
1  paH   31  1910/03/26     p   pah   True   True  False
2    C   33  2020/03/26     C     c  False  False  False
'''

# 5. islower, isupper
df['name7'] = df['name'].str.islower()
print(df)
'''
  name  age    birthday name2 name3  name4  name5  name6  name7
0  leh   18  1920/09/28     l   leh  False   True  False   True
1  paH   31  1910/03/26     p   pah   True   True  False  False
2    C   33  2020/03/26     C     c  False  False  False  False
'''

# 6. get_dummies -> one-hot 인코딩
'''
명목형 데이터 Cat Dog Bird를 분석에 사용하려고 한다.
하지만 머신러닝, 딥러닝은 수치에 최적화되어있어 영문자를 숫자로 바꿔줘야한다.
단순히 0, 1, 2로 바꿨을 때 0, 1, 2도 명목형 데이터로 다뤄지길 기대한다.
하지만 머신러닝/ 딥러닝은 수치로 생각한다. 따라서 크기 비교를 하고 데이터마다 가중치가 생긴다. -> 좋지 않음

따라서 특정 방법으로 바꿔야 한다. -> one-hot 인코딩
해당 명목형 자료만 1 나머지는 0으로 한다. 
모든 자료의 값이 1로 같아서 가중치가 생기지 않는다.
cat dog bird
 1   0   0
 0   1   0
 0   0   1 
 
 one-hot 인코딩 기능을 갖는 함수가 get_dummies()이다.
'''
pets = pd.Series(['Cat','Dog','Bird'])
print(pets.str.get_dummies())
'''
   Bird  Cat  Dog
0     0    1    0
1     0    0    1
2     1    0    0
'''