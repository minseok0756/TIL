import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
'''
[[1 2 3]
 [4 5 6]]
'''
print("색인1:", arr[..., 0]) # [1 4] -> 값만 뽑는다
print("색인2:", arr[..., [0]])
# [[1]
#  [4]] -> arr의 shape을 유지하며 뽑는다

xxx = np.insert(arr, 0,  [[100],[200]], axis=1)
# [1, 4]
print(xxx)
'''
[[100 200   1   2   3]
 [100 200   4   5   6]]
'''
xxx = np.insert(arr, [0], [[100],[200]], axis=1)
print(xxx)
'''
[[100   1   2   3]
 [200   4   5   6]]
'''

'''
총정리
가. insert(arr, idx, value, axis) 위의 예시에 따라 axis는 1이라고 하자
- 1. 먼저 arr[..., idx]를 확인한다. 예시에 따라 [1, 4]라고 하자
- 2. 결론적으로 [a, b]에서 a자리 값은 인덱스 1에 b자리 값은 인덱스 4에 insert 된다.
xxx = np.insert(arr, 0, [100,200], axis=1)
print(xxx)
[[100   1   2   3]
 [200   4   5   6]]

xxx = np.insert(arr, 0, [[100,200],[300,400]], axis=1)
print(xxx)
[[100 300   1   2   3]
 [200 400   4   5   6]]
 
xxx = np.insert(arr, 0, [[100,200]], axis=1)
print(xxx)
[[100   1   2   3]
 [200   4   5   6]]

xxx = np.insert(arr, 0, [[100],[200]], axis=1)
print(xxx)
[[100 200   1   2   3]
 [100 200   4   5   6]]
- 바로 위 예에서 [100], [200]에는 b자리에 insert할 값이 없다.
- 하지만 결과로 보아 브로드캐스팅 된다고 볼 수 있다. 
- 모든 예를 확인한 결과 중첩리스트는 여러값을 저장시키는 용도로 사용된 것이라고 할 수 있다.

나. insert(arr, [idx], value, axis) 위의 예시에 따라 axis는 1이라고 하자
-1. 먼저 [idx]의 경우 arr의 shape을 유지시킨채로 색인함을 기억하자.
-2. 색인한 shape대로 insert한다.
xxx = np.insert(arr, [0], [[100],[200]], axis=1)
print(xxx)
[[100   1   2   3]
 [200   4   5   6]]

xxx = np.insert(arr, [0], [[100,300],[200,400]], axis=1)
print(xxx)
[[100 300   1   2   3]
 [200 400   4   5   6]]
 
xxx = np.insert(arr, [0], [[100,200]], axis=1)
print(xxx)
[[100 200   1   2   3]
 [100 200   4   5   6]]
 
xxx = np.insert(arr, [0], [100,200], axis=1)
print(xxx)
[[100 200   1   2   3]
 [100 200   4   5   6]]
- 위 두 예제는 색인의 size와 insert하는 값의 size가 맞지않다
- 결과로 보아 브로드캐스팅 된다고 볼 수 있다.
'''