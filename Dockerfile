FROM python:3.8.5

RUN pip install --upgrade pip

COPY . /local
WORKDIR /local

RUN pip install -r requirements.txt