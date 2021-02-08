from itertools import cycle
from pwn import *

HOST = "localhost"
PORT = 4000

extraced_hex_string = "7c417d5532544773711b11075469095c6b01014279590210461340631d432357477862142f5d59137c57731743133c3b064340015a787217784537592a4a7347431d52354b0441131c6d10407f4b5970284b733e1704"
xor_key = "MySup3rS3cr3tX0rKey!"

borgovs_moves = "".join(chr(ord(a) ^ b) for a, b in zip(cycle(xor_key), bytes.fromhex(extraced_hex_string)))

io = remote(HOST, PORT)
io.recvuntil(': ')
io.sendline(borgovs_moves)
io.interactive()
