# Resignation
**Category:** pwn

**Author:** s3nn__

## Description
One of Shaibel's first lessons to Beth was showing her how to resign...

Returning back to the board, help Beth force resignation from her teacher.

## Points
150

## Solution
<details>
 <summary>Reveal Spoiler</summary>

This is a classic stack-based buffer overflow, however the binary is statically linked and there are not enough ROP gadgets to construct a full <code>execve</code>chain. Instead, players will have to use sigreturn-oriented programming to populate the necessary registers. Roughly, the steps to solve are as follows:

1. Calculate offset to RIP
2. Find POP RAX RET gadget
3. Overwrite RIP with gadget
4. Craft fake SIGRRETURN frame to populate RDI, RAX and RIP to call <code>execve('/bin/sh', [0])</code>

A solution that performs the above steps is provided in [sol.py](./sol/sol.py)

Run against local binary<br>
<code>
	python3.7 sol.py
</code><br><br>
Run against local docker container<br>
<code>
	python3.7 sol.py HOST=localhost PORT=4337
</code><br><br>
Run against CyberRanges (IP might change, so adjust the value of the <code>HOST</code> parameter))<br>
<code>
	python3.7 sol.py R HOST=192.168.125.11 PORT=4337
</code>