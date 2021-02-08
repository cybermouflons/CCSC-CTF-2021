IMAGE_NAME=cybermouflons/ccsc2021-fortified-walls

docker build ./setup -t ${IMAGE_NAME}

CID=$(docker create ${IMAGE_NAME})
docker cp ${CID}:/root/chall/fortified-walls.tar.gz ./public/
docker rm ${CID}
