# Web crawling
urllib
- urllib.request
    - urllib.request.urlretrieve(url, filename) - tuple로 filename, url의 response header를 반환
    - response = urllib.request.urlopen(url) - http.client.HTTPResponse 객체
        - response.info() - response header 정보
        - response.getcode() - HTTP Status Code 정보
        - response.read() - HTTP 응답 본문(bytes 자료형) 추출
        - response.geturl() - url을 반환
        - response.getheaders() - response header 정보반환
        - response.read().decode('utf-8')
        - response.status - HTTP Status Code 반환
- urllib.parse
    - urllib.parse.urlparse - url을 6개로 분해
        - `<scheme>://<netloc>/<path>;<params>?<query>#<fragment>`
    - urllib.parse.urlencode() - Encode a dict or sequence of two-element tuples into a URL query string.


Requests
- session = requests.Session() - 세션(Session)은 HTTP 요청과 응답 사이에 유지되는 상태 정보를 저장할 수 있는 기능이다. 이를 이용하면 사용자 인증이 필요한 웹 사이트에 접근할 수 있거나, 쿠키를 사용해서 접근 제한이 걸려 있거나, 상태 정보가 저장되어 있는 웹 사이트에 지속적인 접근이 가능하다.
- response = session.get(url) - url에 get방식으로 요청
- response.content - html로 된 문자열


lxml
- lxml.xml
- lxml.html
    - root = fromstring(html로 된 문자열) - html형태의 문자열을 html로 변환
        - response는 html형태의 string이므로 html(또는 xml)로 변환해야함
        - lxml.html.HtmlElement객체(fromstring의 리턴타입임)의 메서드
            - a = root.xpath() - XPath는 XML문장 속의 요소, 속성 등을 지정하기 위한 언어이다. HTML도 XML의 일종으로 간주 될 수 있으므로, XPath를 사용하여 HTML문장의 요소를 지정하는 것도 가능하다.
                - a = root.cssselect('선택자') - css 선택자를 이용하여 요소 지정
            - a.get("속성명") - 속성값 반환
            - a.text_content() - a요소의 텍스트(몸체) 반환


RSS - 블로그 또는 뉴스 사이트 등의 웹사이트는 변경 정보 등을 RSS라는 이름의 XML 형식으로 제공
- 주기적으로 자료를 받음

저장
- csv
    - str.join()
    - csv.writer()
- JSON
    - json 모듈
    - 
[실습](http://localhost:8888/tree/webcrawling_0628) - jupyter notebook으로 연결