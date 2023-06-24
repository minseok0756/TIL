# Python

---

## [실습](./python/)

---

## 리뷰

### 정규표현식
- 문자열에 패턴을 적용하여 일치여부를 판단
    - re.search(pattern, string, flags) - string에서 pattern을 search
        - flags=re.I - 대소문자를 구별하지 않고 search
    - re.compile(pattern) - pattern을 정규식 객체로 compile(패턴을 저장시킨다고 이해)
    - re.sub(pattern, rep, string) - string에서 pattern을 찾아 rep로 치환
    - re.findall(pattern, string) - pattern과 일치하는 문자열을 찾아 list로 반환
    - \A, ^ - pattern을 string의 시작부분에서 찾음
    - \Z, $ - pattern을 string의 끝부분에서 찾음
    - pattern1|pattern2 - pattern1 또는 pattern2
    - .x - x앞에 한글자가 있음을 의미
    - x+ - x가 한번이상 반복됨을 의미
    - x? - x가 없거나 한번나옴
    - x* - x가 없거나 여러번(한번포함)나올 수 있음
    - x{n,m} - x가 n번이상 m번이하로 나옴
    - [abc] - a 또는 b 또는 c       
    [a-z] - 알파벳 소문자 하나      
    [A-Z] - 알파벳 대문자 하나      
    [0-9] - 숫자 하나       
    [가-힣] - 한글 하나      
    [a-zA-Z0-9] - 알파벳 대/소, 숫자중 하나
    - [^] - 부정을 의미     
    대괄호 없는 ^ - pattern을 string의 시작부분에서 찾음
    - escape문자
        - \d - [0-9]와 동일       
        \D - [^0-9]와 동일        
        \s - whitespace문자(공백문자 - \n, \t등)와 일치       
        \S - whitespace문자가 아닌 문자와 일치       
        \w - [a-zA-Z0-9가-힣_]와  동일        
        \W - [^a-zA-Z0-9가-힣_]와  동일       
        \. - . 문자와 동일        
        \* - * 문자와 동일        
        \+ - + 문자와 동일        
        \? - ? 문자와 동일        
        \$ - $ 문자와 동일

### 오라클DB 연동
- ```python
    connect변수 = cx.Oracle.connect() # oracle 연결

    with connect변수.cursor() as 변수명:
        변수명.execute("SQL query")

        # SQL query에 변수가 들어가는 경우
        변수명.execute("SQL query", 변수1=값1, 변수2=값2, ...)

        # 여러 변수가 묶여서 여러번 들어가는 경우
        변수명.execute("(:1, :2, :3, ...)", [(값1, 값2, 값3, ...), (다른값1, 다른값2, 다른값3, ...), ...])

        변수 = cur.fetchone() # 단일 레코드 결과 저장
        변수 = cur.fetchall() # 다중 레코드 결과 저장, list로 반환

        con.commit() # DML query인 경우
  ```