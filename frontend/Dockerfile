FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080/tcp

ENTRYPOINT ["python","run.py"]