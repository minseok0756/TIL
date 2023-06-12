## Pandas

- pandas에서 테이블 구조를 DataFrame, 행과 열 단위을 Series라고 한다.
- 행과 열에 모두 인덱스가 있다.
    - (행)인덱스는 항상 출력되고 변경가능하다.  
    기본값 0,1,2,...  
    A,B,C,...등으로 변경할 수 있다.
    - (열)인덱스는 출력되지 않는다.
- 여러 DataFrame을 만들수 있고 병합(SQL join)할 수 있다.

## 집중할 부분
1. 데이터 프레임 생성 방법
    - ***파일에서 읽어오기***
    - dict 이용
    - 중첩리스트 이용
    - series이용
2. 색인
    - loc[] 이용
    - iloc[] 이용
3. 분할 합병 등
4. 그룹핑
    - group by
5. 병합

## [실습](./pandas/sample01_Dataframe_생성.py)

## 정리

### DataFrame 생성 방법
- dict 이용
- 중첩리스트 이용
- Series 이용