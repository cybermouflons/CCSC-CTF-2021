IMAGE_NAME=cybermouflons/ccsc2021-confusing-moves
PYPI_IMAGE_NAME=cybermouflons/ccsc2021-confusing-moves-internalpypi

cat <<- EOF > docker-compose.override.yml
version: '3.5'

services:

  web:
    image: ${IMAGE_NAME}
  
  internalpypi:
    image: ${PYPI_IMAGE_NAME}
EOF

docker-compose -f setup/docker-compose.yml -f docker-compose.override.yml build

rm docker-compose.override.yml