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
--> 로그인 유저
--> ModelViewSet을 활용 

- Diary 게시판 페이지 
Diary ( diary ) 
--> 

4. 백엔드 구조 설계 
GitHub Action - AWS Lightsail - 

5. 작업 주요 이슈 (in Code) 
- 작업 환경 설정
VSCODE 환경 설정
GitHub Repository 설정 

- 백엔드
CORS 세팅
AWS 설정
Nginx 설정 확인 ( Static 관련 설정 )
CI / CD 정책 설정
Jwt 인증 정책관련 설정 


- 프론트엔드
서식 / 마크다운을 수용할 수 있는 텍스트 필드 구성
인증 데이터 체크 설정

6. 작업 주요 이슈 (out of Code)
작업 템포관련 
작업 분량설정 관련 
프로젝트 주체성 관련