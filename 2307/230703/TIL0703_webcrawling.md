# Web Crawling

mini project - 멜론, 벅스, 지니차트
- 입력 - 크롤링
    - 대상 분석
    - Selenium
        - driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        - driver.get(url)
        - ***driver.page_source***
- 처리 - 파싱, 추출, 가공, 저장
    - BeautifulSoup(***driver.page_source***, 'html.parser')
    - .select()
    - pd.DataFrame()
    - df.to_excel()
- 출력

youtube project
- 입력 - 크롤링
    - 대상 분석
    - Selenium
        - driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        - driver.get(url)
        - ***driver.page_source***
- 처리 - 파싱, 추출, 가공, 저장
    - BeautifulSoup(***driver.page_source***, 'html.parser')
    - .select()
    - pd.DataFrame()
    - df.to_excel()
- 출력
    - 시각화
        - pd.read_excel()
        - Series.str.replace()
        - Series.astype()
        - df.pivot_table()
        - df.reset_index()
        - df.sort_values()
        - plt.pie()

[실습](http://localhost:8888/tree/webcrawling_0703)