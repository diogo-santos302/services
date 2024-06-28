FROM canyan/janus-gateway:latest

RUN apt-get update && apt-get install -y nginx

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./echotest.html /usr/share/nginx/html
COPY ./echotest.js /usr/share/nginx/html
COPY ./settings.js /usr/share/nginx/html
COPY ./janus.js /usr/share/nginx/html

EXPOSE 8081
EXPOSE 8188

CMD service nginx start && /usr/local/bin/janus
