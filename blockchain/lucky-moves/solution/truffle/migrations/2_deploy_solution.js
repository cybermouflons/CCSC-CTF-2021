const Solve = artifacts.require("Solve");
const fs = require('fs');

module.exports = (deployer) => {
    const luckymovesContractAddress = process.env.LUCKYMOVES_ADDR;

    deployer.deploy(Solve, luckymovesContractAddress)
        .then(() => Solve.deployed())
        .then(_instance => fs.writeFileSync("./solve_address.txt", _instance.address));
};