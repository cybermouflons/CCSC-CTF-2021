FROM cybermouflons/minideb-xinetd-python:0.1.0-python3.8

COPY ./pyproject.toml /root/chall/pyproject.toml
COPY ./poetry.lock /root/chall/poetry.lock

WORKDIR /root/chall/ 

RUN pip install poetry && \
    python -m poetry export -f requirements.txt > requirements.txt
RUN pip install --no-deps -r requirements.txt

COPY ./ /root/chall/

ENV ARGS "/root/chall/service.py"

ENV TF_CPP_MIN_LOG_LEVEL 3