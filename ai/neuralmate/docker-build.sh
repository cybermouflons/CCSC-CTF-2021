IMAGE_NAME=cybermouflons/ccsc2021-neuralmate

docker build ./setup -t ${IMAGE_NAME}

CID=$(docker create ${IMAGE_NAME})

docker cp ${CID}:/root/chall/neuralmate.py ./public/
docker cp ${CID}:/root/chall/service.py ./public/
docker cp ${CID}:/root/chall/requirements.txt ./public/ 
docker cp ${CID}:/root/chall/model ./public/
docker cp ${CID}:/root/chall/boards ./public/ 
docker rm ${CID}
