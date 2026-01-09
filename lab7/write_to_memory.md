# Challenge `Write to Memory` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 15 in the `03_write.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the beginnig of the `buffer` is in the 7th register of the stack.
2. We can use 
    ```
    elf = ELF('03_write')
    target_address = elf.symbols['target']
    ```
   to obtain the address of the `target` variable.
3. By sending `p32(target_address) + b'.%7$n'` as input, will put the address of `target` at the beginning of the `buffer` and then use the `%n` format specifier to write the number of bytes written so far (which is 5, address + '.') into that address, changing the value of `target`, printing the flag.

[(POC)](write_to_memory_poc.py)
