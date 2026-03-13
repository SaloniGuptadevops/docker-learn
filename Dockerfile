#Take Pateela

FROM nginx

WORKDIR /app

copy index.html /var/www/html

EXPOSE 80
