# Django 복습

## Django 설치하기

Django 설치 <br>
`C:\>pip install Django`

Django 버전확인 <br>
`C:\>python -m django --version`

## Window 가상 환경 구성하기

1. Anaconda 설치
2. conda 가상 환경 세팅하기
- `conda create -name <가상 환경 이름> <설치할 파이썬 버전>`
- 또는
- `conda create -n <가상 환경 이름> <설치할 파이썬 버전>`

가상 환경 목록 보기<br>
`conda info -envs`

가상 환경 진입 <br>
`activate <가상 환경 이름>`

가상 환경 빠져나오기 <br>
`conda.bat deacticate`

## ToDoList 만들기

장고 프로젝트 만들기 <br>
`django-admin startproject <프로젝트명>` - 프로젝트명으로 된 폴더가 생김

Application 구성하기 <br>
`python manage.py startapp <Application명` - manage.py파일이 있는 위치에서 실행해야 한다. manage.py 파일이 있는 같은 경로에 애플리케이션명으로 된 폴더(myapp라고 부르자)가 생김. <br>
(`python manage.py ~` 는 CMD에서 장고에 대한 작업을 실시할 때 manage.py를 이용해서 명령을 내리는 것을 의미한다.)

실제로 프로젝트에 추가된 app 입력하기 - 애플리케이션 폴더와 같은 위치에 프로젝트명으로 된 폴더가 하나 더 있다(프로젝트app라고 부르자). 해당 폴더에 settings.py에서 `INSTALLED_APPS` 에 애플리케이션명을 추가한다. app을 만들 때마다 추가해야 한다.

프로젝트 실행 <br>
`python manage.py runserver`

### URL 설정하기

장고 프로젝트에서 url을 설정할 때는 기본 URL에 대해서 신경 쓰지 않는다. 사용자가 처음 접속하는 화면에 대해서 ''라는, 비어있는 URL로 나타낼 것이다. 이는 "http://127.0.0.1:8000/"과 의미적으로 같다.

<br>

프로젝트app에 urls.py파일에 urlpatterns에 `path('admin/', admin.site.urls)` 는 사용자가 'admin/'이라는 주소로 접근했을 때, 즉 실제로는 "http://127.0.0.1:8000/admin"에 접근했을 때 admin.site.urls로 접근하라는 의미이다. 기본적으로 제공하는 admin 관련 app의 urls.py로 넘겨서 처리하겠다는 의미이다. 

<br>

사용자가 ''에 접근했을 때 myapp의 urls.py파일로 처리를 넘겨준다. <br>
`path('', include('myapp'))` - myapp은 직접 새롭게 추가한 app이기 때문에 include라는 함수를 사용해야 한다. include 함수를 사용하기위해 import한다. `from django.urls import include`

<br>

myapp의 urls.py에서 다시 한 번 처리한다. myapp폴더에는 아직 urls.py파일이 없는데 만들어 준다.
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]
```
특정 URL로 접근한 사용자에게 보여 줄 화면을 처리할 함수를 연결해야 하는데, 이는 같은 경로의 view.py 파일이 담당한다. 특정 위치로 접근한 사용자에게 어떤 화면을 보여 줄지 실제로 처리하는 것이 view.py 파일이다. 따라서 해당 파일도 import해준다. from 뒤의 .은 같은 경로임을 의미한다.

<br>

위에서 ''와 view.index를 연결시켰으므로 view.py에 index함수를 만들어 준다.
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("myapp first page")
    # 단순히 인자로 받은 문자열을 사용자의 화면에 보여주는 함수
```

### HTML 템플릿 사용하기

myapp 내부에 templates라는 폴더를 만들고, 그 안에 myapp이라는 폴더를 또 만든다. HTML파일을 템플릿으로 사용하려고 할 때, 장고는 해당 앱에서 templates라는 폴더를 탐색하게 된다. 그리고 동일한 앱의 이름으로 된 폴더를 찾아 그 내부에 있는 htaml파일을 불러와 사용한다.

