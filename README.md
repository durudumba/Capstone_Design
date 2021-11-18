## 2021년 1학기 캡스톤 디자인 인공지능 모델제작

### 목표

바다이미지를 해당 바다 클래스로 분류

-------------

#### 1. 데이터 수집

* ```chrome driver(version=91.0.4472.19)```, ``` chrome web browser(version=91)```

* Python Selenium 라이브러리를 활용해 chrome driver를 구동, 웹 이미지 크롤링

* 각 클래스별 이미지 데이터 저장

  

#### 2. 데이터 전처리 및 증강

* 클래스에 부합하지 않는 이미지 검토
* 성능향상을 위한 이미지 데이터량 증강(흑백, 회전)
* 편향을 방지하기 위한 이미지 크기, 클래스별 이미지 갯수 균일화



#### 3. 모델 제작

*  Google [Teachable Machine][tmlink] 서비스 활용

[tmlink]: https://teachablemachine.withgoogle.com/



#### 4. 모델 평가

* Test 기능의 부재 → 학습되지 않은 클래스별 이미지활용
* 각 이미지의 정확도로 평가

