# ML

분류(classificatiion) 성능 평가 지표
- 분류에는 이진분류/멀티분류가 있는데 특히 이진분류에서 중요한 지표(멀티분류에도 적용 가능)
    - 정확도(Accuracy)
    - 오차행렬(Confusion Matrix)
    - 정밀도(Precision)
    - 재현율(Recall)
    - F1 스코어
    - ROC AUC

<br>

정확도(Accuracy)
- 실제 데이터에서 예측 데이터가 얼마나 같은지 판단하는 지표
- 정확도 = (예측 결과가 동일한 데이터 건수)/(전체 예측 데이터 건수)
- 이진 분류의 경우 데이터의 구성에 따라 ML 모델의 성능을 왜곡할 수 있기 때문에 정확도 수치 하나만 가지고 성능을 평가하지 않음
- 특히 정확도는 불균형한(imbalanced) 레이블 값 분포에서 ML 모델의 성능을 판단할 경우, 적합한 평가 지표가 아님
- 여러 가지 분류 지표와 함께 적용하여 모델 성능을 평가해야 한다.

<br>

오차 행렬(Confusion Matrix)
- 오차 행렬은 이진 분류의 예측 오류가 얼마인지와 더불어 어떠한 유형의 예측 오류가 발생하고 있는지를 함께 나타내는 지표
- 4분면의 왼쪽과 오른쪽은 예측된 class를 기준으로 Negative와 Positive로 분류
- 위와 아래는 실제 class를 기준으로 Negative와 Positive로 분류
- 예측 class와 실제 class에 따라 TN, FP, FN, TP 형태로 오차 행렬의 4분면을 구성
    - TN은 예측값을 Negative 값인 0으로 예측했고 실제값 또한 Negative 값인 0일 때
    - FP은 예측값을 Positive 값인 1으로 예측했는데 실제값은 Negative 값인 0일 때
    - FN은 예측값을 Negative 값인 0으로 예측했는데 실제값은 Positive 값인 1일 때
    - TP은 예측값을 Positive 값인 1으로 예측했고 실제값 또한 Positive 값인 1일 때
- confusion_matrix()

<br>

정밀도(Precision) / 재현율(Recall)
- 정밀도는 예측을 Positive로 한 대상 중에 실제 값이 Positvie로 일치한 데이터의 비율
- 재현율은 실제 값이 Positive인 대상 중에 예측값이 Positive로 일치한 데이터의 비율
    - 재현율은 민감도로도 불림
- 정밀도 = TP / (FP + TP)
    - precision_score()
- 재현율 = TP / (FN + TP)
    - recall_score()
- 실제 Positive 양성 데이터를 Negative로 잘못 판단하게 되면 업무상 큰 영향이 발생하는 경우 재현율이 중요 지표이다.
    - 암 판단 모델, 금융사기 등
- 실제 Negative 음성 데이터를 Positive로 잘못 판단하게 되면 업무상 큰 영향이 발생하는 경우 정밀도가 중요 지표이다.
    - 스팸메일 여부 판단 모델 - 일반메일(Negative)을 스팸메일(Positive)로 분류하면 업무에 차질이 생긴다
- 정밀도/재현율 트레이드오프(Trade off)
    - 분류하려는 업무의 특성상 정밀도 또는 재현율이 특별히 강조되어야 할 경우 분류의 결정 임계값(Threshold)을 조정해 정밀도 또는 재현율의 수치를 높일 수 있다
    - 정밀도와 재현율은 상호 보완적인 평가 지표이기 때문에 어느 한쪽을 강제로 높이면 다른 하나의 수치는 떨어지기 쉽다.(Trade-off)

    - 사이킷런은 개별 데이터별로 예측 확률을 반환하는 메서드인 predict_proba()를 제공한다.
    - 학습이 완료된 사이킷런 Classifier 객체에서 호출 가능하다.
    - 테스트 피처 데이터 세트를 파라미터로 입력하면 레코드별로 개별 클래스 예측확률을 반환한다.
    - predict()와 다른점은 반환 결과가 클래스값이 아닌 예측확률이라는 점이다.
        - predict()는 예측확률에 근거하여 더 높은 확률의 레이블을 결과로 반환한다.
        - predict()메서드는 predict_proba()메서드에 기반해 생성된 API이다.
    - Binarizer 클래스 객체를 사용하면 predict()의 의사(pseudo)코드를 만들 수 있다.
        - binarizer = Binarizer(threshold)
        - binarizer.fit(predict_proba(test))
        - binarizer.transform(predict_proba(test))

    - precision_recall_curve(y_test, pred_proba) - 임계값에 따른 평가지표 반환
        - 리턴값 - precisions, recalls, thresholds

<br>

F1 Score
- F1 스코어는 정밀도와 재현율을 결합한 지표
- F1 스코어는 정밀도와 재현율이 어느 한쪽으로 치우치지 않는 수치를 나타낼 때 상대적으로 높은 값을 가짐
- 𝑭𝟏 = 𝟐 ∗ (𝒑𝒓𝒆𝒄𝒊𝒔𝒊𝒐𝒏 ∗ 𝒓𝒆𝒄𝒂𝒍𝒍)/(𝒑𝒓𝒆𝒄𝒊𝒔𝒊𝒐𝒏 + 𝒓𝒆𝒄𝒂𝒍𝒍)
- F1_score()

<br>

ROC(Receiver Operation Characteristic) 곡선 / AUC(Area Under Curve)
- ROC 곡선과 이에 기반한 AUC 스코어는 이진 분류의 예측 성능 측정에서 중요하게 사용되는 지표
- ROC 곡선은 FPR이 변할 때 TPR이 어떻게 변하는지를 나타내는 곡선
    - TPR은 True Positive Rate로 실제 Positive를 제대로 얘측한 비율을 의미
    - TPR은 TP / (FN + TP), 재현율 또는 민감도로 불림
    - TPR은 실제값 Positive가 정확히 예측되야 하는 수준을 나타냄

    - TNR은 실제값 Negative가 정확히 예측되야 하는 수준을 나타냄
    - TNR은 TN / (FP + TN), 특이도라고 불림

    - FPR은 False Positive Rate로 실제 Negative를 잘못 예측한 비율을 의미
    - FPR은  FP / (FP + TN), 1-특이도이다.
- FPR을 X축으로, TPR을 Y축으로 잡는다
- ROC 곡선은 FPR을 0부터 1까지 변경하면서 TPR의 변화값을 구한다.
    - 분류 결정 임계값을 변경하면 FPR값을 0부터 1까지 변경할 수 있다.
    - 임계값=1 - FPR=0 / 임계값=0 - FPR=1
- AUC 값은 ROC 곡선 밑의 면적을 의미하며 일반적으로 1에 가까울수록 좋다(0.5에 가까울수록 성능이 떨어짐)
- roc_curve(y_test, pred_proba)
    - 리턴값 - fpr, tpr, thresholds
- roc_auc_score(y_test, pred_proba)

---

[실습](http://localhost:8888/tree/ML_0719)

