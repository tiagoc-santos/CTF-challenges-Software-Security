# Challenge `Sometimes we are just temporarily blind-v2` writeup

- Vulnerability: What type of vulnerability is being exploited
  - SQL injection
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25262` in the search bar.
- Impact: What results of exploiting this vulnerability
  - Allows any user to access information in the database.
- NOTE: Eventhough the blog posts are no longer visible in the main page, information about the number of results found with the query is still displayed. We can take advantage of this to perform blind SQL injection attacks.

## Steps to reproduce

The steps to reproduce and the details about the resolution are the same as in the original version of this challenge. Please refer to [here](sometimes_we_are_just_temporarily_blind.md#steps-to-reproduce) for the detailed steps.

- Note: The only difference is that in this version of the challenge, the flag is case sensitive.
  

[(POC)](sometimes_we_are_just_temporarily_blind_poc.py)
