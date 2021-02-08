from base64 import b64encode
from itertools import cycle

encoded_borgovs_moves = "N2M0MTdkNTUzMjU0NDc3MzcxMWIxMTA3NTQ2OTA5NWM2YjAxMDE0Mjc5NTkwMjEwNDYxMzQwNjMxZDQzMjM1NzQ3Nzg2MjE0MmY1ZDU5MTM3YzU3NzMxNzQzMTMzYzNiMDY0MzQwMDE1YTc4NzIxNzc4NDUzNzU5MmE0YTczNDc0MzFkNTIzNTRiMDQ0MTEzMWM2ZDEwNDA3ZjRiNTk3MDI4NGI3MzNlMTcwNA=="

def encode(text, key):
    return b64encode(
        "".join(
            "{:02x}".format(a ^ ord(b))
            for a, b in zip(cycle(bytes(key, "utf-8")), text)
        ).encode()
    ).decode("utf-8")


def validate():
    moves = input("Please enter Borgov's moves: ")
    return encode(moves, "MySup3rS3cr3tX0rKey!") == encoded_borgovs_moves


if __name__ == "__main__":
    if validate():
        from secret import flag

        print(flag)
    else:
        print("Better luck next time kiddo ... ")