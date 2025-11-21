# Challenge `Python requests Again` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Cookie exploitation
- Where: Where is the vulnerability present
  - Interaction between the `/hello`, `/more`, and `/finish` endpoints, specifically how the session cookie is used to track the `current_value`.
- Impact: What results of exploiting this vulnerability
  - Allows to reset the tries by reseting the cookies and sending a `GET` request to the `hello` endpoint when `current_value != target`, until they match.
- NOTE: Any other observation

## Steps to reproduce

1. Initializa a session by sending a `GET` request to the `hello` endpoint 
2. Loop to get more numbers by sending a `GET` request to the `more`endpoint
3. At each iteration retrieve the `current_value` and `target`and then check if they are equal.
4. If `current_value == target`, send a `GET`request to the `finish` endpoint, get the flag and end the loop. 
5. If they are not equal, reset the session cookies by sending a new `GET`. request to the `hello` endpoint, in order to get more tries and repeat the process

[(POC)](python_requests_again_poc.py)