<br>

index.html파일을 만든다. 실제로 웹 브라우저에서 보여주려면 view.py에서 처리해야 한다. render 함수를 사용한다.
```python
def index(request):
    return render(request, 'myapp/index.html')
```
사용자가 특정 url에 접근해서 index 함수를 실행할 때 기본적으로 request를 받아와 user나 session과 같은 값들을 참조할 수 있게 되고, 이를 render를 통해 사용자에게 웹 페이지를 보여줄 때 그대로 가져가게 된다.

### 데이터베이스 테이블 만들기

model.py에 테이블과 데이터에 대한 형태를 설정한다. 장고에서 하나의 모델(테이블)은 하나의 클래스로 나타낸다. Todo라는 클래스 이름이 모델이 이름이다. 클래스 내부에 데이터의 이름(content)과 그 데이터의 형태(models.CharField)를 정의하면 된다. 
```python
from django.db import models

class Todo(models.Model):
    content = models.CharField(max_length = 255)
```
Todo라는 모델에 대해서 데이터가 content라는 값 하나만을 가지게 했고, 그 데이터의 형태는 CharField 형태이며, 추가로 최대 길이를 255로 제한했다.

<br>

장고 서버에 실제로 적용해준다. manage.py 파일이 있는 경로로 이동한 후 <br>
`python manage.py makemigrations`
migrations는 단순히 데이터베이스에 전해 줄 초안,설계도, 작업 지시서와 비슷한 역할을 한다. 즉, 아직 데이터베이스에 모델과 같은 테이블이 생성된 것은 아니다. <br>
`python manage.py migrate` - 데이터베이스에 실제로 테이블을 만든다. 처음에는 cmd창에 결과가 여러 줄 나오는데, 이는 migrate를 처음해서 그런 것이다. 기본적으로 장고에서 제공하는 model들이 있기에, 첫 migrate에서 기본 제공 model들 또한 데이터베이스에 적용되어 만들어진 것이다.

<br>

model 확인하기 <br>
`python manage.py dbshell` - 데이터베이스에 접근한다. <br>
`.tables` - 데이터베이스에 존재하는 테이블 확인한다. 장고가 기본적으로 제공하는 모델들에 의해 생성된 테이블도 있고, 직접 만든 테이블도 있다. 테이블명은 <애플리케이션이름>_<모델이름>과 같은 규칙으로 만들어진다. <br>
`PRAGMA table_info(테이블명);` - 테이블 정보를 확인한다. '단순Number | 컬럼이름 | Type | notnull 여부 | pk 여부'를 확인할 수 있다. 1은 true, 0은 false를 의미한다. id라는 컬럼을 장고가 자동으로 생성한다. <br>
`select * from 테이블명;` - 데이터를 확인한다. <br>
`.quite` - dbshell에서 빠져나온다

<br>

사용자가 html 화면에서 텍스트를 입력하고 버튼을 눌렀을 때, 해당 텍스트가 서버에 전송되도록 한다. index.html 파일을 수정한다.
```html
<div class="messageDiv">
    <form action="./createTodo/" method="POST">{% csrf_token %}
        <div class="input-group">
            <input id="todoContent" name="todoContent" type="text" class="form-control" placeholder="메모할 내용을 적어주세요">
            <span class="input-group-btn">
                <button class="btn btn-default" type="submit">메모하기!</button>
            </span>
        </div>
    </form>
</div>
```
기본적으로 html에서 서버로 데이터를 전달할 때는 form 태그로 감싸져야 한다. form 태그 안에는 이를 서버로 제출하는 submit type의 button이 존재하며, 직접 서버에 전달해 줄 데이터가 담기는 input이 존재한다. form 태그의 action과 method를 직접 설정해야 한다. method는 크게 POST방식과 GET방식이 있다. POST방식을 사용할 때, {%csrf_token%}을 적어 주어야 한다는 것을 기억하자. action은 서버로 데이터를 전달할 때 어떠한 url로 전달할 것인지를 나타낸다. 'createTodo'라는 url로 전달된다. '메모하기!'라고 적힌 button 태그를 클릭하여 서버에 데이터를 전달하게 된다.

