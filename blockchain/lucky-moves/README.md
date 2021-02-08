# Confusing Moves
**Category:** blockchain

**Author:** \_Roko'sBasilisk\_

## Description

Chess is not a game of luck... or is it?

NOTE: The contract is deployed on tEhereum Ropsten testnet. You can use this faucet https://faucet.ropsten.be/ to get some Ether in your wallet.

## Points
500

## Solution

<details>
 <summary>Reveal Spoiler</summary>

This challenge provides participants with a deployed smart contract on Ethereum Ropsten testnet. The contract's source code is provided as well, so the first step towards solving this, is to understand the code of the smart contract. In a nutshell, the smart contract provides a random number generator and uses that to compare with what the user provded in the `spin` function. The vulnerability here is the attempt to generate randomness using on-chain values (i.e. seed in smart contracts storage and block number). The execution will alwaus be deterministic - and HAS to be by design - in order to be validated by all the blockchain nodes in a distirbuted manner. Therefore generating random numbers like this in a smart contract is a very bad idea.

This example is almost identical to the vulnerability in Slotethereum's smart contracts (https://github.com/slotthereum/source/issues/1).

To solve this, participants must first fetch the seed from the contract's internal storage. Although this is declared as private, it can still be exposed using the `getStorageAt` call of the Ethereum RPC API. With the seed in hand, participants must develop their own smart contract (example given in [Solve.sol](./solution/truffle/contracts/Solve.sol) ) that calls the provided contract's spin function. The rand function can be replicated in the Sovle contract and therefore since the transaction will be in the same block for both of the contracts the random value can be predicted. 

This should be repeated 8 times in sucession so that the `hits` mapping  within the contract equals to 255 for the participant's address.

When this is achieved, participants, must use their private key to sign the message "Gib me flag" and send the signature to the netcat service provided. 

A fully automated example of the whole exploit chain is provided in the [solution](./solution) folder. Just set the appropriate environment variables and run `solve.sh`.

</details>