# [Css](https://www.w3.org/Style/CSS/Overview.en.html)(cascading style sheets)

cascading - 재정의 가능

web-ui site
1. www.w3c.org
2. www.w3schools.com
3. developer.mozilla.org

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
- 크기 단위(size)
    - 기본 - 16px(픽셀)
    - 상대값
        - 100%, 200%
        - 1em, 2em
            - 자식으로 갈수록 중첩(자손까지 적용)
        - 1rem, 2rem
            - 중첩되지 않음

- 색상(color)
    - 색상 이름 영단어 표기
    - 16진수 - RGB값
    - 10진수 - RGBA값, A는 투명도
        - rgb(r, g, b)
        - rgba(r, g, b, a)

- display
    - display:none - 태그를 화면에서 보이지 않게 한다.(영역조차 없음)
    - display:block - 태그를 block형식으로 지정(width, height 적용가능)
    - display:inline - 태그를 inline형식으로 지정(width, height 적용 불가능)
    - display:inline-block - 태그를 inline-block형식으로 지정
        - inline이지만 width와 height 적용 가능
    
- visibility
    - visibility:hidden - 태그를 보이지 않게 한다.(영역은 보인다.)
    - visibility:collapse - 테이블 태그를 보이지 않게 한다.(영역조차 없음)

- opacity
    - opacity:숫자 - 0일 수록 투명 1일 수록 불투명

- box model
    - border : 테두리      
        - border-top/right/bottom/left-width : 값       
        border-width : 값 (모두 동일)     
        border-width : 값 값 (상하 좌우)      
        border-width : 값 값 값 (상 좌우 하)      
        border-width : 값 값 값 값 (상 우 하 좌)
        - border-top/right/bottom/left-style : 값       
        - border-color : 값       
        - border : width style color(한번에 지정가능 - 일반적임)
        - border-radius:값 - border의 꼭지점이 부드럽게 그려짐 
    - padding : 언쪽여백(내용과 border간 여백)        
    margin : 바깥쪽여백(border와 border간 여백)
        - margin/padding-top/right/bottom/left : 값     
        margin/padding : 값 (모두 동일)     
        margin/padding : 값 값 (상하 좌우)      
        margin/padding : 값 값 값 (상 좌우 하)      
        margin/padding : 값 값 값 값 (상 우 하 좌)
        - margin : auto - 중양정렬
    - box-sizing : border-box - width, height값이 실제 박스크기를 지정(padding, border, margin width,height크기에 맞춰짐)

- background
    - background-image : url('이미지 경로')
    - background-repeat:        
    repeat - 이미지 반복        
    repeat-x - x축으로 반복     
    repeat-y - y축으로 반복     
    no-repeat - 반복 없음
    - background-attachment:        
    fixed - 스크롤시 이미지 고정        
    scroll : 고정안됨
    - background-position : 이미지 위치
    - background-color: powderblue;
    - background-size: cover;       
    cover - 이미지가 배경을 완전히 덮음(이미지가 짤리더라도)     
    certain - 이미지가 완전히 보이도록 나타냄

- font
    - generic family - 웹 브라우저에서 기본 제공
        - serif, sans serif
    - font-family : font1, font2, ..., generic family
    - font-size : 값        
    xx-small        
    x-small        
    small        
    medium        
    large        
    x-large        
    xx-large        
    px, em, rem
    - font-style
    - font-weight       
    bold, 숫자(100~900, 클수록 굵음)
    - font: font-style font-weight font-size font-family(한번에 지정가능, 일반적)
    - font-face
    ```css
    @font-face {
    	font-family:font family;
	    src:url('font파일경로') format('truetype');
    }
    ```
    
- text
    - text-align - 정렬      
    left - 왼쪽 정렬    
    right - 오른쪽 정렬    
    center - 가운데 정렬
    justify - 양쪽 정렬    
    - text-decoration :        
    underline - 밑줄       
    overline - 윗줄       
    line-through - 가운데줄       
    - text-transform :      
    capitalize - 첫글자 대문자      
    uppercase - 대문자로      
    lowercase - 소문자로     
    - text-indent : 값 - 들여쓰기
    - line-height - 줄간격
    - letter-spacing - 글자간 간격
    - word-spacing - 단어간 간격       

- position
    - position : static, relative, fixed, absolute      
    static - normal position    
    relative - normal position을 기준       
    fixed - 브라우저 화면 기준      
    absolute - 부모 tag 기준
    - top. bottom, right, left와 같이 사용
    - z-index : 값 - 요소의 stack 순서를 변경, 값이 클수록 위로 올라옴(먼저 보임)

- float
    - 요소를 가로 방향으로 배치(다른 요소와 겹치지 않음)
    - left, right
    - clear - float 중지    
    left - The element is pushed below left floated elements   
    right - The element is pushed below right floated elements   
    both - The element is pushed below both left and right floated elements   

- flex
    - 기본적으로 부모/자식 관계 설정
    - 부모 - flex container
        - 반드시 display:flex 지정
    - 자식 - flex item
    - flex-direction    
    row - 앞에서 뒤로         
    row-reverse - 뒤에서 앞으로         
    column - 위에서 아래로         
    column-reverse - 아래서 위로         
    - flex-wrap     
    wrap - 브라우저창 축소 시 여러 줄에 걸쳐 보여짐     
    wrap-reverse - 브라우저창 축소 시 여러 줄에 걸쳐 반대 순서로 보여짐     
    nowrap - 브라우저창 축소 시 같이 축소됨     
    - flex-flow : flex-direction flex-wrap (한번에 지정 가능)
    - justfy-content - 정렬(주축이 row인 경우)
    flex-start - 왼쪽 정렬     
    flex-end - 오른쪽 정렬       
    center - 가운데 정렬     
    space-around - 요소간 공간이 모두 같은 너비(컨테이너의 앞뒤 공간은 요소간 공간의 절반)       
    space-between - 양쪽 정렬       
    space-evenly - 모든 공간이 같은 너비(컨테이너의 앞뒤 공간까지 포함)
    - align-items - 교차축(메인축이 아닌 축) 정렬(교차축이 column인 경우)       
    flex-start - 위쪽 정렬      
    flex-end - 아래쪽 정렬       
    center - 가운데 정렬        
    stretch - 컨테이너 위,아래에 닿게 늘림
    - aligh-self - align-items속성에 의해 설정된 기본정렬을 재정의
    flex-start - 위쪽 정렬      
    flex-end - 아래쪽 정렬       
    center - 가운데 정렬        
    stretch - 컨테이너 위,아래에 닿게 늘림
    - flex-basis:크기 - item의 초기길이 지정
    - flex-grow:값 - container에 여분의 공간이 있는 경우 일정 비율에 따라 확대
    - flex-shrink:값 - container에 공간이 부족한 경우 일정 비율에 따라 축소
        - 값이 클수록 더 많이 축소, 0이면 축소 안됨
    - flex: grow shrink basis (한번에 지정)
    - Media Query - 다양한 미디어 유형에 대해 다양한 스타일 규칙을 적용     
    반응형 앱 - view port에 따라서 위젯(태그)의 위치/크기를 자동으로 변경가능한 앱
    ```css
    @media 미디어타입 and ( 표현식 ) {
        CSS 코드;
    }
    ```
    



flex grid는 알아서 해봐라(구글링)