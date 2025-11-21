# Challenge `Secure by Design` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Exploits Access Control through cookie manipulation.
- Where: Where is the vulnerability present
  - In the server's authentication mechanism, specifically in the identity verification method.
- Impact: What results of exploiting this vulnerability
  - Allows any user to impersonate the admin user by forging a session cookie. This grants unauthorized access to admin content, which in this case, reveals the flag.
- NOTE: Any other observation

## Steps to reproduce

1. Establish a connection by sending a `GET` request and save the cookies.
2. Substitute the `user` field in the cookies for the base64 encoded version of the word `admin`, decoded to UTF-8 (`YWRtaW4=`).
3. Set the cookies with this new `user` field.
4. Make a `POST` request with this new cookies (that will grant admin access) and retrieve the flag.

- NOTE: In order to realize that the server was using base64 encoding, I printed the session cookies after a failed authentication attempt and realized that the username I used was base64 encoded. 

[(POC)](secure_by_design_poc.py)

