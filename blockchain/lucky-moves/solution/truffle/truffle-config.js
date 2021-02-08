const HDWalletProvider = require('@truffle/hdwallet-provider');

const infura_project_id = process.env.INFURA_PROJECT_ID
const mnemonic = process.env.WALLET_MNEMONIC

module.exports = {

  networks: {
    ropsten: {
      provider: () => new HDWalletProvider(mnemonic, `https://ropsten.infura.io/v3/${infura_project_id}`),
      network_id: 3, // Ropsten's id
      gas: 5500000, // Ropsten has a lower block limit than mainnet
      confirmations: 0, // # of confs to wait between deployments. (default: 0)
      timeoutBlocks: 200, // # of blocks before a deployment times out  (minimum/default: 50)
      skipDryRun: true // Skip dry run before migrations? (default: false for public nets )
    },
  },

  mocha: {},

  compilers: {
    solc: {
      version: "0.8.0", // Fetch exact version from solc-bin (default: truffle's version)
    }
  },


  db: {
    enabled: false
  }
};