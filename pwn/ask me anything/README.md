# Ask Me Anything
**Category:** pwn

**Author:** R3D

## Description
This your chance to have a talk with Beth Harmon. We created this AMA(Ask Me Anything) service to provide the opportunity to simpletons like you to peek inside the mind of a genius like Beth Harmon.
Ask anything, don't be rude, don't be a brute and who knows you might actually get her to disclose some of her secrets :)

## Points
200

## Solution
<details>
 <summary>Reveal Spoiler</summary>

### Exploit
If you don't understand the following check the solution script, if you still dont understand maybe you should read more about ASLR and ROP and get back to this later.
<code>rop = base + p64(RET) + p64(POP_RDI) + p64(BINSH) + p64(SYSTEM)</code>

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
