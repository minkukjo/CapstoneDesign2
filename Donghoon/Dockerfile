# Pull base image.
FROM ubuntu:14.04
MAINTAINER Hoon

# Install Node.js
RUN apt-get update
RUN apt-get install --yes curl
RUN curl --silent --location https://deb.nodesource.com/setup_8.x | sudo bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes build-essential

# Bundle app source
COPY . /src

# Install app dependencies
WORKDIR /src/
RUN npm install

# Binds to port 8080
EXPOSE 8080

#Defines runtime

CMD ["npm", "start"]