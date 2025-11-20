import requests
import re

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25053 

link = f"{SERVER}:{PORT}"

# Create a session to persist the cookies between requests
s = requests.Session()

# Start the game: get the initial cookie
r = s.get(f"{link}/hello")
cookies = r.cookies

while True:
    r = requests.get(f"{link}/more", cookies=cookies)
    cookies = r.cookies
    numbers = list(map(int, re.findall(r"-?\d+", r.text)))
    here_you_have, target, current_value = numbers
    if(current_value == target):
        r = requests.get(f"{link}/finish", cookies=cookies)
        print(r.text)
        break

