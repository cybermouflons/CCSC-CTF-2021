const LuckyMoves = artifacts.require("LuckyMoves");
const fs = require('fs');

module.exports = async (deployer) => {
    await deployer.deploy(LuckyMoves, {from: process.env.FROM_ADDR})
        .then(() => LuckyMoves.deployed())
        .then(_instance => fs.writeFileSync("./luckymoves_address.txt", _instance.address));
};