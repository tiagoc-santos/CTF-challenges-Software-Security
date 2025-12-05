# Challenge `Just my boring cookies` writeup

- Vulnerability: What type of vulnerability is being exploited
  - XSS
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25251` search box
- Impact: What results of exploiting this vulnerability
  - Allows any user to inject malicious code into the website (in this case to see their own cookies)

## Steps to reproduce

1. Write `<script>document.write(document.cookie)</script>` in the search box and click `Search`.
2. Your cookies (and the flag) will appear bellow the search bar.

[(POC)](just_my_boring_cookies_poc.py)