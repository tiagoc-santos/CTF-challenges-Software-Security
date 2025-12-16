# Challenge `Super Secure System` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 10 in the `check.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `buffer` and the return address of the `check_password` function in the memory (44 bytes). We can also find the address of the instructions that prints the flag (line 26).
2. We can send a string with 36 characters to fill the the space between the `buffer` and the `ebx` register, followed by the value of the `ebx` register in little-endian order, followed by 4 characters to fill the space between the `ebx` register and the return address, ended by the address of the instruction that prints the flag written in little-endian order to overwrite the return address of the `check_password` function.
3. The return address will be overwritten with the address of the instruction that prints the flag, so when the function returns, it will not return to line 25 of `check.c` but to line 26 instead, printing the flag.

**Notes**: 
- In order to get, the value of the `ebx` register when entering the `check_password` function, we can use the command: `print/x $ebx` in pwndbg while the program is paused at the beginning of the function.
- The address of the `ebx` register in this case ended with `0x00`, so we had to change it to `0x01` to avoid null byte termination in the input string.

[(POC)](super_secure_system_poc.py)
