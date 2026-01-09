# Challenge `Calling Functions Again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 19 in the `07_call_functions.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the beginnig of the `buffer` is in the 7th register of the stack.
2. We can use 
    ```
    elf = ELF('07_call_functions')
    win_address = elf.symbols['win']
    puts_address = elf.got['puts']
    ```
   to obtain the address of the `win` function and the `GOT` for the `puts` function.
3. Sending the output of `fmtstr_payload(7, {puts_address: win_address})` as input, will automatically generate a format string payload that places `puts_address` into the buffer and using the 7th register writes the numerical value of `win_address` into the `GOT` of the `puts` function. When `puts` is executed the program calls `win` printing the flag.

[(POC)](calling_functions_again_poc.py)
