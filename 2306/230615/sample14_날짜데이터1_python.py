import numpy as np
import pandas as pd

'''
   python 날짜 데이터 함수

'''

from datetime import datetime

print("1. 현재날짜:", datetime.now()) #2023-06-05 16:10:28.236017
print("1. 현재날짜:", datetime.today()) #2023-06-05 16:10:28.237015

print("2. 년도:", datetime.today().year)
print("2. 월:", datetime.today().month)
print("2. 일:", datetime.today().day)
print("2. 시간:", datetime.today().hour)
print("2. 분:", datetime.today().minute)
print("2. 초:", datetime.today().second)

# 특정날짜 생성
new_date = datetime(2022,5,19) #  datatime 생성
new_date = datetime(year=2022, month=5, day=19) #  datatime 생성
new_date = datetime(year=2022, month=5, day=19, hour=12, minute=20) #  datatime 생성
print(new_date)

#문자열 --> 날짜로 변경
#  datetime.strptime('문자열', '%Y-%m-%d %H:%M:%S')
s = "2022년12월13일 12:24:13"
s_date = datetime.strptime(s, '%Y년%m월%d일 %H:%M:%S')
print(s, s_date, type(s_date)) #<class 'datetime.datetime'>

# 날짜 --> 문자열로 변경
#  날짜타입변수.strftime('포맷')
s = s_date.strftime('%Y년%m월%d일 %H:%M:%S')
print(s, type(s)) #<class 'str'>