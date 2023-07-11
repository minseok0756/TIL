# Django

mini project - 맛집 공유 사이트

MVT 코딩 순서
- 프로젝트 뼈대 만들기 : 프로젝트 및 앱 개발에 필요한 디렉토리와 파일
생성
- 모델 코딩하기 : 테이블 관련 사항을 개발(models.py, admin.py 파일)
- URLconf 코딩하기 : URL 및 뷰 매핑 관계를 정의(urls.py 파일)
- 템플릿 코딩하기 : 화면 UI 개발(templates/ 디렉토리 하위의 *.html 파일들)
- 뷰 코딩하기 : 애플리케이션 로직 개발(views.py 파일)


프로젝트 뼈대 만들기 순서 명령
- (base) C:\MyTest>django-admin startproject RestaurantShare - RestaurantShare라는 프로젝트 생성
- (base) C:\MyTest\RestaurantShare >python manage.py startapp
shareRes - shareRes라는 애플리케이션 생성
- (base) C:\MyTest\RestaurantShare> python manage.py startapp
sendEmail - sendEmail라는 애플리케이션 생성
- (base) C:\MyTest\RestaurantShare\RestaurantShare>notepad settings.py - 설정 파일 확인 및 수정
    - INSTALLED_APPS =[ ~, 'shareRes’, 'sendEmail', ]
    - #TIME_ZONE = 'UTC'        
    TIME_ZONE = 'Asia/Seoul'
- (base) C:\MyTest\RestaurantShare>python manage.py migrate - 데이터베이스에 기본 테이블을 생성
    - db.sqlite3가 생성됨
- (base) C:\MyTest\RestaurantShare>python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인
    - (base) C:\MyTest\RestaurantShare>python manage.py runserver 127.0.0.1:8000
    - (base) C:\MyTest\RestaurantShare>python manage.py runserver 0:8000

Admin 사이트 접속
- 기본적으로 제공하는 Admin 사이트에 접속해서 테이블이 생성되었는지 확인
- 브라우저의 주소창에 IP 주소와 포트번호 동일, URL경로만 /admin 추가
    - http://127.0.0.1:8000/admin
- Admin 사이트에 로그인하기 위한 관리자(슈퍼유저)를 생성
    - (base) C:\MyTest\RestaurantShare>python manage.py createsuperuser
- Admin 사이트에서 Users와 Groups 테이블을 포함하여 새롭게 만들 테이블에 대한 데이터의 입력, 변경, 삭제 등의 작업을 할 수 있음
- Admin 화면에서 기본적으로 Users와 Groups 테이블이 보이는 것은 이미 settings.py 파일에 django.contrib.auth 애플리케이션이 등록되어있기 때문
- 즉 장고에서 기본으로 제공하는 auth 앱에 Users와 Groups 테이블이 미리 정의

골격 생성
- (base) C:\MyTest>tree /F RestaurantShare


Model 코딩
- 모델 작업은 데이터베이스에 테이블을 생성하는 작업
- notepad models.py - 테이블을 정의하기 위해 메모장으로 models.py 열기
    - ```python
        class Category(models.Model):
            category_name = models.CharField(max_length = 100)

        class Restaurant(models.Model):
            category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) #foreignkey 설정(카테고리를 삭제하면 기본 카테고리로 설정)
            restaurant_name = models.CharField(max_length = 100) #맛집 이름
            restaurant_link = models.CharField(max_length = 500) #맛집 URL
            restaurant_content = models.TextField() # 맛집 설명
            restaurant_keyword = models.CharField(max_length = 50) #키워드
      ```
- notepad admins.py - 정의된 테이블이 Admin 화면에 보이게 등록하기 위해 메모장으로 admins.py 열기
    - admin.site.register(Category)     
    admin.site.register(Restaurant)
- (base) C:\MyTest\RestaurantShare>python manage.py makemigrations - 데이터베이스에 변경이 필요한 사항을 추출함
    - makemigrations 명령에 의해 polls/migrations 디렉토리 하위에 마이그레이션 파일들이 생김(0001_initial,py)
- python manage.py migrate - 데이터베이스에 변경사항을 반영함
- python manage.py runserver - 현재까지 작업을 개발용 웹 서버로 확인함


URLconf, View 및 Template
- 로직의 흐름상 URLconf를 먼저 코딩한 후에 뷰,템플릿 또는 템플릿, 뷰 순서로 코딩하는 것이 일반적

URLconf
- 프로젝트 폴더의 공통 urls.py에 웹 앱의 url를 추가할 때마다 계속 추가하는 것은 번거로우므로 웹 앱별로 다른 ruls.py를 선언하고 프로젝트 폴더의 공통 urls.py에 해당 파일들을 포함하도록 만든다.
    - urls.py(C:\MyTest\RestaurantShare\RestaurantShare) 파일에 코딩
        - ```python
            [
                path('admin/', admin.site.urls),
                path('', include('shareRes.urls')),
                path('sendEmail/', include('sendEmail.urls')),
            ]
          ```
    - urls.py(C:\MyTest\RestaurantShare\shareRes) 파일에 코딩
        - ```python
            [
            path('', views.index, name='index'),

            path('restaurantDetail/delete',views.Delete_restaurant, name='resDelete'),
            path('restaurantDetail/<str:res_id>',views.restaurantDetail, name='resDetailPage'), # http://localhost:8000/restaurantDetail/1 요청처리
            path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate'),
            path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate, name='resUpdatePage'), # http://localhost:8000/restaurantDetail/updatePage/1

            path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'), #http://localhost:8000/restaurantCreate
            path('restaurantCreate/create',views.Create_restaurant,name='resCreate'), ##http://localhost:8000/restaurantCreate/create

            path('categoryCreate/',views.categoryCreate, name='cateCreatePage'),
            path('categoryCreate/create',views.Create_category, name='cateCreate'),
            path('categoryCreate/delete',views.Delete_category, name='cateDelete'),
            ]
          ```
    - urls.py(C:\MyTest\RestaurantShare\sendEmail) 파일에 코딩
        - ```python
            [
            path('send/', views.sendEmail) #http://localhost:8080/seneEmail/send/ 호출시 매칭
            ]
          ```

View 및 Template
- 뷰함수와 템플릿은 서로에게 영향을 미치기 때문에 보통 같이 작업
- ```python
    def index(request):
        categories = Category.objects.all()
        restaurants = Restaurant.objects.all()
        content = {'categories': categories, 'restaurants': restaurants}
        return render(request, 'shareRes/index.html', content)
        # return HttpResponse("index")
        # return render(request,'shareRes/index.html')
  ```

- index.html
- ```html
    <a href="categoryCreate/" class="categoryAddBtn btn btn-info" role="button">+</a>
  ```
    - role="button" - The button role is for clickable elements that trigger a response when activated by the user. Adding role="button" tells the screen reader the element is a button, but provides no button functionality.
    - href="categoryCreate/" -> view.categoryCreate

    - ```python
        def categoryCreate(request) : #기존 카테고리 출력
            categories = Category.objects.all()
            content = {'categories': categories}
            # return HttpResponse("categoryCreate")
            return render(request, 'shareRes/categoryCreate.html',content)
      ```

    - ```html
        <form action="./create" method="POST" onsubmit="return categoryAddCheckFrom();">{% csrf_token %}
            <div class="input-group">
                <input type="submit" class="resAddBtn btn btn-success" role="button" value="추가"/>
                <input id="categoryName" name="categoryName" type="text" class="form-control" placeholder="추가할 카테고리명을 입력하세요." style="width:650px; float:right; border-radius:4px;">
            </div>
        </form>
        <a href ="/" class="resAddBtn btn btn-info" role="button">홈으로</a>
      ```
        - onsubmit="return categoryAddCheckFrom();" - 함수를 실행시켜 true값을 리턴해야 제출됨     
        ```html
        <script>
            function categoryAddCheckFrom(){
                if($('#categoryName').val().length <= 0){
                    alert('추가할 카테고리 이름을 입력해주세요.')
                    $('#categoryName').focus()
                    return false;
                }
                else{
                    return true;
                }
            }
        </script>
        ```
            - jquery syntax
                - The jQuery syntax is tailor-made for selecting HTML elements and performing some action on the element(s).
                - Basic syntax - $(selector).action()
                    - $ - define/access jQuery
                    - (selector) - query(or find) HTML elements
                        - It's based on the existing CSS Selectors
                    - jQuery action() - be performed on the element(s)
            - $('#categoryName') - id = categoryName인 태그 선택
                - <input id="categoryName" name="categoryName" type="text" class="form-control" placeholder="추가할 카테고리명을 입력하세요." style="width:650px; float:right; border-radius:4px;">
            - .val() - returns the value of the value attribute of the FIRST matched element.
                - <input>에 입력한 값을 반환
                - .length - 반환된 글자의 개수
            - .focus() - The focus() method triggers the focus event
                - The focus event occurs when an element gets focus (when selected by a mouse click or by "tab-navigating" to it)
                - 반환된 글자수가 0보다 작거나 같으면 <input>태그에 focus event가 발생된다.

        - "./create" url에 POST method로 key = 'categoryName' value = text에 적힌 데이터를 submit. - views.Create_category()
            - ```python
                def Create_category(request): # 카테고리 새로 추가하기
                    category_name = request.POST['categoryName']
                    new_category = Category(category_name = category_name)
                    new_category.save()
                    return HttpResponseRedirect(reverse('index'))
                    # return HttpResponse("여기서 category Create 기능을 구현할거야.")
              ```
                - index url로 요청

    - categoryCreate.html 나머지부분
    - ```html
        {% for category in categories %}
        {% if category.id == 3%}
            <div class="input-group">
                <span class="input-group-addon" style="border:1px solid #ccc; border-radius: 4px;">{{ category.category_name }}</span>
            </div>
        {% endif %}
        {% endfor %}
      ```
    - ```html
        {% for category in categories %}
        {% if category.id != 3%}
        <form action="./delete" method="POST">{% csrf_token %}
            <div class="input-group">
                <span class="input-group-addon" id="" style="border:1px solid #ccc; border-radius: 4px;">{{category.category_name}}</span>
                <input type="hidden" name="categoryId" id="categoryId" value="{{category.id}}"/>
                <input type="submit" class="resAddBtn btn btn-danger" role="button" value="삭제"/>
            </div>
        </form>
        {% endif %}
        {% endfor %}
      ```
        - "./delete" url에 POST method로 key = 'categoryId' value = category.id 데이터를 submit - views.Delete_category()
        - ```python
            def Delete_category(request):
                category_id = request.POST['categoryId']
                delete_category = Category.objects.get(id = category_id)
                delete_category.delete()
                return HttpResponseRedirect(reverse('cateCreatePage'))
          ```
            - url name = 'cateCreatePage' url로 요청 
                - views.categoryCreate()
                - shareRes/categoryCreate.html
                - 삭제된 카테고리 데이터를 기반으로 카테고리 추가하기 페이지 다시 구성
                - 웹 브라우저에서는 삭제버튼을 누르면 해당 카테고리가 삭제됨
    - ```html
        <a href ="/" class="resAddBtn btn btn-info" role="button">홈으로</a>
      ```
        - index.html 화면으로


- index.html - `<a>`이후 다음부분
- ```html
    <ul class="restaurantListDiv nav nav-pills nav-stacked">

        {% for category in categories %}
        <li class="category deactive">{{ category.category_name}}</li>
        <ul class="restaurantList">

            {% for restaurant in restaurants %}
            {% if restaurant.category == category %}
            <div class="input-group">
                <span class="input-group-addon">
                    <input name="checks" id="check{{restaurant.id}}" type="checkbox" value="{{restaurant.id}}">
                </span>
                <a href="restaurantDetail/{{restaurant.id}}">
                    <input name="res{{restaurant.id}}" id="res{{restaurant.id}}"
                        type="text" class="form-control" disabled style="cursor: pointer;" value="{{restaurant.restaurant_name}}">
                </a>
            </div>
            {% endif %}
            {% endfor %}

        </ul>
        {% endfor %}
    </ul>
  ```
    - ```html
        <script>
            $(document).ready(function(){
                $('.restaurantListDiv>li').click(function(){
                    if ($(this).hasClass('active')){
                        $(this).addClass('deactive')
                        $(this).removeClass('active')
                        $(this).next('ul').slideUp();
                    }else{
                        $(this).removeClass('deactive')
                        $(this).addClass('active')
                        $(this).next('ul').slideDown();
                    }

                    
                })
            });
        </script>    
      ```
        - $(document).ready() - The Document Ready Event
            - ```js
                $(document).ready(function(){

                    // jQuery methods go here...
                });
              ```
                - This is to prevent any jQuery code from running before the document is finished loading (is ready).
                - It is good practice to wait for the document to be fully loaded and ready before working with it.
                - 같은표현      
                ```js
                $(function(){

                // jQuery methods go here...

                });
                ```
        - $('.restaurantListDiv>li') 
            - <ul class="restaurantListDiv nav nav-pills nav-stacked"> 자식태그인
            - <li class="category deactive">{{ category.category_name}}</li> 선택
        - .click() - click event
        - $(this) - Selects the current HTML element
            - <li>를 의미
        - .hasClass('active') - active클래스를 가지고 있는지 확인
        - .addClass('deactive) - deactive클래스 추가
        - .removeClass('active') - active클래스 제거
        - .next('ul') - <li>태그의 바로 뒤 형제태그 중 <ul>태그
            - .slideUp() - <ul>태그를 slide up
            - .slideDown() - <ul>태그를 slide down
    
    - `<a href="restaurantDetail/{{restaurant.id}}"></a>` - 'restaurantDetail/`<str:res_id>`' url로 이동
        - views.restaurantDetail()
        - ```python
            def restaurantDetail(request,res_id) :
                restaurant = Restaurant.objects.get(id = res_id)
                content = {'restaurant': restaurant}
                # return HttpResponse("restaurantDetail")
                return render(request, 'shareRes/restaurantDetail.html', content)
          ```
        - ```html
            <script>
                function checkFrom(){
                    if ($('#resTitle').val().length <= 0){
                        alert("맛집 이름을 입력해주세요.")
                        $('#resTitle').focus()
                        return false
                    }else if($('#resLink').val().length <= 0){
                        alert("관련 링크를 입력해주세요.")
                        $('#resLink').focus()
                        return false
                    }else if($('#resContent').val().length <= 0){
                        alert("상세 내용을 입력해주세요.")
                        $('#resContent').focus()
                        return false
                    }else if($('#resLoc').val().length <= 0){
                        alert("장소 키워드를 입력해주세요.")
                        $('#resLoc').focus()
                        return false
                    }else{
                        return true
                    }
                }
            </script>

            <div class="input-group">
                <span class="input-group-addon" id="sizing-addon2">카테고리</span>
                <input id="resCategory" name="resCategory" type="text" class="form-control" disabled
                       value="{{restaurant.category.category_name}}">
            </div>
            <div class="input-group">
                <span class="input-group-addon" id="sizing-addon2">맛집 이름</span>
                <input id="resTitle" name="resTitle" type="text" class="form-control" disabled
                        value="{{restaurant.restaurant_name}}">
            </div>
            <div class="input-group">
                <span class="input-group-addon" id="sizing-addon2">관련 링크</span>
                <input id="resLink" name="resLink" type="text" class="form-control" disabled
                        value="{{restaurant.restaurant_link}}">
            </div>
            <div class="input-group">
                <span class="input-group-addon" id="sizing-addon2">상세 내용</span>
                <textarea id="resContent" name="resContent" cols="90" rows="10" disabled value="">
                    {{restaurant.restaurant_content}}
                </textarea>
            </div>
            <div class="input-group">
                <span class="input-group-addon" id="sizing-addon2">장소 키워드</span>
                <input id="resLoc" name="resLoc" type="text" class="form-control" disabled value="{{restaurant.restaurant_keyword}}">
            </div>

            <form action="./delete" method="POST">{% csrf_token %}
                <input type="hidden" id="resId" name="resId" value="{{restaurant.id}}"/>
                <input type="submit" class="resAddBtn btn btn-danger" value="삭제하기">
            </form>
          ```
            - 'restaurantDetail/delete' url에 POST method로 key = resId, value = restaurant.id 데이터를 제출 - views.Delete_restaurant()
                - ```python
                    def Delete_restaurant(request):
                        res_id = request.POST['resId']
                        restaurant = Restaurant.objects.get(id = res_id)
                        restaurant.delete()
                        return HttpResponseRedirect(reverse('index'))
                  ```
                    - 해당 레코드 삭제 후 'index' url로 요청 

        - restaurantDetail.html 나머지 부분
        - ```html
            <a href ="/" class="resAddBtn btn btn-info" role="button">홈으로</a>
          ```
            - 'index' url로 이동
        - ```html
            <a href ="./updatePage/{{restaurant.id}}" class="resAddBtn btn btn-danger" role="button">수정하기</a>
          ```
            - 'restaurantDetail/updatePage/`<str:res_id>`'로 이동 - views.restaurantUpdate()
            - ```python
                def restaurantUpdate(request,res_id):
                    categories = Category.objects.all()
                    restaurant = Restaurant.objects.get(id = res_id)
                    # print(restaurant)
                    content = {'categories': categories, 'restaurant': restaurant}
                    return render(request, 'shareRes/restaurantUpdate.html', content)
              ```
                - ```html
                    <script>
                        function checkFrom(){
                            if ($('#resTitle').val().length <= 0){
                                alert("맛집 이름을 입력해주세요.")
                                $('#resTitle').focus()
                                return false
                            }else if($('#resLink').val().length <= 0){
                                alert("관련 링크를 입력해주세요.")
                                $('#resLink').focus()
                                return false
                            }else if($('#resContent').val().length <= 0){
                                alert("상세 내용을 입력해주세요.")
                                $('#resContent').focus()
                                return false
                            }else if($('#resLoc').val().length <= 0){
                                alert("장소 키워드를 입력해주세요.")
                                $('#resLoc').focus()
                                return false
                            }else{
                                return true
                            }
                        }
                    </script>

                    <form action="./update" method="POST" onsubmit="return checkFrom();">{% csrf_token %}
                        <span class="input-group-addon" id="sizing-addon2">카테고리</span>
                        <select id="resCategory" name="resCategory" class="resCategory" size="1" required autofocus>
                            {% for category in categories %}
                            {% if category == restaurant.category %}
                            <option value="{{category.id}}" selected>{{category.category_name}}</option>
                            {% else %}
                            <option value="{{category.id}}">{{category.category_name}}</option>
                            {% endif %}
                            {% endfor %}
                        </select>  
                        </div>
                        <div class="input-group">
                            <span class="input-group-addon" id="sizing-addon2">맛집 이름</span>
                            <input id="resTitle" name="resTitle" type="text" class="form-control" placeholder="맛집 이름을 입력해주세요."
                                aria-describedby="sizing-addon2" value="{{restaurant.restaurant_name}}">
                        </div>
                        <div class="input-group">
                            <span class="input-group-addon" id="sizing-addon2">관련 링크</span>                                         <input id="resLink" name="resLink" type="text" class="form-control" placeholder="관련 링크를 입력해주세요."
                                aria-describedby="sizing-addon2" value="{{restaurant.restaurant_link}}">
                        </div>
                        <div class="input-group">
                            <span class="input-group-addon" id="sizing-addon2">상세 내용</span>
                            <textarea id="resContent" name="resContent" cols="90" rows="10" placeholder="상세 내용을 입력해주세요.">
                                {{restaurant.restaurant_content}}
                            </textarea>
                        </div>
                        <div class="input-group">
                            <span class="input-group-addon" id="sizing-addon2">장소 키워드</span>
                            <input id="resLoc" name="resLoc" type="text" class="form-control" placeholder="장소 키워드를 입력해주세요."
                                aria-describedby="sizing-addon2" value="{{restaurant.restaurant_keyword}}">
                        </div>
                        <input type="hidden" id="resId" name="resId" value="{{restaurant.id}}"/>
                        <input type="submit" class="resAddBtn btn btn-info" role="button" value="맛집 수정!"/>
                        </div>
                    </form>
                  ```
                    - 'restaurantDetail/updatePage/update' url에 POST method로 {'resCategory':category.id}, "resTitle":'restaurant.restaurant_name', "resLink":'restaurant.restaurant_link', "resContent":'restaurant.restaurant_content', "resLoc":'restaurant.restaurant_keyword', "resId":restaurant.id} 데이터를 checkFrom 함수가 true를 리턴하면 제출 - views.Update_restaurant()
                        - ```python
                            def Update_restaurant(request):
                                print("여기 왔나요?")
                                resId = request.POST['resId']
                                change_category_id = request.POST['resCategory']
                                change_category = Category.objects.get(id = change_category_id)
                                change_name = request.POST['resTitle']
                                change_link = request.POST['resLink']
                                change_content = request.POST['resContent']
                                change_keyword = request.POST['resLoc']
                                before_restaurant = Restaurant.objects.get(id = resId)
                                before_restaurant.category = change_category
                                before_restaurant.restaurant_name = change_name
                                before_restaurant.restaurant_link = change_link
                                before_restaurant.restaurant_content = change_content
                                before_restaurant.restaurant_keyword = change_keyword
                                before_restaurant.save()
                                return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))
                          ```
                            - 수정된 데이터를 Restaurant model에 저장
                            - 'resDetailPage' url로 요청 - views.restaurantDetail()
                                - ```python
                                    def restaurantDetail(request,res_id) :
                                        restaurant = Restaurant.objects.get(id = res_id)
                                        content = {'restaurant': restaurant}
                                        # return HttpResponse("restaurantDetail")
                                        return render(request, 'shareRes/restaurantDetail.html', content)
                                  ```
                                    - 수정된 데이터를 기반으로 restaurantDetail.html이 변경되어 있음

- index.html - `<a>`이후 다음부분
- ```html
    <a href="restaurantCreate/" class="sendBtn btn btn-info" role="button">맛집 추가하기</a>
  ```
    - "restaurantCreate/" url로 이동 - restaurantCreate()
    - ```python
        def restaurantCreate(request) :
            categories = Category.objects.all()
            content = {'categories': categories}
            # return HttpResponse("restaurantCreate")
            return render(request,'shareRes/restaurantCreate.html',content)
      ```
    - ```html
        <script>
            function checkFrom(){
                if ($('#resTitle').val().length <= 0){
                    alert("맛집 이름을 입력해주세요.")
                    $('#resTitle').focus()
                    return false
                }else if($('#resLink').val().length <= 0){
                    alert("관련 링크를 입력해주세요.")
                    $('#resLink').focus()
                    return false
                }else if($('#resContent').val().length <= 0){
                    alert("상세 내용을 입력해주세요.")
                    $('#resContent').focus()
                    return false
                }else if($('#resLoc').val().length <= 0){
                    alert("장소 키워드를 입력해주세요.")
                    $('#resLoc').focus()
                    return false
                }else{
                    return true
                }
            }
        </script>

        <form action="./create" method="POST" onsubmit="return checkFrom();">{% csrf_token %}
            <div class="inputDiv">
                <div class="input-group">
                    <span class="input-group-addon" id="sizing-addon2">카테고리</span>
                    <select id="resCategory" name="resCategory" class="resCategory" size="1" required autofocus>
                        {% for category in categories %}
                        {% if category.id == 3 %}
                        <option value="{{category.id}}" selected>{{category.category_name}}</option>
                        {% else %}
                        <option value="{{category.id}}">{{category.category_name}}</option>
                        {% endif %}
                        {% endfor %}
                    </select>  
                </div>
                <div class="input-group">
                    <span class="input-group-addon" id="sizing-addon2">맛집 이름</span>
                    <input id="resTitle" name="resTitle" type="text" class="form-control" placeholder="맛집 이름을 입력해주세요." aria-describedby="sizing-addon2">
                </div>
                <div class="input-group">
                    <span class="input-group-addon" id="sizing-addon2">관련 링크</span>
                    <input id="resLink" name="resLink" type="text" class="form-control" placeholder="관련 링크를 입력해주세요." aria-describedby="sizing-addon2">
                </div>
                <div class="input-group">
                    <span class="input-group-addon" id="sizing-addon2">상세 내용</span>
                    <textarea id="resContent" name="resContent" cols="90" rows="10" placeholder="상세 내용을 입력해주세요."></textarea>
                </div>
                <div class="input-group">
                    <span class="input-group-addon" id="sizing-addon2">장소 키워드</span>
                    <input id="resLoc" name="resLoc" type="text" class="form-control" placeholder="장소 키워드를 입력해주세요." aria-describedby="sizing-addon2">
                </div>
                <input type="submit" class="resAddBtn btn btn-info" role="button" value="맛집 추가!"/>
            </div>
        </form>
      ```
        - 'restaurantCreate/create' url에 POST method로 {'resCategory':category.id}, "resTitle":'text', "resLink":'text', "resContent":'text', "resLoc":'text'} 데이터를 checkFrom 함수가 true를 리턴하면 제출 - views.Create_restaurant()
        - ```python
            def Create_restaurant(request) :
                category_id = request.POST['resCategory']
                category = Category.objects.get(id = category_id)
                name = request.POST['resTitle']
                link = request.POST['resLink']
                content = request.POST['resContent']
                keyword = request.POST['resLoc']
                new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link,
                                    restaurant_content = content, restaurant_keyword = keyword)
                new_res.save()
                return HttpResponseRedirect(reverse('index'))
          ```
            - POST method로 넘어온 데이터를 기반으로 Restaurant model에 새로운 레코드 생성
            - 'index' url로 요청 - views.index()
            - 새로운 레코드를 기반으로 index.html 구성

