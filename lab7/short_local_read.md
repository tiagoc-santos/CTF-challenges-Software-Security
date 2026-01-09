# Challenge `Short Local Read` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 13 in the `02_local__short_read.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the address that holds `secret_value` is stored in the 7th register immediately after the format string of the `printf`.
2. By sending `%7$s` as input, the program will read the the value pointed by the memory address stored in the 7th register printing the flag.

[(POC)](short_local_read_poc.py)
