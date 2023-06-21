## JavaScript

## [실습](./)

## 리뷰

### html내 js사용
- 위치
    - head
        - internal
        - external
    - body
        - internal
    - body끝

### 데이터형
- 기본형 데이터 타입
    - 정수&실수 - number
    - 문자 - string
    - 논리 - boolean
        - true/false
    - null
    - NaN
    - undefined
- 참조 데이터 타입
    - (JSON)배열: [값, 값2, ...]
    - JSON(객체): {key:value}
    - 함수(일급 객체)
    - 클래스

### 변수
- 변수 선언/초기화
    1. 변수선언     
    var/let 변수명;
    2. 변수초기화       
    변수명=값;
    3. 1+2(python 동일방식)     
    var/let 변수명=값;
- var vs let
    - var   
        - 변수 중복 선언 가능     
        - old버전     
        - 함수 scope
    - let(권장)   
        - 변수 중복선언 불가능    
        - es6버전     
        - 블럭 scope
- 변수타입확인 - typeof
- 상수 - const 변수명=값;
    - 값 변경 불가

### 연산자
- 산술연산자
    - +, -, *, /, %
    - 연결연산자: +     
    문자열 + 문자열 = 문자열합치기      
    문자열 + 비문자열 = 문자열비문자열합치기
- 대입연산자
    - +=, -=, *=, /=, %=
- 비교연산자
    - ==, >, >=, <, <=, !=
    - ==(equal 연산자) - 값만 비교
    - ===(identical 연산자) - 타입까지 비교
        - undefined 확인시 사용
- 논리연산자
    - ||(or), &&(and), !(not)
    - false로 처리  
        - 0, "", null, undefined, NaN - 모두 기본형 데이터
        - false처리값1 || false처리값2 -> 값1이 true이면 값1을 반환하고 false이면 값2를 반환    
        false처리값1 && false처리값2 -> 값1이 true이면 값2을 반환하고 false이면 값1를 반환
- 증감연산자
    - 증가(++): 1증가
    - 감소(--): 1감소
    - 전치(++/--변수): 선 증/감 후 대입
    - 후치(변수++/--): 선 대입 후 증/감
- 3항연산자     
    - python      
    변수= 참 if 조건식 else 거짓    
    - js      
    변수= (조건식)? 참:거짓;
- spread연산자
    - 배열/JSON구조를 없애고 원소를 펼침        
    특정 배열/JSON을 복사, 삽입, 추가하기 쉽다
    - 문법: ...배열/JSON

### 조건문
- if문      
    - python        
    들여쓰기의 의미가 있다
    ```python 
    if 조건식:  
        문장
    ```
    - js        
    가독성을 위한 들여쓰기
    ```javascript  
    if (조건식){
        문장
    }
    ```
- if~else문
    - python    
    ```python
    if 조건식:
        문장
    else:
        문장
    ```
    - js    
    ```javascript
    if(조건식){
		문장
	}else{
		문장
	}
    ```
- 다중 if문
    - python   
    ```python 
    if 조건식:
        문장
    elif 조건식:
        문장
    else:
        문장
    ```
    - js       
    ```javascript
    if(조건식){
		문장
	}else if{
        문장
    }else{
		문장
	}
    ```
- switch문      
```js
switch(변수){
    case 값1: 문장; break;
    case 값2: 문장2; break;
    ...
    case 값n: 문장n; break;
    default: 문장;
}
```

### 반복문
- while문
    - python
    ```python
    시작값
    while 조건식:
        문장
        증가/감소연산자
    ```
    - js
    ```javascript
    시작값(초기값)
    while(조건식){
        문장
        증가/감소연산자
    }
    ```
- do~while문    
    - 조건이 false라도 적어도 한번은 문장을 실행한다
    - 끝에 세미콜론 필수
    - ```js
        시작값;
        do{
            문장;
            증감연산자;
        }while(조건식);
      ```
- for문
    - python    
    ```python
    for 변수 in 집합형:
        문장
    ```
    - js
    ```js
    for(시작값; 조건식; 증감식;){
        문장;
    }
    ```
- break/continue문
    - python
    ```python
    for 변수 in 집합형:
        문장
        if 조건식: break
        if 조건식: continue
    ```
    - js
    ```js
    for(시작값; 조건식; 증감식;){
        문장
        if(조건식) break;
        if(조건식) continue;
    }    
    ```

### 간단한 함수
- 키보드로 입력
    - prompt()
    - 문자로 반환
- 숫자형으로 변환
    - Number.parseInt() - 권장
    - parseInt() - Window 객체