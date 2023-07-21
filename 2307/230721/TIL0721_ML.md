# ML

회귀 실습
- 평가 지표
    - from sklearn.metrics import mean_absolute_error, mean_squared_error
    - MSE(Mean Squred Error) - 예측 값과 실제값의 차이에 대한 제곱에 대하여 평균을 낸 값
        - mean_squared_error()
    - MAE(Mean Absolute Error) - 예측 값과 실제값의 차이에 대한 절대값에 대하여 평균을 낸 값
        - mean_absolute_error()
    - RMSE(Root Mean Squared Error) - MSE에 루트를 씌운 값

<br>

LinearRegression
  - LinearRegression()
  - .fit()
  - .predict()

<br>

규제(Regularization) - 학습이 과대적합 되는 것을 방지하고자 일종의 penalty를 부여하는 것
- L2 규제 - 릿지(Ridge)
    - 각 가중치 제곱의 합에 규제 강도(Regularization Strength)람다를 곱하여 오차에 더한다.
    - 람다를 크게 하면 가중치가 더 많이 감소되고(규제를 중요시함), 함다를 작게하면 가중치가 증가한다.(규제를 중요시하지 않음)
- L1규제 - 라쏘(Lasso)
    - 가중치의 절대값을 더한 값에 규제 강도(Regularization Strength)람다를 곱하여 오차에 더한다.
    - 어떤 가중치는 실제로 0이 된다. 즉 모델에서 완전히 제외되는 특성이 생기는 것이다.

<br>

릿지(Ridge)
- Ridge(alpha)
    - alpha - 규제 강도 람다. 클수록 규제를 중요시 함
- .fit()
- .predict()
- .coef_ - 기울기 파라미터(가중치/계수)를 담은 벡터
    - alpah가 커질수록 작아진다.

<br>

라쏘(Lasso)
- Lasso(alpha)
    - alpha - 규제 강도 람다. 클수록 규제를 중요시 함
- .fit()
- .predict()
- .coef_ - 기울기 파라미터(가중치/계수)를 담은 벡터

<br>

엘라스틱넷(ElasticNet)
- L1 + L2 혼합사용
- ElasticNet(alpha, l1_ratio)
    - alpha - 규제 강도 람다. 클수록 규제를 중요시 함
    - l1_ratio - 0에 가까울 수록 L2규제, 1에 가까울 수록 L1규제
- .fit()
- .predict()

<br>

RobustScaler
- 중앙값이 0, IQR이 1이 되도록 변환
- outlier 값 처리에 유용
- RobustScaler()
- .fit()
- .transform()

<br>

파이프라인
- from sklearn.pipeline import make_pipeline
- make_pipeline()
    - make_pipeline( StandardScaler(), ElasticNet())
- .fit()
    - .fit(x_train, y_train)
- .predict()
    - .predict(x_test)
    - 표준화 스케일링과 엘라스틱넷 모두 적용

<br>

Polynomial Features
- 다항식의 계수간 상호작용을 통해 새로운 feature 생성
    - [a, b] 2개의 feature가 존재한다고 가정
    - degree=2로 설정한다면 polynomial features는 [1, a, b, a^2, ab, b^2]가 된다.
- from sklearn.preprocessing import PolynomialFeatures
- PolynomialFeatures(degree)
- .fit()
- .transform()

<br>

앙상블(Ensemble)
- 여러개의 머신러닝 모델을 이용해 최적의 답을 찾아내는 기법
- 여러 모델을 이용하여 데이터를 학습하고, 모든 모델의 예측결과를 평균하여 예측

<br>

앙상블 기법의 종류
- 보팅(Voting): 투표를 통해 결과 도출
- 배깅(Bagging): 샘플 중복 생성을 통해 결과 도출
- 부스팅(Boosting): 이전 오차를 보완하면서 가중치 부여
- 스태킹(Stacking): 여러 모델을 기반으로 예측된 결과를 통해 meta모델이 다시 한번 예측

<br>

보팅(Voting) - 회귀(Regression)
- 투표를 통해 결정하는 방식
- 보팅은 다른 알고리즘 모델을 조합해서 사용합니다.
- from sklearn.ensemble import VotingRegressor, VotingClassifier

- VotingRegressor(single_models)
    - single_models - 반드시 튜플형태로 모델을 정의해야 한다.
    - single_models = [
        ('linear_reg', linear_reg),
        ('ridge', ridge),
        ('lasso', lasso),
        ('elasticnet_pipeline', elasticnet_pipeline),
        ('poly_pipeline', poly_pipeline)
      ]

- .fit() / .predict()

<br>

보팅(Voting) - 분류(Classification)
- from sklearn.ensemble import VotingClassifier

