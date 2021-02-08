// SPDX-License-Identifier: UNLICENSED

pragma solidity 0.8.0;

contract LuckyMoves {
    uint256 private seed = 1;
    uint256 private constant MAXBET = 75149865395201;

    mapping(address => uint8) public hits;

    constructor() {
        seed = rand(1024);
    }

    function rand(uint256 max) private view returns (uint256 result) {
        uint256 blockNum = block.number - (seed % 255);
        uint256 hashVal = uint256(blockhash(blockNum));
        return (uint256(hashVal) % max);
    }

    function spin(uint256 bet) public returns (uint256 result) {
        require(bet < MAXBET, "Your bet must be lesst than 75149865395201");

        uint256 num = rand(MAXBET);
        seed = rand(1024);

        if (num == bet) {
            if (hits[tx.origin] > 0) {
                hits[tx.origin] <<= 1;
            }
            hits[tx.origin] += 1;
        } else {
            hits[tx.origin] = 0;
        }

        return num;
    }

    function hasSolved(address player) public view returns (bool) {
        return hits[player] == 255;
    }
}
