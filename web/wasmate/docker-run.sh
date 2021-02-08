IMAGE_NAME=cybermouflons/ccsc2021-wasmate

docker run --read-only --tmpfs=/tmp --rm -p 3000:3000 -it ${IMAGE_NAME} 