import json

from web3 import Web3, HTTPProvider
from os import environ, path

BASE_DIR = path.dirname(path.realpath(__file__))

INFURA_PROJECT_ID = environ.get('INFURA_PROJECT_ID')
LUCKYMOVES_ADDR = environ.get('LUCKYMOVES_ADDR', None) or open(path.join(BASE_DIR, "luckymoves_address.txt"), "r").read()
FLAG = open(path.join(BASE_DIR, "flag.txt"), "r").read()
COMPILED_LUCKYMOVES = json.load(open(path.join(BASE_DIR, "LuckyMoves.json"), "r"))

w3 = Web3(HTTPProvider(f"https://ropsten.infura.io/v3/{INFURA_PROJECT_ID}"))

intro = f"""Chess is a game of skill.
Luck, rarely affects the superiority of a skilled grandmaster.
Yet sometimes you need to have luck by your side...

Baltik argues that you can never be lucky enough to win a game of chess, so he created a smart contract on the blockchain to test this.

Exploit the LuckyMoves.sol contract which is deployed at {LUCKYMOVES_ADDR} on the Ethereum Ropsten Testnet.

When done, sign a message "Gib me flag" with the private key of your the Ethereum address used to exploit the contract.
Send the signed message to this server by following the instructions below and your flag will be yours!
============================================================================================================
"""

print(intro)

# Message hash of "Gib me flag" message
expected_message_hash = "0xb407ccc274837cb6a3b45544386b551fca6883cddbfe3c9b7f302fd335d73c22"

sig = input("Please enter your signature as a hex string:\n")

public_addr = w3.eth.account.recoverHash(expected_message_hash, signature=sig)

luckymoves_contract = w3.eth.contract(
    address=LUCKYMOVES_ADDR,
    abi=COMPILED_LUCKYMOVES["abi"]
)

is_solved = luckymoves_contract.functions.hasSolved(public_addr).call()

if is_solved:
    print(FLAG)
else:
    print("It seems that you haven't yet solved the challenge my friend...")