# Challenge `Return Address Again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 18 in the `08_return.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the beginnig of the `buffer` is in the 7th register of the stack.
2. We can use 
    ```
    elf = ELF('08_return')
    win_address = elf.symbols['win']
    ```
   to obtain the address of the `win` function.
3. Since ASLR is disabled on the server, we can leak a stack address to calculate the location of the return address. We send ``%1$p`` to leak a stack pointer, then calculate the return address location as `leaked_address - 32` (the offset of `-32` was determined through local debugging by comparing the leaked address to the actual return address location found via info frame in pwndbg, then verified by brute-forcing nearby offsets).
4. Sending the output of `fmtstr_payload(7, {return_address: win_address})` as input, will result in a format string payload that places the stack address with `return_address` into the buffer and using the 7th register writes the value of `win_address` into that location, overwriting the saved return address so that when the current function returns, `win` is called, printing the flag.

[(POC)](return_address_again_poc.py)
