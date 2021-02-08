import sys
import inspect

from base64 import b64encode
from itertools import cycle
from jinja2 import Environment, FileSystemLoader

from secret import borgovs_moves

key = "MySup3rS3cr3tX0rKey!"


def encode(text, key):
    return b64encode(
        "".join(
            "{:02x}".format(a ^ ord(b))
            for a, b in zip(cycle(bytes(key, "utf-8")), text)
        ).encode()
    ).decode("utf-8")


if __name__ == "__main__":
    borgovs_moves = encode(borgovs_moves, key)
    encode_func_code = inspect.getsource(encode)

    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)

    template = env.get_template("borgovs-moves.py.template")
    with open("borgovs-moves.py", "w") as f:
        f.write(
            template.render(
                ENCODED_BORGOVS_MOVES=borgovs_moves,
                ENCODE_FUNC=encode_func_code,
                XOR_KEY=key,
            )
        )
