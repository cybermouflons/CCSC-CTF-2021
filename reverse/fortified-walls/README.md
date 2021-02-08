# Crack in the Armor
**Category:** reverse

**Author:** \_Roko'sBasilisk\_

## Description

Borgov's knights tenaciously siege Beth's castle. The rooks move forward in a bid to fortify the walls.
Pressure is overwelming, yet she must endure. Borgov's head, ostensibly impenertable, can you find a way read through his next moves?

**NOTE:** The obfuscated python script will run only with **Python 3.7**

## Points
350

## Solution

<details>
 <summary>Reveal Spoiler</summary>

This challenges provides an obfuscated script string using PyArmor. PyArmor is currently one of the state-of-the-art protection techniques for Python scripts. It uses anti-debugging techniques, runtime encryption and codesusms which makes it very hard to reverse. The easiest way to reverse such binary is to build python from source and wirete code objects to disk as they evaluated. Still this does not beat the runtime unpacking (https://pyarmor.readthedocs.io/en/latest/how-to-do.html), however it becomes possible get constants, execution flow, names and many useful information from the code object structures. 

The solution provided in [solution folder](../solution) consists of a docker container that builds a patched Python 3.7 from source that dumps the code objects to disk in a `bytecode.pyc` file as they are evaluated (See [patch](../solution/ceval.patch). Now you can disassemble those code objects to extract readable information from. (Alternatively you can just run `strings` to get the strings in the file but disassembling provides more structured information.) To disassemble the objects a sample script is given in [disass.py](../disass.py). Note that the disassembling must run using Python3.7 in order to unpack teh code objects correctly. The unpacked code objects are given in [disass.txt](../disass.txt).

Finally, analyzing the unpacked code objects we can see some function names being called and the values of some constants. At this point, participants should search for the known text `"Please enter Borgov's moves: "`, in the line directly below that there is an interesting string `MySup3rS3cr3tX0rKey!`. Immediately, we know that we are dealing with some sort of XOR encryption just by the name and that this is the key. Scorlling further up in the code objects we can see another interesting string `N2M0MTdkNTUzMjU0NDc3MzcxMWIxMTA3NTQ2OTA5NWM2YjAxMDE0Mjc5NTkwMjEwNDYxMzQwNjMxZDQzMjM1NzQ3Nzg2MjE0MmY1ZDU5MTM3YzU3NzMxNzQzMTMzYzNiMDY0MzQwMDE1YTc4NzIxNzc4NDUzNzU5MmE0YTczNDc0MzFkNTIzNTRiMDQ0MTEzMWM2ZDEwNDA3ZjRiNTk3MDI4NGI3MzNlMTcwNA==` along with some interesting function names in the constants section (`cycle`, `b64encode`, `zip`....). Decoding the base64 string returns "7c417d5532544773711b11075469095c6b01014279590210461340631d432357477862142f5d59137c57731743133c3b064340015a787217784537592a4a7347431d52354b0441131c6d10407f4b5970284b733e1704".

From these clues the players are expected to try XORing the bytes of the decoded hex string with the given XOR key which will result to Borgov's next moves. The result can then be sent to the remote service and the flag is returned.

</details>