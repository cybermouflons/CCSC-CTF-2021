IMAGE_NAME=cybermouflons/ccsc2021-duncan-chess-academy
PORT=8080

cat <<- EOF > docker-compose.override.yml
version: '3.5'

services:

  web:
    ports:
      - ${PORT}:5000
EOF

docker-compose -p dca -f setup/docker-compose.yml -f docker-compose.override.yml up && docker-compose -p dca -f setup/docker-compose.yml -f docker-compose.override.yml rm -fsv

rm docker-compose.override.yml