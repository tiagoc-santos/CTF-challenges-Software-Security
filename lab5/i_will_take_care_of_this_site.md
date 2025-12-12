# Challenge `I will take care of this site` writeup

- Vulnerability: What type of vulnerability is being exploited
  - SQL injection
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25261` in the `/login` endpoint.
- Impact: What results of exploiting this vulnerability
  - Allows any user to login as admin.

## Steps to reproduce

1. Go to the login page
2. Login with username :`admin'--` and any password
3. You will login as admin and be able to access its profile page where the flag is present.

Note: If you try to login as `'a` with any password, you will be redirected to an error page where you can see the SQL query used in the login page. The query is the following: `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = '<username>' AND password = <password>`. If you login as `admin'--`, the query becomes `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = 'admin'-- AND password = <password>`, which comments out the password check and allows you to login as admin.

[(POC)](i_will_take_care_of_this_site_poc.py)
