FROM node:20 AS build
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
RUN npm install -g @angular/cli
RUN npm install --save @types/lodash 
COPY . /app
EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0"]