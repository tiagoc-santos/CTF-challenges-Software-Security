# Challenge `PwnTools Sockets` writeup

- Vulnerability: What type of vulnerability is being exploited
  - The server is vulnerable to protocol abuse.
- Where: Where is the vulnerability present
  - The service running on `mustard.stt.rnl.tecnico.ulisboa.pt:25055`, and the commands `MORE` and `FINISH`. 
- Impact: What results of exploiting this vulnerability
  - Allows to find the flag by repeatedly sending the `MORE` command until it reaches the target. 
- NOTE: Any other observation

## Steps to reproduce

1. Connect to the remote server using the `remote` command.
2. Read the server's initial message using `s.recvuntil()` and `s.recvline()`. Extract `target` and `current_value`.
3. Loop to get more numbers by sending `MORE` command.
4. At each iteration retrieve the `current_value` and `target`and then check if they are equal.
5. If `current_value == target`, send a `FINISH`command to the server, get the flag and end the loop. 
6. Close the server connection.

[(POC)](pwnTools_sockets_poc.py)

