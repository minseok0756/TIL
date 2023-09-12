# Django 복습

## Django 설치하기

Django 설치 <br>
`C:\>pip install Django`

Django 버전확인 <br>
`C:\>python -m django -version`

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

프로젝트app에 urls.py파일에 urlpatterns에 `path('admin/', admin.site.urls)` 는 사용자가 'admin/'이라는 주소로 접근했을 때, 즉 실제로는 "http://127.0.0.1:8000/admin"에 접근했을 때 admin.site.urls로 접근하라는 의미이다. 기본적으로 제공하는 admin 관련 app의 urls.py로 넘겨서 처리하겠다는 의미이다. 

사용자가 ''에 접근했을 때 myapp의 urls.py파일로 처리를 넘겨준다. <br>
`path('', include('myapp'))` - myapp은 직접 새롭게 추가한 app이기 때문에 include라는 함수를 사용해야 한다. include 함수를 사용하기위해 import한다. `from django.urls import include`

myapp의 urls.py에서 다시 한 번 처리한다. myapp폴더에는 아직 urls.py파일이 없는데 만들어 준다.
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
]
```
특정 URL로 접근한 사용자에게 보여 줄 화면을 처리할 함수를 연결해야 하는데, 이는 같은 경로의 view.py 파일이 담당한다. 특정 위치로 접근한 사용자에게 어떤 화면을 보여 줄지 실제로 처리하는 것이 view.py 파일이다. 따라서 해당 파일도 import해준다. from 뒤의 .은 같은 경로임을 의미한다.

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
`select * from 테이블명;` - 데이터를 확인한다.

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
     # return HttpResponse("DB에 저장되었어요 =>" + user_input_str)
```
서버는 함수의 인자인 request로 데이터를 받아온다. request에서 index.html의 input태그속성 중 name값을 이용해서 input 태그 안에 있는 문자열을 받아올 수 있다. POST방식으로 제출했으므로 request에서 POST에 접근한다. - `request.POST['todoContent]` <br>
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