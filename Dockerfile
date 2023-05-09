FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /timestamp
COPY requirements.txt /timestamp/
RUN apt-get update && \
    apt-get install -y nano && \
    pip install -r requirements.txt
COPY . /timestamp/
