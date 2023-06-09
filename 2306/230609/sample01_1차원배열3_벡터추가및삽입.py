import numpy as np

'''
     1. ndarray 추가

      문법:
        arr = np.append(arr, values, axis=None)

      - 추가된 새로운 배열을 반환
      - axis=None 이면 flatten 된후에 추가된다.


     2. ndarray 삽입

       문법:
         arr = np.insert(arr, idx|fancy|slice, value,  axis ).

         - fancy 사용시 value와 shape가 일치해야 된다.
'''
#  1. ndarray 추가
#  np.append(arr,  value,  axis )
arr = np.array([9,8,7,5,4,3])
new_arr = np.append(arr, [1,2,3])
print(arr)       # [9 8 7 5 4 3]
print(new_arr)   # [9 8 7 5 4 3 1 2 3]

'''
np.append에 마우스를 올려놓으면 '-> ndarray' 표현이 있음
                             -> 리턴타입을 의미한다

def fun()[-> 리턴타입] :
    문장
    return 값

리턴값이 리턴타입으로 나온다.
'''
# def fun()->str:
#     return "hello"
#
# def fun2()->int:
#     return 10
#
# def fun3()->None:
#     pass
#
# print(fun(), fun2(), fun3())

#  2. ndarray 삽입
#  np.insert(arr, idx|fancy, value,  axis )

# 가. idx 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, 0, [1,2,3]) # 0번째 위치에 삽입
print(arr)  # [9 8 7 5 4 3]
print(new_arr)  # [1 2 3 9 8 7 5 4 3]

# 나. fancy 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, [0,3,1], [1,2,3])  # 0->1 , 3->2, 1->3 삽입됨(일대일 대응). 따라서 갯수가 일치해야 된다.
print(arr)        #  [9 8 7 5 4 3]
print(new_arr)    #  [1 9 3 8 7 2 5 4 3]

#  다. slice 이용
arr = np.array([9,8,7,5,4,3])
new_arr = np.insert(arr, np.s_[0:2], [1,2]) # 일대일 대응
# new_arr = np.insert(arr, slice(0,2), [1,2]) # np.s_ 대신 slice를 사용해도 된다.
print(arr)  # [9 8 7 5 4 3]
print(new_arr)  # [1 9 2 8 7 5 4 3]