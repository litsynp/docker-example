# docker-example

## Description

- backend: Django (`django-admin startproject backend`으로 생성)

- frontend: React.js (`npx create-react-app frontend`으로 생성)

- db: PostgreSQL 사용

## 사용법

- requirements.txt에 필요한 모듈을 담아둔다

- frontend에서 `npm i`를 해서 모듈을 최신화한다

- 프로젝트 루트 디렉토리에서 `docker compose up --build`를 한다

- 서버를 내릴 땐 `docker compose down`을 하고, 삭제할 때는 `docker compose down -v`를 한다

- 다시 올릴 땐 `docker compose up`을 한다 (삭제 후에 돌릴 땐 `--build` 를 붙여준다 (처음에만 빌드!))

## env 파일 관리

- settings 디렉토리에 dev, prod 버전의 env 파일이 존재한다
