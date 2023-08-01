## 함수
def facNumber(num):
    if (num == 1) :
        return 1
    return num * facNumber(num-1)

## 메인
print(facNumber(10))
