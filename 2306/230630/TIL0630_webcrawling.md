# Web Crawling

네이버 뉴스 크롤링
- 입력 - 크롤링
    - 대상 분석
    - urllib.request.urlopen()
- 처리 - 파싱, 추출, 가공, 저장
    - BeautifulSoup()
        - BeautifulSoup(html, 'html.parser')
            - 'lxml' - xml or html로 파싱
            - 'html.parser' - html로 파싱
    - findAll() = find_all()
    - .text = .get_text() / ['속셩명'] = .get('속성명')
    - pd.DataFrame()
    - df.to_csv()
- 출력
    - 화면출력


[Selenium](https://www.selenium.dev/)
- 크롬드라이브, 크롬브라우저 사용
- 웹 자동화
    - 자동으로 티켓팅
- import
    - from selenium import webdriver
    - from selenium.webdriver.chrome.service import Service as ChromeService
    - from webdriver_manager.chrome import ChromeDriverManager
- 브라우져 열기
    - driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
- 페이지 이동
    - .get("url")
- 윈도우 사이즈 조절
    - .set_window_size(1024, 768) - 1024*768px
- 브라우저의 스크롤 위치 이동
    - .execute_script("window.scrollTo(200, 300);") - 왼쪽에서 200px, 아래로 300px
        - .execute_script('js 코드') - js코드 실행
- alert 다루기
    - alert창으로 이동 - .switch_to.alert
    - alert창의 텍스트 - .switch_to.alert.text(이동후에 텍스트를 출력할 수 있음)
    - alert창에서 확인 버튼 누르기 - .switch_to.alert.accept()
    - alert창 만들기 - .execute_script("alert('selenium test');")
- 버튼 클릭하기
    - .find_element(By.CSS_SELECTOR,"선택자").click()
- 텍스트 데이터 가져오기
    - import
        - from selenium.webdriver.common.by import By
    - find_element(By.CSS_SELECTOR,'선택자'): 한개의 엘리먼트를 선택        
    find_elements(By.CSS_SELECTOR,'선택자'): 여러개의 엘리먼트를 선택
        - .text - text가져오기
        - .get_attribute('속성명') - 속성값 가져오기
- import time
    - time.sleep(3) - 3초후에 다음코드 실행
- 브라우져 종료
    - .quit()


웹크롤링 미니 프로젝트
1. 수집 데이터 선정
2. 대상사이트 분석(구조 분석), 선정된 데이터의 위치 찾기
3. 수집(웹 크롤링)
4. 추출(스크레이핑)
5. 가공
6. 저장
7. 시각화

[실습](http://localhost:8888/tree/webcrawling_0630)