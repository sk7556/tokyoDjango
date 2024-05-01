# tokyoDjango
AWS 배포를 목표로 개인홈페이지를 만들어 기능추가를 하는 django프로젝트 

[목차]

1. 프로젝트 목표  
간단 CRUD가 가능한 Django 프로젝트를 구성하고 
이를 AWS Lightsail에 올려 도메인과 함께 서비스함으로서 
발생할 수 있는 이슈를 체크하고 기술을 습득하기 위해 프로젝트를 진행했습니다

2. 사용 기술

활용된 언어 : Python / HTML / JavaScript
활용된 프레임워크 : Django / BootStrap
클라우드 및 플랫폼 서비스 : AWS LightSail
버전관리 시스템 : GitHub
웹 서버/서비스 운영: Nginx, Gunicorn


3. 프로젝트 구성
- 이력서 페이지 
이력서 (resume)
--> Django의 기능을 통해 DB에 입력된 데이터를 받아 노출 

이력서 업데이트 (resume/update)
--> JS, DRF API를 통해 이력사항을 입력받아 DB에 업로드
--> 로그인 유저만 업로드 가능 


- toDo 페이지
toDo ( toDo )
--> DRF API를 통해 CRUD를 수행하여 메모를 작성하는 페이지 
--> CUD의 경우 로그인 유저만 사용하도록 구성
--> ModelViewSet을 활용 

- Diary 게시판 페이지 
Diary ( diary ) 
--> 함수 뷰와 Django 기능을 활용해서 CRUD가 가능하도록 설계
--> CUD의 경우 로그인 유저만 사용하도록 구성

4. 백엔드 구조 설계 
GitHub Action - [AWS Lightsail - Gunicorn - Nginx - Django - DB] - Browser

Gunicorn - wsgi
nginx - web server 


5. 작업 주요 이슈 (in Code) 
- 작업 환경 설정
VSCODE 환경 설정
AWS에 연결된 ssh를 VSCODE에 연결하여 활용할 수 있도록 세팅 

GitHub Repository 설정 
main - release 브랜치로 나누어 업데이트에 활용할 브랜치를 구분 


- 백엔드
CORS 세팅
보안 강화를 하려고했으나 https 설정을 실패하면서 현재 배포된 웹페이지에서 CORS에러 발생

AWS 설정
최소한의 비용을 지불하는 ubuntu 계정을 사용 
github repository를 연동하여 CI/CD에 활용할 수있도록 설정
사용할 수 있는 nginx와 gunicorn 설치

Nginx 설정 확인 ( Static 관련 설정 )
default.conf 에 static 파일, media 파일들을 세팅
사용하게 될 포트와 django 프로젝트들을 기록 

Gunicorn 설정
사용하게 될 nginx 서비스를 연결 


CI / CD 정책 설정
Github action에서 사용하게될 설정들을 연결 
requirements 리스트를 활용해 의존성 설치 및 git pull, 그리고 nginx 리부트하도록 설정

Jwt 인증 정책관련 설정 
drf-simple-jwt 모듈을 활용하여 jwt를 활용하기로 결정
로그인 시 토큰을 받아 로컬 스토리지에서 기록하고, js를 통해 프론트엔드에서 확인, 
백엔드에서는 로그인 상태를 체크하여 인증 확인할 수 있도록 구성 

- 프론트엔드
서식 / 마크다운을 수용할 수 있는 텍스트 필드 구성
인증 데이터 체크 설정

6. 작업 주요 이슈 (out of Code)
작업 템포관련 
인강을 들으며 느긋하게 작업을 할 까 했는데, 밀도있게 작업하지 못하여 늘어진 부분이 있었다

작업 분량설정 관련 
상세 내용에 대한 인지가 부족해 중간중간 내용을 변경하거나 아쉬운 부분을 수정하는데 시간이 많이 소모되었다 

프로젝트 주체성 관련
처음에는 간단하게 이력서만 올라간 페이지를 만들고 싶었으나
배포와 관련된 실습이 필요하다 생각하여 관련 요소를 체크하다가 프로젝트의 주제가 변경되게 되었다