# Cap-i-sh
**Category:** misc
**Author:** ishtar

## Description
Beep boop bop...
A blessing and a curse :/

## Solution
<details>
 <summary>Reveal Spoiler</summary>

The main objective of this challenge is to familiarize the player with Linux capabilities (`man 7 capabilities`).
Abusing the `CAP_SYS_ADMIN` capability given to the python3 interpreter, in order to elevate privileges and obtain the flag.

Solution steps:
1. Identify possible ways to escalate privileges. Using `getcap -r / 2>/dev/null`, we can identify all binaries with capabilities.
2. Exploit `CAP_SYS_ADMIN` capability given to `python3` interpreter to escalate privileges and obtain the flag.

There are multiple ways to complete the challenge. One of them is described in the solution script, which is provided in [solve.py](./solution/solve.py)
</details>

