# Wasmate
**Category:** web,pwn

**Author:** \_Roko'sBasilisk\_

## Description

I'm sick of missing all the obvious checkmate moves! Hopefully, my new cutting-edge tool will alert me whenever there is a possible checkmate in a single move! 

Let's do this...

## Points
500

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The source code is given to the participants which makes it easy to identify the technology stack of the challenge. It is a simple NodeJS web application which uses WebAssembly for some operations. Using WebAssembly introduces speed and efficiency, yet it opens the door for exploiting memory corruption vulnerabilities (albeit somewhat differently) in a web application environment.

In this case reviewing the provides [chesslib.c](./setup/lib/chesslib.c) file we can see there is a buffer overflow issue in the snippet below:
```C
extern int check_mate(char* fen) {
    BoardChecker checker;
    checker.is_mate = &C;
    checker.logger = &logger;
   
    strcpy(checker.fen, fen);
    return checker.is_mate(checker.fen);
}
```

The `fen` buffer is copied to the `checker.fen` buffer (128 bytes length) without the appropriate length checks. 

By inpsecting the BoardChecker structure (provided in [chesslib.h](./setup/lib/chesslib.h) it is easy to see, that by overwriting the fen buffer we cna overwrite the `is_mate` function pointer. This function is invoked in the `check_mate` function which is in turn used by the main web application. With this in mind, it can also be observer that the `logger` function is vulnerable to a code injection attack as it uses `emscripten_run_script_int` to execute native javascript. Keep in mind we also control teh arguments that will be called with (`fen`). In a NodeJS environment this shouts RCE! 

Now the final missing piece is to identify what value the is_mate pointer needs to be replaced with. Fortunately, this can be easily inferred in the case of WebAssembly because when a function pointer is declared within the scope of the function (`checker.logger = &logger;`) it is assigned to a indirect index pointer that is then used to invoke the function using the `call_indirect` instruction. The indices are assigned in the order they appear, thus in this case the index pointer of logger function would be '2' or in hex '0x02'. Alternatively, participants can run the challenge locally and print the pointer assigned at runtime to inspect the value. 

Normally having achieved RCE, it is possible to perform an OOB attack and retrieve the flag using an http/dns request or something like that, however in the environment that the challenge is deployed, outbound connections are restricted and the file-system is read-only. In this case the attack can still be performed blindly. `emscripten_run_script_int` returns the output of the evaluated javascript as an integer so theoretically we can convert whatever the response is to integer and return it. Practically though, the template ([index.ejs](./setup/views/index.ejs)) only changes on 4 distinct values (0,1,8,16). With this in mind we can utilise the changes in the response when the function output is 0 and 1, therefore performing a boolean based blind attack. 

Stitching all these clues together, an attack can be composed as follows:

1. Craft a payload that overwrites the is_mate function pointer with the value 0x02 (`logger` function pointer) and uses the appropriate payload to read the flag fetches the character at position 0 and compare it with a letter.
2. Identify the changes in response and bruteforce the flag character by character until the whole flag is revealed.

A fully scripted solution that performs this attack is provided at [solution.py](./solution/solution.py)

### References:
https://i.blackhat.com/us-18/Thu-August-9/us-18-Lukasiewicz-WebAssembly-A-New-World-of-Native_Exploits-On-The-Web-wp.pdf

https://www.youtube.com/watch?v=DFPD9yI-C70&ab_channel=BlackHat

</details>