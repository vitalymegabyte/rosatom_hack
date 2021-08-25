# base image
FROM node:12-buster-slim

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache react_app dependencies
COPY package.json /app/package.json
RUN npm install

COPY . .

# start react_app
CMD ["npm", "start"]
