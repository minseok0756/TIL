# Pandas

[실습](./)

---

## 정리

### DataFrame의 컬럼과 인덱스 변경
- 컬럼명
    - pd.DataFrame(..., columns=[col1, col2, ...])
    - df.columns = [값, 값2, ...]
- 인덱스
    - pd.DataFrame(..., index=[값, 값2, ...])
    - df.index=[값, 값2, ...]

### DataFrame의 속성 정보
- 컬럼
    - df.columns
    - df.keys()
- 인덱스
    - df.index
- 값 
    - df.values
    - df.to_numpy()

### 인덱스 관리
- df.index = [값, ...]
- df.set_index() / df.reset_index()
- df.reindex()
- pd.concat(..., ignore_index=True)

### 색인
- 컬럼 선택
    - 단일 컬럼
        - df['컬럼명']
        - df.컬럼명
    - 다중 컬럼
        - df[['컬럼명', '컬럼명']]
- 행 선택
    - df.loc[] / df.iloc[]
        - 인덱싱, fancy, 슬라이싱, boolean
- 행 및 컬럼 선택
    - df.loc[,] / df.iloc[,]
- 색인을 이용한 값 변경
    - df.loc[,] / df.iloc[,] = 값

### 컬럼 추가
- df['컬럼명'] = []
- df.assign(**n)
- pd.concat([df,df2], axis=1)

### 컬럼 삽입
- df.insert()

### 컬럼 삭제
- 단일 삭제
    - del df['컬럼명']
    - df.pop('컬럼명')
- 다중 삭제
    - df.drop(columns=['컬럼명', ...])
    - df.drop(['컬럼명', ...], axis=1)

### 행 추가
- df.loc[] = []
- pd.concat([df,df2], axis=0, ignore_index=True)

### 행 삭제
- df.drop(index=[인덱스명, ...])
- df.drop([인덱스명, ...], axis=0)