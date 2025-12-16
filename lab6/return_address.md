# Challenge `Return Address` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 15 in the `return.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `buffer` and the return address of the `challenge` function (22 bytes). We can also find the address of the `win` function.
2. We can then send a string with 22 characters to fill the buffer followed by the address of the `win` function written in little-endian order to overwrite the return address of the `challenge` function.
3. The return address will now point to the `win` function, causing the program to jump to `win` instead of returning to `main`, and reveal the flag.

Note: In the solution implementation below, the address of the `win` function is retrieved dynamically using the `elf.symbols` feature of ``pwntools``. Thus, in order for the solution to work, the binary must be in the same folder as the poc.

[(POC)](return_address_poc.py)
