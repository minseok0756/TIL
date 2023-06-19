## Web Application Architecture

### Web Application Architecture
- 웹사이트(쿠팡, 네이버, ...) -> 서버(웹 서버)

### 클라이언트
- 사용자
- 웹브라우저(크롬, 엣지, 파이어폭스)

### 웹서버
- Apache, Ngix 대표적임
- 우리는 vsc에 확장팩인 live server를 이용
- 서버에 html(css, javescript)이 저장됨
- 정적 파일(html, css, javascript)만을 담당(처리)
    - 1. 웹서버에 요청(웹브라우저에서 url입력)
        - url포맷 : http://서버IP:port번호/자원
    - 2. a.html검색 - 찾지 못하면 not Found:404 에러코드 반환(코드 200은 성공을 의미)
    - 3. 응답 - 찾은 a.html전달(다운로드)
    - 4. 브라우저가 html을 다운받은 후 (브라우저 메모리에)저장
    - 5. 랜더링(브라우저를 통해 보여줌)       
    -> 저장은 서버에 실행은 클라이언트에서      
    -> js : client-side 프로그래밍


### container 서버
- 동적(python:Django, 자바계열:jsp/servlet, ms계열:c#,ASP,PHP) 파일 처리
- 1. 요청
- 2. 실행 - 요청을 검색(없으면 404에러), 검색해서 있으면 실행
- 3. 결과 - 결과는 html
- 4. 응답
- 5. 랜더링

### WAS(Web Application Server)
- web서버 + container(정적 + 동적)


## html

### Html(Hyper text markup language)
- hyper text : 링크기능
- markup language : `<tag>`로 구성됨

### 태그
- 시작태그, 종료태그(/가 앞에 붙어있음) - 종료태그가 없는 경우도 있음
- 시작태그 몸체(body) 종료태그
    - 몸체 : 값(문자열, 숫자로 적어도 문자열) / 태그-> 중첩된 형태(일반적)
- 시작태그에 속성을 가질 수 있음 `<tag key="value" key="value">`
    - key: 속성명, value: 속성값(무조건 쌍따옴표)
    - 글로벌 속성도 있고 태그에 종속적인 속성도 있음
- 몸체가 없는 태그 - empty tag
    - `<tag></tag>`
    - `<tag/>` - 한꺼번에 쓸 수 있음
- 주석 `<!--주석문-->`

### 기본구조
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Page title</title>
    </head>
<body>
    <h1>This a Heading</h1>
    <p>This is a paragraph</p>
    <p>This is another paragraph</p>
    <a href="daum.net"> 다음 </a>
</body>
</html>
```

### DOM(Document Object Model)
- html문서에 있는 태그에 해당되는 클래스(객체)들이 제공(`<html>`에 해당되는 객체도 있고 `<head>`에 해당되는 객체도 있고)되는데 그 객체를 생성하고 tree로 만드는 구조

### DOM트리(기본구조를 기준으로 작성)
                html    - 태그
            head / body     - 태그
           title / h1    // p   // p   // a     // href     - 태그, 속성(href)
     "page title"/ "h1값"//'p값'//"p값"// "a값" // "a속성값"    - 몸체(값)

### DOM트리용어
- tag, 속성명, 값 - node
    - tag - element node
    - 값 - text node
    - 속성명 - attribute node
- ***선택자(selector)***
    - 최상위 노드 - root node
    - 한 레벨 위 노드 - 부모
    - 한 레벨 아래 노드 - 자식
    - 두 레벨이상 위 - 조상
    - 두 레벨이상 아래 - 자손
    - 부모가 동일한 같은 레벨 - 형제
    - 중요한 이유: css, js를 사용하기 위해서는 태그 또는 속성에 접근해야 하는데 선택자를 통해 접근할 수 있다.

### css
- 스타일 지정
- html에서 3가지 방식으로 사용 가능
    - 인라인 방식(권장하지 않음)
        - 시작태그안에 style속성이용
            - `<p style="color:red"> hello</p>`
    - internal 방식
        - 헤드태그안에 자식으로 style태그 사용
        - ```html
          <head>
            <style>
                css 문법
          ```
    - externam 방식
        - 외부파일(*.css)로 작성하고 링크로 html 연결해서 사용
        - ```html
          <head>
            <link ~ href="*.css">
          ```

### js
- internal 방식
    - ```html
      <head>
            <script>
                js 문법
      ```
- external 방식
    - 외부파일(*.js)
        - ```html
          <head>
                <script src="*.js"> </script>
                <script> js 문법</script> -> internal/external을 같이 쓰려면 태그를 새로 열어야함. external 몸체에 사용할 수 없다.
          </head>
          ```

### html tag는 box구조임
box가 가로로 배치 - 인라인 스타일
    - `<span></span>`
box가 세로로 배치 - 블럭 스타일
    - `<p></p>`
    - `<div></div>`
    - `<h1></h1>`

### a.html파일에서 link
- 다른 웹서버로 연결
- 같은 웹서버의 다른 html(b.html)파일로 연결
- a.html내부 특정위치로 연결

### 테이블
- 테이블 `<table></table>`
- 행 `<tr></tr>`
- 컬럼 `<td></td>`
- 컬럼헤더 `<th></th>`     
(2,2) table 만들기
    ```html
    <table>
        <tr>
            <th></th>
            <th></th>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </table>
    ```
- 그룹핑
    - `<thead></thead>`
    - `<tbody></tbody>`
    - `<tfoot></tfoot>`
    - 주의 : tbody를 가장 마지막에 사용해야함
    - js에서 접근을 위해 사용함
    - 사용하기를 권장함
        - 그룹핑하지 않으면 사용하지 못하는 js프레임워크가 있음
- 병합
    - rowspan= 행의 수
    - colspan= 열의 수


### 사용자가 데이터를 입력할 수 있는 태그

- ***반드시 form태그 안에서 사용해야 한다.***
    - action="타겟"
- 한 줄 입력 태그
- 여러 줄 입력 태그
- 하나만 선택(라디오 버튼)
- 여러 개 선택(체크 박스)
- 누르면 선택할 수 있는 종류가 나오는 태그
- 파일 선택
- ***서브밋 버튼*** - 서버에 제출
    - `<input type="submit">`


### query string

```html
<form action="target.html">
		이름1 <input type="text" name="username">
        <input type="submit" value="전송">
</form>
```
- submit할 때 form tag내에서 name값('username')이 key, 사용자의 입력값이 value로 전달됨      
-> query string이라고 부른다.   
-> key=value로 URL에 표시된다.  
-> 타겟파일과 query string의 구분자는 '?' - 타겟파일 ? key=value    
-> 다중 query string인 경우 - 타겟파일? key=value & key=value   
-> 나중에 동적 파일에서 key를 이용해서 value를 얻는다.  

- query string이 서버에 전달될 때 2가지 방법이 있다. - method="get|post"
    - get: query string이 URL에 보여서 전달됨 -> 보안 취약
    - post: query string이 숨겨져서 전달됨 -> 보안이 엄격

### tag속성
`
<tag key="value" key="value">
`
- key : 속성명
        - 속석명이 tag에 종속적 -> 예) href는 a tag에서만 사용할 수 있음
- value : 속성값

### ***커스텀속성***
- 개발자가 필요해서 임의의 속성명을 지정할 수 있다.
    - 규칙: data-속성명="value"
    - 하나의 태그에 여러개를 사용할 수 있다.


***경로***
- 파일(이미지, js, css) 또는 target(html 또는 동적파일)을 지정할 때 사용
    - `<a href="경로">`
    - `<form action="경로">`
    - `<script src="경로">`
    - `<link href="경로">`
    - `<img src="경로">`
- 종류 2가지
    - 상대 경로
        - /로 시작하지 않음
        - 현재 파일이 있는 디렉토리가 기준
        - . : 현재 디렉토리
        - ..: 부모 디렉토리
    - 절대 경로
        - /로 시작
        - http://127.0.0.1:5500 ->이후부터 지정

## [실습](./)

## 리뷰

### head tag
- title
    - 웹 페이지 제목 지정
    - ```html
        <title>제목</title>
      ```

- base
    - 파일에서 디폴트경로를 지정
    - ```html
        <base href="경로" target="_blank"> 
      ```

- link
    - 외부파일경로 지정
    - ```html
        <link rel="" href="경로">
      ```
            - css external 방식

- style
    - 스타일정보 지정
    - ```html
      <style type="text/css">
        p{
            color:red;	
        }
      </style>
      ```
        - css internal 방식

- script
    - 자바스크립트 명시
    - ```html
        <script>
            console.log("Hello World");
            console.log( "<h1>Hello World</h1>"); 
        </script>
      ```
        - js internal 방식
    - ```html
        <script src="경로"></script>
      ```
        - js external 방식

- header
    - ```html
        <h1></h1>
        <h2></h2>
        <h3></h3>
        <h4></h4>
        <h5></h5>
        <h6></h6>
      ```
- hr
    - 수평선 생성
    - ```html
        <hr size="세로길이" width="가로길이" noshade="noshade" />
      ```

### body tag
- p
    - 문단 지정
    - ```html
        <p>
	    첫 번째 문단입니다.
        </p>
      ```

- br
    - 개행
    - ```html
        첫 번째 라인입니다.<br>
	    두 번째 라인입니다.<br>
      ```

- text format
    - ```html
        <b>문자열을 진하게</b>
        <strong>문자열 강조</strong>
        <i>문자열을 이탤릭체로</i>
        HTML5<sub>아래첨자로</sub>
        HTML5<sup>위 첨자로</sup>
        <address>
            서울시 강남구 역삼동 34-21 번지
        </address>
        <del>가운데 줄긋기</del>
        <ins>밑줄</ins>
      ```

- a
    - 서로 다른 웹페이지 또는 하나의 웹 페이지 내부에서 특정 위치로 이동
    - ```html
        <a href="링크" title="대상의 제목이나 설명" target="_blank"></a>
      ```
    - ```html
        <a href="#Java">java 행으로 이동</a>
        <a id="Java">여기서 부터는 자바행</a>
      ```

- table
    - ```html
        <table border="table두께">
            <caption>테이블 제목</caption>
            <tr>
                <th>1열 제목</th>
                <th>2열 제목</th>
            </tr>
            <tr>
                <td>1행 1열</td>
                <td>1행 2열</td>
            </tr>
            <tr>
                <td>2행 1열</td>
                <td>2행 2열</td>
            </tr>
        </table>
      ```
    - 그룹핑
        - ```html
            <table border="table두께">
                <thead>
                    <tr>
                    <th></th>
                    <th></th>
                    </tr>
                </thead>
                <tfoot><!--tfoot이 tbody보다 먼저-->
                    <tr>
                    <td></td>
                    <td></td>
                    </tr>
                </tfoot>
                <tbody>
                    <tr>
                    <td></td>
                    <td></td>
                    </tr>
                    <tr>
                    <td></td>
                    <td></td>
                    </tr>
                </tbody>
            </table> 
          ```
    - 병합
        - ```html
            <table border='table두께'>
                <tr>
                    <th></th>
                    <th colspan|rowspan="병합수">
                    </th>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
          ```

- 리스트
    - 순서 있는 리스트
        - ```html
            <ol>
                <li></li>
                <li></li>
            </ol>
            <ol start="시작할 번호">
                <li></li>
                <li></li>
            </ol>
          ```
    - 순서 없는 리스트
        - ```html
            <ul type="모양">
                <li>사과
                <li>배
            </ul>
          ```

- semantic
    - header
        - ```html
            <h1>Header</h1>
            <h2>Subtitle</h2>
          ```
    - nav
    - link를 그룹화
        - ```html
            <h3>Nav</h3>
            <a href="">Link 1</a>
            <a href="">Link 2</a>
          ```
    - section
    - 문서의 섹션을 구분, 문서의 내용 기입
        - ```html
            <section>
                문서 내용
            </section>
          ```
    - article
    - 문서를 여러 article요소로 나눔
        - ```html
            <section>
            <article>
                <header>
                    <h1>Article Header</h1>
                </header>
                <p></p>
                <p></p>
                <footer>
                    <h2>Article Footer</h2>
                </footer>
            </article>
            <article>
                <header>
                    <h1>Article Header</h1>
                </header>
                <p></p>
                <footer>
                    <h2>Article Footer</h2>
                </footer>
            </article>
        </section>
          ```
    - aside
    - 문서의 주 내용 외의 내용
        - ```html
            <aside>
            <h3>Aside</h3>
            <p></p>
        </aside>
          ```
    - footer
    - 작성자 정보, 저작권 정보, 또는 관련 문서 링크 등 부가 정보
        - ```html
            <footer>
            <h2>Footer</h2>
            </footer>
          ```

- grouping - span
- inline level, text의 스타일 변경 목적
    - ```html
        <head>
        <style type="text/css">
        #red{
        color: red;
        font-size: 100px;
        }
        </style>
        </head>
        <body>
                <h3></h3>
                <p><span id="red"></span></p>
        </body>
      ```

- form
- 서버에 데이터 전송
    - text
    - ```html
        <form action="동적파일" method="get|post"> 
            <input type="text" name="username" id="username" autofocus required placeholder="이름 입력">
		    <input type="submit" value="버튼이름">
	    </form>
      ```
    - <form action="동적파일" method="get|post"> 
            <input type="text" name="username" id="username" autofocus required placeholder="이름 입력">
		    <input type="submit" value="버튼이름">
	    </form>
    - radio
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="radio" name="제출시key값" value="제출시value값" checked>남<br>
            <input type="radio" name="제출시key값" value="제출시value값">여<br>
            <!-- radio에서 name이 서로 같아야 함 -->
            <input type="submit" value="버튼이름">
        </form> 
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="radio" name="제출시key값" value="제출시value값" checked>남<br>
            <input type="radio" name="제출시key값" value="제출시value값">여<br>
            <input type="submit" value="버튼이름">
        </form> 
    - checkbox
    - ```html
         <form name="myForm" action="동적파일" method="get|post">
            <input type="checkbox" name="제출시key값" value="제출시value값" checked>사과<br>
            <input type="checkbox" name="제출시key값" value="제출시value값">바나나<br>
            <input type="submit" value="전송">
         </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="checkbox" name="제출시key값" value="제출시value값" checked>사과<br>
            <input type="checkbox" name="제출시key값" value="제출시value값">바나나<br>
            <input type="submit" value="전송">
         </form>
    - select
    - ```html
         <form name="myForm" action="동적파일" method="get|post">
            <select name="제출시key값">
                <option value="">선택하시오</option>
                <option value="제출시value값">볼보</option>
                <option value="제출시value값">사브</option>
                <option value="제출시value값">피아트</option>
                <option value="제출시value값" selected>아우디</option>
                <input type="submit" value="전송">
            </select>
         </form> 
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <select name="제출시key값">
                <option value="">선택하시오</option>
                <option value="제출시value값">볼보</option>
                <option value="제출시value값">사브</option>
                <option value="제출시value값">피아트</option>
                <option value="제출시value값" selected>아우디</option>
                <input type="submit" value="전송">
            </select>
         </form> 
    - textarea
    - ```html
         <form name="myForm" action="동적파일" method="get|post">
            <textarea name="제출시key값" rows="행" cols="열">여러 라인 사용 가능
            </textarea>
            <input type="submit" value="전송">
         </form>  
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <textarea name="제출시key값" rows="행" cols="열">여러 라인 사용 가능
            </textarea>
            <input type="submit" value="전송">
         </form>
    - submit reset
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
                <input type="submit" value="전송">
                <input type="reset" value="취소">
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
                <input type="submit" value="전송">
                <input type="reset" value="취소">
           </form>
    - file
    - ```html
        <form name="myForm" action="동적파일" method="post" 
         enctype="multipart/form-data">
            파일선택1:<input type="file" name="theFile"><br>
            파일선택2:<input type="file" name="file" id="theFile" multiple="multiple" accept="image/*" ><br>
            <input type="submit" value="전송">
        </form>
      ```
    - <form name="myForm" action="동적파일" method="post" 
         enctype="multipart/form-data">
            파일선택1:<input type="file" name="theFile"><br>
            파일선택2:<input type="file" name="file" id="theFile" multiple="multiple" accept="image/*" ><br>
            <input type="submit" value="전송">
        </form>
    - number
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="number" name="제출시key값"
                                id="estimated_hours" min="0" max="1000" step="2"> 
            <input type="submit" value="전송">	
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="number" name="제출시key값"
                                id="estimated_hours" min="0" max="1000" step="2"> 
            <input type="submit" value="전송">	
        </form>
    - email
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="email" name="제출시key값" required="required"
                        placeholder="aaa@bbb.com">
            <input type="submit" value="전송">	
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="email" name="제출시key값" required="required"
                        placeholder="aaa@bbb.com">
            <input type="submit" value="전송">	
        </form>
    - range
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="range" name="제출시key값" id="range" min="1" max="50"
                step="2" value="초기값">
            <input type="submit" value="전송">
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="range" name="제출시key값" id="range" min="1" max="50"
                step="2" value="초기값">
            <input type="submit" value="전송">
        </form>
    - date
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="date" name="제출시key값" id="date"> 
            <input type="submit" value="전송">
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="date" name="제출시key값" id="date"> 
            <input type="submit" value="전송">
        </form>
    - search
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="search" name="제출시key값" id="search">
            <input type="submit" value="전송">	
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="search" name="제출시key값" id="search">
            <input type="submit" value="전송">	
        </form>
    - color
    - ```html
        <form name="myForm" action="동적파일" method="get|post">
            <input type="color" name="제출시key값" id="color"> 
            <input type="submit" value="전송">
        </form>
      ```
    - <form name="myForm" action="동적파일" method="get|post">
            <input type="color" name="제출시key값" id="color"> 
            <input type="submit" value="전송">
        </form>
    - hidden
    - ```html
        <form action="target.html">
		    <input type="hidden" name="제출시key값" id="age" value="제출시value값"><br>
		    <input type="submit" value="전송">
	    </form> 
      ```
    - <form action="target.html">
		    <input type="hidden" name="제출시key값" id="age" value="제출시value값"><br>
		    <input type="submit" value="전송">
	    </form> 

- image
- 이미지 처리
    - ```html
        <img src="이미지경로" alt="이미지없을시message" 
            width="200" height="200"><br>
        <img src="이미지경로" alt="이미지없을시message" 
            width="200" height="200"><br>
      ```

- 특수문자
    - ```html
        <p>3&lt;4</p>   <!-- 작다 -->
        <p>30&gt;4</p>  <!-- 크다 -->
        <p>&quot;홍길동&quot;</p>   <!-- 쌍따옴표 -->
        <p>이순신&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;유관순</p>     <!-- 공백 -->
      ```