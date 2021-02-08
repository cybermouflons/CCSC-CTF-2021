docker network create --driver bridge wcd --subnet 172.16.3.0/24
docker-compose -f setup/docker-compose.yml -p "chess-trickery" up --build -d