- VotingClassifier(models, voting)
    - voting = 'hard'|'soft'
    - hard - 결과 값에 대한 다수 class를 차용
        - 분류를 예측한 값이 1,0,0,1,1라고 가정하면 1이 3표, 0이 2표로 1이 최종값으로 예측됨
    - soft -  각각의 확률의 평균 값을 계산한 다음에 가장 확률이 높은 값으로 확정
        - class 0이 나올 확률이 (0.4, 0.9, 0.9, 0.4, 0.4)이었고 class1이 나올 확률이 (0.6, 0.1, 0.1, 0.6 ,0.6)이었다면 class0이 나올 최종확률은 다섯개의 평균인 0.44, class1이 나올 최종확률은 0.4 가 되어 class0가 최종값으로 예측됨

- .fit() / .predict()

<br>

배깅(Bagging)
- Bootstrap Aggregating의 줄임말
- Bootstrap은 여러 개의 데이터셋을 중첩을 혀용하게 하여 샘플링하여 분할하는 방식
    - 데이터 셋의 구성이 [1,2,3,4,5]로 되어있다면
    - 그룹1 = [1,2,3] / 그룹2 = [1,3,4] / 그룹3 = [2,3,5]
- 하나의 단일 알고리즘에 대하여 여러 개의 샘플 조합으로 앙상블
- 대표적인 배깅 앙상블 - RandomForest

<br>

RandomForest
- DecisionTree기반 배깅 앙상블
- 굉장히 인기있는 앙상블 모델
- 사용성이 쉽고, 성능도 우수함
- from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
- RandomForestRegressor()
    - 주요 하이퍼파라미터
    - random_state: 랜덤 시드 고정값. 고정해두고 튜닝할 것
    - n_jobs: CPU 사용갯수
    - max_depth: 깊어질 수 있는 최대 깊이. 과대적합 방지용
    - n_estimators: 앙상블하는 트리의 갯수
    - max_features: 최대로 사용할 feature의 갯수. 과대적합 방지용
    - min_samples_split: 트리가 분할할 때 최소 샘플의 갯수. default=2 과대적합 방지용
- .fit() / .predict() 

<br>

부스팅(Boosting)
- 약한 학습기를 순차적으로 학습하되 이전 학습에 대하여 잘못 예측된 데이터에 가중치를 부여해 오차를 보완해 나가는 방식
- 장점
    - 성능이 매우 우수하다(Lgbm, XGBoost)
- 단점
    - 부스팅 알고리즘의 특성상 계속 약점(오분류/잔차)을 보완하려고 하기 때문에 잘못된 레이블링이나 아웃라이어에 필요 이상으로 민감할 수 있다.
    - 다른 앙상블 대비 학습식나이 오래걸린다.

<br>

대표적인 부스팅 앙상블
- AdaBoost
- GradientBoost
- LightGBM(LGBM)
- XGBoost

<br>

GradientBoost
- 성능이 우수함
- 학습시간이 해도해도 너무 느리다.
- from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier

- GradientBoostingRegressor()
    - 주요 하이퍼파라미터
    - random_state: 랜덤 시드 고정 값. 고정해두고 튜닝할 것!
    - n_jobs: CPU 사용 갯수
    - learninig_rate: 학습율. 너무 큰 학습율은 성능을 떨어뜨리고, 너무 작은 학습율은 학습이 느리다. 적절한 값을 찾아야함. n_estimator와 같이 튜닝. default=0.1
    - n_estimators: 부스팅 스테이지 수. (랜덤포레스트 트리의 갯수 설정과 비슷한 개념). default=100
    - subsample: 샘플 사용 비율(max_features와 비슷한 개념). 과대적합 방지용
    - min_sample_split: 노드 분할시 최소 샘플의 갯수. default=2 과대적합 방지용

- .fit() / .predict() 

<br>

XGBoost(eXtreme Gradient Boosting)
- 사이킷런 패키지가 아닙니다.
- 성능이 우수함
- GBM보다는 빠르고 성능도 향상되었습니다.
- 여전히 학습시간이 매우 느리다
- from xgboost import XGBRegressor, XGBClassifier

- XGBRegressor()
    - 주요 하이퍼파라미터
    - random_state: 랜덤 시드 고정 값. 고정해두고 튜닝할 것!
    - n_jobs: CPU 사용 갯수
    - learninig_rate: 학습율. 너무 큰 학습율은 성능을 떨어뜨리고, 너무 작은 학습율은 학습이 느리다. 적절한 값을 찾아야함. n_estimator와 같이 튜닝. default=0.1
    - n_estimators: 부스팅 스테이지 수. (랜덤포레스트 트리의 갯수 설정과 비슷한 개념). default=100
    - max_depth: 트리의 깊이. 과대적합 방지용. default=3
    - subsample: 샘플 사용 비율(max_features와 비슷한 개념). 과대적합 방지용. default=10
    - max_features: 최대로 사용할 feature의 비율. 과대적합 방지용. default=10

