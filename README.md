# Docker Example

**English** | [한국어](https://github.com/litsynp/docker-example/blob/main/README.ko.md)

![Web App Screenshot](https://user-images.githubusercontent.com/42485462/175573053-a9292722-8c12-492a-b60c-14cb4d12fab5.png)

This is a repository to demonstrate how to develop a full-stack web application using Docker.

You can simply run the application with [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).

The application implemented is a todo app like a [Microsoft To Do](https://todo.microsoft.com/).

## Description

- Back-end: Django (Created using `django-admin startproject backend`)

- Front-end: React (Created using `npx create-react-app frontend`)

- Database: [PostgreSQL](https://www.postgresql.org/)

## Installation

- Clone the repository using this command.

  ```sh
  $ git clone --recursive https://github.com/litsynp/docker-example.git
  ```

  - If you missed `--recursive` option, fetch the frontend submodule using `git clone`.

## How To

- Put all the python modules in `requirements.txt`.

- Run `yarn` in `frontend` directory to fetch yarn modules.

  ```sh
  $ cd frontend
  $ yarn
  ```

- Run `docker compose up --build` in the root directory. You will create front-end, back-end and database Docker containers.

- When the docker containers are all up and running, open another terminal and run `docker-compose exec backend python manage.py migrate` to proceed with data migration. If you skip this, you will encounter an error in Django backend container later, because the DB has not been initialized.

## Stop/Remove the servers and containers

- `docker compose down` for just stopping the server.

  - If you want to run the server again after stopping it, run `docker compose up` again.

- `docker compose down -v` to stop and **remove** the server. This will remove all the volumes of the containers.

  - If you want to run the server again after stopping and removing it, run `docker compose up --build`. Build only when you are running the server for the first time.

## Notes

- The production build `prod` includes NGINX as a load balancer.

- To run as production build, append `-f docker-compose.prod.yml` after `docker compose` for all the commands above.

  - e.g., `docker compose -f docker-compose.prod.yml up`

- You can include `.vscode`, which includes workspace settings for [Visual Studio Code](https://code.visualstudio.com/), to `.gitignore` as well. It is included as an example here.

## Secret Management - `.env`

`.env` files are for keeping secrets and credentials that should not be exposed to Git repository.

You must inlcude them to `.gitignore` so that the Git repository doesn't include it.

- There are sample `.env` files of `dev` and `prod` build in `settings` directory.
