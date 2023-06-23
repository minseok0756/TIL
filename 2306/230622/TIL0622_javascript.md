# JavaScript

## 객체
객체(클래스 정도로 생각) - 사용하기 위해서 반드시 생성      
속성: property(변수)      
동작: method(함수)      
-변수로 접근 -> 변수명.함수()    
-객체로 접근 -> 클래스명.함수()
- 시스템이 제공하는 객체(내장 객체, 빌트인 객체)
    - 데이터 관련 객체 - 명시적으로 생성
        - 수치 관련 객체: Number
        - 문자 관련 객체: String
        - 날짜 관련 객체: Date
        - 논리 관련 객체: Boolean
        - 배열 관련 객체: Array
    - 브라우저 관련 객체        
    -브라우저를 실행하면 자동 생성        
    ->변수명이 자동으로 객체의 소문자로 지정
    BOM(Browser Object Model)       
        - Window: 창(브라우저 창)
        - Screen: 창의 크기(너비, 높이)
        - Navigator: 브라우저의 정보(크롬인지 엣지인지, 버전 등)
        - History: 브라우저 창에서 <-. ->
        - Location: url
    - 문서(html) 관련 객체 - 브라우저에 html문서를 open할 때 자동 생성      
    DOM(Document Object Model)를 이용해서 node 접근하여 값 변경/수정/삭제/추가
        - Document
- 사용자 정의 객체
    - JSON - 배열도 JSON이지만 여기서는 {key:value}를 의미
    - 클래스

---

### 이벤트
- 이벤트 발생 주체  
    - 사용자 발생
        - 마우스
            - 클릭, 더블 클릭
            - 드래그
            - 마우스오버, 마우스아웃(오버의 반대)
        - 키보드
            - 입력
    - 시스템 발생
        - 웹 브라우저가 html문서를 보고 모든 DOM tree를 만들었을 때 사건을 발생시킴
- 이벤트 소스 - 이벤트가 발생한 곳(태그)
    - 예)       
    ```html
    <button>ok</button>
    <button>cancel</button>
    ```
    - 위 상황에서 사용자가 ok 버튼을 클릭하면 이벤트소스는 ```<button>ok</button>```임
- 이벤트 타입
    - click, mouseover, mouseout, keyup, ...
- 이벤트 핸들러 - 발생된 이벤트타입과 실제 처리하는 함수를 연결
    - 사용형태 - 이벤트소스에 속성으로 `on이벤트타입="함수명()"` 설정
    - 시스템이 발생시킬 경우 - 바디에 속성으로 `onload="함수명()"` 설정
- 이벤트 사용방법
    - DOM Level 0
        - 인라인방식 - 이벤트소스 속성에 `on이벤트타입="함수명()"`
        - 고전방식
    - DOM Level 2
- 이벤트 객체 - 이벤트를 발생시키면 자동으로 생성된 후 이벤트 핸들러가 호출하는 함수에 전달된다.
    - 사용 - 전달받은 함수에서 event변수로 사용
        - event.preventDefault() - 무조건 동작되는 기본동작 방지
        - event.stopPropagation() - 이벤트전파 방지

---

## [실습](./)

---

## 리뷰

### 데이터 객체
- 문자열 객체
    - 생성      
    ```python
    class 클래스명:
        pass
    변수=클래스명()
    ```
    ```js
    var 변수명= new String(문자열)
    var 변수명= "문자열"
    ```
    - property, method확인      
    ```python
    print(dir(str))
    ```
    ```js
    console.dir(String)
    ```
    - ***변수명***.property/method        
        - 문자열 길이- length     
        - 문자열에서 지정한 index에 해당하는 문자 - charAt()     
        - 문자열에서 지정한 문자에 해당하는 index - indexOf()        
        - 문자열 연결 - concat()      
        - 문자열을 대/소문자로 - toUpperCase() / toUpperCase()      
        - 부분열 - substring(start, end) / substr(start, 개수)     
        - 문자열에서 지정한 문자열 치환 - replace()      
        - 양쪽 공백제거 - trim()      
        - 문자열에서 특정구분자를 기준으로 분리하여 배열로 반환 - split()     
        - 특정문자열을 포함하니? - includes()     
        - 특정문자열로 시작/끝나니? - startsWith() / endswith()     
