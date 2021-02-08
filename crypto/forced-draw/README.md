# Forced Draw

**Category:** crypto

**Author:** koks

## Description

I kept telling him it's a forced draw but he didn't believe me.
We played it out a for a while until he finally realized and agreed on a draw. What a noob!

I was so tilted towards the end I forgot to write down the last 7 moves...

The officials couldn't help me much. They just gave me some hashes and their hashing algorithm.

Can you help me figure out what the last 7 moves were?

Flag Format:
Concatenate moves 49, 50, 51, 52, 53, 54 and 55 with `_` (without the move number) and wrap in `CCSC{}`.

Example:

```
20. c5+ Kh8
21. Qc4 Bg5
22. Qxd4 Qxd4
23. Bxd4 Nxd3
24. Bxe3 Rae8
25. Bf2 Bxf4
26. Bxc6 Bh3+
27. Bg2 Bxg3

CCSC{c5+_Kh8_Qc4_Bg5_Qxd4_Qxd4_Bxd4_Nxd3_Bxe3_Rae8_Bf2_Bxf4_Bxc6_Bh3+_Bg2_Bxg3}
```

## Points

200

<details>
<summary>Reveal Spoiler</summary>

Identify that the position hashes are generated using Zorbist Hashing (https://iq.opengenus.org/zobrist-hashing-game-theory/). Since there are only 7 pieces left on the board for the game given, we can enumerate all possible piece moves at every turn, hash the new positions using the algorithm given, and if we get a matching hash it means we found the correct piece move that was actually played.

</details>
