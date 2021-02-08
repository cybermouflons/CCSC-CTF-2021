IMAGE_NAME=cybermouflons/ccsc2021-singularity

docker build ./setup -t ${IMAGE_NAME}

CID=$(docker create ${IMAGE_NAME})

docker cp ${CID}:/home/sage/chall/flag.enc ./public/
docker cp ${CID}:/home/sage/chall/encrypt.py ./public/
docker rm ${CID}
