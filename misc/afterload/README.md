# Afterload
**Category:** misc
**Author:** ishtar

## Description
Beep boop bop...
A blessing and a curse :/

## Solution
<details>
 <summary>Reveal Spoiler</summary>

The main objective of this challenge is to familiarize the player with "shared library hijacking" and "function hooking" in Linux, abusing the preload mechanism.
The `ld.so.preload` file does not suffer from the `LD_PRELOAD` environment variable restrictions when running SUID binaries. Thus, it is possible to define our custom shared library which will allow us to escalate our privileges upon running any SUID binary, by hooking any function used (while privileges are not dropped), such as `geteuid` in `su` (as in the provided solution).

Solution steps:
1. Identify possible ways to escalate privileges. `ld.so.preload` file is world-writable (`find / -type f -writable 2>/dev/null`).
2. Compile an evil shared library, and escalate privileges to obtain the flag.

A solution for this challenge, is provided in [solve.c](./solution/solve.c)
</details>
