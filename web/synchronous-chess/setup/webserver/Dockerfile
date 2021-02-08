FROM python:2.7-alpine
RUN apk add --virtual build-deps file make g++ gcc musl-dev libffi-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app/ /app
WORKDIR /app
CMD gunicorn --keep-alive 10 -k gevent -b 0.0.0.0:80 -w 4 app:app --access-logfile /tmp/gunicorn-access.log --error-logfile /tmp/gunicorn-error.log
