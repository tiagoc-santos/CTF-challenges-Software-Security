import requests
import random

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25052 

link = f"{SERVER}:{PORT}"

# Create a session to persist the cookies between requests
s = requests.Session()

# Access the first link to set the user cookie
s.get(link)
low = 0
high = 100000

while True:
    i = random.randint(low, high)
    response = s.get(link + "/number/" + str(i))

    if ("SSof" in response.text):
        print(response.text)
        print(i)
        break

    if("Higher!" in response.text):
        low = i
    elif("Lower!" in response.text):
        high = i
