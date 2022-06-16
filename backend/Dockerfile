FROM python:3.10.5-alpine3.16

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["python", "app.py"]