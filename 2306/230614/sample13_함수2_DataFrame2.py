import numpy as np
import pandas as pd

## 3. DataFrame의 기본 함수
'''
   1. 값 변경                                  ==>  df.replace()
   2. 컬럼명 및 인덱스명 변경                     ==> df.rename(columns|index)
   3. 모든(특정) 컬럼(행)값의 참/거짓 여부          ==>  df.any() , df.all()
   4. 중복조회 및 제거                           ==>  df.duplicated(),  df.drop_duplicates()

   5. 임의의 함수 적용 ==> df.apply(함수, axis=0|1)
      임의의 함수를 한번에 DataFrame의 행과 열에 적용.

   6. 값이 있으면 True, 아니면 False ==> df.isin(집합형)
                                  ==> SQL의 in 연산자와 동일

   7. Count number of distinct elements in specified axis. 
      unique한 값의 종류의 갯수 ==> df.nunique(dropna=True) 
                            dropna=False 면 nan 포함해서 갯수 반환
                            
      series.unique ==> 값 자체를 반환  
'''
df = pd.DataFrame({ "a" : [0 ,10, 100],
                    "b" : [2, 20, 200],
                    "c" : [3, 30, 300]},
                    index = list('ABC'))

print("1. DataFrame")
print(df)
'''
     a    b    c
A    0    2    3
B   10   20   30
C  100  200  300
'''

# 1. 값 변경
# df.replace({'lavel':old, 'lavel':[old, old], ...}, new) ==> 'lavel'에 있는 old를 new로 변경
# new -> scalar / dict / series 사용 가능
new_df = df.replace({'a':100,'b':2,'c':[30,300]}, -1) # 모두 같은 값으로 변경
'''
    a    b  c
A   0   -1  3
B  10   20 -1
C  -1  200 -1
'''
new_df = df.replace({'a':100,'b':2,'c':[30,300]}, {'a':-1,'b':-2,'c':-3}) # lavel마다 다른 값으로 변경
'''
    a    b  c
A   0   -2  3
B  10   20 -3
C  -1  200 -3
'''
new_df = df.replace({'a':100,'b':2,'c':[30,300]}, df.loc['A']) # Series는 index 주의하기 -> 잘 사용하지 않을 듯
                                                               # -> series와 dict가 연동된다.
'''
    a    b  c
A   0   *2  3
B  10   20 *3
C  *0  200 *3
'''
print(new_df)

# 1-2. df.replace({old:new, old:new}) ==>  old를 new로 변경
new_df = df.replace({20:2000, 30:3000}) # 20이 중복되면 전부 바꿈
print(new_df)
'''
     a     b     c
A    0     2     3
B   10 *2000 *3000
C  100   200   300
'''

# 2. 컬럼명 및 인덱스명 변경
new_df = df.rename(columns={'a':'col1', 'b':'col2'})
new_df = new_df.rename(index={'A':'row1', 'B':'row2'})
print(new_df)
'''
      col1  col2    c
row1     0     2    3
row2    10    20   30
C      100   200  300
'''

# 3. 모든(특정) 컬럼(행)값의 참 여부
x = df.all(axis=0) # 모든 컬럼값이 참이냐?
print(x)
'''
a    False
b     True
c     True
dtype: bool
'''

x = df.all(axis=1) # 모든 행값이 참이냐?
print(x)
'''
A    False
B     True
C     True
dtype: bool
'''

x = df.any(axis=0) # 하나라도 컬럼값이 참이냐?
print(x)
'''
a    True
b    True
c    True
dtype: bool
'''

x = df.any(axis=1) # 하나라도 행값이 참이냐?
print(x)
'''
A    True
B    True
C    True
dtype: bool
'''

##################################################
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

# 4. 행의 중복 여부 확인
x = df.duplicated() # 중복된 행이니?
print(x)
'''
0    False
1     True
2    False
3    False
4     True
5    False
6     True
dtype: bool
정렬과는 연관이 없는지 확인하기############################
'''

# 5. 중복된 행 제거후 반환
new_df = df.drop_duplicates()
'''
    k1  k2
0  one   1
2  one   2
3  two   3
5  two   4
'''
new_df = df.drop_duplicates(ignore_index=True)
'''
    k1  k2
0  one   1
1  one   2
2  two   3
3  two   4
'''
print(new_df)

###########################################################
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

# 6. df에 임의의 함수 적용
x = df.apply(np.sum,axis=0)
print(x)
'''
국어    350
수학    500
dtype: int64
'''
x = df.apply(np.sum,axis=1)
print(x)
'''
0    150
1    160
2    170
3    180
4    190
dtype: int64
'''
x = df.apply(np.mean,axis=1)
print(x)
'''
0    75.0
1    80.0
2    85.0
3    90.0
4    95.0
dtype: float64
'''

# 7. df.isin(집합형) - 중요, SQL in연산자와 비슷
new_df = df.isin([60,80]) # df에서 60 또는 80이 있냐?
print(new_df)
'''
      국어     수학
0  False  False
1   True   True
2  False  False
3   True  False
4  False   True
'''

new_df = df.isin({'수학':[60,80]}) # 수학에서만 60또는 80이 있냐?
print(new_df)
'''
      국어     수학
0  False  False
1  False   True
2  False  False
3  False  False
4  False   True
'''

##################################################################
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

# 8. Count number of distinct elements in specified axis.
#    unique한 값의 종류의 갯수를 반환 - 기본적으로 null 제외
x = df.nunique(axis=0)
print(x)
'''
col1    2  
col2    2 
col3    2
col4    0
dtype: int64
'''
x = df.nunique(axis=1)
print(x)
'''
1    2
2    2
3    1
4    2
5    2
dtype: int64
'''

x = df.nunique(axis=0, dropna=False) # null값 포함
print(x)
'''
col1    3
col2    3
col3    3
col4    1
dtype: int64
'''
x = df.nunique(axis=1, dropna=False) # null값 포함
print(x)
'''
1    3
2    3
3    2
4    3
5    3
dtype: int64
'''