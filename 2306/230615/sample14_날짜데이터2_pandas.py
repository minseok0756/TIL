import numpy as np
import pandas as pd

'''
   pandas 날짜 데이터 함수

    1. str --> datetime로 변환
      pd.to_datetime('날짜', format='')

    2. datetime을 지정된 범위에서 반환
      pd.date_range('날짜', '날짜')

    3.  DatetimeProperties 속성 이용한 날짜 정보 구하기
      df['xxx'].dt.year -> df['xxx']이 날짜 데이터일때만 가능

    4. datetime --> str로 변환
      df['xxx'].astype(str)
'''
from datetime import datetime

# 1. str --> datetime로 변환
xxx = pd.to_datetime('2023/6/15')
xxx = pd.to_datetime('2023-6-15')
xxx = pd.to_datetime('2023 6 15')
print(xxx) # 2023-06-15 00:00:00

# xxx = pd.to_datetime('2023:6:15')
# print(xxx) # 에러발생 ':'구분자는 날짜로 인식하지 못한다.

xxx = pd.to_datetime('2023:6:15', format='%Y:%m:%d')
print(xxx) # 2023-06-15 00:00:00

xxx = pd.to_datetime('2023년6월15일 12:24:45', format='%Y년%m월%d일 %H:%M:%S')
print(xxx) # 2023-06-15 12:24:45

# 2. 연산 가능 -> 차이값을 day로 반환
xxx = pd.to_datetime('2023/6/15')
xxx2 = pd.to_datetime('2023/1/15')
print(xxx-xxx2) # 151 days 00:00:00

# 3. datetime을 지정된 범위에서 반환
# 가. start와 end명시
xxx = pd.date_range('2023/1/1', '2023/6/1') # 일단위 -> freq='D' 기본값
print(xxx, type(xxx))
'''
DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
               '2023-01-09', '2023-01-10',
               ...
               '2023-05-23', '2023-05-24', '2023-05-25', '2023-05-26',
               '2023-05-27', '2023-05-28', '2023-05-29', '2023-05-30',
               '2023-05-31', '2023-06-01'],
              dtype='datetime64[ns]', length=152, freq='D')
'''

xxx = pd.date_range('2023/1/1', '2023/6/1', freq='M') # 월단위
print(xxx)
'''
DatetimeIndex(['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30',
               '2023-05-31'],
              dtype='datetime64[ns]', freq='M')
'''

xxx = pd.date_range('2023/1/1', '2023/6/1', freq='2M') # 2개월단위
print(xxx)
'''
DatetimeIndex(['2023-01-31', '2023-03-31', '2023-05-31'],
dtype='datetime64[ns]', freq='2M')
'''

xxx = pd.date_range('2023/1/1', '2030/6/1', freq='Y') # 년단위
print(xxx)
'''
DatetimeIndex(['2023-12-31', '2024-12-31', '2025-12-31', '2026-12-31',
               '2027-12-31', '2028-12-31', '2029-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')
'''

xxx = pd.date_range('2023/1/1', '2030/6/1', freq='2Y') # 2년단위
print(xxx)
'''
DatetimeIndex(['2023-12-31', '2025-12-31', '2027-12-31', '2029-12-31'], 
dtype='datetime64[ns]', freq='2A-DEC')
'''

# 나. start + periods(개수)
xxx = pd.date_range('2023/1/1', periods=5) # 일단위 -> freq='D' 기본값
print(xxx)
'''
DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05'],
              dtype='datetime64[ns]', freq='D')
'''

xxx = pd.date_range('2023/1/1', periods=5, freq='M') # 월단위
print(xxx)
'''
DatetimeIndex(['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30',
               '2023-05-31'],
              dtype='datetime64[ns]', freq='M')
'''

xxx = pd.date_range('2023/1/1', periods=5, freq='Y') # 년단위
print(xxx)
'''
DatetimeIndex(['2023-12-31', '2024-12-31', '2025-12-31', '2026-12-31',
               '2027-12-31'],
              dtype='datetime64[ns]', freq='A-DEC')
'''

