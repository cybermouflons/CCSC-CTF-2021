IMAGE_NAME=cybermouflons/ccsc2021-less-said-the-better

docker build ./setup -t ${IMAGE_NAME}

CID=$(docker create ${IMAGE_NAME})

docker cp ${CID}:/home/sage/chall/chall.txt ./setup/ 
docker rm ${CID}