- index.html 나머지 부분
- ```html
    <script>
    function emailCheckForm(){
        var isCheckLessThanOne = true
        for(i = 1; i <= 6; i++){
            var idString = "check"+i
            var isChecked = $("#"+idString).is(':checked')
            console.log("check"+i,isChecked)
            if (isChecked){
                isCheckLessThanOne = false
                break
            }
        }
        console.log(isCheckLessThanOne)
        if($('#inputReceiver').val().length <= 0){
            alert("이메일 수신자를 1명 이상 입력해주세요.")
            $('#inputReceiver').focus()
            return false
        }else if($('#inputTitle').val().length <= 0){
            alert("이메일 제목을 입력해주세요.")
            $('#inputTitle').focus()
            return false
        }else if(isCheckLessThanOne){
            alert("맛집을 하나 이상 선택해주세요.")
            return false
        }else{
            return true;
        }
    }
    </script>
  ```
    - .is() - checks if one of the selected elements matches the selectorElement
        - the selected elements - "#"+idString
        - the selectorElement - :checked
    - :checked - selects all checked checkboxes or radio buttons

  ```html
    <form action="./sendEmail/send/" method="POST" onsubmit="return emailCheckForm();"> 
        <input name="checks" id="check{{restaurant.id}}" type="checkbox" value="{{restaurant.id}}">
        <input name="res{{restaurant.id}}" id="res{{restaurant.id}}"
        type="text" class="form-control" disabled style="cursor: pointer;" value="{{restaurant.restaurant_name}}">


        <div class="emailContentHeader">
            <h4>수신자 <span class="inputReceiverSub">콤마(,)로 구분해서 여러명에게 보낼 수 있습니다.</span></h4>
            <input class="inputReceiver" name="inputReceiver" id="inputReceiver" type="text" placeholder="수신자를 적어주세요."/><br/>
        </div>
        <div class="emailContentHeader">
            <h4>제목</h4>
            <input class="inputTitle" name="inputTitle" id="inputTitle" type="text" placeholder="제목을 적어주세요."/><br/>
        </div>
        <div class="emailContent">
            <h4>인사말</h4>
            <textarea class="inputContent" name="inputContent" id="inputContent" cols="50" rows="10" placeholder="인사말을 적어주세요."></textarea>
        </div>
                                    
        </div>
        <div>
            <input type="submit" class="sendBtn btn btn-info" role="button" value="이메일 발송하기"/>
        </div>    
    </form>
  ```
    - 'send/' url에 POST method로 {"checks":restaurant.id}, "res{{restaurant.id}}":'restaurant.restaurant_name', "inputReceiver":'text', "inputTitle":'text', "inputContent":'text'} 데이터를 emailCheckForm 함수가 true를 리턴하면 제출 - views.sendEmail()
    - ```python
        def sendEmail(request):
            return HttpResponse("sendEmail")
      ```

---

[실습](./RestaurantShare/)