- .fit() / .predict() 

<br>

LightGBM
- 사이킷런 패키지가 아닙니다.
- 성능이 우수함
- 속도도 매우 빠릅니다.
- from lightgbm import LGBMRegressor, LGBMClassifier

- LGBMRegressor()
    - 주요 하이퍼파라미터
    - random_state: 랜덤 시드 고정 값. 고정해두고 튜닝할 것!
    - n_jobs: CPU 사용 갯수
    - learninig_rate: 학습율. 너무 큰 학습율은 성능을 떨어뜨리고, 너무 작은 학습율은 학습이 느리다. 적절한 값을 찾아야함. n_estimator와 같이 튜닝. default=0.1
    - n_estimators: 부스팅 스테이지 수. (랜덤포레스트 트리의 갯수 설정과 비슷한 개념). default=100
    - max_depth: 트리의 깊이. 과대적합 방지용. default=3
    - colsample_bytree: 샘플 사용 비율(max_features와 비슷한 개념). 과대적합 방지용. default=1.0

- .fit() / .predict() 

<br>

Stacking
- 개별 모델이 예측한 데이터를 기반으로 final_estimator 종합하여 예측을 수행합니다.
- 성능을 극으로 끌어올릴 때 활용하기도 합니다.
- 과대적합을 유발할 수 있습니다. (특히 데이터셋이 적은 경우)
- from sklearn.ensemble import StackingRegressor
- StackingRegressor(stack_models, final_estimator)
    - stack_models = [
          ('elasticnet', poly_pipeline),
          ('randomforest', rfr),
          ('gbr', gbr),
          ('lgbm', lgbm)
      ]
- .fit() / .predict() 

<br>

Weighted Blending
- 각 모델의 예측값에 대하여 weight를 곱하여 최종 output 계산
- 모델에 대한 가중치를 조절하여 최종 아웃풋을 산출합니다.
- 가중치의 합은 1이 되도록 합니다.
- final_outputs = {
      'elasticnet': poly_pred,
      'randomforest': rfr_pred,
      'gbr': gbr_pred,
      'xgb': xgb_pred,
      'lgbm': lgbm_pred,
      'stacking': stack_pred
  }
- final_prediction=\
  final_outputs['elasticnet']*0.1\
  +final_outputs['randomforest']*0.1\
  +final_outputs['gbr']*0.2\
  +final_outputs['xgb']*0.25\
  +final_outputs['lgbm']*0.15\
  +final_outputs['stacking']*0.2

<br>

하이퍼파라미터 튜닝
- 하이퍼파라미터 튜닝시 경우의 수가 너무 많습니다.
- 따라서 우리는 자동화할 필요가 있습니다.
- sklearn 패키지에서 자주 사용되는 하이퍼파라미터 튜닝을 돕는 클래스는 다음 2가지가 있습니다.
    - RandomizedSerchCV 2, GridSearchCV

<br>

RandomizedSearchCV
- 모든 매개 변수 값이 시도되는 것이 아니라 지정된 분포에서 고정된 수 매개 변수 설정이 샘플링됩니다.
- 시도 된 매개 변수 설정의 수는 n_iter에 의해 제공됩니다
- from sklearn.model_selection import RandomizedSearchCV

- RandomizedSearchCV(estimator, params, random_state, cv, n_iter, scoring)
    - estimator - LGBMRegressor()
    - params = {
          'n_estimators': [200, 500, 1000, 2000],
          'learninig_rate': [0.1, 0.05, 0.01],
          'max_depth': [6, 7, 8],
          'colsample_bytree': [0.8, 0.9, 1.0],
          'subsample': [0.8, 0.9, 1.0]
      }
    - n_iter - n_iter 값을 조절하여, 총 몇 회의 시도를 진행할 것인지 정의합니다. (회수가 늘어나면 더 좋은 파라미터를 찾을 확률은 올라가지만, 그만큼 시간이 오래걸립니다.)
    - scoring - 'neg_mean_squared_error'

- .fit() / .predict() 

<br>

GridSearchCV
- 모든 매개 변수 값에 대하여 완전 탐색을 시도합니다.
- 따라서 최적화할 파라미터가 많다면 시간이 매우 오래 걸립니다.
- from sklearn.model_selection import GridSearchCV
- GridSearchCV(LGBMRegressor(), params, cv=3, n_jobs=-1, scoring='neg_mean_squared_error')
- .fit() / .predict() 

---

[실습](http://localhost:8888/tree/ML_0721)