# Pandas

## [실습](./)

## 리뷰

### null 조회/ 삭제/ 값 변경

- null인지 nuull이 아닌지 조회 -> Boolean
    - pandas 함수 / DataFrame 함수
        - isna(),  isnull()
        - notnull()
            - DataFrmae - df / Series - df[] / df[[]]
- null 행/열 삭제
    - df.dropna()
- null 값 변경
    - df.fillna()
        - 컬럼마다 다르게 변경 -> value = {'컬':값, ...}

### 정렬 값/ 인덱스

- 특정 컬럼값을 기준으로 정렬
    - df.sort_values()
        - 다중정렬 -> by=['컬', '컬', ...]
- 인덱스/컬럼 라벨값을 기준으로 정렬
    - df.sort_index()

### 함수

- DataFrame 과 Series가 모두 사용할 수 있는 함수
    - DataFrame - axis 주의 / Series - axis 없음   
>   | 기능| 함수||
>   | -| -|-|
>   | 최대/ 최소/ 합계/ 곱| max()/ min()/ sum()/ prod()||
>   | 누적 최대/ 최소/ 합계/| cummax()/ cummin()/ cumsum()/ cumprod()||
>   | 최대(소)값을 갖는 label| idxmax()/ idxmin()||
>   | 평균/ 중앙값/ 분산/ 표준편차| mean()/ median()/ var()/ std()||
>   | 원소 갯수| count() -> null제외||
>   | 통합 통계/ df,series정보| describe()/ info()||
>   | 특정 컬럼값을 각각 다른 값으로 변경| replace(dict,dict)||
>   | 값 변경| replace(dict)| 색인 = 값|
>   | 라벨 변경| rename()| 속성 = 값|
>   | 모든(특정) 컬럼/행값의 참 여부| all()/ any()||
>   | 행의 중복 여부| duplicated()||
>   | 중복행 제거후 반환| drop_duplicates()||
>   | 임의의 함수 적용| apply()||
>   | 멤버쉽연산자 기능| isin()||
>   | unique한 값의 갯수| nunique()||

- Series만 사용할 수 있는 함수
>   | 기능| 함수||
>   | -| -|-|
>   | unique한 값 자체를 반환| unique()||
>   | 값의 빈도수 반환| value_counts()| count()와 비교|
>   | 범위에 있으면 True| between()||

- 문자열 함수 - Series.str.함수
>   | 기능| 함수|
>   | -| -|
>   |문자열값 변경| replace()|
>   |문자열값 인덱싱/슬라이싱| Series.str[::]|
>   |문자열값 대/소문자로| upper()/ lower()|
>   |특정 문자 포함 여부| contains('a\|b')