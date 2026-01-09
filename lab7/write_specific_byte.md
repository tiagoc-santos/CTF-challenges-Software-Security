# Challenge `Write Specific Byte` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 17 in the `05_write_specific_byte.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the beginnig of the `buffer` is in the 7th register of the stack.
2. We can use 
    ```
    elf = ELF('05_write_specific_byte')
    target_address = elf.symbols['target']
    ```
   to obtain the address of the `target` variable.
3. By sending `p32(target_address + 3) + b'.%253x%7$hhn'` as input, we will put the address of ``target`` + 3 (the 4th byte of the target) at the beginning of the buffer and then use te `%hhn` to write the number of bytes written so far (258: 4 from the address + 253 from the hex padding + 1 from '.') into that address, changing the value of the byte at `target` + 3 to 2 (since ``258 % 256 = 2``) and printing the flag.

[(POC)](write_specific_byte_poc.py)
