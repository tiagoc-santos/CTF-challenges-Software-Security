# Challenge `Calling Functions` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 21 in the `functions.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `buffer` and the `fp` variable (32 bytes). We can also check the address of the `win` function to know where to jump to.
2. We can then send a string with 32 characters to fill the buffer followed by the address of the `win` function written in little-endian order.
3. The `fp`variable is then changed to the address where the `win` function is written in memory, the function is called and the flag is revealed.

Note: In the solution implementation below, the address of the `win` function is retrieved dynamically using the `elf.symbols` feature of ``pwntools``. Thus, in order for the solution to work, the binary must be in the same folder as the poc.

[(POC)](calling_functions_poc.py)
