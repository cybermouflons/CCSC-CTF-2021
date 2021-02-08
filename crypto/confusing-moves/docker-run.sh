PORT=5000

cat <<- EOF > docker-compose.override.yml
version: '3.5'

services:

  web:
    ports:
      - ${PORT}:5000
  
EOF

docker-compose -f setup/docker-compose.yml -f docker-compose.override.yml up --build --force-recreate && docker-compose -f setup/docker-compose.yml -f docker-compose.override.yml rm -fsv

rm docker-compose.override.yml