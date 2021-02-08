FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y
RUN apt install -y git zlib1g-dev libffi-dev libssl-dev libbz2-dev libncursesw5-dev libgdbm-dev liblzma-dev libsqlite3-dev uuid-dev libreadline-dev vim build-essential

COPY ceval.patch /chall/ceval.patch

RUN git clone https://github.com/python/cpython && \
    cd cpython && \
    git checkout 3.7 && \
    git apply /chall/ceval.patch && \
    ./configure && \
    make && \
    make install

CMD ["python3", "/chall/borgovs-moves.py"]
