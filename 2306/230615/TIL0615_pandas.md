# Pandas

## [실습](./)

## 리뷰

### 날짜 데이터 함수

>|기능|함수||
>|-|-|-|
>|str->datetime|pd.to_datetime(DataFrame/Series)|***pandas함수***|
>|지정된 범위에서 날짜 반환|pd.date_range()|***pandas함수***|
>|날짜타입의 Series에서 연/월/일/시/분/초 정보보기| Series.dt.정보|***Series함수***|
>|datetime -> str|DataFrame/Series.astype(str)|***DataFrame/Series 함수***|

사용해본 pandas함수(6) : 
DataFrame()/ Series()/ concat()/ to_datetime/ date_range()/ merge()/ read_csv()

### 병합
- SQL join과 유사
    - pd.merge()
        - inner / outer
            - 같은 컬럼명으로 병합
                - 같은 컬럼명이 여러개 - on=['컬','컬']
            - 다른 컬럼명으로 병합
            - 컬럼과 인덱스롤 병합
            - 인덱스와 인덱스를 병합
            - 원하는 컬럼만 병합에 참여시킬 수 있다.
                - df['컬'], df[['컬','컬']]

### Groupby
- SQL group by와 유사
    - df.groupby('기준컬럼')[['조회컬럼', '조회컬럼']].그룹함수
    - df.groupby('기준컬럼')[['조회컬럼', '조회컬럼']].apply(함수)    
    - df.groupby('기준컬럼')[['조회컬럼', '조회컬럼']].agg(함수, 함수, ...) - 각 조회컬럼에 모든함수가 적용됨     
    df.groupby('기준컬럼').agg({'조회컬럼':[함수, 함수, ...], '조회컬럼':[함수, 함수, ...]}) - 각 조회컬럼에 명시된 함수가 적용됨
        - 함수
            1. 함수명
            2. '함수명'
            3. 사용자 정의 함수 - 파라미터에 저장되는 값 : 그룹화된 Series
    
### CSV 파일 읽기
- ***pd***.read_csv()
    - 특정 컬럼을 인덱스로 변경하여 읽기 - index_col=0
    - 컬럼명 변경하여 읽기 - names=[]
    - 특정 컬럼 선택해서 읽기 - usecols=[]
    - 지정한 행갯수만큼 읽기 - nrows=scalar
    - 다른 구분자로 된 파일 읽기 - sep='다른 구분자'
- ***df***.to_csv() - csv파일로 저장




    