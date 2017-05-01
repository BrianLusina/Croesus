FROM ubuntu:latest

MAINTAINER Brian Lusina "lusinabrian@gmail.com"

# install node
RUN apt-get update -y && apt-get install -y node

# We copy just the requirements.txt first to leverage Docker cache
COPY ./package.json /app/package.json

WORKDIR /app

RUN npm install

COPY . /app

# this will expose this app to other containers via port 8000
EXPOSE 5000

CMD ["npm", "run", "build"]

CMD ["npm", "run", "start"]
