![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=BBooing%20&fontSize=90)
# 31-1st-MUZIMAKZI-backend
## 류미류, 이강호
In order to succeed, We must first believe that we can. by Nikos Kazantzakis

## Introduction
- 기간: 2022-04-11 ~ 2022-04-22
- 구성: Front-end 4명(with 본희, 재혁, 효정, 정수), Back-end 2명 (with 미류, 강호)

## Our System
![초반](https://user-images.githubusercontent.com/91510831/164958293-42e72cdf-2c3e-407b-a7fa-ec662bb2e327.gif)
![중반](https://user-images.githubusercontent.com/91510831/164958302-b9c0b99b-1417-478a-aa06-8525724763b5.gif)
![후반](https://user-images.githubusercontent.com/91510831/164958305-2b386973-3ac5-4405-843c-8b9b72394ef0.gif)

## Data Modeling
<img width="851" alt="스크린샷 2022-04-24 오후 2 43 11" src="https://user-images.githubusercontent.com/91510831/164958343-2a3bf5a5-71da-44e2-b5b8-7b3c732a8f54.png">

## Tech & Features
### Tech
|Index|Use|Description|
|:---:|:---:|:---:|
|1|MySQL|데이터베이스|
|2|Django|웹 프레임워크|
|3|EC2|클라우드 배포|
|4|S3|클라우드 저장|
|5|KakaoAPI|소셜 로그인|
|6|Git|버전 컨트롤|

### Features
- 소셜 로그인
    - [KakaoAPI](https://developers.kakao.com/)를 활용하여 소셜 로그인 기능 구현.
    - FE 에서 Kakao accesstoken을 서버에 전달하고, JWT를 활용하여 새로운 access token 발행.
- 강의 조회
    - Query Parameter를 활용하여 다중필터 기능 구현.
    - 또한, Q객체에서 더 나아가, 다중필터를 Key-Value형태로 정의하고, 추가적인 필터 Index가 필요할 경우 확장이 가능하도록 구현.
- 강의 검색
    - 강의 Keyword를 문자열 형태로 전달받고(with Query Parameter), DB에 저장된 강의 제목을 필터링하여 조회결과 반환.
- AWS S3 
    - 서버 부하를 줄이기 위해, 이미지 원본은 AWS S3에 저장하고(with boto3) 가벼운 URL을 DB에 저장하여 구현.
    - Upload, Delete 구현하여 이미지 삭제 시, S3 저장소에도 삭제될 수 있도록 구현.
- DB Hit 최적화
    - Django ORM으로 DB에 접근할 때, caching이 가능하도록 코드 작성.
    - 실제, 240번 Query 횟수를 4번으로 줄임으로써, 효율적인 서버 구축.
- 테스트 코드
    - Unittest를 진행함으로써, 시스템 안정성 확보.
    - 또한, 외부 API (Kakao API, AWS S3)에 대해서 Mock Response로 전달하여, 테스트 진행.
    - Unittest 통과 이후, Postman으로 통합테스트 진행.
    - 테스트 코드에 대한 문서화 (with Postman API Documentation)


## 기억에 남는 코드
<img width="1243" alt="스크린샷 2022-04-24 오후 2 45 24" src="https://user-images.githubusercontent.com/91510831/164958424-c05139ca-2a86-458a-89a9-441a15e7c1a9.png">
<img width="1254" alt="스크린샷 2022-04-24 오후 2 45 07" src="https://user-images.githubusercontent.com/91510831/164958416-2fbd87fe-d923-4b78-91ae-f37095749e64.png">

## Notion
[1] Notion : https://quirky-eocursor-b74.notion.site/bbooing-Standing-Meeting-bed5f8dfe56f42dca04c6e92b4a97b59 <br>
[2] PostMan: https://documenter.getpostman.com/view/20018497/Uyr8ndsz

## Reference
- 해당 프로젝트는 [탈잉사이트](https://taling.me/?utm_source=google&utm_medium=cpc&utm_campaign=p2p&utm_content=pc_%EB%B8%8C%EB%9E%9C%EB%93%9C_00.%EC%9D%BC%EB%B0%98&utm_term=%ED%83%88%EC%9E%89&gclid=CjwKCAjwx46TBhBhEiwArA_DjNhbnjzjYyzERizl8zjsFwD3I8asbAkPDnjRL7h-Et2Axx62f2NFHRoCGo0QAvD_BwE)를 참조하여 학습목적으로 제작되었습니다
- 해당 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다
- 해당 프로젝트에서 사용하고 있는 이미지는 위코드에서 구매한 것으로, 외부인이 사용할 수 없습니다.
