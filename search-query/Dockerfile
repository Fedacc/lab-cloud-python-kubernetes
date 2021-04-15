FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000/tcp

ENTRYPOINT ["python","run.py"]