# Django

- [Django Database 변경](%EC%9E%A5%EA%B3%A0%20DB%20%EC%97%B0%EB%8F%99.txt)
- [Django 필드타입, 옵션](%EC%9E%A5%EA%B3%A0%20%EB%AA%A8%EB%8D%B8%20%ED%95%84%EB%93%9C%20%ED%83%80%EC%9E%85.txt)
- [Django 문법](%EC%9E%A5%EA%B3%A0%20%ED%83%AC%ED%94%8C%EB%A6%BF%20%EB%AC%B8%EB%B2%95.txt)


Mini project - To do list
1. 화면설계
    - 입력, 기능, 출력, ...
2. 데이터 설계(DB모델링)
    - 데이터 식별, 도출(저장, 사용)
        - 테이블: Todo
        - 필드명: content, isDone, Datetime
        - 필드타입: CharField(255), BooleanField(F), DateTimeField()


MVT 코딩 순서
- 프로젝트 뼈대 만들기 : 프로젝트 및 앱 개발에 필요한 디렉토리와 파일
생성
- 모델 코딩하기 : 테이블 관련 사항을 개발(models.py, admin.py 파일)
- URLconf 코딩하기 : URL 및 뷰 매핑 관계를 정의(urls.py 파일)
- 템플릿 코딩하기 : 화면 UI 개발(templates/ 디렉토리 하위의 *.html 파일들)
- 뷰 코딩하기 : 애플리케이션 로직 개발(views.py 파일)


프로젝트 뼈대 만들기 순서 명령
- (base) C:\MyTest>django-admin startproject ToDoList - ToDoList라는 프로젝트 생성
- (base) C:\MyTest\ToDoList>python manage.py startapp my_to_do_app - my_to_do_app라는 애플리케이션 생성
- (base) C:\MyTest\ToDoList>notepad settings.py - 설정 파일 확인 및 수정
    - INSTALLED_APPS =[ ~, ' my_to_do_app ’, ]
    - #TIME_ZONE = 'UTC'        
    TIME_ZONE = 'Asia/Seoul'
- (base) C:\MyTest\ToDoList>python manage.py migrate - 데이터베이스에 기본 테이블을 생성
    - db.sqlite3가 생성됨
- (base) C:\MyTest\ ToDoList >python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인
    - (base) C:\MyTest\ToDoList>python manage.py runserver 127.0.0.1:8000
    - (base) C:\MyTest\ ToDoList >python manage.py runserver 0:8000

Admin 사이트 접속
- 기본적으로 제공하는 Admin 사이트에 접속해서 테이블이 생성되었는지 확인
- 브라우저의 주소창에 IP 주소와 포트번호 동일, URL경로만 /admin 추가
    - http://127.0.0.1:8000/admin
- Admin 사이트에 로그인하기 위한 관리자(슈퍼유저)를 생성
    - (base) C:\MyTest\ToDoList>python manage.py createsuperuser
- Admin 사이트에서 Users와 Groups 테이블을 포함하여 새롭게 만들 테이블에 대한 데이터의 입력, 변경, 삭제 등의 작업을 할 수 있음
- Admin 화면에서 기본적으로 Users와 Groups 테이블이 보이는 것은 이미 settings.py 파일에 django.contrib.auth 애플리케이션이 등록되어있기 때문
- 즉 장고에서 기본으로 제공하는 auth 앱에 Users와 Groups 테이블이 미리 정의

골격 생성
- (base) C:\MyTest>tree /F ToDoList


Model 코딩
- 모델 작업은 데이터베이스에 테이블을 생성하는 작업
- notepad models.py - 테이블을 정의하기 위해 메모장으로 models.py 열기
    - models.CharField(max_length = 255)
    - models.BooleanField(default=False)
        - default - 레코드 생성시 값을 입력하지 않으면 default값으로 저장됨
- notepad admins.py - 정의된 테이블이 Admin 화면에 보이게 등록하기 위해 메모장으로 admins.py 열기
    - admin.site.register(Todo)
- (base) C:\MyTest\ToDoList>python manage.py makemigrations - 데이터베이스에 변경이 필요한 사항을 추출함
    - makemigrations 명령에 의해 polls/migrations 디렉토리 하위에 마이그레이션 파일들이 생김(0001_initial,py)
- python manage.py migrate - 데이터베이스에 변경사항을 반영함
- python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인함


URLconf, View 및 Template
- 로직의 흐름상 URLconf를 먼저 코딩한 후에 뷰,템플릿 또는 템플릿, 뷰 순서로 코딩하는 것이 일반적

URLconf
- 프로젝트 폴더의 공통 urls.py에 웹 앱의 url를 추가할 때마다 계속 추가하는 것은 번거로우므로 웹 앱별로 다른 ruls.py를 선언하고 프로젝트 폴더의 공통 urls.py에 해당 파일들을 포함하도록 만든다.
    - urls.py(C:\MyTest\ToDoList\ToDoList) 파일에 코딩
        - ```python
            [    path("admin/", admin.site.urls),
                 path("", include('my_to_do_app.urls')),
            ]
          ```
    - urls.py(C:\MyTest\ToDoList\my_to_do_app) 파일에 코딩
        - ```python
            [    path('', views.index, name='index'),
                 path('createTodo/', views.createTodo, name='createTodo'),
                 path('doneTodo/', views.doneTodo, name='doneTodo'), 
            ]
          ```
View 및 Template
- 뷰함수와 템플릿은 서로에게 영향을 미치기 때문에 보통 같이 작업
- ```python
    def createTodo(request):
        user_input_str = request.POST['todoContent']
        new_todo = Todo(content=user_input_str)
        new_todo.save()
        return HttpResponseRedirect(reverse('index'))
        # return HttpResponse("DB에 저장되었어요 =>" + user_input_str)
  ```
- Todo(content=user_input_str)
    - Todo모델에 레코드 생성. content 필드에 user_input_str을 isDone 필드에 False(default)를 저장

- ```html
            <div class="toDoDiv">
                <ul class="list-group">
                    {% for todo in todos %}
                    {% if todo.isDone == False %}
                    <form action="./doneTodo/" method="GET">
                        <div class="input-group" name='todo1'>
                            <li class="list-group-item">{{ todo.content }}</li>
                            <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
                            <span class="input-group-addon">
                                <button type="submit" class="custom-btn btn btn-danger">완료</button>
                            </span>
                        </div>
                    </form>
                    {% else %}
                    {% endif %}
                    {% endfor %}
                </ul>
            </div>
  ```
    - ```html
        <form action="./doneTodo/" method="GET">
            <input type="hidden" id="todoNum" name="todoNum" value="
      ```
    - 제출시 GET method로 './doneTodo/' url에 제출
    - key name = todoNum, value = todo.id

- ```python
    def doneTodo(request):
        done_todo_id = request.GET['todoNum']
        print("완료한 todo의 id",done_todo_id)
        todo = Todo.objects.get(id = done_todo_id)
        todo.isDone = True
        todo.save()
        return HttpResponseRedirect(reverse('index'))
  ```
    - request.GET['todoNum'] - 제출된 data에서 key name이 'todoNum'인 value를 string으로 반환
    - return HttpResponseRedirect(reverse('index')) - GET method도 HttpResponseRedirect 사용