# Web Crawling

- 사이트를 하나 지정한 후에 웹 브라우저를 열어서 접속하기
    - webbrowser.open(url) 
    - 결과가 false인경우
        - 네트워크가 끊기는 경우
        - 서버 문제
        - 예외처리를 잘 해야함. 예외처리를 습관화해야 한다.
            -  예외처리를 잘 해야하는 경우
                1. 파일을 다룰 때
                2. DB접속할 때
                3. 네트워크

- 특정 검색어를 입력해 결과 얻기
    - 네이버에서 검색창에 검색어를 입력한 url = https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=파이썬
    - url에서 '?'이후에는 파라미터값이 온다
    - url을 나눠서 '파이썬' 앞까지 search_url 변수에, '파이썬'을 search_word 변수에 저장(사이트 마다 형식이 다름)
    - 합쳐서 url을 만들고 webbrowser.open로 접속
    - search_word를 바꿔가며 search할 수 있다.

- 웹 페이지의 html 소스 가지고 오기
    - requests.get(url)
    - Response[200] - 200 : 성공을 의미
    - requests.models.Response 객체
        - .text - html 소스파일을 문자열로 출력
        - .iter_content(chunk_size) - 요청/응답 데이터를 반복하여 대용량 응답을 위해 콘텐츠를 한 번에 메모리로 읽는 것을 방지하며 byte 타입으로 반환. chunk_size는 메모리로 읽어햐하는 바이트 수

- BeatifulSoup4(BS4) - '파싱', '추출'
- BeatifulSoup(html, 'lxml') - XML 또는 HTML로 파싱
    - .prettify() - 시각적으로 구조화
    - .find()            
    .find_all()
        - 인자값
            1. '태그'
            2. '태그', {'속성':'속성값'} - 지정된 태그 중 속성값을 갖는 태그를 가져옴
                - 태그없이 속성만을 사용할 수 없다
        - 리턴값 - 태그 한 줄 / 여러 줄(리스트로 반환)
        - .get_text - 텍스트 문자열을 문자열로 반환     
        .text       
        .string
        - .get('속성명') - 속성명에 해당하는 속성값을 반환
        - .replace_with('새 태그 또는 문자열') - 기존의 태그나 문자열을 새로운 태그나 문자열로 바꿈
    - .태그 - find('태그)와 같은 역할
        - soup.태그.태그2 - 태그안에 태그2를 찾음
        - 여러줄을 찾을 수 없음 - find_all()을 사용해야 한다
    - .select() - find('태그)와 같은 역할, 리스트로 반환
        - 인자값
            - '태그(공백)태그2' - 태그에서 태그2를 모두 가져온다
            - '태그.class속성값' - 태그 중 class=속성값인 태그를 모두 가져온다
            - '태그#id속성값' - 태그 중 id=속성값인 태그를 모두 가져온다
            - css처럼 태그없이 사용가능, [속성명] 사용가능
                - 다른 선택자들 시도해봐야 함

- BeautifulSoup 정리
1. requests.get(url)
2. .text
3. BeautifulSoup(text, 'lxml')
4. .find()/.find_all()
    - .태그 / .select()
5. .get_text()
    - .text / .string

- 웹 페이지에서 이미지 가져오기
1. 이미지를 다운받을 디렉토리 생성 / 파일명정하기
    - 디렉토리 : os.makedirs(경로)
    - 파일명 : os.path.basename(url)
2. 저장
    - opeen(os.path.join(디렉토리, 파일명), 'wb')
    - write - 이미지 데이터를 나눠서 저장
        - requests.get(url).iter_content(chunk_size)
    - close

- os 라이브러리  
    - os.path.basename(경로) - 경로에서 파일 이름만 추출     
    - os.makedirs(경로) - 경로 생성      
    - os.path.exists(경로) - 경로 존재여부       
    - os.path.join(경로, 경로, ...) - 경로를 합침        
    - os.listdir(경로) - 경로에 파일 목록을 보여줌


 - 리스트 vs 튜플
    - mutable vs immutable
    - 속도 느림 vs 빠름
    - 따라서 tuple을 이용해서 딥러닝 데이터를 학습시킴
    - numpy의 array도 튜플을 이용해서 만들었음

---

[실습](http://localhost:8888/tree/webcrawling_0629)