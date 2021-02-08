FROM python:3.8.1-slim

# Install pipenv
RUN pip install poetry

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add flag
COPY flag.txt /root/flag.txt

# add requirements
COPY ./pyproject.toml /usr/src/app/pyproject.toml
COPY ./poetry.lock /usr/src/app/poetry.lock

# install requirements
RUN poetry install

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# removing flag file because it's copied it elsewere already
RUN rm flag.txt

# run server
CMD ["./entrypoint.sh"]
