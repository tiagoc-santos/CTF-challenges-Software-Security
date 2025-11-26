# Challenge `Another jackpot` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Race Condition
- Where: Where is the vulnerability present
  - in the `login` endpoint bewteen lines 160 to 176
- Impact: What results of exploiting this vulnerability
  - Allows unauthorized users to have admin priveleges during the vulnerability timeframe

## Steps to reproduce

1. Send a `POST` request to `/login` endpoint with cookies where the `username` field is `admin` 
2. At the same time as the first step, send a `GET` request to the `jackpot` endpoint

Note: These steps need to be repeated in a loop until the flag is received, since step 2 needs to happen after the server sets the username as `admin` and before it checks the password.

[(POC)](another_jackpot_poc.py)
