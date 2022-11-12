FROM python:3.9.6-slim-buster 

COPY . /app 
WORKDIR /app
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

