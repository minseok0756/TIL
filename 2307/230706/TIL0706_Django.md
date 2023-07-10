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
    - makemigrations 명령에 의해 polls/migrations 디렉토리 하위에 마이그레이션 파일들이 생김(0001_initial,py)

- python manage.py migrate - 데이터베이스에 변경사항을 반영함
- python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인함


URLconf, View 및 Template
- 로직의 흐름상 URLconf를 먼저 코딩한 후에 뷰,템플릿 또는 템플릿, 뷰 순서로 코딩하는 것이 일반적

URLconf
- 프로젝트 폴더의 공통 urls.py에 웹 앱의 url를 추가할 때마다 계속 추가하는 것은 번거로우므로 웹 앱별로 다른 ruls.py를 선언하고 프로젝트 폴더의 공통 urls.py에 해당 파일들을 포함하도록 만든다.
    - urls.py(C:\MyTest\projectsite\mysite) 파일에 코딩
        - [, path('polls/', include(polls.urls)), ]
    - urls.py(C:\MyTest\projectsite\mysite\polls) 파일에 코딩
        - [, path('url', views.함수명, name='')]
        - path(route, view, kwargs, name)
            - route - url pattern을 포함하는 string
                - 요청을 처리할 때 장고는 요청된 url과 urlpatterns을 위에서부터 차례로 비교하며 서치한다.
                - domain 이름이나 GET/POST parameter를 서치하지 않는다.
                - path parameter : url 사이에 있는 파라미터. 파라미터 타입을 정의한다.
                    - 파라미터 타입     
                    int : 정수형 숫자     
                    str : 모든 문자열       
                    slug : -(하이픈)이나 _(언더스코어)를 포함한 영숫자, 문자열
                        - ```'<int:question_id>/'``` - <파라미터타입:파라미터>
                        - 호출하는 view function에 question_id = int인자로 사용가능
                - 정규표현식을 사용해 url 패턴을 정의할 수 있다. 파라미터는 P<name>pattern 형태로 나타낸다.(re_path 함수를 사용한다.)
                    - re_path(r'^articles/(?P<year>[0-9]{4})/$', ...)
                    - articles로 시작하는 path에 year라는 파라미터를 보내는 데 이는 0부터 9사이의 4자리 숫자로 끝난다.
            - view - 장고가 매치되는 urlpattern을 찾으면 HttpRequest object를 첫 인자로 특정 view함수와 route로부터 any captured values를 keyword 인자로서 호출하는데, 호출되는 view 함수를 지정
            - name - url을 naming한다. naming한 url은 django어디서든지 참조할 수 있다. (특히 template에서)
        

