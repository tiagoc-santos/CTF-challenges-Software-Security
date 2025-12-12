# Challenge `Money, money, money!` writeup

- Vulnerability: What type of vulnerability is being exploited
  - SQL injection
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25261` in the `/update_profile` endpoint.
- Impact: What results of exploiting this vulnerability
  - Allows any user to change database values (in this case the number of tokens).

## Steps to reproduce

1. Go to the register page and create a new user.
2. Login and go to your profile page.
3. In the update profile form, in the "Bio" field, enter the following payload: `', tokens = {tokens}, bio ='` where `{tokens}` is your jackpot value.
4. The amount of tokens will be updated to the jackpot value and the flag revealed.

Note: If you try to update your bio to `'a`, you will be redirected to an error page where you can see the SQL query used in the `update_profile` endpoint. The query is the following: `UPDATE user SET bio = '<bio>' WHERE username = '<username>'`. If you update your bio to  `', tokens = {tokens}, bio ='` where `{tokens}` is your jackpot value, the query becomes `UPDATE user SET bio = '', tokens = {tokens}, bio ='' WHERE username = '<username>'`, which updates the number of tokens to the jackpot value.

[(POC)](money_money_money_poc.py)
