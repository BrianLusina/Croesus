FROM node:7

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

RUN mkdir -p /src/app

WORKDIR /src/app

# copy package.json
COPY package.json /src/app

# run an npm install
RUN npm install

# bundle app source
COPY . /src/app

EXPOSE 3000

CMD ["npm", "run", "start"]