<br>

myapp urls.py파일에 'createTodo' url에 대한 처리를 추가한다.
```python
urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
 ]

```
`path('createTodo/', views.createTodo, name='createTodo')`는 'createTodo/'라는 url에 대해서는 views.py 파일의 createTodo함수로 처리하라는 의미이다. name은 각 path로 메핑시켜줄 때 url을 적는 대신 name을 이용해서 접근할 수 있도록 하기 위함이다.

<br>

view.py에서 처리할 createTodo 함수를 만들어준다. 사용자가 서버에 전달한 데이터를 받아와서 데이터베이스에 저장하도록 함수를 만들어준다.
```python
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

def createTodo(request):
     user_input_str = request.POST['todoContent']
     new_todo = Todo(content=user_input_str)
     new_todo.save()
     return HttpResponseRedirect(reverse('index'))
```
서버는 함수의 인자인 request로 데이터를 받아온다. request에서 index.html의 input태그속성 중 name값('todoContent')을 이용해서 input 태그 안에 있는 문자열을 받아올 수 있다. POST방식으로 제출했으므로 request에서 POST에 접근한다. - `request.POST['todoContent]` <br>
데이터를 저장하려는 model을 사용하기 위해 model.py파일을 불러와야 한다. - `from .models import *` <br>
모델을 통해 새로운 데이터를 생성한다. 이때 우리가 이용하는 모델은 'Todo' 모델이고, content라는 값에 사용자가 입력한 값을 넣어주었다. - `Todo(content=user_input_str)` <br>
데이터베이스에 저장한다. - `new_todo.save()` <br>
함수에서 일정한 처리 후 메인 페이지로 돌아가려면, 다시 메인 페이지의 url로 돌아가게 해야 한다. HttpResponseRedirect 함수를 이용한다. 일반적으로 HttpResponseRedirect 함수를 이용할 때 원하는 url에 쉽게 매핑해 주려고 reverse 함수를 이용한다. reverse에는 url이 아닌 url매핑시 지정한 name을 인자로 넣는다.
```python
from django.http import HttpResponseRedirect
from django.urls import reverse

return HttpResponseRedirect(reverse('index'))
```

<br>

웹에서 메인 페이지 하단 부분에 그동안 데이터베이스에 기록된 데이터들을 보여준다. 먼저 view.py 파일에서 index함수를 수정한다.
```python
def index(request):
     todos = Todo.objects.all() 
     content = {'todos': todos} 
     return render(request, 'my_to_do_app/index.html', content)
```
Todo모델에 접근하고, objects에 접근한 후 all 함수를 통해 모든 데이터를 가져온다. - `todos = Todo.objects.all()` <br>
가져온 데이터를 content라는 딕셔너리를 만들어서 'todos'라는 key에 할당시킨다. - `content = {'todos': todos}` <br>
render 함수의 마지막에 content 딕셔너리를 함께 전달한다. render 함수의 두 번째 인자로 넘겨주는 화면에서 해당 딕셔너리를 사용할 수 있다.- `return render(request, 'my_to_do_app/index.html', content)`

