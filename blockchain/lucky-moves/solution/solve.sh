IMAGE_NAME=lucky-moves-solution

[[ -z "$INFURA_PROJECT_ID" ]] && { echo "INFURA_PROJECT_ID environment variable not set!"; exit 1; }
[[ -z "$WALLET_MNEMONIC" ]] && { echo "WALLET_MNEMONIC environment variable not set!"; exit 1; }
[[ -z "$WALLET_PRIVKEY" ]] && { echo "WALLET_PRIVKEY environment variable not set!"; exit 1; }
[[ -z "$LUCKYMOVES_ADDR" ]] && { echo "LUCKYMOVES_ADDR environment variable not set!"; exit 1; }
[[ -z "$CHALL_HOST" ]] && { echo "CHALL_HOST environment variable not set!"; exit 1; }
[[ -z "$CHALL_PORT" ]] && { echo "CHALL_PORT environment variable not set!"; exit 1; }

docker build . -t ${IMAGE_NAME} --build-arg LUCKYMOVES_ADDR=${LUCKYMOVES_ADDR} --build-arg INFURA_PROJECT_ID=${INFURA_PROJECT_ID} --build-arg WALLET_MNEMONIC="${WALLET_MNEMONIC}" --build-arg WALLET_PRIVKEY="${WALLET_PRIVKEY}"

docker run --env LUCKYMOVES_ADDR=${LUCKYMOVES_ADDR} --env INFURA_PROJECT_ID=${INFURA_PROJECT_ID} --env WALLET_PRIVKEY="${WALLET_PRIVKEY}" --env CHALL_HOST=${CHALL_HOST} --env CHALL_PORT=${CHALL_PORT} -it ${IMAGE_NAME} 