# ML/DL - pandas

Series 추출
- 문자형 인덱스인 경우 - 문자와 위치모두 인덱싱, fancy, 슬라이싱 사용 가능
    - s['문자'], s[['문자', ...]], s['문자':'문자']
    - s[위치], s[[위치, ...]], s[위치:위치]
- 정수형 인덱스인 경우 - 정수는 인덱싱과 fancy, 위치는 슬라이싱 사용 가능
    - s[정수], s[[정수, ...]]
    - s[위치:위치]

<br>

DataFrame 추출
1. 열만 추출 - 인덱싱, fancy
    - 위치 인덱스 사용 불가
    - 문자형 인덱스인 경우
        - df['컬럼명'] : Series반환 / df[['컬럼명', ...]] : DataFrame 반환
    - 정수형 인덱스인 경우
        - df[정수] / df[[정수, 정수]]
2. 행만 추출  - 슬라이싱, DataFrame 반환
    - 위치 인덱스 사용 가능
    - 문자형 인덱스인 경우
        - df['인덱스명':'인덱스명'] / df[위치:위치]
    - 정수형 인덱스인 경우
        - df[위치:위치]
3. 데이터 추출 
    - 첫 추출의 리턴타입이 Series
        - df['컬렴명'][Series 추출]
    - 첫 추출의 리턴타입이 DataFrame
        - df[[컬럼명, ...]][DataFrame 추츨]
        - df[컬럼명:컬럼명][DataFrame 추출]

<br>

df.loc/iloc 리턴타입
- df.loc/iloc[행, 열]
    - 행 - 인덱싱, fancy, 슬라이싱
    - 열 - 인덱싱, fancy, 슬라이싱
    - 총 9가지 경우의 수
    - 행 또는 열에 인덱싱이 하나라도 있으면 결과는 Series. 이외에는 모두 DataFrame
    - 다음은 결과는 같지만 리턴타입이 다른 경우이다.
        - df.loc['행', :] - Series 리턴
        - df.loc[['행'], :] -  DataFrame 리턴
        - df.loc['행':'행', :] -  DataFrame 리턴(두 행은 같은 행을 의미)

---

[실습](http://localhost:8888/tree/pandas_0711)