FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && \
    apt-get install -y build-essential libjpeg-dev zlib1g-dev libpng-dev && \
    pip install -r requirements.txt
COPY . /code/