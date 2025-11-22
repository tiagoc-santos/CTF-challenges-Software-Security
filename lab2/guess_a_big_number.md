# Challenge `Guess a Big Number` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Endpoint is vulnerable to a targetted attack.
- Where: Where is the vulnerability present
  - `/number/{id}` endpoint.
- Impact: What results of exploiting this vulnerability
  - Allows to find the server's guess by binary search enumeration.
- NOTE: Any other observation

## Steps to reproduce

1. Access the server to establish a session and receive initial cookie
2. Access `/number/{id}` endpoints with different values
3. Parse the response for "Higher!" or "Lower!" hints
4. Use a binary search algorithm to narrow down the range based on hints
5. Continue until the flag's prefix `SSof` appears in response 

[(POC)](guess_big_number_poc.py)