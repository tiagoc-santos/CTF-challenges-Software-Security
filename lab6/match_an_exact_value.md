# Challenge `Match an Exact Value` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 16 in the `match.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `buffer` and the `test` variable (64 bytes).
2. We can then send a string with 64 characters to fill the buffer followed by ``dcba`` to overwrite the `test` variable.
3. The `test`variable is then changed to `0x61626364` and the flag is revealed.

Note: `0x61626364` is the hexadecimal representation of the ASCII string `abcd`, but the value is stored in little-endia. Thus, we need to send `dcba` to get the correct value. 

[(POC)](match_an_exact_value_poc.py)
