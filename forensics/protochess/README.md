# Protochess
**Category:** forensics,crypto

**Author:** \_Roko'sBasilisk\_

## Description

Do you know that Shatranj is a proto-version of chess? But anyway, it's time to move on to modern stuff.


## Points
150

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The purpose of this challenge is to disect and isolate the gRPC messages in order to get the iv, encrypted_flag and key so that they can be trivially decrypted using AES in CBC mode.

The solution is as follows:
1. Open pcap file and isolate relevant gRPC protocol packets (can be identified from port numbers and data)
2. Use the provided proto file to have wireshark disect the packets for you. (See https://grpc.io/blog/wireshark/)
3. Get iv, ciphertext (flag) and key and use python or any other apprpriate tool to decrypt the ciphertext and get the flag.


</details>