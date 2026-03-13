<<<<<<< HEAD
#Take Pateela

FROM nginx

WORKDIR /app

copy index.html /var/www/html

EXPOSE 80
=======
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","run.py"]
>>>>>>> c8dca5c94e18ebf806ef7f67fdfea849eba1967e
