# Challenge `Simple Local Read` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Format String Vulnerability
- Where: Where is the vulnerability present
  - Line 14 in the `01_local_read.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to read/write to arbitrary memory content and control the program flow.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), to analyze the stack before the `printf` call, we can see the address that holds `secret_value` is stored in the 7th register immediately after the format string of the `printf`.
2. By sending `%08x.%08x.%08x.%08x.%08x.%08x.%s` as input, the program will print the content of the 6 first registers and read the content of the address stored in the 7th register, which is the `secret_value` printing the flag.

[(POC)](simple_local_read_poc.py)
