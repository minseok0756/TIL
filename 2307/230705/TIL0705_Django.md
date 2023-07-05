# Django

웹서버
- client가 요청한 url을 분석하여 was에 전달
- was에서 보낸 결과 데이터를 html로 만들어(렌더링) client에게 보냄(response)


WAS(Web Application Server)
- 분석된 결과를 전달받아 서치함
    - SQL을 이용해 DB서치
    - API를 이용해 다른 서버에 요청
    - ...
- 서치한 결과를 웹서버에 전달


웹 프로그래밍
- http프로토콜로 통신하는 클라이언트와 서버를 개발
    - http프로토콜을 통해서 요청 / 응답
    - http 메시지 구조 - 스타트라인, 헤더, 빈 줄, 바디
        - 스타트라인    
            - 요청메시지 - 요청라인(request line)       
                - 요청방식(method), 요청url, 프로토콜버전
                    - 요청방식 - GET, POST      
                    GET - 지정한 url의 정보를 가져오는 메소드, 가장 많이 사용       
                    POST - 리소스 생성, 중요하거나 보안이 필요한 정보(로그인 정보)
                    - url
                        - url 구성항목 - url스킴, 호스트명, 포트번호, 경로, 쿼리스트링
                            - 포트번호 - http:80, https:443
                        - 간편url - 쿼리스트링 없이 경로만 가진 간단한 구조의 url
            - 응답메시지 - 상태라인(status line)        
                - 상태코드 - 서버의 처리 결과를 확인
                    - 2xx - success
                        - 200 - OK
                    - 3xx - redirection -> 완전한 처리를 위해 추가적인 동작을 필요로 하는 경우. 다시 request하라고 함
                    - 4xx - client error
                        - 403 - forbidden
                        - 404 - not found
                    - 5xx - server error
                        - 503 - service unavailable
- 주로 웹 서버를 개발
- Django(python) 같은 웹 프레임워크를 사용
    - 프레임워크 - 빠르고 쉽게 만들 수 있다. 섬세하게 원하는대로 만들 수 없다.
        - 원하는 대로 만드려면 라이브러리를 사용해야함


Django 웹 프레임워크
- MVC 패턴 기반 MVT
    - MVC패턴 (Model View Controller) - 일반적
        - model - DB모델링(데이터저장)
        - view - 사용자 인터페이스, html(데이터를 html로 구성)
        - controller - 데이터 처리 로직, function(기능)
        - 요소간에 영향을 주지 않음

    - MVT패턴 (Model View Template) - Django
        - model - 데이터베이스에 저장되는 데이터를 의미
            - 설계(DB모델링)를 먼저 해야함
        - view - function(기능), 프로그램 로직이 동작하여 데이터를 가져오고 처리한 결과를 템플릿에 전달
        - template - 사용자에게 보여지는 ui부분, html(데이터를 html로 구성)
        - Django의 MVT패턴
            - 클라이언트로부터 요청을 받으면 URL.conf를 이용하여 URL을 분석
            - URL 분석 결과를 통해 해당 URL에 대한 처리를 담당할 뷰를 결정
                - urls.py에 코딩
            - 뷰는 자신의 로직을 실행하면서. 만일 데이터베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환
            - 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에 전송할 HTML 파일을 생성
            - 뷰는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답

- 객체 관계 매핑(Object-Relational Mapping)
    - 데이터베이스 시스템과 데이터 모델 클래스를 연결

- 프로젝트 - 사이트에 대한 전체 프로그램, 뼈대라고함          
애플리케이션 - 모듈화된 단위 프로그램

- MVT 코딩순서
1. 프로젝트 뼈대 만들기 - 프로젝트 및 앱 개발에 필요한 디렉토리와 파일
생성
2. 모델 코딩하기 - 테이블 관련 사항을 개발(models.py, admin.py)
    - 설계
        - 데이터 식별
        - 데이터도출 - 타입, 길이
        - 제약조건
3. URLconf 코딩하기 - URL 및 뷰 매핑 관계를 정의(urls.py)
    - project에 있는 urls.py
    - application에 있는 urls.py
4. 템플릿 코딩하기 - 화면 UI 개발(index.html(초기화면), template/*.html)
5. 뷰 코딩하기 - 애플리케이션 로직 개발(views.py)

프로젝트 뼈대 만들기
1. (base) C:\MyTest>django-admin startproject mysite - mysite라는 프로젝트 생성
2. (base) C:\MyTest\projectsite>python manage.py startapp polls - polls라는 애플리케이션 생성
3. (base) C:\MyTest\projectsite\mysite>notepad settings.py - 설정 파일을 확인 및 수정
    - notepad는 윈도우 메모장 명령어
    - 메모장이 켜지면 세팅 변경
        - ALLOWED_HOSTS 항목을 적절하게 지정
            - ALLOWED_HOSTS = ['192.168.35.61', 'localhost', '127.0.0.1’]
        - 애플리케이션들은 모두 설정 파일에 등록(polls 애플리케이션도 등록)
            - INSTALLED_APPS =[ ~, 'polls.apps.PollsConfig’, ]
        - 프로젝트에 사용할 데이터베이스 엔진
            - 장고는 디폴트로 SQLite3 데이터베이스 엔진을 사용하도록 설정
        - 타임존 지정(기본은 세계표준시(UTC)로 되어 있음. 한국시간으로 변경)
            - #TIME_ZONE = 'UTC'
            - TIME_ZONE = 'Asia/Seoul'
4. python manage.py migrate - 데이터베이스에 기본 테이블을 생성
5. python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인
    - ctrl + c 로 종료