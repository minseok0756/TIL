# Matplotlib

- 시각화 - 외우지 말자 -> 홈페이지 샘플소스를 복사, 수정하여 사용
    - matplotlib 라이브러리 - 복잡함
    - seaborn 라이브러리 - matplotlib이 복잡하여 만들어짐 -> 덜복잡함 + 많은 기능
    - pandas - 내장 라이브러리

## [실습](https://www.kaggle.com/minseok0756/code?userId=15542269&sortBy=dateRun&tab=profile)

## 리뷰

### 기본 순서
1. (생략가능) 도화지 생성
    - plt.figure()
2. (생략가능) 붓 생성
    - plt.axes()
3. 그래프 그리기
    - plt.그래프()
4. 그래프 보이기
    - plt.show()

### 다중 그래프(여러 도화지에 그리기)
- fig, axs = plt.subplots(행,열) -> type(axd) - numpy.ndarray
    - ndarray색인 방식으로 도화지 선택
- figure.add_subplot(행,열, n)
    - n=1,2,3,4,...로 도화지 선택

### 모든 그래프 공통
- 축 라벨 지정
    - plt.xlabel() / plt.ylabel()
- 축 범위 지정
    - plt.axis([xmin, xmax, ymin, ymax])
- 축 눈금 지정
    - plt.xticks() / plt.yticks()
- 축 눈금에 라벨 지정
    - plt.xticks/yticks([눈금], labels=[라벨])
    - plt.xticks/yticks([눈금], (라벨))
- 그리드 설정
    - plt.grid()
- 제목 설정
    - plt.title()
- 그래프에 text 추가
    - plt.text(x위치, y위치, msg)

### 선 그래프
- 선 그래프 그리기
    - plt.plot()
        - 선 색상 - color='',
        - marker - marker='',
        - 선 스타일 - linestyle=''
- 여러 선 그래프 한번에 그리기
    - plt.plot()    
    plt.plot()  
    ...     
    ***plt.legend(['', '', ...])***
    - plt.plot(..., label='')   
    plt.plot(..., label='')     
    ...     
    ***plt.legend()***

### 막대 그래프
- 범주형 데이터
- 막대 그래프 그리기 / 가로로 그리기
    - plt.bar() / plt.barh()
        - 막대 넓이 - width=
        - 막대 색상 - color=''
        - 막대 테두리 색상 - edgecolor=''
        - 막대 투명도 - alpha=
        - 테두리 선 스타일 - linestyle=''
        - 눈금라벨기준 막대 위치 - align=''
- 쌓아서 그리기
    - plt.bar()     
    plt.bar(..., bottom=)       
    plt.bar(..., bottom=)

### 산점도
- 산점도 그리기
    - plt.scatter()
        - 점 면적 크기 - s=
        - 점 색상 - c=
        - 점 투명도 - alpha=

### 파이차트
- 파이차트 그리기
    - plt.pie(ratio, )
        - ratio에 대응되는 라벨 - label=[]
        - 부채꼴에 표시될 숫자 형식 - autopct=''
        - 그래프가 그려지기 시작하는 지점의 각도 - startangle=
        - 그래프가 그려지는 방향 - counterclock=
        - 부채꼴이 중심에서 떨어져 나가는 정도 - explode=
        - 그림자 - shadow=
        - 부채꼴 색상 - color=''

### 히스토그램
- 히스토그램 그리기
    - plt.hist()
        - 계급의 수 - bins=

### 박스 플롯
- box plot 그리기
    - plt.boxplot()
        - 데이터셋당 라벨 지정 - labels=[]
- 한꺼번에 여러가지 그리기
    - plt.boxplot([데이터셋, ...], labels=['라벨', ...])
    - plt.boxplot(DataFrame, labels=DataFrame.columns))

### 파일 저장
- 변수 = plt.gcf()      
변수.savefig('파일명')