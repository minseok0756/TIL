# JavaScript

DOM(Document Object Model)
- ***tag마다 객체가 제공된다*** - property, method가 있다
- 객체(element node) 접근 방법        
    - Document 객체 이용 - 웹브라우저에서 html문서를 보면 자동으로 Document객체생성, 변수명은 소문자(document)
        - method를 통해 DOM tree의 특정 node 접근가능
            - id로 접근 - document.getElementById("id값"); -> 1개 반환(id는 하나니까)
            - ***css 선택자로 접근***       
                - document.querySelector("css선택자") -> 1개 반환       
                - document.querySelectorAll() -> n개 반환


Ajax(Asynchronous javasrcipt and xml)       
- Asynchronous: 비동기
    - 동기 방식
        - 상황: 서버에 파일이 있고 데이터를 포함하고 있다.
        1. 브라우저가 서버에 요청
        2. 서버가 파일을 찾고(search) / 브라우저는 응답을 기다려야 함
        3. 파일을 찾으면 브라우저에 전달해줌(응답) - html로 전달
        - 1,2,3 순서대로 작동
            - 작업 순서가 보장됨
        - ***html***로 응답받는다
            - 따라서 브라우저 전체 화면이 바뀜(전체화면 리로딩)
            - 성능이 떨어짐(현재 페이지에서 약간의 변화만 필요한 경우에도 페이지 전체를 리로딩해야함)
        
    - 비동기 방식
        - 상황: 서버에 파일이 있고 데이터를 포함하고 있다.
        1. 브라우저가 서버에 요청
        2. 서버에서 요청에 대해 search / 브라우저는 요청하고 자기 할일함
        3. 브라우저는 자기 할일 함
        4. 브라우저는 자기 할일 함
        5. (search 끝)응답 - Data(Xml, ***JSON***)로 전달 -> 현재 보여지는 화면의 일부분 변경 가능       
        이벤트로 응답했는지를 알 수 있음
        - 성능이 좋음
            - 자기 할일 가능
            - 전체화면 리로딩없이 일부분만 변경 가능
        - 순서가 보장되지 않음

- XMLHttpRequest 객체 이용 - property, method
- http://reqres.in 이용 - 제이슨을 반환해주는 서버가 필요해서 사용
    - http://reqres.in에 들어가서 원하는 탭 누르고 Request에 주소를 클릭하여 url로 사용

---

## [실습](./)

---

## 리뷰

### DOM
- ```html
    <head>
        <script>
            function 함수명(){
                document.getElementById("id")
                document.querySelector("#id|.class")
                document.querySelectorAll("#id|.class")
            }
        </script>
    </head>
    <body>
        <이벤트소스 id|class="id|class" on이벤트타입="함수명()"></이벤트소스>
    </body>
  ```
- .innerText - tag의 Text값을 반환
- .innerHTML - tag의 Text + 자식tag까지 반환
- .속성명 - tag의 속성값 반환
- .value - form tag에서 value값 반환

### template 리터럴
- 문자열 생성
- ```js
    `hello`
  ```
- 구조 유지하며 출력
- ```js
    var n = `<table>
               <tr>
                 <td>A</td>
               </tr>
             </table>`;
  ```
- 변수 삽입 용이
- ```js
    var n = `<table>
               <tr>
                 <td>${변수명}</td>
               </tr>
             </table>`;
  ```

### 객체 분해 할당
- 배열
- ```js
    var [변수, 변수2=값, ...변수3]=[값, 값, 값, ...]
  ```
- JSON
- ```js
    var {변수, 변수2}={변수:값, 변수2:값}
  ```

### Ajax
1. 객체 생성 - new XMLHttpRequest()
2. 응답을 처리하는 함수를 이벤트 핸들러로 등록 - XMLHttpRequest.onreadystatechange = 함수명
3. url정보 및 추가 정보 설정 - XMLHttpRequest.open(method, url)
4. 요청 보내기 - XMLHttpRequest.send()
- XMLHttpRequest.responseText - 서버에 요청하여 응답으로 받은 데이터를 문자열로 반환
- JSON.parse(JSON문자열) - JSON문자열을 js객체(JSON객체)로 변환