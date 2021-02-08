# Queen's Encryption

**Category**: crypto

**Author**: koks

## Description

Have a good rest tonight. You'll need all the energy you can get for your game that resumes tomorrow.

Oh and by the way, I've studied the current position and noticed a weakness in one of his pieces. I think I have a solid tactic for your next move.

P.S. They won't know what hit them! I've encrypted my message using your favourite algorithm.

## Points

150

## Solution

<details>
  <summary>Reveal Spoiler</summary>
  A series of 19 [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) strings is given. The title should be a strong indicator that the position of the Queen is important. By visualizing the boards we can see that in some boards the black Queen is missing so we should focus only on the white Queen. A lookup table is also provided that maps a square (e.g. b7) to 2 possible values (only 64 squares but 128 possible ASCII characters.) Once the 19 positions of the Queen are retrieved, we can bruteforce the possible combinations of text that those positions map to (2^19 combinations). We can apply some heuristics here to reduce the noise (e.g. we know the flag starts with `CCSC{` and ends with `}`)
</details>
