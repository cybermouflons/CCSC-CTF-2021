FROM bitnami/python

RUN install_packages tcpdump curl

COPY . /chall

WORKDIR /chall

RUN pip install poetry && poetry install 
