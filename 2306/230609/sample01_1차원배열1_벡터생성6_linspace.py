import numpy as np

'''
    np.linspace(start, stop, [num=50, endpoint=True])
    => [start, stop] 구간에서 start와 stop을 포함하여 등간격인 점을 num개 반환
    => 기본 type은 float64, num 값을 지정하지 않으면 기본은 50
    => endpotin의 기본값이 True이므로 기본적으로 stop값이 범위에 포함됨.
       포함시키지 않을려면  endpoint=False 로 지정한다.
       -> endpoint=True인 경우 [start, stop]사이를 n-1등분한다.
       -> endpoint=False인 경우 [start, stop)사이를 n등분한다.
'''
print("1. np.linspace(0, 1, 11)")
# [0, 1]] 사이의 값을 0과 1을 포함하여 11개 생성 -> [0, 1]사이를 10등분 하겠다는 의미
data = np.linspace(0, 1, 11 )
print(data, data.dtype)  # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]   float64
                         # [0, 1] 사이를 10등분하여 각 구간의 길이가 0.1임을 알 수 있다

print("2. np.linspace(0, 0.9, 10)")
# [0, 0.9] 사이의 값을 0과 1을 포함하여 10개 생성 -> [0, 0.9]사이를 9등분 하겠다는 의미
data = np.linspace(0, 0.9, 10) # [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]

data = np.linspace(0, 0.9, 10, endpoint=False)
# [0, 0.9) 사이의 값을 0만을 포함하여 10개 생성 -> [0, 0.9)사이를 10등분 하겠다는 의미
print(data) # [0.   0.09 0.18 0.27 0.36 0.45 0.54 0.63 0.72 0.81]
            # [0, 0.9) 사이를 10등분하여 각 구간의 길이가 0.09임을 알 수 있다.

