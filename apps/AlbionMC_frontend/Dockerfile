FROM node:21.6

WORKDIR /app

COPY package.json .

RUN npm i

COPY . .

CMD ["npm", "run", "prod"]