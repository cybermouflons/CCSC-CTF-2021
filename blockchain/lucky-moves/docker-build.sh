IMAGE_NAME=cybermouflons/ccsc2021-lucky-moves

[[ -z "$INFURA_PROJECT_ID" ]] && { echo "INFURA_PROJECT_ID environment variable not set!"; exit 1; }
[[ -z "$WALLET_MNEMONIC" ]] && { echo "WALLET_MNEMONIC environment variable not set!"; exit 1; }
[[ -z "$FROM_ADDR" ]] && { echo "FROM_ADDR environment variable not set!"; exit 1; }

docker build ./setup -t ${IMAGE_NAME} --build-arg INFURA_PROJECT_ID=${INFURA_PROJECT_ID}  --build-arg FROM_ADDR=${FROM_ADDR} --build-arg WALLET_MNEMONIC="${WALLET_MNEMONIC}"

CID=$(docker create ${IMAGE_NAME})

cp setup/truffle/contracts/LuckyMoves.sol public/LuckyMoves.sol
docker cp ${CID}:/challenge/luckymoves_address.txt ./public/
docker cp ${CID}:/challenge/getflag.py ./public/
docker rm ${CID}