# ML

titanic 전처리 실습
- 결측값 대체
    - from sklearn.impute import SimpleImputer
    - imputer = SimpleImputer(strategy='')
        - strategy - 'mean', 'median', 'most_frequent', ...
    - imputer.fit()
    - imputer.transform()
    - 두 개 이상의 column을 한 번에 처리할 때 사용한다.

<br>

분류 실습
- LogisticRegression/ SGDClassifier(SGD: 확률적 경사 하강법)/ KNeighborsClassifier/ SVC(서포트 벡터 머신)/ DecisionTreeClassifier
    - 객체 생성
        - KNeighborsClassifier(n_neighbors)
    - .fit()
    - .predict()
    - (pred == y.test).mean()

---

[실습](http://localhost:8888/tree/ML_0720)