- 수치 객체
    - 생성
    ```js
    var 변수명= new Number(숫자)
    var 변수명= 숫자
    ```
    - property, method확인      
    ```js
    console.dir(Number)
    ```
    - ***Number***.property/method
        - js에서 표현가능한 최대/소값 - MAX_VALUE / MIN_VALUE
        - 숫자형태의 문자열을 정수/실수로 변환 - parseInt() / parseFloat()
        - NaN 이니? - isNaN()
        - 정수니? - isInteger()
    - ***변수명***.property/method
        - 값을 지정된 소수자리까지 반올림하여 문자열로 반환 - toFixed()
- 날짜 객체
    - 생성
    ```js
    var 변수명= new Date([값]);
    ```
    - property, method확인
    ```js
    console.dir(Date)
    ```
    - ***변수명***.property/method
        - 현재 연도/월/일/시/분/초 반환 - getFullYear() / getMonth() / getDate() / getHours() / getMinutes() / getSeconds()
        - 특정 날짜 설정 - setFullYear(값) / setMonth(값) / setDate(값) / setHours(값) / setMinutes(값) / setSeconds(값)
- 논리 객체
    - 생성
    ```js
    var 변수명= new Number(값)
    ```
    - property, method확인
    ```js
    console.dir(Boolean)
    ```
    - ***변수명***.property/method
        - boolean값을 문자열로 - toString()
        - boolean객체값을 기본값으로 - valueOf()
- 배열 객체
    - 생성
    ```js
    var 변수명= new Array(값, 값2, ...);
    var 변수명= [값, 값2, ...];
    ```
    - property, method확인
    ```js
    console.dir(Array)
    ```
    - 조회
        - 변수명[index]
    - for문
    ```js
    for(let 변수명 of 배열){
         문장
    } // 배열의 원소를 변수에 하나씩 대입
    ```
    ```js
    for(let 변수명 in 배열){
         문장
    } // 배열의 index를 변수에 하나씩 대입
    ```
    - ***변수명***.property/method
        - 배열의 원소 갯수 - length
        - 값 추가 - push()
        - 값 변경 - 변수명[index]=값;
        - 값 삭제 - pop()
        - 값 삽입 및 삭제 - splice()
        - 거꾸로 - reverse()
        - 정렬 - sort()
        - 부분 배열() - slice()
        - 특정값의 index - indexOf()
        - 배열의 원소를 구분자를 기준으로 하나의 문자열로 묶음 (문자열 객체의 split과 반대)- join("구분자")

### 브라우저 객체
- Screen, Navigator, Location, History
- Window
    - 전역객체(최상위 객체)
    - property,method에 접근할 때 변수명 생략가능
        - property - screen, navigator, location, history, document
        - method - alert(), prompt(), parseInt(), ...

### 사용자 정의 객체
- JSON
    - 생성
    ```js
    let 변수명 = {key:value, [key값을 저장한 변수명]:value};
    ```
    - 조회
        - 변수명[key], 변수명[key값을 저장한 변수명]
        - 변수명.key

### 함수
- 함수 선언식
- ```js
    function 함수명( [변수, ...] ){
         문장;
         [ return 값 ]
    } - 대괄호는 배열이 아닌 옵션을 의미        
    호출: 함수명();
  ```
- 함수 표현식
- ```js
    var 변수 = function( [변수, ...] ){
                     문장;
                     [ return 값 ]
                }; - 함수명이 없음       
    호출: 변수명();
  ```
- default, rest 파라미터
- ```js
  function 함수명(변수=값, ...변수){
      문장;
  }
  ```
- arrow함수
- ```js
    var 변수명= (n, n2, ...)=>{
        문장;
    }
    호출: 변수명()
  ```
    - 파라미터가 한 개인 경우 괄호를 생략할 수 있다.
    - 실행할 문장이 return 하나인 경우 중괄호를 생략할 수 있다.

### 이벤트
- ```html
    <script>
        function 함수명(){
            문장;
        }
    </script>
    <body onload="함수명()"> <!-- 시스템이 이벤트 발생  -->
        <이벤트소스 on이벤트타입="합수명()"></이벤트소스>
    </body>
  ```
- 이벤트가 발생하면 자동으로 객체 생성 - event
- 무조건 동작되는 기능을 방지 - event.preventDefault()
- 이벤트 전파 방지 - event.stopPropagation()
- 여러 함수를 호출할 수 있다.
- ```html
    <이벤트소스 on이벤트타입="함수명(); 함수명2()" >일반적이지 않음</이벤트소스>
  ```


