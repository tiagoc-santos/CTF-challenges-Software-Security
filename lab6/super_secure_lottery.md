# Challenge `Super Secure System` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Buffer Overflow
- Where: Where is the vulnerability present
  - Line 18 in the `lottery.c` file
- Impact: What results of exploiting this vulnerability
  - Allows anyone to write/execute arbitrary code on regions of memory they shouldn't have access to.

## Steps to reproduce

1. Using a debugger (pwndbg for instance), we can check the distance between the `guess` and `lottery` (48 bytes).
2. We can send a string with the same character 56 times. This will fill the space between `guess` and `lottery` (48 bytes) and overwrite `lottery` (8 bytes), with the same character.
3. Since the the first 8 characters of `guess` and `lottery` are the same, the check in line 20 will pass and the flag will be printed.

**Notes**: 
- The canaries are only checked when the function returns. In this case, since the `run_lottery` function does not return (infinite `while` loop), the canary is never checked. Therefore the canaries do not prevent the buffer overflow.

[(POC)](super_secure_lottery_poc.py)