# 활용
xxx = pd.date_range('2023/6/1', periods=5)
df = pd.DataFrame({"시작가격":[500,200,50,240,455],
                   '종가':[1500,1200,150,1240,1455]
                   }, index=xxx)
print(df)
'''
            시작가격    종가
2023-06-01   500  1500
2023-06-02   200  1200
2023-06-03    50   150
2023-06-04   240  1240
2023-06-05   455  1455
'''

# 4. series --> datetime
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

born = df['Born']
print(born)
'''
0    1920-07-25
1    1876-06-13
2    1820-05-12
3    1867-11-07
4    1907-05-27
5    1813-03-15
6    1912-06-23
7    1777-04-30
Name: Born, dtype: object -> object는 문자열이라는 의미
날짜데이터이면 datetime64로 나와야한다
'''

print(born+'100') # born이 문자열이라 연산이아닌 연결이된다. -> 따라서 날짜로 바꿔야 연산할 수 있다.
'''
0    1920-07-25100
1    1876-06-13100
2    1820-05-12100
3    1867-11-07100
4    1907-05-27100
5    1813-03-15100
6    1912-06-23100
7    1777-04-30100
Name: Born, dtype: object
'''

born = pd.to_datetime(df['Born'])
print(born)
'''
0   1920-07-25
1   1876-06-13
2   1820-05-12
3   1867-11-07
4   1907-05-27
5   1813-03-15
6   1912-06-23
7   1777-04-30
Name: Born, dtype: datetime64[ns] -> datetime64로 변경
'''

died = pd.to_datetime(df['Died'])
df['생애-일']= died - born
df['생애-년']= died.dt.year - born.dt.year
print(df)
'''
                   Name        Born  ...       생애-일  생애-년
0     Rosaline Franklin  1920-07-25  ... 13779 days    38
1        William Gosset  1876-06-13  ... 22404 days    61
2  Florence Nightingale  1820-05-12  ... 32964 days    90
3           Marie Curie  1867-11-07  ... 24345 days    67
4         Rachel Carson  1907-05-27  ... 20777 days    57
5             John Snow  1813-03-15  ... 16529 days    45
6           Alan Turing  1912-06-23  ... 15324 days    42
7          Johann Gauss  1777-04-30  ... 28422 days    78
'''
# df --> datetime도 가능하지만 여기까지..


# 5. series.dt 속성 -> series의 dtype이 날짜타입이어야한다.
xxx = pd.date_range('2023/1/1', periods=5)
print(xxx)
'''
DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
               '2023-01-05'],
              dtype='datetime64[ns]', freq='D') -> dtype=날짜타입인거 확인
'''

df=pd.DataFrame({"cur_date":xxx})
print(df.info()) # info함수로도 날짜타입 확인가능

# print(dir(df['cur_date'].dt))
'''
['as_unit', 'ceil', 'date', 'day', 'day_name', 'day_of_week', 'day_of_year', 'dayofweek', 'dayofyear', 'days_in_month', 'daysinmonth', 'floor', 'freq', 'hour', 'is_leap_year', 'is_month_end',
'is_month_start', 'is_quarter_end', 'is_quarter_start', 'is_year_end', 'is_year_start', 'isocalendar', 'microsecond', 'minute', 'month', 'month_name', 'nanosecond', 'normalize', 'quarter',
'round', 'second', 'strftime', 'time', 'timetz', 'to_period', 'to_pydatetime', 'tz', 'tz_convert', 'tz_localize', 'unit', 'weekday', 'year']
'''

print("년도:", df['cur_date'].dt.year)
'''
년도: 0    2023
1    2023
2    2023
3    2023
4    2023
Name: cur_date, dtype: int32
'''

print("월:", df['cur_date'].dt.month)
'''
월: 0    1
1    1
2    1
3    1
4    1
Name: cur_date, dtype: int32
'''

print("일:", df['cur_date'].dt.day)
'''
일: 0    1
1    2
2    3
3    4
4    5
Name: cur_date, dtype: int32
'''

# 6. datetime --> str
print(df['cur_date'].astype(str))
'''
0    2023-01-01
1    2023-01-02
2    2023-01-03
3    2023-01-04
4    2023-01-05
Name: cur_date, dtype: object -> dtype이 문자열로 변경
'''
