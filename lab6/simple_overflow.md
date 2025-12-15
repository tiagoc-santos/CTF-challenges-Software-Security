# Challenge `Simple Overflow` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 15 in the `simple.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `buffer` and the `test` variable (129 bytes).
2. We can then send a string with 129 characters to fill the buffer and then overwrite the `test` variable.
3. The `test`variable is then changed and the flag is revealed.


[(POC)](simple_overflow_poc.py)
