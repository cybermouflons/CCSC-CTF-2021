# Doubled Pwns
**Category:** pwn

**Author:** s3nn__

## Description
This is Beth's chance to get back at Benny by attacking his doubled pwns.

## Points
300

## Solution
<details>
 <summary>Reveal Spoiler</summary>

There is a double-free vulnerability in the binary; libc2.27 is used, compiled with tcache support. Players need to exploit the double-free vulnerability to carry out a tcachebin dup to

1. Carry out an unsortedbin attack to get a heap and libc leak
2. Overwrite the \_\_free_hook to achieve code execution

A solution that performs the above steps is provided in [sol.py](./sol/sol.py)
Use the following:

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
