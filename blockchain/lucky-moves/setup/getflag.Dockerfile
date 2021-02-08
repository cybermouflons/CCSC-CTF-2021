FROM node:15.12.0-alpine3.10 AS builder

COPY ./truffle /challenge

WORKDIR /challenge

RUN npm install

RUN npx truffle compile


FROM cybermouflons/minideb-xinetd-python:0.1.0


COPY ./getflag /challenge

COPY --from=builder /challenge/build/contracts/LuckyMoves.json /challenge/LuckyMoves.json

WORKDIR /challenge

RUN install_packages build-essential python3-dev python3-setuptools

RUN pip install -r requirements.txt

ENV ARGS "/challenge/getflag.py"
ENV PORT 8085
