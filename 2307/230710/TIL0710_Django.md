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

  ```




######################################################
jquery syntax
- The jQuery syntax is tailor-made for selecting HTML elements and performing some action on the element(s).
- Basic syntax - $(selector).action()
    - $ - define/access jQuery
    - (selector) - query(or find) HTML elements
    - jQuery action() - be performed on the element(s)
    - (ex) $(".test").hide() - hides all elements with class="test".


The Document Ready Event
- You might have noticed that all jQuery methods in our examples, are inside a document ready event:
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

jQuery Selectors
- jQuery selectors allow you to select and manipulate HTML element(s).
- jQuery selectors are used to "find" (or select) HTML elements based on their name, id, classes, types, attributes, values of attributes and much more. It's based on the existing CSS Selectors, and in addition, it has some own custom selectors.
- All selectors in jQuery start with the dollar sign and parentheses: $().
    - $(this) - Selects the current HTML element


jQuery Syntax For Event Methods
```js
$("p").click(function(){
  // action goes here!!
});
```






The button role is for clickable elements that trigger a response when activated by the user. Adding role="button" tells the screen reader the element is a button, but provides no button functionality.






[실습](./RestaurantShare/)