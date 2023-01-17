# Docker Example

[English](https://github.com/litsynp/docker-example/blob/main/README.md) | **한국어**

![Web App Screenshot](https://user-images.githubusercontent.com/42485462/175573053-a9292722-8c12-492a-b60c-14cb4d12fab5.png)

Docker를 이용한 간단한 full stack 개발을 위해 만들어진 예시용 repository 입니다.

[Docker](https://www.docker.com/)와 [Docker Compose](https://docs.docker.com/compose/)를 이용해 웹 애플리케이션을 간단하게 실행해볼 수 있습니다.

구현된 예제는 [Microsoft To Do 앱](https://todo.microsoft.com/)과 유사한 Todo 앱입니다.

## 설명

- 백엔드: [Django](https://www.djangoproject.com/) - [Django REST Framework](https://www.django-rest-framework.org/) (`django-admin startproject backend`으로 생성)

- 프론트엔드: [React](https://reactjs.org/) - [Create-React-App](https://create-react-app.dev/) (`npx create-react-app frontend`으로 생성)

- 데이터베이스 (DB): [PostgreSQL](https://www.postgresql.org/)

## 설치

- 해당 repository를 서브모듈과 함께 clone 받습니다.

  ```sh
  $ git clone --recursive https://github.com/litsynp/docker-example.git
  ```

  - `--recursive` 옵션을 빼고 실행하셨다면, `git clone`을 이용해 프론트엔드 모듈을 따로 받아줍니다.

## 사용법

- `requirements.txt`에 필요한 모듈을 담아둡니다.

- frontend 경로에서 `yarn`을 해서 모듈을 최신화합니다.

  ```sh
  $ cd frontend
  $ yarn
  ```

- 프로젝트 루트 디렉토리에서 `docker compose up --build`를 실행합니다. 프론트엔드와 백엔드, 데이터베이스 도커 컨테이너를 생성하게 됩니다.

- 도커 컨테이너가 완전히 올라간 후, 다른 터미널을 하나 더 열어서 `docker-compose exec backend python manage.py migrate` 를 입력하여 데이터 마이그레이션을 진행합니다. 이를 진행하지 않으면 DB가 생성되지 않기 때문에 나중에 Django 백엔드에서 오류가 발생합니다.

## 서버와 컨테이너 중지 및 삭제

- 서버를 내릴 땐 `docker compose down`을 실행합니다.

  - 서버를 내린 후 다시 올릴 땐 `docker compose up`을 실행하면 됩니다.

- 서버를 내리고 **삭제까지** 할 때는 `docker compose down -v`를 실행합니다. 컨테이너의 볼륨도 지우게 됩니다.

  - 서버를 내리고 삭제한 후 다시 올릴 땐 `docker compose up --build`을 실행하면 됩니다. 항상 처음에만 빌드하면 됩니다.

## 추가 사항

- Production build (배포 버전)에는 로드 밸런서로 사용할 NGINX가 포함되어 있습니다.

- Production build로 실행하려면 위의 명령어들 (`docker compose`) 뒤에 `-f docker-compose.prod.yml` 명령어를 붙여서 사용하면 됩니다.

  - (e.g., `docker compose -f docker-compose.prod.yml up`)

- [Visual Studio Code](https://code.visualstudio.com/)의 워크스페이스 설정을 담고 있는 폴더인 `.vscode`를 `.gitignore`에 추가하셔도 됩니다. 여기서는 예시로 포함해두었습니다.

## 비밀 파일 관리 - `.env`

`.env` 파일은 주로 공개되선 안되는 비밀 정보를 담는 데에 사용되며, Git repository에 공개되선 안됩니다.

`.gitignore` 파일에 `.env`를 추가해 Git repository에 추가되지 않도록 합시다.

- `settings` 디렉토리에 예시를 위한 `dev`, `prod` 빌드 버전의 `.env` 파일이 존재합니다.

## ELK 로깅

- logging-example 서브 모듈을 사용하여 **배포 버전**에서 로깅이 가능합니다.
- *단일 compose 파일 실행시 동작하지 않습니다.*

### 동작 방식
1. NGINX의 로그파일을 Filebeat로 수집
2. 수집한 로그를 Logstash에 전달
3. 전달 받은 로그를 Elasticsearch에 저장
4. 저장된 로그를 Kibana를 통해 분석

### 사용법

  ```sh
 $ docker compose -f docker-compose.prod.yml -f docker-compose.logging.yml up --build
  ```

### Kibana를 통한 로그 시각화 방법
1. localhost:5601 접속
2. 상단 메뉴에서 index management 검색 
3. 수집된 로그 인덱스 확인 weblogs-yyyy.MM.dd 형식
4. 좌측 메뉴의 Analytics의 Dashboard 클릭
5. Create data view를 통해 인덱스 선택
   - 전체 조회 : Index Pattern에 `weblogs-*` 입력 및 저장
   - 선택 조회 : Index Pattern에 보고싶은 날짜입력 (eg. `weblogs-2023.01.01`)
6. Create Visualization 클릭
7. 보고 싶은 필드를 화면에 드롭다운 하여 시각화