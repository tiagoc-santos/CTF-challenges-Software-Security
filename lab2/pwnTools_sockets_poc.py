from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25055

### run a remote process
s = remote(SERVER, PORT, timeout=9999)

def extract_target(text):
    m = re.search(r"get to (\d+)", text)
    return int(m.group(1))

def extract_current(text):
    m = re.search(r"CURRENT\s*=\s*(-?\d+)", text)
    return int(m.group(1))

# Read initial block
msg = s.recvuntil(b"CURRENT").decode()
msg += s.recvline().decode()

target = extract_target(msg)
current = extract_current(msg)

while True:
    if current == target:
        s.sendline(b"FINISH")
        print(s.recvall(timeout=2).decode())
        break

    s.sendline(b"MORE")

    msg = s.recvuntil(b"CURRENT").decode()
    msg += s.recvline().decode()

    current = extract_current(msg)

s.close()