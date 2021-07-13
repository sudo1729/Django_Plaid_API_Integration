FROM alpine:latest
RUN mkdir /app
RUN apk add --no-cache python3 py3-pip

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
# CMD python3 manage.py runserver 0.0.0.0:$PORT