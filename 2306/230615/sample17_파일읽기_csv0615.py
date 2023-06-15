import numpy as np
import pandas as pd

###########################################
### 5.  csv 파일
###########################################
'''
    CSV 파일 읽기
    
    df = pd.read_csv(경로)
    
'''
# 1. csv 파일 읽기의 기본
df = pd.read_csv('./data/scientists.csv')
print(df)
'''
                   Name        Born        Died  Age          Occupation
0     Rosaline Franklin  1920-07-25  1958-04-16   37             Chemist
1        William Gosset  1876-06-13  1937-10-16   61        Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
3           Marie Curie  1867-11-07  1934-07-04   66             Chemist
4         Rachel Carson  1907-05-27  1964-04-14   56           Biologist
5             John Snow  1813-03-15  1858-06-16   45           Physician
6           Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
7          Johann Gauss  1777-04-30  1855-02-23   77       Mathematician
'''

# 2. 특정 컬럼을 인덱스로 변경
df = pd.read_csv('./data/scientists.csv', index_col=0)
df = pd.read_csv('./data/scientists.csv', index_col='Name')
print(df)
'''
                            Born        Died  Age          Occupation
Name                                                                 
Rosaline Franklin     1920-07-25  1958-04-16   37             Chemist
William Gosset        1876-06-13  1937-10-16   61        Statistician
Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
Marie Curie           1867-11-07  1934-07-04   66             Chemist
Rachel Carson         1907-05-27  1964-04-14   56           Biologist
John Snow             1813-03-15  1858-06-16   45           Physician
Alan Turing           1912-06-23  1954-06-07   41  Computer Scientist
Johann Gauss          1777-04-30  1855-02-23   77       Mathematician
'''

# 3. 컬럼명 변경
df = pd.read_csv('./data/scientists.csv', header=0, names=['name','born','died','age','occupation'])
# df = pd.read_csv('./data/scientists.csv', names=['name','born','died','age','occupation'])
print(df)
'''
                   name        born        died  age          occupation
0     Rosaline Franklin  1920-07-25  1958-04-16   37             Chemist
1        William Gosset  1876-06-13  1937-10-16   61        Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90               Nurse
3           Marie Curie  1867-11-07  1934-07-04   66             Chemist
4         Rachel Carson  1907-05-27  1964-04-14   56           Biologist
5             John Snow  1813-03-15  1858-06-16   45           Physician
6           Alan Turing  1912-06-23  1954-06-07   41  Computer Scientist
7          Johann Gauss  1777-04-30  1855-02-23   77       Mathematician
'''

# 4. 컬럼 선택 -> 지정된 순서가 아닌 원본 순서로 출력됨
df = pd.read_csv('./data/scientists.csv', usecols=['Name','Age'])
print(df)
'''
                   Name  Age
0     Rosaline Franklin   37
1        William Gosset   61
2  Florence Nightingale   90
3           Marie Curie   66
4         Rachel Carson   56
5             John Snow   45
6           Alan Turing   41
7          Johann Gauss   77
'''

# 5. 지정된 갯수만 보기 -> df.head()와 같은 역할
df = pd.read_csv('./data/scientists.csv', nrows=3)
print(df)
'''
                   Name        Born        Died  Age    Occupation
0     Rosaline Franklin  1920-07-25  1958-04-16   37       Chemist
1        William Gosset  1876-06-13  1937-10-16   61  Statistician
2  Florence Nightingale  1820-05-12  1910-08-13   90         Nurse
'''

# 6. ,가 아닌 임의의 구분자로 되어있는 경우(|연산자 가정)
df = pd.read_csv('./data/piped.csv')
print(df)
'''
              |Date|Open|High|Low|Close|Volume
0  0|7/21/2014|83.46|83.53|81.81|81.93|2359300
1    1|7/18/2014|83.3|83.4|82.52|83.35|4020800
2  2|7/17/2014|84.35|84.63|83.33|83.63|1974000
3  3|7/16/2014|83.77|84.91|83.66|84.91|1755600
4    4|7/15/2014|84.3|84.38|83.2|83.58|1874700
5   5|7/14/2014|83.66|84.64|83.11|84.4|1432100
6  6|7/11/2014|83.55|83.98|82.85|83.35|2001400
7   7|7/10/2014|85.2|85.57|83.36|83.42|2713300
8    8|7/9/2014|84.83|85.79|84.76|85.5|1540700
9   9|7/8/2014|86.29|86.57|84.69|84.69|2164000
'''

df = pd.read_csv('./data/piped.csv', sep='|')
print(df)
'''
           Date   Open   High    Low  Close   Volume
0  0  7/21/2014  83.46  83.53  81.81  81.93  2359300
1  1  7/18/2014  83.30  83.40  82.52  83.35  4020800
2  2  7/17/2014  84.35  84.63  83.33  83.63  1974000
3  3  7/16/2014  83.77  84.91  83.66  84.91  1755600
4  4  7/15/2014  84.30  84.38  83.20  83.58  1874700
5  5  7/14/2014  83.66  84.64  83.11  84.40  1432100
6  6  7/11/2014  83.55  83.98  82.85  83.35  2001400
7  7  7/10/2014  85.20  85.57  83.36  83.42  2713300
8  8   7/9/2014  84.83  85.79  84.76  85.50  1540700
9  9   7/8/2014  86.29  86.57  84.69  84.69  2164000
'''

df = pd.read_csv('./data/piped.csv', sep='|', index_col=0)
print(df)
'''
        Date   Open   High    Low  Close   Volume
                                                 
0  7/21/2014  83.46  83.53  81.81  81.93  2359300
1  7/18/2014  83.30  83.40  82.52  83.35  4020800
2  7/17/2014  84.35  84.63  83.33  83.63  1974000
3  7/16/2014  83.77  84.91  83.66  84.91  1755600
4  7/15/2014  84.30  84.38  83.20  83.58  1874700
5  7/14/2014  83.66  84.64  83.11  84.40  1432100
6  7/11/2014  83.55  83.98  82.85  83.35  2001400
7  7/10/2014  85.20  85.57  83.36  83.42  2713300
8   7/9/2014  84.83  85.79  84.76  85.50  1540700
9   7/8/2014  86.29  86.57  84.69  84.69  2164000
'''

# 7. csv 파일로 저장
df.to_csv('./data/piped_copy.csv') # 구분자가 ,로 저장됨