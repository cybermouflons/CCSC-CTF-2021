IMAGE_NAME=cybermouflons/ccsc2021-duncan-chess-academy

cat <<- EOF > docker-compose.override.yml
version: '3.5'

services:

  web:
    image: ${IMAGE_NAME}
EOF

tar czf ./public/webapp.tar.gz -C ./setup/webapp/ --exclude="__pycache__" . 

docker-compose -f setup/docker-compose.yml -f docker-compose.override.yml build

rm docker-compose.override.yml