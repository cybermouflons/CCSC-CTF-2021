docker network create --driver bridge sql-truncation --subnet 172.16.5.0/24
docker-compose -f setup/docker-compose.yml -p "cate-bianca" up --build -d
