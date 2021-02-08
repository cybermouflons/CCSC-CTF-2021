# Chessanalyzer
**Category:** pwn

**Author:** R3D

## Description
Beth had to always write down every move in order to later analyze and improve her game.

We took care of the analysis part. Our software analyzes your moves to help you improve as fast as possible.

## Points
150

## Solution
<details>
 <summary>Reveal Spoiler</summary>

### Vulnerability
1. It provides an information leak opportunity when the `move.color`
   pointer is overwritten and the album name is printed.
2. It provides a write what where primitive when the `move.color` pointer
   is overwritten and input is provided to the second prompt.

### Exploit
1. Leak the address of puts@got
2. Get EIP control
3. Identify libc and gather offsets
4. Overwrite puts@got with system

A solution that performs the above steps is provided in [sol.py](./sol/sol.py)

Run against local docker container<br>
<code>
	python2.7 sol.py HOST=localhost
</code>

Run against CyberRanges (IP might change, so adjust the value of the <code>HOST</code> parameter))<br>
<code>
	python2.7 sol.py R HOST=192.168.125.11
</code>

Run against local binary<br>
<code>
	python2.7 sol.py
</code>
</details>
