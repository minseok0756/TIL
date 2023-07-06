# Django

프로젝트 뼈대 만들기
- Admin 사이트 접속
    - 기본적으로 제공하는 Admin 사이트에 접속해서 테이블 생성 확인
        - http://127.0.0.1:8000/admin
    - Admin 사이트에 로그인하기 위한 관리자(슈퍼유저)를 생성
        - (base) C:\MyTest\projectsite>python manage.py createsuperuser
            - 서버를 올린 상태이면 ctrl + c로 중단하고 입력해도 되고 추가로 아나콘다 프롬프트를 열어 입력해도 된다
        - 비밀번호 잘 기억하기 - 잊어버리면 처음 부터 다시 해야함
    - Admin 사이트에서 Users와 Groups 테이블을 포함하여 새롭게 만들 테이블에 대한 데이터의 입력, 변경, 삭제 등의 작업을 할 수 있음
        - Admin 화면에서 기본적으로 Users와 Groups 테이블이 보이는 것은 이미 settings.py 파일에 django.contrib.auth 애플리케이션이 등록되어있기 때문
        - 장고에서 기본으로 제공하는 auth 앱에 Users와 Groups 테이블이 미리 정의

- 골격 생성
    - (base) C:\MyTest>tree /F projectsite


Model 코딩
- 모델 작업은 데이터베이스에 테이블을 생성하는 작업
- notepad models.py - 테이블을 정의하기 위해 메모장으로 models.py 열기
    - PK는 Django에서 자동으로 생성
    - varchar(200) -> models.CharField(max_length=200)
    - datetime -> models.DateTimeField('date published')
    - integer -> models.IntegerField(default=0)
    - models.ForeighKey(참조필드)

- notepad admins.py - 정의된 테이블이 Admin 화면에 보이게 등록하기 위해 메모장으로 admins.py 열기

- python manage.py makemigrations - 데이터베이스에 변경이 필요한 사항을 추출함
    - makemigrations 명령에 의해 polls/migrations 디렉토리 하위에 마이그
레이션 파일들이 생김(0001_initial,py)

- python manage.py migrate - 데이터베이스에 변경사항을 반영함
- python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인함


URLconf, View 및 Template
- 로직의 흐름상 URLconf를 먼저 코딩한 후에 뷰,템플릿 또는 템플릿, 뷰 순서로 코딩하는 것이 일반적

URLconf
- 프로젝트 폴더의 공통 urls.py에 웹 앱의 url를 추가할 때마다 계속 추가하는 것은 번거로우므로 웹 앱별로 다른 ruls.py를 선언하고 프로젝트 폴더의 공통 urls.py에 해당 파일들을 포함하도록 만든다.
    - urls.py(C:\MyTest\projectsite\mysite) 파일에 코딩
        - [, path('app폴더/', include(app폴더.urls)), ]
    - urls.py(C:\MyTest\projectsite\mysite\polls) 파일에 코딩
        - [, path('url', views.함수명, name='')]
        - path parameter : url 사이에 있는 파라미터. 파라미터 타입을 정의한다.
            - int : 정수형 숫자     
            str : 모든 문자열       
            slug : -(하이픈)이나 _(언더스코어)를 포함한 영숫자, 문자열
                - 'calendar/<int:year>/<int:month>'
            - urls.py에서 path parameter로 정의하면 view 메소드에서 해당 인자를 넘겨받을 수 있다.
        - 정규표현식을 사용해 url 패턴을 정의할 수 있다. 파라미터는 P<name>pattern 형태로 나타낸다.(re_path 함수를 사용한다.)
            - re_path(r'^articles/(?P<year>[0-9]{4})/$', ...)
            - articles로 시작하는 path에 year라는 파라미터를 보내는 데 이는 0부터 9사이의 4자리 숫자로 끝난다.
        - name - url에 별칭을 지정

View 및 Template
- 뷰함수와 템플릿은 서로에게 영향을 미치기 때문에 보통 같이 작업
- View
    - 모델(에서정의한클래스).objects.all() - 모든 데이터 출력, 리스트로 반환
        - .order_by('필드명')/('-필드명') - 오름차순정렬/내림차순
    - get_object_or_404(모델, ...) - 조건을 만족하는 오브젝트가 있으면 해당 오브젝트를 리턴하고, 없으면 404 처리
        - from django.shortcuts import get_object_or_404
            - 기존의 template 모듈의 loader로 템플릿를 불러오고 render로 인자를 넘기는 부분을 shortcuts 모듈의 render라는 단축 메소드로 코드를 줄일 수 있다.
                - ```python
                    from django.template import loader
                    from datetime import datetime
                    def index(request):
                        template = loader.get_template('index.html') # html 파일을 로딩
                        now = datetime.now()
                        context = {
                            'current_date': now # current_date변수를 template에서 사용가능 - {{ current_date}}
                        } # 템플릿에 전달할 데이터를 세팅할 수 있는 오브젝트
                        return HttpResponse(template.render(context, request))
                  ```
                - ```python
                    from django.shortcuts import render
                    def select(request):
                        context = {"number": 4} # number변수를 template에서 사용가능 - {{ number}}
                        return render(request, 'select.html', context)
                  ```
        - get_object_or_404(Question, pk=question_id)
            - Question객체 중 pk값이 question_id인 것이 있으면 가져오고 그렇지 않으면 404 에러를 발생시켜라
        - 에러가 발생한 경우 render로 'error_message'가 넘어간다.

- Template
    - template 폴더가 없어 만들어서 코딩해야함
    - {% %} - 명령어(제어문, 반복문, ...) 사용을 의미
        - {% if %} {% else %} {% endif %}
        - {% for %} {% endfor %}
        - {% csrf token %} - 보안을 위함
    - {{}} - view에서 render로 넘어온 인자를 변수로 사용
        - or 연산자로 나타내는 함수는 장고에 내장된 필터 함수이다. date 필터로 변수를 포매팅한다.
            - {{ current_date|date:"Y년 m월 d일 H시 i분 s초" }}
    - URL 별칭
        - URL 하드코딩 - url링크가 수정되는 경우 일일이 찾아가며 수정해야한다.
            - ```<a href="/polls/{{ question.id }}/">```
        - URL 별칭 사용하기
            - URL 매핑에 name 속성을 부여 - path(..., Name='')
            - ```<a href="{% url '별칭' question.id %}">```
                - question.id는 URL 매핑에 정의된 ```<int:question_id>```에 전달해야 하는 값을 의미
                - 이 때 파라미터 명을 함께 사용할수 있다.
                    - {% url 'detail' question_id=question.id %}
                - 2개 이상의 파라미터를 사용해야 한다면 공백 문자 이후에 덧 붙여준다.
                    - {% url 'detail' question_id=question.id page=2 %}
        - 다른 앱이 프로젝트에 추가되어 서로 다른 앱에서 동일한 URL 별칭을 사용하여 중복이 발생하는 경우
            - polls/urls.py에 네임스페이스를 의미하는 app_name 변수를 지정
                - app_name = 'polls'
            - app_name을 추가하여 url 별칭 사용
                - ```<a href="{% url 'polls:detail' question.id %}">```

    - #################### detail.html 부터 다시


두 프롬프트가 같은 서버를 올리면 웹 브라우저가 제대로 request하지 못한다