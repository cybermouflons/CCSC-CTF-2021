docker network create --driver bridge synchronous --subnet 172.16.4.0/24
docker-compose -f setup/docker-compose.yml -p synchronous-chess up --build -d --squash
