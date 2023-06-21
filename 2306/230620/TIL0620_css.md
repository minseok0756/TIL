## [css](https://www.w3.org/Style/CSS/Overview.en.html)(cascading style sheets)

cascading -> 재정의 가능

주석
/*~*/

css 문법
선택자 {
    속성:속성값;
    속성:속성값;
    ...
}

***선택자(selector)***
DOM트리에서 node를 선택하는 방법

속성(property)
- 색상, 위치, 글꼴, ...

id속성
모든 태그에 사용가능
일반적으로 속성값에 유일한 값을 지정함 - 식별목적
id를 식별하는 식별자 #id

class속성
중복 가능
식별하는 식별자 .class

자식 : >
자손 : (공백)
바로뒤 형제 : +
형제들 : ~

속성명으로 선택
[속성명]
[속성명="값"] - 속성값까지 일치하는 것을 선택
태그[속성명] - 특정태그에 있는 속성명으로 한정
[속성^=값] - 시작하는 속성값
[속성&=값] - 끝나는 속성값
[속성*=값] - 포함하는 속성값

의사코드(pseudo code)
값 자체에 의미가 있음
선택자:의사코드

js에서도 css선택자를 이용


크기
기본크기 : 16px = 1em = 1rem

색상
영단어
16진수 - RGB값
10진수 - RGBA값, A는 투명도

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