데이터를 전달했으면 이를 사용자에게 직접보여주기 위해 index.html 파일을 수정한다.
```html
<div class="toDoDiv">
    <ul class="list-group">
        {% for todo in todos %}
        <form action="./doneTodo/" method="GET">
            <div class="input-group" name='todo1'>
                <li class="list-group-item">{{ todo.content }}</li>
                <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
                <span class="input-group-addon">
                    <button type="submit" class="custom-btn btn btn-danger">완료</button>
                </span>
            </div>
        </form>
        {% endfor %}
    </ul>
</div>
```
{% %}와 같이 템플릿 태그를 이용하면 html 파일 내부에서 파이썬 문법을 사용할 수 있다. for문과같은 반복문을 입력할 때 사용한다. - `{% for todo in todos %}` <br>
content 딕셔너리로 html 파일에 데이터를 넘겨주었는데, 딕셔너리 안에 있는 key값을 이용해 바로 value에 접근할 수 있다. 따라서 `{% for todo in todos %}`에서 todo는 넘겨받은 데이터 하나하나를 의미한다. <br>
{{ }} 또한 템플릿 태그이다. 사용자에게 직접 보여주는 값을 의미한다. - `{{ todo.content }}` <br> 
`todo.content`를 통해 todo의 데이터에서 content라는 (칼럼)값에 접근한다. <br>
`<input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>`에서 input 태그는 type이 hidden으로 되어서 존재하기는 하지만 사용자에게 보이지 않는 요소이다. 해당 요소의 value에 todo데이터의 id를 입력해 준 이유는 해당 todo를 완료해서 삭제하려고 할 때 id를 이용해서 삭제하기 위함이다. <br>
완료 버튼을 눌렀을 때 `'/deleteTodo/'`의 url로 이동하게끔 한다. 또한 GET방식을 이용한다. - `<form action="./doneTodo/" method="GET">`

<br>

myapp urls.py파일에 'deleteTodo' url에 대한 처리를 추가한다.
```python
urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('deleteTodo/', views.deleteTodo, name='deleteTodo'),
 ]
```

<br>

view.py에서 deleteTodo 함수를 만들어서 데이터 삭제 기능을 진행한다.
```python
def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id",done_todo_id) # cmd창에 출력됨
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
```
html의 form 태그에서 method가 GET이었기 때문에 request에서도 GET으로 데이터를 받아온다. - `request.GET['todoNum']` <br>
Todo 모델의 objects에 접근하고 get함수를 통해 데이터를 가져올 수 있는데, 이때 서버에서 받아온 id값을 이용해서 특정 데이터를 가져올 수 있다. - `Todo.objects.get(id = done_todo_id)` <br>
데이터를 담은 변수에서 delete 함수를 호출하면 데이터를 삭제할 수 있다. - `todo.delete()`

## HTML에서 if문 사용

```python
{% if 조건식 %}
...
{% else %}
{% endif %}
```

## app은 왜 나누고, 어떻게 나눌까?

app 구조화에 대한 핵심은 '유지 보수'이다. 개발된 소프트웨어를 운영 및 관리하는 것을 말한다. 
- app의 재활용성: 각각의 기능별(로그인 기능, CRUD기능, 검색 기능, 동영상 재생 기능 등)로 app 단위로 나눠 개발한다면 추후 동일한 기능에 대해서 개발이 필요할 때 이전에 만들어 둔 app을 패ㅣ징화해서 또다시 사용할 수 있다.
- 오류를 해결하는데 더 도움이 될 수 있다.
- 추가 개발을 하는데도 큰 도움이 된다.

## MVC?

소프트웨어를 개발하는 개발 방법론(디자인 패턴)이다. 사용자에게 보이는 화면단 로직과 내부적으로 실행되는 비즈니스 로직을 나누어 서로에게 영향이 없도록 시스템을 개발하고 유지 보수할 수 있다. <br>
장고도 MVC 패턴을 따른다. MVC는 Model, View, Controller를 의미한다.
- Model은 장고 프로젝트에서도 model로 다뤄진다. 대표적인 역할은 데이터에 대한 부분들이고, 장고 프로젝트에서도 model은 데이터베이스와 직접적으로 연관되는 개념이다. Model은 장고 프로젝트에서 models.py와 연관이 있으며, 해당 파일을 통해 웹 페이지가 가지는 데이터를 정의하고 관리한다. 또한 Controller에서 해당 Model에 접근해 데이터를 가져오거나 데이터를 Model의 형태에 맞춰서 저장하는 등의 조작도 이루어진다.
    > 주로 사용되는 데이터를 정의할 수 있는 종류에는 CharField, DateField, EmailField, FileField, TextField, IntegerField, BooleanField가 있다.
    > 참고 https://docs.djangoproject.com/en/4.2/ref/models/fields/#field-types
