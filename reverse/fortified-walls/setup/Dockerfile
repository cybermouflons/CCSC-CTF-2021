FROM cybermouflons/minideb-xinetd-python:0.1.0

COPY . /root/chall/ 

WORKDIR /root/chall/ 

RUN pip install poetry && \
    poetry install && \
    poetry run pyarmor obfuscate borgovs-moves.py && \
    cd dist && \
    tar -czvf ../fortified-walls.tar.gz --exclude='secret.py' . 

ENV ARGS "/root/chall/borgovs-moves.py"
ENV PORT 4000