# Challenge `Write Big Numbers` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 17 in the `06_write_big_number.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the beginnig of the `buffer` is in the 7th register of the stack.
2. We can use 
    ```
    elf = ELF('06_write_big_number')
    target_address = elf.symbols['target']
    ```
   to obtain the address of the `target` variable.
3. By sending the output of `fmtstr_payload(7, {target_address: 0xdeadbeef})` as input, will automatically generate a format string that puts the `target_address` at the beginning of the `buffer` and then uses calculated padding characters and `%n` to write the number of bytes written so far into that address, changing the value of `target` to `0xdeadbeef`, printing the flag.

[(POC)](write_big_numbers_poc.py)
