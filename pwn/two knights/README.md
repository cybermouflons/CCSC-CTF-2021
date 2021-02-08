# Two Knights
**Category:** pwn

**Author:** s3nn__

## Description
Beth got transported to the future where she found Elliot; he needs her help to understand why...

Sometimes two knights are better than a bishop pair

## Points
250

## Solution
<details>
 <summary>Reveal Spoiler</summary>

This is a classic stack-based buffer overflow, however there are not traditional ROP gadgets that end with the <code>ret</code> instruction. Instead, players will have to use jump-oriented programming to construct a JOP chain. Roughly, the steps to solve are as follows:

1. Calculate offset to RIP
2. Overwrite RBP for later usage
3. Overwrite RIP with stack pivot and start of JOP chain
4. Craft JOP chain to call <code>execve('/bin/sh', ['/bin/sh', '-p', '0'])</code>
	- this pops a shell on the target
	- it also doesn't drop privileges; this is required because the binary has the SUID bit set and the owner of the binary and the flag is ***root***

A solution that performs the above steps is provided in [sol.py](./sol/sol.py)

Run against local docker container<br>
<code>
	python3.7 sol.py R LHOST
</code>

Run against CyberRanges (IP might change, so adjust the value of the <code>HOST</code> parameter))<br>
<code>
	python3.7 sol.py R HOST=192.168.125.11
</code>

Run against local binary<br>
<code>
	python3.7 sol.py
</code>
</details>