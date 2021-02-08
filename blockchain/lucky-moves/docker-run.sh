IMAGE_NAME=cybermouflons/ccsc2021-lucky-moves

[[ -z "$INFURA_PROJECT_ID" ]] && { echo "INFURA_PROJECT_ID environment variable not set!"; exit 1; }

docker run --rm -p 8085:8085 --env INFURA_PROJECT_ID=${INFURA_PROJECT_ID} -it ${IMAGE_NAME}