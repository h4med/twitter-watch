# FROM python:3.8
FROM mcr.microsoft.com/playwright/python:v1.31.0-focal

ENV PYTHONUNBUFFERED=1

# RUN apt-get update \
#   # dependencies for building Python packages
#   && apt-get install -y build-essential

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 

EXPOSE 8000