# Django 복습

ToDoList에서 다룬 코드는 생략한다. 다루지 않은 함수나 방식을 위주로 적는다.

## 맛집 공유 사이트

### 이메일 보내기

메일을 보내는 데는 SMTP라는 메일 발송 서버를 이용해야 한다. 쉽게는 구글과 네이버 SMPT를 이용할 수 있다. 구글의 SMPT를 사용한다. 

이메일 발송 기능 구현 <br>
1. 사용자가 선택한 맛집 및 입력한 내용 받아 오기<br>
```python
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list, '/', inputReceiver, '/', inputTitle, '/', inputContent)
    return HttpResponseRedirect(reverse('index'))
```
`request.POST.getlist('checks')` - getlist 함수를 이용하면 html의 input태그에서 하나의 name에 여러 value값을 서버에 넘겨준 경우, 이 데이터를 list로 받아올 수 있다.

2. 사용자가 선택한 맛지과 인사말을 이용해서 이메일 본문 작성하기 <br>
본문을 작성할 때는 html 형태로 만들어야 한다.
```python
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(request):
    ... # 위 1 코드 생략
    
    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>" + inputContent + "<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"
    
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>" + restaurant.restaurant_name + "</h2>"
        mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
        mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"
    # print(mail_html)
    return HttpResponseRedirect(reverse('index'))
```
`import smtplib` - 이메일을 발송하기 위해 필요한 라이브러리를 import 한다. <br>
`from email.mime.text import MIMEText` - 메일 본문을 html 형태로 나타내기 위한 라이브러리를 import 한다. <br>
`from email.mime.multipart import MIMEMultipart` - html 형태의 메시지를 포함하는 메시지 객체를 위한 라이브러리를 import한다. <br>
html 작성 방법에 대한 정보는 없었다. <br>
`mail_html += "<h2>" + restaurant.restaurant_name + "</h3>"`에서 `</h2>`를 사용하지 않은 이유 <br>
`mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"`에서 `"<p>"`앞 뒤로 '+'를 사용한 이유를 모르겠다.


3. 사용자가 입력한 수신자에게 입력한 제목과 2에서 완성한 본문으로 이메일 발송하기
`from email.mime.text import MIMEText`, `from email.mime.multipart import MIMEMultipart` 사용법 - https://stackoverflow.com/questions/882712/sending-html-email-using-python
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative') # 객체 생성
msg['Subject'] = "Link" # 이메일 제목 설정
msg['From'] = me # 수신자의 이메일을 적는다.
                 # 다중 사용자에게 보내려면 리스트 형태로 수신자를 설정한다.
                 # 본 프로젝트의 경우 inputReceiver에 대해 split함수를 통해 리스트 형태로 쪼갠다.
