FROM python:alpine3.15

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3","app.py" ]