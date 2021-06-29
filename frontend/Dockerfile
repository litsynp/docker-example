FROM node:latest
USER root

WORKDIR /frontend
COPY . /frontend

# Make variable API_URL to put uri into url
# uri 변수 형태로 받아서 url에 넣어 작동하도록 함
ARG API_URL
ENV REACT_APP_HOST_IP_ADDRESS $API_URL

RUN npm install
COPY . ./

# build file을 개발용에서는 불러오지 않기 때문에 개발용에서는 npm start 가능
RUN npm run build
