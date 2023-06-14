import numpy as np
import pandas as pd

## 3. Series의 기본 함수
'''
   1. 값 변경                                  ==>  df[컬럼].replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df[컬럼].rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df[컬럼].any() , df[컬럼].all()
   4. 중복조회 및 제거                           ==>  df[컬럼].duplicated(),  df[컬럼].drop_duplicates()

   5. 임의의 함수 적용 ==> df[컬럼].apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   6. 값이 있으면 True, 아니면 False ==> df[컬럼].isin(집합형)
                                  ==> SQL의 in 연산자와 동일

   7. Count number of distinct elements in specified axis. 
      unique한 값의 종류의 갯수 ==> df[컬럼].nunique(dropna=True) 
                            dropna=False 면 nan 포함해서 갯수 반환

   -------------------------여기부터는 Series만 가지고 있는 함수
   
   8. df['col1'].unique() ==> 유니크 값 반환, Series만 사용 가능   
   
   9. df['col1'].value_counts() ==> 값의 빈도수 반환
   
   10. df['col1'].between(start, end) ==> 범위에 있으면 True, 없으면 False
 
'''
df = pd.DataFrame({"a": [0, 10, 100],
                   "b": [2, 20, 200],
                   "c": [3, 30, 300]},
                  index=list('ABC'))
print("1. DataFrame")
print(df)
'''
     a    b    c
A    0    2    3
B   10   20   30
C  100  200  300
'''
# 1. 값 변경
new_df = df['a'].replace({0:-1, 10:-2})
print(new_df)
'''
A    *-1
B    *-2
C    100
Name: a, dtype: int64
'''

# 2. Series name 변경
x = df['a'].rename('col1')
print(x)
'''
A      0
B     10
C    100
Name: *col1, dtype: int64
'''

# 3. 모든(특정)값의 참 여부
x = df['a'].all() # False
x = df['a'].any() # True
print(x)

# a컬럼값이 모두 10보다 크냐?
x= (df['a']>10).all()
print(x) # False

####################################################################
df = pd.DataFrame({"k1":['one']*3 + ['two']*4,
                  "k2":[1,1,2,3,3,4,4] })
print(df)
'''
    k1  k2
0  one   1
1  one   1
2  one   2
3  two   3
4  two   3
5  two   4
6  two   4
'''

# 4. 중복여부
x = df['k1'].duplicated() # Series내에서 반복된 값이냐?
print(x)
'''
0    False
1     True
2     True
3    False
4     True
5     True
6     True
Name: k1, dtype: bool
'''

# 5. 중복 제거후 반환
x = df['k1'].drop_duplicates()
print(x)
'''
0    one
3    two
Name: k1, dtype: object
'''

x = df['k1'].drop_duplicates(ignore_index=True)
print(x)
'''
0    one
1    two
Name: k1, dtype: object
'''

###################################################################
df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
   국어   수학
0  50  100
1  60   60
2  70  100
3  80  100
4  90   80
'''

# 6. 임의의 함수 적용
x = df['국어'].apply(np.sum)
print(x)
'''
0    50
1    60
2    70
3    80
4    90
Name: 국어, dtype: int32
'''

x = df['국어'].apply(lambda n:n+1) # lambda함수 적용 가능
print(x)
'''
0    51
1    61
2    71
3    81
4    91
Name: 국어, dtype: int64
'''

# 7. df['국어'].isin(집합형) - 중요, SQL in연산자와 비슷
new_df = df['국어'].isin([60,80])
print(new_df)
'''
0    False
1     True
2    False
3     True
4    False
Name: 국어, dtype: bool
'''

##############################################################
df = pd.DataFrame({ "col1" : [1 ,2, 2, None, 1],
                    "col2" : [2, 3, 2, 2, np.nan],
                    "col3" : [ np.nan, 3, 2, 3, 3],
                    "col4" : [ np.nan, np.nan, np.nan, np.nan, np.nan]},
                    index = [1, 2, 3, 4, 5])
print(df)
'''
   col1  col2  col3  col4
1   1.0   2.0   NaN   NaN
2   2.0   3.0   3.0   NaN
3   2.0   2.0   2.0   NaN
4   NaN   2.0   3.0   NaN
5   1.0   NaN   3.0   NaN
'''

# 8. df['col1'].nunique()
x = df['col1'].nunique()
print(x) # 2

x = df['col1'].nunique(dropna=False)
print(x) # 3

# 9. df['col1'].unique() ==> 유니크 값 반환, Series만 사용 가능
x = df['col1'].unique()
print(x) # [ 1.  2. nan]


# 10. df['col2'].value_counts() ==> 값의 빈도수 반환
# 기본적으로 null값은 포함하지 않음
x = df['col2'].value_counts()
print(x)
'''
col2
2.00    3
3.    1
Name: count, dtype: int64
'''

x = df['col2'].value_counts(ascending=True) # ascending 기본값은 False -> 내림차순
print(x)
'''
col2
3.0    1
2.0    3
Name: count, dtype: int64
'''

x = df['col2'].value_counts(ascending=True, dropna=False)
print(x)
'''
col2
3.0    1
NaN    1
2.0    3
Name: count, dtype: int64
'''

###################################################################
df = pd.DataFrame({"국어":[50,60,70,80,90],"수학":[100,60,100,100,80]})
print(df)
'''
   국어   수학
0  50  100
1  60   60
2  70  100
3  80  100
4  90   80
'''

# 11. df['국어'].between(start, end) ==> 범위에 있으면 True, 없으면 False
x = df['국어'].between(70, 100)
print(x)
'''
0    False
1    False
2     True
3     True
4     True
Name: 국어, dtype: bool
'''