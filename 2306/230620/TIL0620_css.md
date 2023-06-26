# [Css](https://www.w3.org/Style/CSS/Overview.en.html)(cascading style sheets)

cascading - 재정의 가능

---

## [실습](./)

---

## 리뷰

### 사용 방식
- inline 방식
- ```html
    <tag style="속성:속성값"></tag>
  ```
- internal 방식
- ```html
    <style>
        선택자 {
            속성:속성값;
            속성:속성값;
            ...
        }
    </style>
  ```
- external 방식
- ```html
    <link rel "stylesheet" type="text/css" href="css파일경로">
    <body>
        <tag id|class="id|class"></tag>
    </body>
  ```

### 선택자(selector)
- DOM트리에서 node를 선택하는 방법
- * - 모든 node 선택
- 태그, 태그, ... - 특정 태그 선택
- #id - 특정 id값을 갖는 태그 선택
- .class - 특정 class값을 갖는 태그 선택
- 태그1 `>` 태그2 - 태그1 자식중 태그2 선택
- 태그1 (공백) 태그2 - 태그1의 (자식까지 포함한)자손 중 태그2 선택
- 태그1 + 태그2 - 태그1의 바로 뒤 형제 태그2 선택
    - 태그2가 바로 뒤 형제가 아닐 경우 적용되지 않음
- 태그1 ~ 태그2 - 태그1의 형제들 태그2 선택
- [속성명] - 속성명을 갖는 태그 모두 선택
- [속성명="값"] - 속성값까지 일치하는 태그 선택
- 태그[속성명] - 속성명을 갖는 특정 태그 선택
- [속성^="값"] - "값"으로 시작하는 속성값을 갖는 태그 선택
- [속성&="값"] - "값"으로 끝나는 속성값을 갖는 태그 선택
- [속성*="값"] - 포함하는 속성값

### [의사코드](https://www.w3schools.com/cssref/css_selectors.php)(psueudo code)
- :link - 방문하지 않은 링크
- :visited - 방문한 링크
- :hover - mouse over한 링크
- :actice - 선택된 링크(마우스로 클릭한 상태)
- :focus - 마우스로 선택된 것
- :first-child - 지정 태그의 '부모기준' 첫 번째 지정태그 선택
- :last-child - 지정 태그의 '부모기준' 마지막 지정태그 선택
- :only-child - 형제 태그가 없는 지정 태그 선택
- :nth-child(n) - 지정 태그의 '부모기준' n번째 자식태그 선택
    - n을 간단히 바꿀 수 있음 - 2n, 2n+1, ...
- :not(selector) - selector에 의해 선택된 태그를 제외한 태그 선택(부정)
- :disabled - 속성값이 disabled인 태그 선택
- :enabled - 속성값이 enabled인 태그 선택
- :checked - 속성값이 checked 태그 선택
- :empty - 몸체가 없는 태그 선택

### 속성
- 크기 단위
    - 기본 - 16px(픽셀)
    - 상대값
        - 100%, 200%
        - 1em, 2em
            - 자식으로 갈수록 중첩(자손까지 적용)
        - 1rem, 2rem
            - 중첩되지 않음

- 색상
    - 색상 이름 영단어 표기
    - 16진수 - RGB값
    - 10진수 - RGBA값, A는 투명도
        - rgb(r, g, b)
        - rgba(r, g, b, a)












display 속성
- 보인다(기본)
- 보이지 않는다
    - none
- 가로 / 세로
    - 가로 : inline
    - 세로 : block


***box model***
내용 - 너비(width) 높이(height) -> 지정하지 않으면 내용에 맞게 할당된다. -> width는 화면 전체에 맞게 할당된다.
border : 테두리
padding : 언쪽여백(내용과 border간 여백)
margin : 바깥쪽여백(border와 border간 여백)

font
- generic family
    - serif: 꼬리있음
        - font family: ...
    - san serif: 꼬리없음
        - font family: ...
    - mono space
- font family="A", "B", "C", ... generic family;    
A부터 쓰여있는 순서로 검색해서 있으면 사용하고 없으면 뒤에 순서로 넘어감. 마지막에는 기본적으로 있는 generic family를 선택


web-ui site
1. www.w3c.org
2. www.w3schools.com
3. developer.mozilla.org


***position***
top, bottom, left, right(스타일 속성)와 함께 사용
- static: normal position, position값 적용안됨
- relative, absolute, fixed : 상대위치, position값 적용
    - relative: normal positioin 기준
    - absolute: 부모 tag 기준 (부모는 relative 지정)
    - fixed: 브라우저 화면(viewport) 기준


레이아웃
- float 속성을 이용하여 레이아웃을 만들었음(레이아웃은 symantic에서 봤던 그림)
    - left
    - right
    - none
- clear - float에 독립적
    - left
    - right
    - both


축
- 행 : 주축, 메인축
- 열 : 교차축
메인과 교차축이 서로 바뀔 수 있음


반응형 웹
- view port에 따라서 위젯(태그)의 위치/크기를 자동으로 변경가능한 웹
- flex로 쉽게 구현할 수 있다.


flex grid는 알아서 해봐라(구글링)