FROM node:15.12.0-alpine3.10 AS builder

COPY ./truffle /challenge

WORKDIR /challenge

RUN npm install

ARG INFURA_PROJECT_ID
ENV INFURA_PROJECT_ID=${INFURA_PROJECT_ID}
ARG WALLET_MNEMONIC
ENV WALLET_MNEMONIC=${WALLET_MNEMONIC}
ARG WALLET_PRIVKEY
ENV WALLET_PRIVKEY=${WALLET_PRIVKEY}
ARG LUCKYMOVES_ADDR
ENV LUCKYMOVES_ADDR=${LUCKYMOVES_ADDR}

RUN npx truffle migrate --network ropsten --reset

FROM bitnami/python:3.7-prod

COPY --from=builder /challenge/solve_address.txt /challenge/solve_address.txt
COPY --from=builder /challenge/build/contracts/Solve.json /challenge/Solve.json
COPY --from=builder /challenge/build/contracts/LuckyMoves.json /challenge/LuckyMoves.json

COPY ./exploit/requirements.txt /challenge/requirements.txt

RUN install_packages build-essential python3-dev python3-setuptools

WORKDIR /challenge

RUN pip install -r requirements.txt

COPY ./exploit /challenge

CMD ["python", "exploit.py"]
