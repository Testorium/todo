FROM node:22-alpine

WORKDIR /app

COPY ./frontend/package-lock.json ./
COPY ./frontend/package.json ./

RUN npm install

COPY ./frontend .

EXPOSE 3000

CMD ["npm", "run", "dev"]
