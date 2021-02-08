FROM python:3.8.1-slim

# install netcat
RUN apt-get update \
  && apt-get -y install netcat \
  && apt-get clean

# Install pipenv
RUN pip install pipenv

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add flag
COPY flag.txt /root/flag.txt

# add requirements
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock

# install requirements
RUN pipenv install 

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server
CMD ["./entrypoint.sh"]
