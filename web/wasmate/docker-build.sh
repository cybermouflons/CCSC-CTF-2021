IMAGE_NAME=cybermouflons/ccsc2021-wasmate

docker build ./setup -t ${IMAGE_NAME}

CID=$(docker create ${IMAGE_NAME})

docker cp ${CID}:/root/wasmate.tar.gz ./public/
docker rm ${CID}