- View의 역할은 사용자에게 보여주는 화면이다. 장고 프로젝트에서는 templates이다. 저장된 html들은 단순히 파일 자체로 사용되는 것이 아니라, Controller에 의해서 데이터를 전달받거나 전달하는데 매개체로 이용된다. html 파일들을 저장할 때 'app 이름 폴더'안에 'templates' 폴더를 만들고, 또 그 안에 'app 이름 폴더'를 만들어서 html파일을 저장했다. 여러 개의 app 사이에서 동일한 이름의 html 파일을 가질 때 발생할 수 있는 문제점을 막기 위해서이다.
- Controller는 장고에서 view.py 파일과 연관이 있다. Controller는 사용자에게 보이는 화면에 대한 것이 아니라, 그 뒤에서ㅓ 진행되는 내부 로직을 담당한다. views.py에서는 함수들을 정의하며, 특정 함수 내에서 특정 로직을 처리하도록 한다. 사용자가 특정 url에 접근했을 때 urls.py 파일을 통해 해당 url에 대해서는 view.py의 어떤 함수로 처리를 넘길 것인지 지정한다. 또한 return은 render와 같은 함수를 이용해 html을 사용자에게 보여주도록 로직을 마무리한다.
    > 함수는 인자로 request를 받는다. 이는 웹에서 '요청'을 받는 것인데, 해당 요청안에 다양한 데이터나 상태 값들이 포함되어 함수로 전달된다. <br>

엄밀히 이야기하면, 장고 프로젝트는 MVT 패턴을 따른다. MVC 패턴이 더 일반화된 개념으로 볼 수 있으며, MVC 패턴을 이해하고 장고 프로젝트와의 연관성을 이해한다면 MVT 패턴도 쉽게 이야기 할 수 있다.

## CRUD

CRUD(Create, Read, Update, Delete)는 단어 그대로 4가지 기능을 이야기하는데, 이는 소프트웨어가 기본적으로 기져야 할 또는 기본적으로 가지는 기능을 이야기한다. <br>
- Create는 데이터를 만드는 기능이다. 데이터를 생성해 데이터베이스에 저장한다는 의미이다.
- Read는 데이터를 읽도록 하는 기능이다. 우리가 메인 페이지에서 사용자가 그동안 입력한 데이터를 보여주도록 했다. 이것이 Read 기능이다.
- Update는 데이터를 갱신하도록 하는 기능이다. 일반적으로 웹 페이지에서 글을 게시한 후 수정할 수 있게 하는 기능이다.
- Delete는 데이터를 지우는 기능이다. 데이터베이스에서 특정 데이터를 삭제하는 기능이다.

구현한 프로젝트에서 Create와 Delete 기능의 차이가 존재한다. 서버에 전달하는 방식인 POST와 GET의 차이이다. GET으로 전달되는 방식은 주소값 뒤에 물음표(?)를 이용해 전달되는 값(파라미터)이 표시된다. 하지만 POST로 전달되는 방식은 숨겨져서 보내진다(숨겨진다는 표현보다 body안에 담겨 보내지는 것이다). ***요청에 대한 처리 로직에서 데이터에 대한 변경(Create, Update, Delete)이 이루어지는 경우 POST 방식을 사용한다.*** 그 외에는 GET 방식으로 처리한다.
> |GET|POST|
> |-|-|
> |주소값에 전달되는 값이 표시됨|표시되지 않음|
> |데이터가 보이므로 보안에 취약|보안에 우수|
> |데이터가 주소값에 표시되야 하므로 데이터 길이제한이 있음|길이 제한이 없으며 복잡한 형태의 데이터 또한 전송가능|
> |전송 속도가 빠름|상대적으로 느림|