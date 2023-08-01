## 함수 선언부


## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)
## 데이터 추가 : 모모가 카톡 1회
katok.append(None) # 1단계 : 빈칸 추가
katok[5] = '모모' # 2단계 : 데이터 입력
print(katok)
## 데이터 삽입 : 미나가 카톡 연속 40회 (미나가 3등)
katok.append(None) # 1단계 : 빈칸 추가
# 2단계 : 3등까지 한칸씩 뒤로
katok[6] = katok[5] # 모모
katok[5] = None
katok[5] = katok[4] # 지효
katok[4] = None
katok[4] = katok[3] # 사나
katok[3] = None
# 3단계 : 3등칸에 미나 입력
katok[3] = '미나'
print(katok)
## 데이터 삭제 : 사나가 카톡 차단(4등 집에 감)
katok[4] = None # 1단계 : 지우기
# 2단계 : 한칸씩 앞으로..... 마지막 친구까지.
katok[4] = katok[5] # 지효
katok[5] = None
katok[5] = katok[6] # 모모
katok[6] = None
# 3단계 : 마지막 칸을 제거
del(katok[6])
print(katok)
