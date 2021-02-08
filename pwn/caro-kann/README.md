# Caro-Kann Defence
**Category:** pwn

**Author:** s3nn__

## Description
The Caro-Kann is all pwns and no hope...

Show Beth why there are better defences against 1.e4

## Points
300

## Solution
<details>
 <summary>Reveal Spoiler</summary>

There is a Double-free vulnerability in the binary; libc2.31 is used, compiled without tcache support. Players need to exploit the double-free vulnerability to carry out a fastinb dup to

1. Carry out an unsortedbin attack to get heap and libc leak
2. Overwrite the \_\_malloc_hook to achieve code execution

A solution that performs the above steps is provided in [sol.py](./sol/sol.py). Use the following:

Run against local docker container<br>
<code>
	python3.7 sol.py R LHOST
</code>

Run against CyberRanges (IP might change in [sol.py](./sol/sol.py))<br>
<code>
	python3.7 sol.py R
</code>

Run against local binary<br>
<code>
	python3.7 sol.py
</code>

</details>
