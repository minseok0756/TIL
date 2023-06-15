import numpy as np
import pandas as pd

###########################################
### 4.  df.groupby 이용
###########################################

'''
    group by
    https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
    
    1. 기본
    - df.groupby('컬럼명')['선택컬럼'].그룹함수
    
    2. apply 함수 또는 agg 또는 aggregate 함수
    - df.groupby('컬럼명')['선택컬럼'].agg(함수명)
    - df.groupby('컬럼명')['선택컬럼'].agg([함수명, 함수명2, ...])
    
    3. 여러 컬럼에 다양한 함수 적용
    - df.groupby('컬럼명').agg({
                                컬럼명1:[그룹함수, 그룹함수],
                                컬럼명2:[그룹함수, 그룹함수]
                                })
                                
'''

department = {"deptno":[10,20,30,40],'dname':['개발','인사','영업','관리'],'loc':['서울','부산','제주','광주']}
employee = {"empno":['A1','A2','A3','A4','A5'],"ename":['홍길동','유관순','안중근','강감찬','이순신'],
            "sal":[1000,1500,2300,3400,4500],"hireday":['2019/01/02','2018/01/02','2017/01/02','2016/01/02','2015/01/02'],
            "deptno":[10,20,10,30,10]}
dept = pd.DataFrame(department)
emp = pd.DataFrame(employee)

print(dept)
'''
   deptno dname loc
0      10    개발  서울
1      20    인사  부산
2      30    영업  제주
3      40    관리  광주
'''

print(emp)
'''
  empno ename   sal     hireday  deptno
0    A1   홍길동  1000  2019/01/02      10
1    A2   유관순  1500  2018/01/02      20
2    A3   안중근  2300  2017/01/02      10
3    A4   강감찬  3400  2016/01/02      30
4    A5   이순신  4500  2015/01/02      10
'''

# 1. 부서별 sal 합, 평균, 최대, 최소, 갯수
xxx = emp.groupby(by='deptno')['sal'].sum()
'''
deptno
10    7800
20    1500
30    3400
Name: sal, dtype: int64
'''

xxx = emp.groupby(by='deptno')['sal'].mean()
'''
deptno
10    2600.0
20    1500.0
30    3400.0
Name: sal, dtype: float64
'''

xxx = emp.groupby(by='deptno')['sal'].max()
'''
deptno
10    4500
20    1500
30    3400
Name: sal, dtype: int64
'''

xxx = emp.groupby(by='deptno')['sal'].min()
'''
deptno
10    1000
20    1500
30    3400
Name: sal, dtype: int64
'''

xxx = emp.groupby(by='deptno')['sal'].count()
print(xxx)
'''
deptno
10    3
20    1
30    1
Name: sal, dtype: int64
'''

print(pd.DataFrame(xxx)) # DataFrame으로 만들기
                         # index라벨이 deptno
'''
        sal
deptno
10        3
20        1
30        1
'''

# 2. apply 또는 agg 함수 적용
def my_mean(v):
    print(v, type(v)) # deptno로 그룹화된 sal값이 n에 전달됨
    '''
    0    1000
    2    2300
    4    4500
    Name: sal, dtype: int64
    1    1500
    Name: sal, dtype: int64
    3    3400
    Name: sal, dtype: int64
    '''
    n = len(v)
    sum = 0
    for k in v:
        sum += k
    return sum/n

xxx = emp.groupby(by='deptno')['sal'].agg(my_mean) # 사용자 정의함수
print(xxx)
'''
deptno
10    2600.0
20    1500.0
30    3400.0
Name: sal, dtype: float64
xxx = emp.groupby(by='deptno')['sal'].mean()과 결과가 동일
'''

xxx = emp.groupby(by='deptno')['sal'].agg(np.mean) # numpy 함수
# xxx = emp.groupby(by='deptno')['sal'].agg(mean) # mean은 python에 없는 함수라서 에러 발생
xxx = emp.groupby(by='deptno')['sal'].agg('mean') # 따옴표를 붙이면 정상적으로 작동한다.
                                                  # import 되어있는 라이브러리에서 찾는건지 모르겠다
                                                  # numpy를 import하지 않아도 정상적으로 작동한다.
                                                  # pandas에서 찾는 건지.. 잘 모르겠음
print(xxx) # 결과 같음

# 3. apply 또는 agg 함수 적용 - 멀티함수 적용
xxx = emp.groupby(by='deptno')['sal'].agg([np.sum, np.mean, np.max, np.size])
xxx = emp.groupby(by='deptno')['sal'].agg(['sum', 'mean', 'max', 'count'])
'''
         sum    mean   max  count
deptno
10      7800  2600.0  4500      3
20      1500  1500.0  1500      1
30      3400  3400.0  3400      1
'''

# xxx = emp.groupby(by='deptno')[['sal', 'ename']].agg(['sum', 'count', 'max'])
'''
         sal                  ename           
         sum count   max        sum count  max
deptno                                        
10      7800     3  4500  홍길동안중근이순신     3  홍길동
20      1500     1  1500        유관순     1  유관순
30      3400     1  3400        강감찬     1  강감찬
'''
print(xxx)

# 4. 여러 컬럼에 다양한 함수 적용
xxx = emp.groupby(by='deptno').agg({
                                    'sal':['sum','max','min'],
                                    'deptno':['count']
                                    })
print(xxx)
'''
         sal             deptno
         sum   max   min  count
deptno
10      7800  4500  1000      3
20      1500  1500  1500      1
30      3400  3400  3400      1
'''

# emp와 dept 병합후에 groupby 적용해보기
new_df = pd.merge(emp, dept, how='inner', on='deptno')
xxx = new_df.groupby('deptno')[['sal','ename']].count()
print(xxx)