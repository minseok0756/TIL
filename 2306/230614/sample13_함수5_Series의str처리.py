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
# 1. python의 문자열 함수
# print(dir(str))

# 2. numpy의 문자열 함수
# print(dir(np.char))

# 3. pandas의 문자열 함수
print(dir(pd.Series.str))