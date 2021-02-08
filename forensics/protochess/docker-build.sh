IMAGE_NAME=cybermouflons/ccsc2021-protochess
ENC_HOST=172.18.0.16
ENC_PORT=50051
CLIENT_HOST=172.18.0.32

docker build ./setup -t ${IMAGE_NAME}

docker network create --subnet=172.18.0.0/16 challnet || true

CID=$(docker run --net challnet --rm -d --ip ${ENC_HOST} --env ENC_PORT=${ENC_PORT} -it --name=enc_service ${IMAGE_NAME}:latest /bin/bash -c "(nohup tcpdump -U -w protochess.pcap &) && poetry run python enc_service.py")

sleep 3

docker exec -it ${CID} /bin/bash -c "curl https://en.wikipedia.org/wiki/Scholar%27s_mate"

docker run --net challnet --rm --ip ${CLIENT_HOST} --env ENC_HOST=${ENC_HOST} --env ENC_PORT=${ENC_PORT} -it --name=enc_client ${IMAGE_NAME}:latest /bin/bash -c "poetry run python enc_client.py"

docker exec -it ${CID} /bin/bash -c "curl https://duckduckgo.com/?q=grpc&t=h_&ia=web"

docker cp ${CID}:/chall/protochess.pcap ./public/ 
docker cp ${CID}:/chall/enc.proto ./public/ 

docker stop ${CID}
docker network rm challnet