msg['To'] = you # 발신자의 이메일을 적는다.

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org" # a plain-text
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
""" # an HTML version

# Record the MIME types of both parts - text/plain and text/html.
# 구성한 문자열에 대해서 MIMEText 객체로 만듦
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost') # 메일 발송 서버 객체 만듦
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string()) # 메일 발송
s.quit()
```

위 코드는 구글 서버를 사용하는 것이 아니다.<br> 
구글 서버를 사용하는 방법 https://stackabuse.com/how-to-send-emails-with-gmail-using-python/에서 'Authenticating with Gmail'부분
```python
import smtplib

gmail_user = 'you@gmail.com'
gmail_password = 'P@ssword!'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print 'Something went wrong...'
```
이와 같이 코드를 구현하더라도 오류가 발생한다. 구글 측에서 외부 특정 계정에 접근하는 것에 대해 보안을 걸어 두었기 때문이다.<br>
오류 해결방법
1.  구글 로그인
2. 우측 상단 동그라미 -> Google 계정
3. 보안
4. 보안 수준이 낮은 앱의 액세스 -> 액세스 사용 설정
5. 보안 수준이 낮은 앱 허용: 사용 활성화
6. 보안 수준이 낮은 앱의 액세스에 "사용"표시 확인 <br>

본 프로젝트에 적용
```python
def sendEmail(request):
    ... # 위 1, 2 코드 생략
    
    # smtp using
    server = smtplib.SMPT_SSL('smtp.gmail.com', 465)
    server.login("djangoemailtester001@gmail.com", "tester001")
    # 본인 구글 아이디와 비밀번호를 입력한다.

    msg = MIMEMultipart('alternative')
    msg['Subject'] = inputTitle
    msg['From'] = "djangoemailtester001@gmail.com"
    msg['To'] = inputReceiver
    msg_html = MIMEText(mail_html, 'html')
    msg.attach(mail_html)
    print(msg['To'],type(msg['To']))
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    server.quit()
    return HttpResponseRedirect(reverse('index'))
```

### PythonAnyWhere로 배포하기

파이썬 배포를 위한 PythonAnyWhere라는 툴이 있는데, 소규모 자원에 대해서는 무료로 사용자들에게 제공한다.

1. 회원가입
https://www.pythonanywhere.com/pricing/ 

2. github에 저장한 프로젝트를 PythonAnyWhere 계정에 복사
- 해당 github repository 주소를 복사한다.
- PythonAnyWhere 'Dashboard' 화면 좌측 하단 '$Bash'를 누른다.
- 'git clone repository주소' 명령어를 이용해 프로젝트를 붙여넣기 해준다.
- Username과 Password에는 github 이메일 계정과 비밀번호를 입력한다.
- 확인을 위해 'tree' 명령어를 입력한다. 디렉터리 내부 구조를 확인할 수 있다.

3. 가상환경 세팅
- cd RestaurantShare-with-Django(프로젝트가 만들어진 디렉터리)
- virtualenv --python=python3.7 restaurantEnv(가상환경이름)
- source restaurantEnv/bin/activate - 해당 가상 환경 실행
- pip install django - 장고 설치
- 우측 상단에 작대기 3개가 그려진 메뉴 버튼을 눌러 'Web'으로 들어가기
- 'Add a new web app' -> 'Next' -> 'Manual configuration' -> 'Python 3.7' -> 'Next' => Webapp이 만들어짐
- 'Virtualenv' 항목 -> 'Enter path to a virualenv, if desired' -> '/home/PythonAnyWhere의 Username/Github 저장소 이름/ 가상 환경 이름' 입력
    > /home/DjangoPracticeAccount/RestaurantShare-with-Django/restaurantEnv

4. 배포 후 프로젝트에 접근할 주소를 Django 프로젝트에서 허용해 주는 과정과 배포 때 사용하는 wsgi 설정
- 'Web'화면에서 'Code'를 찾는다.
- 'Go to directory' -> 'github 저장소 이름 디렉토리' -> (...) -> settings.py 파일 클릭
- 'ALLOWED_HOST' 항목에 "{PythonAnyWhere의 Username}.pythonanywhere.com" 입력 -> 저장(Ctrl + s)
    > "djangopracticeaccount.pythonanywhere.com"
- 'Code'부분에서 "WSGI configuration file"부분에 있는 파란색 글자를 누른다. 그럼 매우 긴 코드가 나타나는데, 모두 지우고 다음과 같이 코드를 작성한다. 저장 후 다시 'Web'으로 돌아간다.
```python
import os
import sys

path = '/home/DjangoPracticeAccount/RestaurantShare-with-Django/RestaurantShare'
# /home/PythonAnyWhere의 Username/github 저장소 이름/Django 프로젝트 이름
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'RestaurantShare.settings' # /Django project 이름.settings

from django.core.wsgi import get_wsgi_applcation
from django.contrib.staticfiles.handlers import StraticFielsHandler
application = StraticFielsHandler(get_wsgi_applcation())
```
- 하단의 초록색 버튼을 눌러준다.
- 해당 버튼의 로딩이 끝나면, 그 위에 있는 Configuration for 뒤의 파란색 글자를 누르면, 배포한 사이트가 나타난다.

### 장고 프레임워크 자체적으로 제공하는 mail 관련 함수를 통해서 수정하기

참고 https://docs.djangoproject.com/en/4.2/topics/email/

```python
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    restaurants = []
    for checked_res_id in checked_res_list:
        restaurants.append(Restaurant.objects.get(id = checked_res_id))

    # 아래에서 body는 a plain text message이여야 한다.
    # 하지만 우리는 html형식에 맞는 문자열로 메일 본문을 구성했다.
    # render_to_string 함수를 사용해 html로 된 template를 문자열처럼 사용할 수 있다.
    content = {'inputContent':inputContent, 'restaurants':restaurants}

    msg_html = render_to_string('sendEmail/email_format.html', content)

    msg = EmailMessage(subject = inputTitle, body = msg_html, 
                        from_email = 'djangoemailtester001@gmail.com',
                        to = inputReceiver.split(','))
    # subject = 메일의 제목 
    # body = 메일의 본문이며 a plain text message이여야 한다.
    # from_email = 발신자의 주소
    # to = 수신자의 주소
    # bcc = “Bcc” header에 사용된 주소의 리스트 또는 튜플 - 책에 to 대신 bcc가 적혀있었는데 오타같다.

    msg.content_subtype = 'html'
    msg.send()
    return HttpResponseRedirect(reverse('index'))
```
이 때 사용되는 html파일은 sendEmail app/tamplates/sendEmail에 만들어야 한다.
```html
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>맛집 공유</h1>
    <p>{{inputContent}}<br>발신자님께서 공유하신 맛집은 다음과 같습니다.</p>
    {%for restaurant in restaurants%}
    <h2>restaurant.restaurant_name</h2>
    <h4>* 관련 링크</h4><p>{{restaurant.restaurant_link}}</p>
    <h4>* 상세 내용</h4> <p>{{restaurant.restaurant_content}}</p>
    <h4>* 관련 키워드</h4><p>{{restaurant.restaurant_keyword}}</p>
    {%endfor%}
</body>
</html>
```
이렇게 코드를 구성하고 메일을 보내면 오류가 발생한다. 메일을 보낼 때 사용하게 될 서버에 대해서 추가적인 설정이 없어, 아마 장고 서버에서는 자동으로 우리 컴퓨터 자체를 smtp 서버로 하여 메일을 발송하려 했을 것이다.

하지만 이에 대한 설정을 진행한 적이 없고, 이전에는 구글의 smtp서버를 이용했다. 따라서 장고가 mail을 발송하려고 할 때 구글의 smpt 서버를 사용하도록 설정해 줘야 한다. 이는 RestaurantShare 폴더 안에 있는 settings.py에서 진행된다.
```python
ALLOWED_HOST = ["djangopracticeaccount.pythonanywhere.com", 
"127.0.0.1", "localhost"]
# [pythonanywhere계정.pythonanywhere.com, 로컬 환경에서 접속하는 127.0.0.1, 'localhost']

# settings.py의 어떤 위치에 해도 상관없다.
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PROT = 587
EMAIL_HOST_USER = 'djangomailtester001@gmail.com' # 구글 계정
EMAIL_HOST_PASSWORD = 'tester001' # 구글 계정 비밀번호
```