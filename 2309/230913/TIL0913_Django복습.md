# Django 복습

ToDoList에서 다룬 코드는 생략한다. 다루지 않은 함수나 방식을 위주로 적는다.

## 맛집 공유 사이트

프로젝트 만들기

app 생성하기 - 두 개의 app을 사용. 하나(shareRes)는 웹 페이지의 전반적인 CRUD 등을 처리하고, 하나(sendEmail)는 이메일을 발송하는 로직을 처리한다.

app을 settings.py에 추가하기

프로젝트명으로 된 폴더에 urls.py파일 수정

각 app에 urls.py 파일 생성하기

shareRes에 model.py파일에 모델 정의하기/makemigrations/migrate

Category에 대한 CRUD 기능 작업(이전 프로젝트와 동일, U빼고 구현)

Restaurant에 대한 CRUD 기능 작업 중 restaurant에 대한 model 정의 및 데이터베이스 반영/makemigrations/migrate
```python
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) #foreignkey 설정(카테고리를 삭제하면 기본 카테고리로 설정)
    restaurant_name = models.CharField(max_length = 100) #맛집 이름
    restaurant_link = models.CharField(max_length = 500) #맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length = 50) #키워드
```
`category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3) ` - 다른 모델을 참조한다는 것을 의미한다. <br>
`(Category)` - 해당 요소가 Category 모델을 참조한다는 의미이다. <br>
`(on_delete)` - 참조하는 요소가 삭제되었을 때 해당 요소는 어떻게 할지를 물어보는 항목이다.
> 우리가 내릴 수 있는 대표적인 4가지 옵션이 있다.
> - CASCADE: 참조되는 요소가 삭제될 때 이를 참조하는 모든 요소도 함께 삭제시킨다.
> - PROTECT: 참조되는 요소를 삭제하려고 할 때 해당 요소를 참조하는 요소가 하나라도 존재한다면 에러를 발생싴킨다. 에러 이름은 ProtectedError이다.
> - SET_NULL: 참조되는 요소가 삭제될 때 이를 참조하는 요소에 대해서 참조 값을 NULL로 설정한다. 이를 사용하려면 추가로 해당 값을 null로 가질 수 있도록 null=True 옵션을 설정해 주어야한다.
> - SET_DEFAULT: 참조되는 요소가 삭제될 때 이를 참조하는 요소에 대해서 참조 값을 설정해 둔 DEFAULT 값으로 설정한다.<br>

`on_delete=models.SET_DEFAULT, default=3`이므로 참조되는 요소가 삭제될 때 자동으로 ***id값이 3인 category를 참조***하도록 한다. 책에서 id가 3인 category_name은 '기본그룹'이다.<br>
fk의 경우 데이터를 저장하는 방식
```python
def Create_restaurant(request) :
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    # Category 모델을 통해 데이터를 받는다.
```
html에서 fk의 경우 데이터에 접근하는 방식 - `restaurant.category.category_name`
> Restaurant의 category, 즉 retaurant.category는 category 자체의 데이터를 의미하므로, category_name을 출력하려면 온점을 한 번 더 이용해 restaurant.category.category_name과 같이 접근해야 한다. (############## 추가 설명이 필요하다.)


<br>

Restaurant에 대한 R 기능 작업 중 restaurant 상세 페이지 url을 `<a href="restaurantDetail/{{restaurant.id}}">`로 설정했을 때 가져오는 방법과 이를 처리하기 위한 urls.py에 추가적인 설정
```python
urlpatterns = [
    ...

    path('restaurantDetail/<str:res_id>',views.restaurantDetail, name='resDetailPage'),

    ...
]
```
`<str:res_id>` - 이렇게 꺾쇠로 표현된 것은 동적인(변화되는) 값을 의미한다. 그리고 그 값을 꺾쇠 안에 있는 이름으로 서버에서 받아 내겠다는 의미이다. 콜론을 중심으로 좌측에는 어떤 데이터 타입으로 받을지를 결정해 주며, 우측은 어떤 이름으로 받을지를 결정해준다. 

<br>

이렇게 설정해 두었으면, 이를 서버에서 받아 처리하기 위해 view.py 파일을 수정한다.
```python
def restaurantDetail(request,res_id) :
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant': restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)
```
`def restaurantDetail(request,res_id) :` - 매개 변수로 res_id를 추가해 주었다. url을 통해서 오는 값은 GET 방식이 아니라면 request에 담기지 않아 이와 같이 추가적인 매개 변수로 받아 내야 서버에서 처리가 가능하다.
> url에 값이 나타나면, GET 방식이라고 하지 않았나요? <br>
> GET 방식으로 서버에 값을 전달하면 url에 변수 이름과 그 값이 나타난다고 설명했다. 그런데 위에서의 내용 또한 어떠한 값이 url에 나타나기에 이것이 GET방식이 아닌지 의문을 가질 수 있다. 하지만 이는 조금 다르다. GET 방식으로 서버에 값을 전달할 때 그 값이 url에 나타난다는 이야기와 url에 값이 나타난다고 해서 GET 방식이라는 이야기는 다르다. 또한 GET 방식에서는 url뒤에 물음표(?)로 시작해 '변수명=값'과 같은 형태를 가진다. 따라서 단순히 url자체의 값이 각 게시글마다 유동적으로 변화되게 하여 이를 처리하는 것임을 기억하자.

<br>

Restaurant에 대한 U 기능 작업 중 urls.py 수정 시 주의사항
```python
urlpatterns = [
    path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate, name='resUpdatePage'), # http://localhost:8000/restaurantDetail/updatePage/1
    ]
```
`path('restaurantDetail/updatePage/update',views.Update_restaurant, name='resUpdate')`가 `path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate, name='resUpdatePage')` 보다 아래줄에 지정되면 에러가 발생한다. url에 update부분이 `<str:res_id>`로 처리되기 때문이다.

<br>

Restaurant에 대한 U 기능 구현(전 프로젝트에서 다루지 않아 코드를 작성함. 하지만 보고 이해할 수 있을 코드라 설명은 생략)
```python
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
`HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))`에 이전에는 보지 못한 `kwargs={'res_id':resId}`가 있다. 먼저 `'resDetailPage'`라는 이름을 갖는 path부터 보자. `path('restaurantDetail/<str:res_id>',views.restaurantDetail, name='resDetailPage')`이다. `kwargs={'res_id':resId}`은 url에 `<str:res_id>`에서 `'res_id'`에 넣을 값을 지정하는 인자이다.