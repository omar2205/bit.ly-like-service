# Building the Frontend
FROM node:16-alpine3.16 as builder

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .

RUN npm install --silent

COPY . .

# EXPOSE 3000

ARG VITE_BACKEND_API_URL

RUN npm run build

# Hosting the Frontend
# FROM alpine:3.16 as static-host
FROM nginx:1.21-alpine

# RUN apk add thttpd

# RUN adduser -D static
# USER static

# WORKDIR /home/static

# COPY --from=builder /usr/src/app/build .

# CMD ["thttpd", "-D", "-h", "0.0.0.0", "-p", "3000", "-d", "/home/static", "-u", "static", "-l", "-", "-M", "60"]

COPY --from=builder /usr/src/app/build /usr/share/nginx/html