View 및 Template
- 뷰함수와 템플릿은 서로에게 영향을 미치기 때문에 보통 같이 작업

    - view.index()
    ```python
      def index(request):
          latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
          context = {'latest_question_list': latest_question_list}
          return render(request, 'polls/index.html', context)
    ```
    - Question.objects.all() - Question의 모든 데이터 출력, 리스트로 반환
        - .order_by('pub_date')/('-pub_date') - pub_date를 기준으로 오름차순정렬/내림차순

    - 기존의 template 모듈의 loader로 템플릿를 불러오고 render로 인자를 넘기는 부분을 shortcuts 모듈의 render라는 단축 메소드로 코드를 줄일 수 있다.
        - 
        ```python
        # loader
        def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        template = loader.get_template("polls/index.html")
        context = {
            "latest_question_list": latest_question_list,
        }
        return HttpResponse(template.render(context, request))
        ```
        ```python
        # shortcut
        def index(request):
            latest_question_list = Question.objects.order_by("-pub_date")[:5]
            context = {"latest_question_list": latest_question_list}
            return render(request, "polls/index.html", context)
        ```
        - shortcuts으로 인해 HttpResponse없이 render(request, template파일경로, dict)만 하면됨
            - dict - key=(template에서 사용할 수 있는 변수명), value= (화면에 출력시 변수에 해당하는 값 출력)
            - render()는 HttpResponse object를 return
        


    - template 폴더가 없어 만들어서 코딩해야함
    - index.html
    ```html
        {% if latest_question_list %}
            <ul>
            {% for question in latest_question_list %}
                <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
    ```
    - {% %} - 명령어(제어문, 반복문, ...) 사용을 의미
        - {% if %} {% else %} {% endif %}
        - {% for %} {% endfor %}
    - latest_question_list - view에서 render()를 통해 넘겨준 변수
    - {{ 변수 }} - 변수값을 html에 출력
        - or 연산자로 나타내는 함수는 장고에 내장된 필터 함수이다. date 필터로 변수를 포매팅 가능하다
            - {{ current_date|date:"Y년 m월 d일 H시 i분 s초" }}
    - `<a href="/polls/{{ question.id }}/">` - `'<int:question_id>/'`url로 연결
        - view.detail() 실행

    
    - view.detail()
    ```python
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    ```
    - detail(request, question_id) - path parameter를 인자로 받아온다
    - get_object_or_404(모델, ...) - 모델에서 조건을 만족하는 레코드가 있으면 리턴하고, 없으면 404 에러발생(에러가 발생한 경우 render로 'error_message'가 넘어간다.)
        - Http404 exception
            - Django provides an Http404 exception
            - If you raise Http404 at any point in a view function, Django will catch it and return the standard error page for your application, along with an HTTP error code 404.
            - ```python
                def detail(request, question_id):
                    try:
                        question = Question.objects.get(pk=question_id)
                    except Question.DoesNotExist:
                        raise Http404("Question does not exist")
                    return render(request, "polls/detail.html", {"question": question})
            ```
        - A shortcut: get_object_or_404()
            - It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist
            - Django provides a shortcut
            - ```python
                from django.shortcuts import get_object_or_404

                def detail(request, question_id):
                    question = get_object_or_404(Question, pk=question_id)
                    return render(request, "polls/detail.html", {"question": question})
            ```
            - Question.objects.get(pk=1) == Question.objects.get(id=1)
    

    - detail.html
    ```html
    <h1>{{ question.question_text }}</h1>

    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

    <form action="{% url 'polls:vote' question.id %}" method="post">
    {% csrf_token %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
    {% endfor %}
    <input type="submit" value="Vote" />
    </form>
    ```
    - `<form action="{% url 'polls:vote' question.id %}" method="post">`
        - URL 별칭
            - URL 하드코딩 - url링크가 수정되는 경우 일일이 찾아가며 수정해야한다.
                - ```<a href="/polls/{{ question.id }}/">```
            - URL 별칭 사용하기
                - URL 매핑에 name 속성을 부여 - path('`<int:question_id>`/', views.detail, Name='detail')
                - ```<a href="{% url 'detail' question.id %}">```
                    - question.id는 URL 매핑에 정의된 path parameter에 전달해야 하는 값을 의미
                    - 이 때 파라미터 명을 함께 사용할수 있다.
                        - {% url 'detail' question_id=question.id %}
                    - 2개 이상의 파라미터를 사용해야 한다면 공백 문자 이후에 덧 붙여준다.
                        - {% url 'detail' question_id=question.id page=2 %}
            - 다른 앱이 프로젝트에 추가되어 서로 다른 앱에서 동일한 URL 별칭을 사용하여 중복이 발생하는 경우
                - polls/urls.py에 네임스페이스를 의미하는 app_name 변수를 지정
                    - app_name = 'polls'
                - app_name을 추가하여 url 별칭 사용
                    - ```<a href="{% url 'polls:detail' question.id %}">```
        - 제출시 POST method로 'vote' url에 제출

    - {% csrf token %} - POST method 사용시 보안을 위한 코드

    - question.choice_set.all
        - Model간 접근 - Question model을 Choice model이 참조
            - Choice객체 -> Question객체
                - c = Choice.objects.get(pk=1)
                - c.question - question은 fk로 지정된 Choice model의 ***필드명***(필드명으로 접근함)
                    - Choice모델에서 pk=1에 해당하는 레코드의 fk필드값과 연결된 Question모델의 레코드를 불러옴
                - c.question.question_text - 레코드에서 question_text 필드값을 불러옴
            - Choice객체 -> Question객체
                - q = Question.objects.get(pk=1)
                - q.choice_set.all() - .***(소문자)모델명***_set으로 Question model에 접근함
                    - .all() - 모든 데이터 반환
                    - .get()   
                    - .create() - 새로운 choice 객체를 만든다.
                    - .count() - 레코드 개수
                    - Choice.objects.filter() - where
                        - .delete() - delete
    
    - `<input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />`
        - POST method에서 key='choice', value='choice.id'
        - for문에서 index 사용(enumerate의 index 느낌)
                - forloop.counter - The current iteration of the loop(1-indexed)
                - forloop.counter() - The current iteration of the loop(0-indexed)
                - forloop.revcounter - The number of iterations from the end of the loop(1-indexed)
                - forloop.revcounter() - The number of iterations from the end of the loop(0-indexed)
                - forloop.first - True if this is the first time through the loop
                - forloop.last - True if this is the last time through the loop
    
    - 'vote' url로 제출 - view.vote() 호출


    - view.vote()
    ```python
    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    ```
    - `selected_choice = question.choice_set.get(pk=request.POST['choice'])`
        - request.POST - key name을 통해 제출된 데이터에 접근하게 해주는 dictionary-like object
            - 항상 string으로 반환
            - request.POST['choice'] - 제출된 data에서 key name이 'choice'인 value를 string으로 반환
    - ```python
        except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
      ```
        - KeyError(python exception) - Raised when a mapping (dictionary) key is not found in the set of existing keys      
        DoesNotExist - Question matching query does not exist.(KeyError과 같은 오류)
            - 'choice'와 매치되는 key name이 없으면 error_message와 함께 detail.html을 다시 보여줌
    - ```python
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
      ```
        - selected_choice.save() - sql commit
        - return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
            - HttpResponseRedirect - HttpResponseRedirect takes a single argument: the URL to which the user will be redirected
        - reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None) - reverse helps avoid having to hardcode a URL in the view function
            - viewname can be a ***URL pattern*** name or the callable view object
                - 'polls:results'
            - If the URL accepts arguments, you may pass them in args
                - args=(question.id,)
        - 'result' url로 redirect - view.result 호출

    
    - view.result()
    ```python
    def results(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})
    ```

    - view.html
    ```html
    <h1>{{ question.question_text }}</h1>

    <ul>
    {% for choice in question.choice_set.all %}
        <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
    {% endfor %}
    </ul>

    <a href="{% url 'polls:detail' question.id %}">Vote again?</a>
    ```
    - <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
        - x|pluralize - x가 1이 아니면 x끝에 's'를 붙여서 출력



주의 - 두 프롬프트가 같은 서버를 올리면 웹 브라우저가 제대로 request하지 못한다

[실습](./projectsite/)