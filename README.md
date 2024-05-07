# tokyoDjango
AWS 배포를 목표로 개인홈페이지를 만들어 기능추가를 하는 Django프로젝트입니다 

배포된 도메인 : http://jungsik.net

[목차]
1. 프로젝트 목표
2. 작업환경 구성
3. 프로젝트 구성
4. 백엔드 구조 설계
5. 작업 주요 이슈
6. 레퍼런스

-----------

## 1. 프로젝트 목표  
간단 CRUD가 가능한 Django 프로젝트를 구성하고

이를 AWS Lightsail에 올려 도메인과 함께 서비스함으로서 

발생할 수 있는 이슈를 체크하고 기술을 습득하기 위해 프로젝트를 진행했습니다

## 2. 작업 환경 구성

### 사용된 기술
* 활용된 언어 : Python / HTML / JavaScript

* 활용된 프레임워크 : Django / BootStrap

* 클라우드 및 플랫폼 서비스 : AWS LightSail

* 버전관리 시스템 : GitHub

* 웹 서버/서비스 운영: Nginx, Gunicorn  

### 작업 환경 설정
* AWS 접속 및 활용

   VSCODE에 SSH 키를 사용하여 AWS 내의 자원들을 관리

* GitHub Repository 설정

   main - release 브랜치로 나누어 업데이트에 활용할 브랜치를 구분 

## 3. 프로젝트 구성
### 이력서 페이지 
#### 이력서 (resume)
<img width="826" alt="resume" src="https://github.com/sk7556/tokyoDjango/assets/109896609/2248fb2c-305c-4bcf-b909-8162268e5ea5">

* Django의 기능을 통해 DB에 입력된 데이터를 받아 노출

#### 이력서 업데이트 (resume/update)
<img width="807" alt="update" src="https://github.com/sk7556/tokyoDjango/assets/109896609/37c867b1-00ab-45ea-bb87-7c79271a0db3">

* JS, DRF API를 통해 이력사항을 입력받아 DB에 업로드
* 로그인 유저만 업로드 가능 


### toDo 페이지
#### toDo ( todo )
<img width="797" alt="todo" src="https://github.com/sk7556/tokyoDjango/assets/109896609/98c3a415-ec77-4035-a711-818b0fbb47c2">

* DRF API를 통해 CRUD를 수행하여 메모를 작성하는 페이지 
* Create, Update, Delete 의 경우 **로그인 유저**만 사용하도록 구성
* ModelViewSet을 활용 

### Diary 게시판 페이지 
#### Diary ( diary ) 
<img width="798" alt="diary" src="https://github.com/sk7556/tokyoDjango/assets/109896609/a13b260a-a8e5-4fd7-b8f8-020bb9b33463">

* 함수 뷰와 Django 기능을 활용해서 CRUD가 가능하도록 설계
* Create, Update, Delete 의 경우 **로그인 유저**만 사용하도록 구성

## 4. 백엔드 구조 설계 
GitHub Action - [AWS Lightsail - Gunicorn - Nginx - Django - DB] - Browser

Gunicorn - wsgi
nginx - web server 

데이터 플로우
1. 유저 request 를 Nginx에 도달
2. Nginx 서비스에서 static파일을 처리, 동적요청은 Gunicorn에 전달
3. Gunicorn이 Django 애플리케이션에서 요청을 처리하고 응답을 생성
4. 생성된 응답은 Nginx를 통해 다시 유저에게 전달 


## 5. 작업 주요 이슈 (in Code) 
### 백엔드 부분

* CORS 세팅
  
   CORS를 사용하여 접근권한 경로를 제한하려고 했지만 https 설정이 되어있지 않아 현재 배포된 웹페이지에서 CORS에러 발생

   추가 비용이 발생하게 될 것 같아 우선순위에서 제거

-----

* AWS 설정
  
   최소한의 비용을 지불하는 ubuntu 계정을 사용
   
   github repository를 연동하여 CI/CD에 활용할 수있도록 설정
   
   Nginx와 Gunicorn 설치 후 Django 프로젝트와 연동하여 서비스 가능하도록 설정

-----

* Nginx 설정 확인 ( Static 관련 설정 )
  
   local 에서의 설정과 다르게 Nginx를 사용하는 단계에서는 정적 파일들에 대한 별도의 관리가 필요함을 배포 후 알게되었음
   
   해결 방법 :

   default.conf 에 static 파일, media 파일들을 세팅 사용하게 될 포트와 django 프로젝트들을 기록 

-----

* CI / CD 정책 설정
  
   yaml파일을 통해 Github action에서 사용하게될 설정들을 연결
   
   requirements 리스트를 활용해 의존성 설치 및 Git pull, 그리고 Nginx 리부트하도록 설정

-----

* JWT 인증 정책관련 설정
     
   DRF-SIMPLE-JWT 패키지을 활용하여 JWT를 활용해서 인증 구조를 만들어보기로 결정
   
   로그인 시 토큰을 받아 로컬 스토리지에서 기록하고, JS를 통해 프론트엔드에서 확인하도록 구성
   
   백엔드에서 Django의 기능을 통해 인증 상태를 확인시키거나 미들웨어를 구성하여 토큰을 확인하는 로직을 구성해야했지만 
   
   잦은 에러로 인해 제거 후 재구성 예정

-----

### 프론트엔드 부분

* 서식 / 마크다운을 수용할 수 있는 텍스트 필드 구성
   
   해결 방법 : 
   
   showdown.js 를 활용하여 마크 다운을 입력받을 수 있도록 구성하여 resume에 적용
   
   Django의 linebreaks를 활용하여 줄바꿈이 가능하도록 diary에 적용

-----

* 인증 데이터 체크 설정
     
   JS에서 fetch 기능을 통해 API에 접근하는데, JWT로 인한 인증 데이터 지정을 위해
   
   Header 설정을 해야하는 이슈가 발생
   
   해결 방법 : 
   
   method와 Header를 일치시켜 API에 인증여부를 바르게 전달할 수 있도록 만들어 에러 해결

-----

### 코드 외 이슈 

* 작업 템포관련
     
   인강을 듣거나 여행을 하는 등 작업에 집중하지 못했었고
   
   구체적인 계획의 부족으로 작업 기한이 늘어나는 이슈가 있었다

-----

* 작업 분량설정 관련
     
   상세 내용에 대한 인지가 부족해 중간중간 내용을 변경하거나 아쉬운 부분을 수정하는데 시간이 많이 소모되었다
   
   도중에 시스템의 에러가 발생하거나 예상하지 못했던 이슈가 생긴데 해결하는데 시일을 꽤 많이 소모했다

-----

* 프로젝트 주체성 관련
  
   처음에는 간단하게 이력서만 올라간 페이지를 만들고 싶었으나
   
   배포와 관련된 실습이 필요하다 생각하여 관련 요소를 체크하다가 프로젝트의 주제가 변경되게 되었다


## 레퍼런스

Django 서비스 AWS로 배포하기 - https://nerogarret.tistory.com/45

실전! GitHub Actions으로 CI/CD 시작하기 - Inflearn 강의
