FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN rm -rf /var/cache/apt/lists

WORKDIR /django

COPY requirements.txt requirements.txt
COPY . .

RUN python -m pip install -r requirements.txt
RUN rm -Rf /root/.cache/pip

ENV DJANGO_SECRET_KEY=value
ENV STATIC_ROOT=value
ENV DJANGO_ALLOWED_HOST=value
ENV DB_ENGINE=value
ENV DB_HOST=value
ENV DB_NAME=value
ENV DB_USER=value
ENV DB_PASS=value
ENV DB_PORT=value