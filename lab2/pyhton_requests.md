# Challenge `Python requests` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Endpoint is vulnerable to a targetted attack
- Where: Where is the vulnerability present
  - `/more` endpoint
- Impact: What results of exploiting this vulnerability
  - Allows to find the solution by simply repeatedly querying the `/more` endpoint until the condition `current_value==target` is met.
- NOTE: Any other observation

## Steps to reproduce

1. Start the game by sending a `GET` request to the server and save the cookies.
2. Loop to get more numbers by sending a `GET` request to the `more`endpoint
3. At each iteration retrieve the `current_value` and `target`and then check if they are equal.
4. If `current_value == target`, send a `GET`request to the `finish` endpoint, get the flag and end the loop. Otherwise, start another iteration.

N. Now something bad happened

[(POC)](python_requests_poc.py)

